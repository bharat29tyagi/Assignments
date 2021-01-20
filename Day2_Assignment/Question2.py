'''This small code takes an input in integer form.
the input will tell us the number of times the 'for loop' should be executed.
Each time the 'for loop' runs, it prints an 'integer' i.e. denoted by 'i',
after a desired number of spaces in order to print the desired pattern.'''

#required input is 6, according to the question no. 2

num = int(input('enter a number: '))

for i in range(1, num):
    print(' '*(num-i),str(i)*i)
