

class calculation:

    def addition(a, b):
        return a+b

    def subtraction(a, b):
        return a-b

    def multiplication(a, b):
        return a*b

    def division(a, b):
        if b==0:
            raise ValueError("Cannot divid by 0 !")
        return a//b

    def even(a):
        if a%2==0:
            return True
        else:
            return False