for i in range(3): 
    print(f"Nhân viên số {i+1} ")
    employeer_id = input("Mã nhân viên(ví dụ: NV001, ...): ")
    full_name = input("Họ và tên nhân viên: ")
    department = input("Phòng ban công tác: ")

    if employeer_id == "" or full_name == "": 
        print("Dữ liệu không hợp lệ : ")
    else : 
        print("Mã nhân viên: ", employeer_id)
        print("Họ và tên nhân viên: ", full_name)
        print("Phòng ban công tác: ", department) 
        
    # luồng hoạt động 
    # khai báo biến sử dụng input và ép kiểu dữ liệu 
    # để vào trong vòng lặp for với range(3) 
    # kiểm tra rỗng và khoảng trắng kết hợp toán tử or 
    # cuối cùng in ra kết quả 
    