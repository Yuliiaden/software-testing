class Math:
    def __init__(self,numbers):
        self.numbers = []
    def multiplication(self):
        return ([i*3 for i in self.numbers])
    def subtraction(self):
        return ([i-5 for i in self.numbers])
    def division(self, a):
        self.a = a
        if a==0:
            return ("error")
        else:
            return ([i/self.a for i in self.numbers])
result = Math([])
result.numbers.append(2)
result.numbers.append(4)
result.numbers.append(3)
print(result.multiplication())
print(result.subtraction())
print(result.division(8))


