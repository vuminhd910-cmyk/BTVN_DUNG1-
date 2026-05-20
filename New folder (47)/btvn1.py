print(" --- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG -- ")

# Vòng Lặp chạy 3 Lần để nhập Lương cho 3 nhân viên
total_budget = 0 
for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)
    # Nhập mức lương
    salary = int(input (" Nhập mức Lương (VNĐ): "))

    # Thuc hien thao tac cong don tien vao chiec hộp
    total_budget += salary 

# Sau khi nhập xong cả 3 người, in tổng tiền ra màn hình
print (" KET QUA: TONG NGAN SACH CAN CHUAN BI LA:", total_budget, "VND")

# lỗi ở đây có 2 lỗi 
# lỗi khai báo biến trong vòng lặp , phải khai báo biến ở ngoài vòng lặp nếu không thì mỗi lần chạy biến sẽ bị reset lại 
# lỗi sử dụng toán tử , sử dụng += chứ không phải = 
 