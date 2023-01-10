import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AaMWJLZTNFxnSORRBjU3WtWamiCshMxe0LG4zf8OjIdoAcJIzkJZEZP25Oc230xkVBgzrUbSNvqN5Rot"
        self.client_secret = "EP-uoKUwqFAt9YysbQ-G6lmTsze09jxowdwGYkX8pUHRd080yb6SL6vu2ZbgWk0UW0h5cLuBjFEISMvU"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)