# A map where the keys are the keys on the number pad, and the values are the
# corresponding characters.
keypad = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqr",
    "7": "stu",
    "8": "vwx",
    "9": "yz",
    "0": ".,!",
    "#": " ",
}

# The cost of a character is simply its position in the string.  Python's
# .find method returns the 0 based index of the character in the string, or
# -1 if it's not found.
def char_cost(char):
    return sum(seq.find(char) + 1 for _, seq in keypad.items())

# The cost of a message is the summation of the costs of each character in the
# message.
def message_cost(message):
    return sum(map(char_cost, message))

print(message_cost(input()))
