# Return all points adjacent to (i, j) in the four cardinal directions.
def adjacents(i, j):
    return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

# Remove the ring connected to position (i, j), and return it's size.
# This is basically an implementation of the "flood fill" algorithm.
def remove_ring(grid, i, j):
    # (i, j) is not part of a ring, stop.
    if grid[i][j] != "x":
        return 0

    grid[i][j] = "."

    size = 1

    # Recursively call remove_ring on all adjacent squares which are within the
    # grids boundaries.
    for ii, jj in adjacents(i, j):
        if ii >= 0 and ii < len(grid) and jj >= 0 and jj < len(grid):
            size += remove_ring(grid, ii, jj)

    return size

# Determine the age of the tree
def age(tree):
    ret = 0
    for i in range(len(tree)):
        for j in range(len(tree)):
            # If the size of the ring connected to i, j is greater than 0,
            # count it.
            if remove_ring(tree, i, j) > 0:
                ret += 1
    return ret

rows = int(input())
tree = [list(input().strip()) for _ in range(rows)]
print(age(tree))
