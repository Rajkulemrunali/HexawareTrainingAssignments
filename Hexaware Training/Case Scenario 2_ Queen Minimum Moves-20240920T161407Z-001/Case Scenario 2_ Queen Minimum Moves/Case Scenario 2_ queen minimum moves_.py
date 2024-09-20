def minimumMoves(N, board):
    queens = []
    for row in range(N):
        for col in range(N):
            if board[row][col] == 'Q':
                queens.append(row)
    
    def is_valid(queens):
        for i in range(N):
            for j in range(i + 1, N):
                if abs(queens[i] - queens[j]) == abs(i - j):
                    return False
        return True
    
    def backtrack(column, queens, moves):
        if column == N:
            if is_valid(queens):
                return moves
            else:
                return float('inf')
        
        min_moves = float('inf')
        original_row = queens[column]  
        
        for row in range(N):
            if row == original_row:
                min_moves = min(min_moves, backtrack(column + 1, queens, moves))
            else:
                queens[column] = row
                min_moves = min(min_moves, backtrack(column + 1, queens, moves + 1))
        
        queens[column] = original_row
        return min_moves
    
    result = backtrack(0, queens, 0)
    return result

N = int(input("Enter Size of Chessboard(N): "))  
print("Enter queen position on board :")
board = [input().strip() for _ in range(N)]

print(minimumMoves(N, board))

