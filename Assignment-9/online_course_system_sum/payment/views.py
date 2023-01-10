# import stripe
# from django.http.response import JsonResponse, HttpResponse
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings
#
#
# # Create your views here.
# def success(request):
#     return render(request, "payment/success.html")
#
#
# def cancel(request):
#     return render(request, "payment/cancel.html")
#
#
# def land(request):
#     return render(request, "payment/land.html")
#
# # new
# @csrf_exempt
# def stripe_config(request):
#     if request.method == 'GET':
#         stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
#         return JsonResponse(stripe_config, safe=False)
#
#
# @csrf_exempt
# def create_checkout_session(request):
#     if request.method == 'GET':
#         domain_url = 'http://localhost:8000/'
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         try:
#             # Create new Checkout Session for the order
#             # Other optional params include:
#             # [billing_address_collection] - to display billing address details on the page
#             # [customer] - if you have an existing Stripe Customer ID
#             # [payment_intent_data] - capture the payment later
#             # [customer_email] - prefill the email input in the form
#             # For full details see https://stripe.com/docs/api/checkout/sessions/create
#
#             # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
#             checkout_session = stripe.checkout.Session.create(
#                 success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
#                 cancel_url=domain_url + 'cancelled/',
#                 payment_method_types=['card'],
#                 mode='payment',
#                 line_items=[
#                     {
#                         'name': 'cpp',
#                         'quantity': 1,
#                         'currency': 'INR',
#                         'amount': '200',
#                     }
#                 ]
#             )
#             return JsonResponse({'sessionId': checkout_session['id']})
#         except Exception as e:
#             return JsonResponse({'error': str(e)})
#
#
# @csrf_exempt
# def stripe_webhook(request):
#     stripe.api_key = settings.STRIPE_SECRET_KEY
#     endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
#     payload = request.body
#     sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#     event = None
#
#     try:
#         event = stripe.Webhook.construct_event(
#             payload, sig_header, endpoint_secret
#         )
#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         return HttpResponse(status=400)
#
#     # Handle the checkout.session.completed event
#     if event['type'] == 'checkout.session.completed':
#         print("Payment was successful.")
#         # TODO: run some custom code here
#
#     return HttpResponse(status=200)


from django.http.response import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from stripe.api_resources.product import Product
from .models import *
from course.models import Course
from django.views.generic import ListView, CreateView, DetailView, TemplateView
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

# class ProductListView(ListView):
#     model = Product
#     template_name = "payments/product_list.html"
#     context_object_name = 'product_list'
#
#
# class ProductCreateView(CreateView):
#     model = Product
#     fields = '__all__'
#     template_name = "payments/product_create.html"
#     success_url = reverse_lazy("home")
#
#
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "payments/product_detail.html"
#     pk_url_kwarg = 'id'
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductDetailView, self).get_context_data(**kwargs)
#         context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
#         return context


@csrf_exempt
def create_checkout_session(request, id):
    request_data = json.loads(request.body)
    course = get_object_or_404(Course, pk=id)

    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        # Customer Email is optional,
        # It is not safe to accept email directly from the client side
        customer_email=request_data['email'],
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                        'name': course.title,
                    },
                    'unit_amount': int(course.course_price * 100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('failed')),
    )

    # OrderDetail.objects.create(
    #     customer_email=email,
    #     product=product, ......
    # )

    order = OrderDetail()
    order.customer_email = request_data['email']
    order.product = course
    order.stripe_payment_intent = checkout_session['payment_intent']
    order.amount = int(course.course_price * 100)
    order.save()

    # return JsonResponse({'data': checkout_session})
    return JsonResponse({'sessionId': checkout_session.id})


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')


# class OrderHistoryListView(ListView):
#     model = OrderDetail
#     template_name = "payments/order_history.html"


def land(request):
    return render(request, "payment/land.html")


def pay(request):
    return render(request, "payment/pay.html")
