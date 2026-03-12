from pipes_logic import PIPE_TYPES as P

# ==========================================
# CẶP 1: MAP 3x3 (Dùng để chạy Demo có hình ảnh)
# ==========================================
# Chuẩn: Một vòng lặp khép kín đơn giản
MAP_3x3_SOLVABLE = [
    [P['corner'], P['straight'], P['corner']],
    [P['straight'], P['empty'], P['straight']],
    [P['corner'], P['straight'], P['corner']]
]

# Lỗi: Cố tình nhét 1 ống chữ Thập vào cạnh viền -> chĩa ra ngoài -> Fail
MAP_3x3_UNSOLVABLE = [
    [P['corner'], P['cross'], P['corner']],
    [P['straight'], P['empty'], P['straight']],
    [P['corner'], P['straight'], P['corner']]
]

# ==========================================
# CẶP 2: MAP 4x4 (Mức độ vừa)
# ==========================================
# Chuẩn: Vòng lặp kép
MAP_4x4_SOLVABLE = [
    [P['corner'], P['straight'], P['straight'], P['corner']],
    [P['straight'], P['corner'], P['corner'], P['straight']],
    [P['straight'], P['corner'], P['corner'], P['straight']],
    [P['corner'], P['straight'], P['straight'], P['corner']]
]

# Lỗi: Góc dưới cùng bên phải thay vì ống Góc (Corner) lại là ống Cụt (End)
MAP_4x4_UNSOLVABLE = [
    [P['corner'], P['straight'], P['straight'], P['corner']],
    [P['straight'], P['corner'], P['corner'], P['straight']],
    [P['straight'], P['corner'], P['corner'], P['straight']],
    [P['corner'], P['straight'], P['straight'], P['end']]
]

# ==========================================
# CẶP 3: MAP 7x7 (Đo lường thời gian bắt đầu lâu)
# ==========================================
# Chuẩn: Mạng lưới chữ thập hoàn hảo
MAP_7x7_SOLVABLE = [
    [P['corner'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['corner']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['corner'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['corner']]
]

# Lỗi: Lỗ hổng (Empty) nằm ngay chính giữa bản đồ (Dòng 3, Cột 3)
MAP_7x7_UNSOLVABLE = [
    [P['corner'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['corner']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['empty'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['corner'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['corner']]
]

# ==========================================
# CẶP 4: MAP 10x10 (Giới hạn của thuật toán Mù)
# ==========================================
# Chuẩn: Cực kỳ nặng máy cho DFS, RAM sẽ tăng vọt
MAP_10x10_SOLVABLE = [
    [P['corner'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['corner']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['corner'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['corner']]
]

# Lỗi: Cố tình đặt 1 ô Trống (Empty) ở tọa độ (5,5)
MAP_10x10_UNSOLVABLE = [
    [P['corner'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['corner']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['empty'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['t_shape'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['cross'], P['t_shape']],
    [P['corner'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['t_shape'], P['corner']]
]