import operator as op

def mathematical_operator(first_number, operator, second_number):
    first_number,second_number=float(first_number), int(second_number)
    valid_operators = {"+":op.add, "-":op.sub, "*": op.mul, "^": op.xor, "/": op.truediv}

    return valid_operators[operator](first_number,second_number)

