def is_palindrome(self, s: str) -> bool:
    # Optimized solution

    # First create string with only alpha numericals
    new_string = ""
    for character in s:
        if character.isalnum():
            new_string += character.lower()

        # Using TWO POINTERS
        ptr1, ptr2 = 0, len(new_string) - 1

        while ptr1 < ptr2:
            if new_string[ptr1] != new_string[ptr2]:
                return False
            ptr1, ptr2 = ptr1 + 1, ptr2 - 1
        return True
