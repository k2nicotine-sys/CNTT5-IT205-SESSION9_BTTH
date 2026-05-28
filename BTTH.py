branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000] 
target_achieved = [True, True, False, True, False]

while True :
    choice = int(input("""
===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====
1. Hiển thị báo cáo doanh thu tổng hợp
2. Thống kê chi nhánh Cao nhất / Thấp nhất
3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)
4. Thoát chương trình
================================================
Nhập lựa chọn của bạn (1-4):
"""))
    match choice :
        case 4:
            print("kết thúc trương trình")
            break

        case 1 :
            for i in range(len(branch_names)):
                status_name = "đạt" if target_achieved[i] else "không đạt"
                print(f"tên cơ sở : {branch_names[i]} | Doanh thu: {daily_revenues[i]} | trạng thái:{status_name}")
        case 2 :
            max_revenue = max(daily_revenues)
            min_revenue = min(daily_revenues)

            max_index = daily_revenues.index(max_revenue)
            min_index = daily_revenues.index(min_revenue)

            print(f"Cao nhất: {branch_names[max_index]}")
            print(f"Thấp nhất: {branch_names[min_index]}")
        case 3 :
            failed_branches = []

            for i in range(len(target_achieved)):
                if target_achieved[i] == False:
                    failed_branches.append(branch_names[i])

            print(failed_branches)
        case _:
            print("lỗi nhập lại")
            continue
    
       
        
