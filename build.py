def build(matrix, val):
    if matrix is None or val is None:
       return False
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == val:
            return (row, col)
        elif matrix[row][col] > val:
            col -= 1
        else:
            row += 1
    return None
