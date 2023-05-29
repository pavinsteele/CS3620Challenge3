# Part 1
def studentdis(x):
    return x*.9


def regulardis(x):
    return x*.95


print(regulardis(studentdis(5)))

# Part 2
result = (lambda x:x*(x+5)**2)(5)
print(result)

# Part 3
prices = [6, 4, 8, 7, 10, 15, 2, 5]
discount = list(map(lambda x: x*.9, prices))
print(discount)

# Part 4


class Computer:
    def getspecs(self):
        self.ram = "16GB"
        self.gpu = "3060"
        self.cpu = "Intel i7"

    def displayspecs(self):
        print(self.ram)
        print(self.gpu)
        print(self.cpu)


class Desktop(Computer):
    def getdesktopspecs(self):
        self.displays = "2 Displays"

    def printdesktopspecs(self):
        print(self.displays)


class Laptop(Computer):
    def getlaptopspecs(self):
        self.screentype = "Touchscreen"

    def printlaptopspec(self):
        print(self.screentype)


mycomputer = Desktop()
mycomputer.getdesktopspecs()
mycomputer.printdesktopspecs()
mycomputer.getspecs()
mycomputer.displayspecs()

mylaptop = Laptop()
mylaptop.getlaptopspecs()
mylaptop.printlaptopspec()
mylaptop.getspecs()
mylaptop.displayspecs()


# Part 5
class Mult:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return Mult(x)

    def __str__(self):
        return "({0})".format(self.x)


num1 = Mult(2)
num2 = Mult(4)
print(num1 * num2)

