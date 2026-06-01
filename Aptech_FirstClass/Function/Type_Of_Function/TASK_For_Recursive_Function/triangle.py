# we have triangle made of blocks. the topmost row has 1 block,
# the next row has 2 blocks, the next row has 3 blocks and so on.
#  and so on. complete  recursive (no loops or miltiplication) 
# the total number in such a triangle with the given number of rows.

# example:
# triangle(0) --> 0
# triangle(1) --> 1
# triangle(2) --> 3

def triangle(rows):
    if rows == 0:
        return 0
    else:
        return rows + triangle(rows - 1)
print(triangle(0)) # output: 0
print(triangle(1)) # output: 1
print(triangle(2)) # output: 3
print(triangle(3)) # output: 6

