def first_repeating_character(s):
    # Scan through the string once and count the number of occurrences of each
    # character.
    occurrences = {}
    for c in s:
        occurrences[c] = occurrences.get(c, 0) + 1

    # Scan through a second time and return the first character which appeared
    # more than once.
    for c in s:
        if occurrences[c] > 1:
            return c

    # The problem stated that a repeating character will exist.
    raise "Bad input man"

print(first_repeating_character(input()))
