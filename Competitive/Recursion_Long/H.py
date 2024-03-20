def is_palindrome_recursive(text, start, end):
    if start >= end:
        return True
    return text[start] == text[end] and is_palindrome_recursive(text, start + 1, end - 1)

def get_reverse_recursive(char):
    reverse_map = {
        'A': 'A', 'M': 'M', 'Y': 'Y', 'Z': '5', 'O': 'O', '1': '1',
        '2': 'S', 'E': '3', "3": 'E', 'S': '2', '5': 'Z',
        'H': 'H', 'T': 'T', 'I': 'I', 'U': 'U', 'J': 'L', 'V': 'V',
        '8': '8', 'W': 'W', 'L': 'J', 'X': 'X'
    }
    if char in reverse_map:
        return reverse_map[char]
    else:
        return char

def is_mirrored_string_recursive(text, start, end):
    if start >= end:
        return True
    return get_reverse_recursive(text[start]) == text[end] and is_mirrored_string_recursive(text, start + 1, end - 1)

def main():
    lst = []
    while True:
        line = input().strip().split()
        if not line:
            break
        text= "".join(line)
        is_regular_palindrome = is_palindrome_recursive(
            text, 0, len(text) - 1)
        is_mirrored_string = is_mirrored_string_recursive(
            text, 0, len(text) - 1)

        if not is_regular_palindrome and not is_mirrored_string:
            lst.append(f"{text} -- is not a palindrome.")
        elif is_regular_palindrome and not is_mirrored_string:
            lst.append(f"{text} -- is a regular palindrome.")
        elif not is_regular_palindrome and is_mirrored_string:
            lst.append(f"{text} -- is a mirrored string.")
        else:
            lst.append(f"{text} -- is a mirrored palindrome.")

    for i in lst:
        print(i)
        print()

if __name__ == "__main__":
    main()
