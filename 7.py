
'''
Q.No.7 Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters
'''
def upper_lower(str):
    n1=0
    n2=0
    for i in str:
        if i.isupper():
            n1=n1+1
        elif i.islower():
            n2=n2+1
    print(f'there is {n1} upper case letter ')
    print(f'there is {n2} lower case letter')

upper_lower("MAnjeSH")


