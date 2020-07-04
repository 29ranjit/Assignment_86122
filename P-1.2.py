print('\n\nAssignment Set I: Program 2 \n\nProgram to find the biggest of 3 numbers using of condition \n\n')

a = int(input("Enter Your First Number: "))
b = int(input("\nEnter Your Second Number: "))
c = int(input("\nEnter Your Third Number: "))

if (a > b) and (a > c):
   largest = a
elif (b > a) and (b > c):
   largest = b
else:
   largest = c
 
if (a < b) and (a < c):
   smallest = a
elif (b < a) and (b < c):
   smallest = b
else:
   smallest = c
 



print('\n\nThe largest number is {}'.format(largest))

print('\nThe smallest number is {}'.format(smallest))