import time
import tracemalloc
import copy

# Import các thành phần từ các file khác
from maps import (
    MAP_3x3_SOLVABLE, MAP_3x3_UNSOLVABLE,
    MAP_4x4_SOLVABLE, MAP_4x4_UNSOLVABLE,
    MAP_7x7_SOLVABLE, MAP_7x7_UNSOLVABLE,
    MAP_10x10_SOLVABLE, MAP_10x10_UNSOLVABLE
)
from pipes_logic import print_board
from solver_dfs import dfs_solve
# TODO: Sau này bạn kia làm xong A* thì bỏ comment dòng dưới
# from solver_astar import astar_solve 

def run_algorithm(algorithm_name, solver_function, board, show_demo=False):
    """Hàm chạy thuật toán và đo lường thông số"""
    print(f"\n[{algorithm_name}] ĐANG GIẢI...")
    
    # Bắt buộc phải COPY map, để không làm hỏng map gốc (vì 2 thuật toán cùng chạy 1 map)
    working_board = copy.deepcopy(board)
    step_counter = [0]
    
    tracemalloc.start()
    start_time = time.time()
    
    # Chạy thuật toán được truyền vào
    success = solver_function(working_board, step_counter=step_counter, show_demo=show_demo)
    
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    if success:
        print(f"✅ [{algorithm_name}] ĐÃ TÌM THẤY LỜI GIẢI!")
        if not show_demo: print_board(working_board)
    else:
        print(f"❌ [{algorithm_name}] KHÔNG THỂ GIẢI ĐƯỢC MAP NÀY!")
        
    print(f"--- THỐNG KÊ [{algorithm_name}] ---")
    print(f"- Số bước thử: {step_counter[0]}")
    print(f"- Thời gian:   {(end_time - start_time):.5f} giây")
    print(f"- RAM tiêu thụ:{peak / 10**6:.5f} MB\n")

if __name__ == "__main__":
    # Chọn map muốn test (Ví dụ: MAP_EASY_3x3)
    current_map = MAP_10x10_UNSOLVABLE  # Bạn có thể đổi sang MAP_EASY_3x3 hoặc MAP_EXPERT_10x10 để thử nghiệm
    
    print("MẠNG LƯỚI ỐNG NƯỚC BAN ĐẦU:")
    print_board(current_map)
    input("Nhấn Enter để chạy các giải thuật...")

    # 1. Chạy thuật toán của bạn (DFS) - Bật show_demo=True để xem hiệu ứng
    run_algorithm("Blind Search: DFS", dfs_solve, current_map, show_demo=False)
    
    # 2. Chạy thuật toán của người kia (A*) - Tạm thời comment lại
    # run_algorithm("Heuristic: A-Star", astar_solve, current_map, show_demo=False)