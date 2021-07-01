'''
10 Write a program to find the factorial of a number using functions
'''
def fraction(a):
    num=1
    if num<0:
        print('not a factorial')
    elif num==0:
        print('the factorial is 1')
    else:

        for i in range(1,a+1):
            num=num*i
            print(f'the fractional of {a} is {num}')

fraction(12)