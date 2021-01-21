'''this snippet of code accepts two inputs in integer form and returns the sum.'''

class Add:

    def return_sum(self):
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))

        return num1 + num2
        
obj = Add()
print(obj.return_sum())
