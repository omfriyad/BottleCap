from rpn import eval as rpn
import attr

variables ={

}


class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class String():
    def __init__(self, value):
        self.value = value[1:-1]

    def eval(self):
        return str(self.value)


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Program():
    def __init__(self, value):
        self.value = value

    # Returning after printing the value
    def eval(self):
        print(self.value.eval())


class Print():
    def __init__(self, value):
        self.value = value

    # Returning after printing the value
    def eval(self):
        rtn = self.value.eval()
        print(rtn)
        return rtn


class Expression():
    def __init__(self, expressions):
        self.expressions = expressions

    def eval(self):
        for expression in self.expressions:
            expression.eval()


class Rpn():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return rpn(self.value)


class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Subtract(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Multiply(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Divide(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Assign():
    def __init__(self, ident, value):
        self.ident = ident.get_value()
        self.value = value
        variables[str(self.ident)] = self.value

    def eval(self):
        return self.value.eval()


class Identifier():
    def __init__(self, value):
        self.value = str(value)
        try:
            if variables[value]:
                pass
        except:
            pass

    def eval(self):
        return variables.get(self.value)

    def get_value(self):
        return self.value
