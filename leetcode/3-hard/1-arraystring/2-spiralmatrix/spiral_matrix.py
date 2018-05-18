#
# Spiral print of a matrix
#    
# Define a method, which takes a matrix, and does a spiral print of
# its elements.
#    
# See below for example matrices and the expected output.
#   
# Given:
#   0  1  2  3
#   4  5  6  7
#   8  9  10 11
#   12 13 14 15
#    
# Output:
#   0 1 2 3 7 11 15 14 13 12 8 4 5 6 10 9

A = [[0, 1, 2, 3],
     [4, 5, 6, 7],
     [8, 9, 10, 11],
     [12, 13, 14, 15]]

B = [[0, 1, 2],
     [4, 5, 6],
     [8, 9, 10]]


# this works for even but don't work for odd size
# and assumes 2 sizes are the same
# apple phone screen question, 4/12/2018
def spiral_print1(M):

    n = len(M)      # of rows
    m = len(M[0])   # of columns
    retval = []
    
    layer = 0
    
    while layer <= n/2:

        edge = n - layer - 1

        # print top
        for x in range(layer, edge):  # all but last
            retval.append(M[layer][x])

        # print right
        for x in range(layer, edge):
            retval.append(M[x][edge])

        # print bottom
        for x in range(edge, layer, -1):
            retval.append(M[edge][x])

        # print left
        for x in range(edge, layer, -1):
            retval.append((M[x][layer]))

        layer += 1

    return retval


class Solution:

    def spiralOrder(self, M):

        if not M:
            return []

        n = len(M)      # of rows
        m = len(M[0])   # of columns
        retval = []

        # define start/end box
        row_s = 0
        row_e = n - 1
        col_s = 0
        col_e = m - 1

        while row_s <= row_e and col_s <= col_e:

            # if one item in box
            if row_s == row_e and col_s == col_e:
                retval.append(M[row_s][col_s])

            # if has only one row
            elif row_s == row_e:
                for x in range(col_s, col_e + 1):  # end+1 since no next step
                    retval.append(M[row_s][x])

            # if only has one column
            elif col_s == col_e:
                for x in range(row_s, row_e + 1):  # end+1 since no next step
                    retval.append((M[x][col_s]))

            else:
                # print top
                for x in range(col_s, col_e):  # for each list, add all but last
                    retval.append(M[row_s][x])

                # print right
                for x in range(row_s, row_e):
                    retval.append(M[x][col_e])

                # print bottom
                for x in range(col_e, col_s, -1):
                    retval.append(M[row_e][x])

                # print left
                for x in range(row_e, row_s, -1):
                    retval.append((M[x][col_s]))

            # shrink box
            row_s += 1
            row_e -= 1
            col_s += 1
            col_e -= 1

        return retval


def main():
    s = Solution()
    v = s.spiralOrder(A)
    print(v)
    v = s.spiralOrder(B)
    print(v)

    v = s.spiralOrder([[2, 3]])
    print(v)

        
if __name__ == '__main__':
    main()



def spiral_matrix(M):

    if not M:
        return []

    n = len(M)      # of rows
    m = len(M[0])   # of columns
    retval = []

    # define start/end box
    row_s = 0
    row_e = n - 1
    col_s = 0
    col_e = m - 1

    while row_s <= row_e and col_s <= col_e:

        # if one item in box
        if row_s == row_e and col_s == col_e:
            retval.append(M[row_s][col_s])

        # if has only one row
        elif row_s == row_e:
            for x in range(col_s, col_e + 1):  # end+1 since no next step
                retval.append(M[row_s][x])

        # if only has one column
        elif col_s == col_e:
            for x in range(row_s, row_e + 1):  # end+1 since no next step
                retval.append((M[x][col_s]))

        else:
            # for each list, add all but last, so all 4 sides are symmetrical

            # print top
            for x in range(col_s, col_e):
                retval.append(M[row_s][x])

            # print right
            for x in range(row_s, row_e):
                retval.append(M[x][col_e])

            # print bottom
            for x in range(col_e, col_s, -1):
                retval.append(M[row_e][x])

            # print left
            for x in range(row_e, row_s, -1):
                retval.append((M[x][col_s]))

        # shrink box
        row_s += 1
        row_e -= 1
        col_s += 1
        col_e -= 1

    return retval
