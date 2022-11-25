-- CREATING THE DEPARTMENT TABLE

CREATE TABLE DEPT(DEPTNO INT(5) PRIMARY KEY ,DNAME VARCHAR(15),LOC VARCHAR(15));
INSERT INTO DEPT VALUES(10,'ACCOUNTS','BANGALORE');
INSERT INTO DEPT VALUES(20,'IT','DELHI');
INSERT INTO DEPT VALUES(30,'PRODUCTION','CHENNAI');
INSERT INTO DEPT VALUES(40,'SALES','HYD');
INSERT INTO DEPT VALUES(50,'ADMN','LONDON');
SELECT * FROM DEPT;

-- CREATING THE EMPLOYEE TABLE
CREATE TABLE EMP(EMPNO INT(5),ENMAE VARCHAR(15),SAL INT(10),HIRE_DATE DATE,COMMISSION INT(10),DEPTNO INT(5),MGR INT(5));
ALTER TABLE EMP ADD FOREIGN KEY (DEPTNO) REFERENCES DEPT(DEPTNO);
-- SELECT * FROM EMP WHERE DEPTNO=10 OR DEPTNO=30;
INSERT INTO EMP VALUES(1001,'SACHIN',19000,'1980-01-01',2100,20,1003);
INSERT INTO EMP VALUES(1002,'KAPIL',15000,'1970-01-01',2300,10,1003);
INSERT INTO EMP VALUES(1003,'STEFEN',12000,'1990-01-01',500,20,1007);
INSERT INTO EMP VALUES(1004,'WILLIAMS',9000,'2001-01-01',null,30,1007);
INSERT INTO EMP VALUES(1005,'JOHN',5000,'2005-01-01',null,30,1006);
INSERT INTO EMP VALUES(1006,'DRAVID',19000,'1985-01-01',2400,10,1007);
INSERT INTO EMP VALUES(1007,'MARTIN',21000,'2000-01-01',1040,null,null);
SELECT * FROM EMP;

-- 1.	Select employee details  of dept number 10 or 30*

Select * from EMP WHERE DeptNo = 10 OR 30;

-- 2. query to fetch all the dept details with more than 1 Employee.
SELECT Dname FROM DEPT WHERE DEPTNO IN ( SELECT DEPTNO FROM emp GROUP BY DEPTNO HAVING COUNT(*) >1 );

-- 3.	Write a query to fetch employee details whose name starts with the letter “S”
select ENMAE from EMP where ENMAE LIKE ('S%') ;

-- 4.	Select Emp Details Whose experience is more than 2 years
SELECT * FROM EMP WHERE timestampdiff(YEAR,HIRE_DATE,CURRENT_DATE) > 2;

-- 5.	Write a SELECT statement to replace the char “a” with “#” in Employee Name ( Ex:  Sachin as S#chin)         
SELECT EMPNO,REPLACE(ENMAE,'A','#') AS ENMAE FROM EMP;

-- 6.	Write a query to fetch employee name and his/her manager name.
SELECT E.ENMAE,M.ENMAE FROM EMP AS EMP INNER JOIN E AS M ON E.EMPNO = M.MGR ;

-- 7.	Fetch Dept Name , Total Salary of the Dept
SELECT DEPTNO,SUM(SAL) FROM EMP GROUP BY DEPTNO;

-- 8.	Write a query to fetch ALL the  employee details along with department name, department location, irrespective of employee existance in the department.
SELECT EMP.*, DNAME, LOC FROM EMP JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO;


-- 9: Write an update statement to increase the employee salary by 10 %
UPDATE EMP SET SAL=SAL+(SAL*10/100);
SELECT * FROM EMP;

-- 10: Write a statement to delete employees belong to Chennai location.
DELETE FROM EMP WHERE DEPTNO = (SELECT DEPTNO FROM DEPT WHERE LOC='CHENNAI');
SELECT * FROM EMP;

-- 11: Get Employee Name and gross salary (sal + comission) .
SELECT E.ENMAE,E.SAL + IFNULL(E.COMMISSION,0) FROM EMP E;

-- 12: Increase the data length of the column Ename of Emp table from  100 to 250 using ALTER statement
ALTER TABLE EMP MODIFY ENMAE VARCHAR(250);
SELECT * FROM EMP;

-- 13: Write query to get current datetime
SELECT current_timestamp();

-- 14: Write a statement to create STUDENT table, with related 5 columns
CREATE TABLE STUDENT(SID INT(5),SNAME VARCHAR(15),ADDRESS VARCHAR(15),MARKS INT(5),PHONENO INT(12));
SELECT * FROM STUDENT;

-- 15:  Write a query to fetch number of employees in who is getting salary more than 10000
SELECT COUNT(*) FROM EMP WHERE SAL>=10000;

-- 16: Write a query to fetch minimum salary, maximum salary and average salary from emp table.
SELECT AVG(SAL),max(SAL),MIN(SAL) FROM EMP;

-- 17: Write a query to fetch number of employees in each location
SELECT D.DNAME,COUNT(*) FROM EMP E,DEPT D WHERE E.DEPTNO=D.DEPTNO GROUP BY LOC;

-- 18: Write a query to display emplyee names in descending order
SELECT * FROM EMP ORDER BY ENMAE DESC;

-- 19: Write a statement to create a new table(EMP_BKP) from the existing EMP table
CREATE TABLE EMP_BKP AS SELECT * FROM EMP;
SELECT * FROM EMP_BKP;

-- 20: Write a query to fetch first 3 characters from employee name appended with salary.
SELECT CONCAT(SUBSTRING(ENMAE,1,3),SAL) AS NAMESAL FROM EMP;

-- 21: Get the details of the employees whose name starts with S
select ENMAE from EMP where ENMAE LIKE ('S%') ;

-- 22: Get the details of the employees who works in Bangalore location
SELECT ENMAE FROM EMP WHERE DEPTNO=(SELECT DEPTNO FROM DEPT WHERE LOC='BANGALORE');

-- 23:  Write the query to get the employee details whose name started within  any letter between  A and K
SELECT ENMAE FROM EMP WHERE ENMAE BETWEEN 'A' AND 'K';

-- 24: Write a query in SQL to display the employees whose manager name is Stefen
SELECT ENMAE FROM EMP WHERE MGR=(SELECT EMPNO FROM EMP WHERE ENMAE='STEFEN');

-- 25:  Write a query in SQL to list the name of the managers who is having maximum number of employees working under him
SELECT M.ENMAE,COUNT(*) FROM EMP E,EMP M WHERE E.MGR=M.EMPNO GROUP BY M.ENMAE HAVING COUNT(*)=(SELECT MAX(MYCOUNT) FROM (SELECT COUNT(*)MYCOUNT FROM EMP GROUP BY MGR)A);

-- 26: Write a query to display the employee details, department details and the manager details of the employee who has second highest salary
SELECT * FROM EMP WHERE SAL = (SELECT MAX(SAL) FROM EMP WHERE SAL < (SELECT MAX(SAL) FROM EMP));

-- 27: Write a query to list all details of all the managers
SELECT M.ENMAE AS MANAGER_NAME,M.MGR FROM EMP E,EMP M WHERE E.MGR = M.EMPNO;

-- 28: Write a query to list the details and total experience of all the managers
SELECT M.ENMAE AS MANAGER_NAME,E.MGR,TIMESTAMPDIFF(YEAR,M.HIRE_DATE,CURRENT_DATE) AS EXPERIENCE FROM EMP E,EMP M WHERE E.MGR = M.EMPNO;

-- 29:  Write a query to list the employees who is manager and  takes commission less than 1000 and works in Delhi
SELECT * FROM EMP E WHERE E.EMPNO IN (SELECT MGR FROM EMP) AND E.COMMISSION < 1000 AND E.DEPTNO=(SELECT DEPTNO FROM DEPT WHERE LOC='DELHI');

-- 30: Write a query to display the details of employees who are senior to Martin
SELECT * FROM EMP WHERE HIRE_DATE < (SELECT HIRE_DATE FROM EMP WHERE ENMAE='MARTIN');
