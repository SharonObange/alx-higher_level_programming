#!/usr/bin/python3
a = 10
b = 5

if __name__ == "__main__":
    from calculator_1 import add
    add_result = add(a, b)

    from calculator_1 import sub
    sub_result = sub(a, b)

    from calculator_1 import mul
    mul_result = mul(a, b)

    from calculator_1 import div
    div_result = div(a, b)

    print("{} + {} = {}" .format(a, b, add_result))
    print("{} - {} = {}" .format(a, b, sub_result))
    print("{} * {} = {}" .format(a, b, mul_result))
    print("{} / {} = {}" .format(a, b, div_result))
