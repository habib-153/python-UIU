def min_moves(matrix):
  """Calculates the minimum number of moves to make the matrix beautiful."""
  target_row = 2 
  target_col = 2 

  for i in range(5):
    for j in range(5):
      if matrix[i][j] == 1:
        current_row, current_col = i, j
        break

  # Calculate the number of row or column swaps needed
  row_moves = abs(current_row - target_row)
  col_moves = abs(current_col - target_col)

  return (row_moves + col_moves)

# Read the input matrix
matrix = []
for _ in range(5):
   row = list(map(int, input().split()))

   matrix.append(row)

min_moves_count = min_moves(matrix)
print(min_moves_count)
