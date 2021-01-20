'''This code works by taking several numbers as input from user,
the numbers are stored in a list.
that list is then passed in a 'function' i.e. sort_even,
which checks if the number is even, if it is even,
that number is stored in a separate list.'''

#enter integers only, separated by space.
list1 = [int(i) for i in (input("Enter numbers: ").split())]
even_numbers = []

def sort_even(arg):
    for i in list1:
        if (i%2 == 0):
            even_numbers.append(i)
    print(sorted(even_numbers))

sort_even(list1)
