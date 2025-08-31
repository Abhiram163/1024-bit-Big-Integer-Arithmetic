def is_magic_square(square):
    n = len(square)
    # Calculate the sum of the first row (target sum)
    target_sum = sum(square[0])
    
    # Check all rows
    for row in square:
        if sum(row) != target_sum:
            return False
    
    # Check all columns
    for col in range(n):
        if sum(square[row][col] for row in range(n)) != target_sum:
            return False
    
    # Check diagonals
    if sum(square[i][i] for i in range(n)) != target_sum:
        return False
    if sum(square[i][n - 1 - i] for i in range(n)) != target_sum:
        return False
    
    return True


# Example run
square = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(square):
    print("It is a magic square!")
else:
    print("Not a magic square.")
