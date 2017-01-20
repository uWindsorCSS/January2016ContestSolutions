# The minimum length of a car is 3 blocks.
MIN_CAR_LENGTH = 3

# A cache to store previously solved problems.
cache = {}

def configurations(open_blocks):
    # If the number of open blocks is less than 0, we are done.
    if open_blocks < 0:
        return 1

    # Check to see if we have solved this already.
    if open_blocks in cache:
        return cache[open_blocks]

    # There is always at least one solution, as we can leave the rest of the
    # parking lot empty.
    ret = 1

    # We can place a car in any open spot that is at least 3 away from the end.
    for offset in range(0, open_blocks - MIN_CAR_LENGTH + 1):
         # Vary the length of the car.
        for car_length in range(MIN_CAR_LENGTH, open_blocks - offset + 1):
            # Subtract an extra one for the empty space.
            ret += configurations(open_blocks - offset - car_length - 1)

    cache[open_blocks] = ret
    return ret

print(configurations(int(input())))
