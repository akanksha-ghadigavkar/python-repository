#write a program to read the employee data such as
#eno,ename,esal,eaddr,married from the keyboard and print that data.
'''
n1=int(input('enter Eno:'))
n2=str(input('enter Ename:'))
n3=int(input('enter Esal:'))
n4=str(input('enter Eadd:'))
n5=str(input('married:'))

'''
'''
# Q.2a] Write a python code to find Area of Circle.


pi=3.14157
r=int(input('Enter the redious of the circle:'))#Radius

Area=pi*r*r

print('Area of circle',Area)#(pi)=22/7,r=radius=14


'''

#b] Write python code to accept 2 numbers from user and display add,
#sub, mul and div.
'''
#add
x=int(input('Enter first number  :'))
y=int(input('Enter second number :'))
result1=x+y
print('X+y=',result1)

#sub
x=int(input('Enter first number :'))
y=int(input('Enter second number :'))
result2=x-y
print('X-y=',result2)

#mul
x=int(input('Enter first number:'))
y=int(input('Enter second number:'))
result3=x*y
print('X*y=',result3)

#div
x=int(input('Enter first number:'))
y=int(input('Enter second number:'))
result4=x/y
print('X/y=',result4)

'''

#Declare a=60 ,b=13 and c= 0 and perform all the bitwise operation
# where c will be storing the result on the interpreter showing the output
'''

#Bitwise operator

a=60 #111100
b=13  #1101
c=0

print(a&b)#and
print(a|b)#or
print(~a)#not
print(a<<b)#leftshift
print(a>>b)#rightshift
print(a^b)#xor

'''
#4Write the program to  declare the salary of 7 employee. calculate the sum of salary
#of all the employee to see the company investment.
'''

emp1=int(input('Salary of emp1:'))
emp2=int(input('Salary of emp2:'))
emp3=int(input('Salary of emp3:'))
emp4=int(input('Salary of emp4:'))
emp5=int(input('Salary of emp5:'))
emp6=int(input('Salary of emp6:'))
emp7=int(input('Salary of emp7:'))

Total_sal=emp1+emp2+emp3+emp4+emp5+emp6+emp7

print('Total salary of employee:',Total_sal)
'''
'''

#1) Accept user's name and birth year. Print user's name and age.
#Hint - age = 2021 - birth year

n=str(input('Enter user name:'))

n1=int(input('Enter Birth year:'))
n2=2022#Current year
age=n2-n1



print('User Name:',n,';' 'Age:',age)

       


#2)  Accept input from user -> score in 5 subjects like math,
#physics, history, english and chemistry. calculate total score and percentage.

math=int(input('Enter the marks of math:'))
phys=int(input('Enter the marks of pjys:'))
his=int(input('Enter the marks of his:'))
eng=int(input('Enter the marks of eng:'))
chem=int(input('Enter the marks of chem:'))

total_score=math+phys+his+eng+chem
percentage=total_score/500*100

print('Total score:',total_score)
print('percentage:',percentage)


'''

'''

#problem statement:

#Based on input age from a person, indicates him following. 

#1. He is minor and can not apply for employment in the org.
#2. He is senior citizen, so he is not applicable for employment. 
#3. As per his age, he can apply for the employment in this org.

age=int(input('Enter your Age:'))
if age<=17:
  print('He is minor and can not apply for employment in the org')
if age>50:
  print('He is senior citizen, so he is not applicable for employment')
if age>=18 and age<50:
  print('As per his age, he can apply for the employment in this org')

'''
'''
#Take the three side for the triangle from the user and check
#whether the triangle is equilateral, isosceles orscalene triangle?

print('Enter the lengths of the triangle sides:')

x=int(input('x: '))
y=int(input('y: '))
z=int(input('z: '))

if x==y==z:
    print('Equilateral triangle')
elif x==y or y==z or z==x:
    print('Isosceles triangle')
else:
    print('Scalene triangle')
    
'''
'''    
#Write a Program to Calculate the Simple Interest for Bank Customer
#for Fixed Deposit

#a. If customer is Female and Senior Citizen 8% rate

#b. If customer is Female and Non-Senior Citizen 6% rate

#c. If customer is Male and Senior Citizen 7% rate

#d. If customer is Male and Non-Senior Citizen 5% rate


p=float(input('Enter the principal amount:'))

n=float(input('Enter the number of years:'))

gender=str(input('Gender(m/f): '))
citizen=str(input('citizen(s/ns): '))



if gender=='f' and citizen=='s':
   r=8/100
   si=(p*r*n)/100

elif gender=='f' and citizen=='ns':
   r=6/100
   si=(p*r*n)/100

elif gender=='m' and citizen=='s':
     r=7/100
     si=(p*r*n)/100

elif gender=='m' and citizen=='ns':
     r=5/100
     si=(p*r*n)/100

else:
  print('Wrong Choice')

print('Simple Interest is: ', si)


'''


'''

#WAP for check a number is leap year or not by using following constraints-:



#Constraints-: 

#1. N div by 400 --> leap year

#2. N div by 4 , N not div by 100 --> leap year

'''
'''
year=int(input('Enter the year:'))

if (year%400==0):
  print(year,'is leap year')
elif (year%4==0 and year%100!=0):
  print(year,'is leap year')
else:
  print(year,'is not leap year')
'''

#Write a program that will ask user to provide values of length
#and breadth of a rectangle and print the area of it. Also check if
#it is square or not and if so print that it's a Square and
#print the Area of square.


#rectangle = length * width
#squre=a2

l=int(input('Enter the length of rectangle:'))
w=int(input('Enter the width of rectangle:'))

Area=l*w
#print('Area of rectangle:',Area)

'''
a=int(input('Enter the value of Hight:'))
a1=int(input('Enter the value of Base:'))
Area=a*a1
'''

if (l==w):
  print('It is a square')
  print('Area is: ',Area)
else: 
  print('It is not a square')
  print('Area of rectangle is :',Area)
  



  






