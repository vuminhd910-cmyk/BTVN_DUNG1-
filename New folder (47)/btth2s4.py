total_revenue = 0
good_days_count = 0
for day in range(1, 8):
    revenue = int(input(f"Nhập doanh thu ngày {day} (VND): "))
    total_revenue = total_revenue + revenue
    if revenue >= 5000000:
        good_days_count = good_days_count + 1

average_revenue = total_revenue / 7

print("BÁO CÁO DOANH THU TUẦN")
print("Tổng doanh thu cả tuần:", total_revenue)
print("Doanh thu trung bình mỗi ngày:", int(average_revenue))
print("Số ngày có doanh thu từ 5000000 trở lên:", good_days_count)
