def string_to_int(str):
    '''
    Write a method to convert a string representation of an integer into its equivalent integer number.

    ex: 
    Input: "123"
    Output: 123

    Input: "-6714"
    Output: -6714
    '''
    if not str:
        return False

    total = 0
    exponent = 0
    end_ptr = len(str) - 1

    for i in range(len(str)):

        if str[0] == "-":
            i = 1

        total +=

        print(type(str[end_ptr]))
        # total += str[end_ptr] * pow(10, exponent)

        if str[end_ptr] == '-':
            total *= -1

        end_ptr -= 1
        exponent += 1

    return total


input_string = "123"
print(string_to_int(input_string))
