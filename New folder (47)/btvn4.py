while True: 
    print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")
    number_staff = int(input("Nhập số lượng nhân sự mới: "))
    if number_staff <= 0 : 
        print("số lượng không hợp lệ, yêu cầu nhập lại")
    else : 
        print(f"[Thành công] đã ghi nhận yêu cầu cấp phát tài sản cho {number_staff} nhân sự mới")
        print("--- CHƯƠNG TRÌNH KẾT THÚC ---") 
        break 
    