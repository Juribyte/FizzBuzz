print('Input a number')
num= int(input())

if ((num%3==0) & (num%5==0)):
        print('FizzBuzz')
elif (num%3 == 0):
       print('Fizz')
elif (num%5 == 0):
       print('Buzz')
else:
        print('Number is not divisible by 3 and 5')



