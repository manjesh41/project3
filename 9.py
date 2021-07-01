'''
Q.No.9 Write a Python function that checks whether a passed string is palindrome or
not
Note: A palindrome is a word, phrase, or sequence that reads the same backward as
forward, e.g., madam or nurses run.ot.
'''
def passed_string(string):
    if (string == string[::-1]):
        print("The string is a palindrome")
    else:
        print("Not a palindrome")
    return
string = input(("Enter a string:"))
passed_string(string)