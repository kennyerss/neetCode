
def reverse_words(input_string):
    '''
    Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

    ex:

    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

    Input: s = "hello world"
    Output: "olleh dlrow"

    Method:
    - First .split() into array of individual words

    Iterate through array
        For each string, just reverse the word

    Join the words together with " " empty space
    '''
    def reverse_string(input_string):
        '''
        Takes in a string and reverses the word

        Using stored variable

        Runtime: O(n) where n is the length our input string
        Space: O(n)
        '''
        # Create result variable for reversed string
        reversed_string = ""
        for i in range(len(input_string)-1, -1, -1):
            # Go from last index to zero index and add to our reversed_string variable
            reversed_string += input_string[i]
        # Return our reversed string when loop finishes
        return reversed_string
    # First split the empty spaces
    word_array = input_string.split()

    for i in range(len(word_array)):
        word = word_array[i]
        # For each word in our word array, reverse the word
        word_array[i] = reverse_string(word)
    # Join the list with empty space
    return " ".join(word_array)


input_string = "Let's take LeetCode contest"
print(reverse_words(input_string))
