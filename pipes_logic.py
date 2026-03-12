import os

# Mã hóa các loại ống (Top, Right, Bottom, Left)
PIPE_TYPES = {
    'straight': (1, 0, 1, 0), 'corner':   (1, 1, 0, 0),
    't_shape':  (1, 1, 1, 0), 'cross':    (1, 1, 1, 1),
    'end':      (1, 0, 0, 0), 'empty':    (0, 0, 0, 0)
}

# Ký tự đồ họa để in ra terminal
VISUAL_MAP = {
    (1, 0, 1, 0): '║', (0, 1, 0, 1): '═',
    (1, 1, 0, 0): '╚', (0, 1, 1, 0): '╔', (0, 0, 1, 1): '╗', (1, 0, 0, 1): '╝',
    (1, 1, 1, 0): '╠', (0, 1, 1, 1): '╦', (1, 0, 1, 1): '╣', (1, 1, 0, 1): '╩',
    (1, 1, 1, 1): '╬',
    (1, 0, 0, 0): '╹', (0, 1, 0, 0): '╺', (0, 0, 1, 0): '╻', (0, 0, 0, 1): '╸',
    (0, 0, 0, 0): ' '
}

def get_all_rotations(pipe_tuple):
    """Lấy các hướng xoay của ống"""
    rotations = set()
    current = pipe_tuple
    for _ in range(4):
        rotations.add(current)
        current = (current[3], current[0], current[1], current[2])
    return list(rotations)

def is_valid_partial(board, row, col):
    """Kiểm tra ống ở (row, col) có khớp với xung quanh không"""
    current = board[row][col]
    rows, cols = len(board), len(board[0])

    if row == 0 and current[0] == 1: return False
    if col == 0 and current[3] == 1: return False
    if row == rows - 1 and current[2] == 1: return False
    if col == cols - 1 and current[1] == 1: return False

    if row > 0:
        if current[0] != board[row - 1][col][2]: return False
    if col > 0:
        if current[3] != board[row][col - 1][1]: return False

    return True

def print_board(board, step=None):
    """In ma trận ra màn hình"""
    os.system('cls' if os.name == 'nt' else 'clear')
    if step is not None: print(f"--- Bước thứ {step} ---")
    else: print("--- TRẠNG THÁI HIỆN TẠI ---")
        
    for row in board:
        print(" ".join([VISUAL_MAP.get(pipe, '?') for pipe in row]))
    print("\n")