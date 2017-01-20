import itertools

def tranpose(m):
    return map(list, zip(*m))

def reverse_rows(m):
    return map(reversed, m)

# An interesting trick: A square matrix can be rotated 90 degrees clockwise
# by taking the transpose, and then reversing the rows.
def rotate_clockwise_90(m):
    return reverse_rows(tranpose(m))

def concat(seq):
    return "".join(seq)

yoyo_size        = int(input())
yoyo_design      = [input() for _ in range(yoyo_size)]
elapsed_time     = int(input())

# We only really need to rotate it n % 4 times, anything more is just spinning
# in circles.
actual_rotations = elapsed_time % 4

for _ in range(actual_rotations):
    yoyo_design = rotate_clockwise_90(yoyo_design)

print("\n".join(map(concat, yoyo_design)))
