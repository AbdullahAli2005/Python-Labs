# backtracking approach 

N = 8  # Size of chessboard (8x8)

def print_solution(board):
    """Print the chessboard configuration."""
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print("\n")  # Line break after each solution


def is_safe(board, row, col):
    """Check if a queen can be safely placed at board[row][col]."""

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col):
    """Recursively try placing queens column by column."""
    # Base case: If all queens are placed
    if col >= N:
        print_solution(board)
        return True

    res = False
    # Try placing queen in all rows of this column
    for i in range(N):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recur to place rest of the queens
            res = solve_nqueens(board, col + 1) or res

            # Backtrack if placing queen here doesn't lead to solution
            board[i][col] = 0

    return res


def eight_queens():
    """Driver function to start the algorithm."""
    board = [[0] * N for _ in range(N)]
    if not solve_nqueens(board, 0):
        print("No solution exists.")
    else:
        print("All possible solutions printed above.")


# Run the program
if __name__ == "__main__":
    eight_queens()
