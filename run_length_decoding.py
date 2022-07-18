
def run_length(input_string):
    '''
    Given an input string, write a function that returns the run-length encoded string for the input string.*

    Input: "wwwwaaadexxxxxx"
    Output: "w4a3d1e1x6"

    Input: "aexd"
    Output: "a1e1x1d1"

    Runtime: O(n)
    Space: O(n)
    '''
    # Variable for indices
    start = 0
    end = len(input_string) - 1

    # Variable to store our result string
    result_string = ""

    # Iterate through our input_string
    while start < end:
        letter = input_string[start]
        result_string += letter
        length = 1
        # Make sure that our next letter (start+1) is within input_string length
        while start < end and letter == input_string[start+1]:
            length += 1
            start += 1
        # Otherwise just increment start index if next letter is not the same as current letter
        start += 1
        result_string += str(length)
        # Make sure to re-initialize our length variable to 0 once we finished counting the same letter in string
        length = 0

    return result_string


input_string = "wwwwaaadexxxxxx"
print(run_length(input_string))
