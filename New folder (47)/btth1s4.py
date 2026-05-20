total_amount = int(input("Nhập tổng số tiền ban đầu của hóa đơn (VND): "))
if total_amount >= 500000:
    discount_amount = total_amount * 0.1 
else:
    discount_amount = 0                  
final_amount = total_amount - discount_amount
print("Tong tien ban dau:", total_amount, "VND")
print("So tien duoc giam:", int(discount_amount), "VND")
print("So tien thuc te phai tra:", int(final_amount), "VND")
