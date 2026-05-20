while True: 
    number_employee = int(input("Nhập số lượng nhân viên: "))

    for i in range(number_employee): 
        print(f"\nnhân viên {i+1}")
        full_name = input("Tên nhân viên: ")
        working_date = int(input("Số ngày đi làm: "))
        
        print("\nThông tin nhân viên:")
        print("Tên nhân viên: ", full_name)
        print("Số ngày đi làm:", working_date)

        if working_date < 20: 
            print("Cần cải thiện chuyên cần")
        else : 
            print("Nhân viên chuyên cần tốt")

    choice = input("bạn có muốn tiếp tục chương trình không(y/n)").lower()
    if choice =="n" : 
        print("Chương trình kết thúc")
        break 