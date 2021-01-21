'''This code accepts two inputs from user,
stores them in different variables, then func. 'swapper()'
swaps the values of the variables and prints them.'''

def swapper(a, b):
    a, b = b, a
    print('\nValues swapped.', '\n\tfirst value: ',a ,'\n\tsecond value: ', b)
    
a = input('Enter first value: ')
b = input('Enter second value: ')

print('\nYour inputs were:', '\n\tFirst value: ' ,a ,'\n\tSecond value', b)
swapper(a, b)
