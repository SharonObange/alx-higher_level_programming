#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            num1 = my_list_1[i] if i < list_length else 0
            num2 = my_list_2[i] if i < list_length else 0

            num1_is_number = isinstance(num1, (int, float))
            num2_is_number = isinstance(num2, (int, float))

            if not num1_is_number or not num2_is_number:
                raise TypeError("wrong type")

            if num1 == 0 or num2 == 0:
                raise ZeroDivisionError("division by 0")

            result = num1 / num2
            result_list.append(result)

        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)

        except TypeError:
            print("wrong type")
            result_list.append(0)

        except IndexError:
            print("out of range")
            result_list.append(0)
        finally:
            pass

    return result_list
