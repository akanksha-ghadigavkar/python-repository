# for loop
#display 3,5,7,9,11,13 using for loop
#range(3,14,2)
'''
for i in range(3,14,2):
    print(i,end=' ')
'''

#continue statement
#input:3,5,7,9,11,13 : range(3,14,2)
#output:3,5,7,11,13 skipping(9)
'''

for i in range(3,14,2):
    if i==9:
      continue
    else:
        print(i,end=' ')
'''



#skip all numbers that divisable by 5 within a given range
'''
start=int(input('Enter the start value:'))
stop=int(input('Enter the stop value:'))
for i in range(start,stop):
    if i%5==0:
        continue
    else:
        print(i,end=' ')


'''

#break statement
'''
start=int(input('Enter the start value:'))
stop=int(input('Enter the stop value:'))
for i in range(start,stop):
    if i%5==0:
        
        break
    else:
        print(i,end=' ')
'''


'''

start=int(input('Enter the start value:'))
stop=int(input('Enter the stop value:'))
for i in range(start,stop):
    if i%5==0:
        print(i)
        break

'''


#pass statement
'''
start=int(input('Enter the start value:'))
stop=int(input('Enter the stop value:'))
for i in range(start,stop):
    if i%5==0:
        pass
        print(i,end=''
'''

'''
for i in range(1,10):
    pass
'''


'''

total=0
for i in range(1,8): #(1,2,3,4,5,6,7)
    total=total+i
print ('The result is:',total)

'''

#find the sum of number from given range
#take start and end value using input()
#find the multiple of all number from a given range


'''
start=int(input('Enter the start value:'))
end=int(input('Enter the end value:'))
mult=1#initializing a veriable for updating values in each round
for i in range(start,end):
 mult=mult*i
print('Result is:',mult)

'''
# factorial
'''
num=int(input('Enter the number:'))
fact=1
for i in range(num,1,-1):
    fact=fact*i

print('Factorial of',num,'is:',fact)
'''
#Revers of a given number

#INPUT:1234
  #1000+200+30+4
#output:4321
  #4000+300+20+1

num=int(input('Enter the number:'))
rev_num=0
while num>0:
    #get the last degit
    last_digit=num%10
    

     #finding the proper place for the last digit
    rev_num=rev_num*10+last_digit
    #update the number

    num=num//10
print('The reverse number is:',rev_num)


#7007
num=int(input('Enter the number:'))
rev_num=0
while num>0:
    #get the last degit
    last_digit=num%10
    

     #finding the proper place for the last digit
    rev_num=rev_num*10+last_digit
    #update the number

    num=num//10
print('The reverse number is:',rev_num)






