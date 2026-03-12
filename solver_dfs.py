import time
from pipes_logic import get_all_rotations, is_valid_partial, print_board

def dfs_solve(board, row=0, col=0, step_counter=None, show_demo=False):
    """Thuật toán DFS có Backtracking"""
    if step_counter is None: step_counter = [0]
        
    if row == len(board): return True
    
    next_row = row if col < len(board[0]) - 1 else row + 1
    next_col = col + 1 if col < len(board[0]) - 1 else 0

    current_pipe = board[row][col]
    original_state = current_pipe 

    for rotation in get_all_rotations(current_pipe):
        board[row][col] = rotation
        step_counter[0] += 1
        
        if show_demo:
            print_board(board, step_counter[0])
            time.sleep(0.05) 
            
        if is_valid_partial(board, row, col):
            if dfs_solve(board, next_row, next_col, step_counter, show_demo):
                return True
                
    board[row][col] = original_state
    return False