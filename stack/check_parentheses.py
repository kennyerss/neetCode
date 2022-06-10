def check_parentheses(string):
    '''
    Runtime: O(n)
    Memory: O(n)

    Solution is to implement stack data structure with array by mapping closing brackets and popping off when brackets match

    ex:
    '([{}])' --> True
    '(})' --> False
    '''

    map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in string:

        # Check if char is in map... it's a closing bracket
        if char in map:

            # Check if stack is not empty and previous element is an opening bracket... POP from stack

            if stack and stack[-1] == map[char]:
                stack.pop()

            else:  # If it's not matching brackets... return False
                return False

        else:  # If we see an opening bracket, add to our stack
            stack.append(char)

    # When for loop is done... if stack is EMPTY return True... otherwise return false
    return True if not stack else False
