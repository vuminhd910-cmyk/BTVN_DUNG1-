print (" --- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT --- ")

# Vòng Lặp chạy đúng 3 Lần cho 3 nhân viên
for employee_number in range(1, 4):
    print(" --- Đang xử lý nhân viên số", employee_number, " -- ")

    # Yêu cầu kế toán nhập dữ Liệu
    working_days = int (input ("Nhập số ngày công trong tháng: "))

    # Kiểm tra diều kiện
    if working_days == 0:
        print ("Cảnh báo: Nhân viên nghỉ cả tháng không được xét thưởng.")

    bonus_amount = working_days * 200000
    print("> đã gửi email : chúc mừng nhận thưởng", bonus_amount, "VND tien thuong!")


print ("Đã hoàn tat qua trình duyệt thường cho 3 nhân viên!")

# lỗi sai ở đoạn sử dụng toán tử phải sử dụng == chứ không phải = 
# == ở đây mới có giá trị so sánh 