#Task 1 Check if a Number is Even or Odd
a = input("Enter a number: ")
a=int(a)
if(a&1 == 0):
    print(a,'is an even number.')
else:
    print(a,'is an odd number.')

#Task 2  Sum of Integers from 1 to 50 Using a Loop

a =0
for i in range(1,51):
    a+=i
print('The sum of numbers from 1 to 50 is:' ,a)