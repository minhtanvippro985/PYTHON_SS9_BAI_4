order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

order_status = ["PENDING" ,"DELIVERING","CANCELLED"]

while True:
    choice = input("""
===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Cập nhật danh sách đơn hàng
3. Thống kê đơn hàng theo trạng thái
4. Thoát chương trình
==================================================
Nhập lựa chọn 1-4 : 
""")
    
    match choice:
        case "1":
            if len(order_list) == 0:
                print("Hiện không có đơn hàng nào")
            else:
                print("Danh sách đơn hàng hiện tại :")
                for order in range(len(order_list)):
                    print(f"{order + 1}. {order_list[order]}")
        case "2":
            while True:
              mini_input = input("""
-------- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -------
|    1. Thêm đơn hàng mới                   |
|    2. Sửa đơn hàng theo vị trí            |
|    3. Xóa đơn hàng theo vị trí            |
|    4. Quay lại menu chính                 |\n
Nhập chức năng 1 - 4 : """)             
              match mini_input:
                
                  case "4":
                        print("Quay lại menu")
                        break
                  case "1":
                      new_order_input = input("Nhập tên đơn hàng mới của bạn : ").strip().upper()
                      if new_order_input == "":
                          print("Không được để trống")
                          continue
                      if new_order_input.count(" "):
                          print("Mã đơn không được chứa kí tự cách")
                          continue
                      
                      new_status_input = input("Nhập trạng thái của đơn hàng : ").strip().upper()
                      if new_status_input == "":
                          print("Không được để trống")
                          continue

                      if not new_status_input in order_status:
                          print("Chỉ nhập trạng thái PENDING / DELIVERING / CANCELLED")
                          continue
                      final_order_input =f"{new_order_input} - {new_status_input}"
                      print(f"Đã nhập {final_order_input} vào danh sách!")
                      order_list.append(final_order_input)
                
                  case "2":
                        edit_position = input("Nhập vị trí đơn hàng cần sửa: ").strip()
                        if not edit_position.isdigit():
                            print("Vị trí không hợp lệ!")
                            continue

                        position = int(edit_position)
                       
                        if position < 1 or position > len(order_list):
                            print("Không tồn tại đơn hàng ở vị trí này!")
                            continue

                        index_to_edit = position - 1
                        print(f"Bạn đang sửa đơn hàng: {order_list[index_to_edit]}")

                        # nhập thông tin mới
                        edit_code = input("Nhập mã đơn hàng mới: ").strip().upper()
                        if edit_code == "":
                            print("Mã đơn hàng không được để trống!")
                            continue

                        edit_stt = (
                            input("Nhập trạng thái mới: ").strip().upper()
                        )
                        if edit_stt not in order_status:
                            print("Trạng thái không hợp lệ!")
                            continue

                        # cập nhật thông tin mới vào List
                        order_list[index_to_edit] = f"{edit_code} - {edit_stt}"
                        print("Cập nhật đơn hàng thành công!")
                      
                  case "3":
                        input_delete_order = input("Nhập đơn hàng mà bạn muốn xóa : ").strip()
                        if input_delete_order.isalpha():
                             print("Nhập sai định dạng")
                             continue
                        if input_delete_order < "0" or input_delete_order > str(len(order_list)):
                             print("không tìm thấy")
                             continue
                        if input_delete_order:
                             input_delete_order = int(input_delete_order)
                             print(f"Đã xóa : {order_list[input_delete_order]}")
                             order_list.pop(input_delete_order)
                  case _ :
                        print("Vui lòng nhập từ 1 - 4")
        case "3":
    
                        count_pending = 0
                        count_delivering = 0
                        count_completed = 0
                        count_cancelled = 0

                        # duyệt qua danh sách để đếm
                        for order in order_list:
                            # tách chuỗi theo dấu " - " để lấy trạng thái
                            parts = order.split(" - ")
                            if len(parts) == 2:
                                status = parts[1].strip()
                                
                                # match-case để kiểm tra trạng thái và tăng biến đếm tương ứng
                                match status:
                                    case "PENDING":
                                        count_pending += 1
                                    case "DELIVERING":
                                        count_delivering += 1
                                    case "COMPLETED":
                                        count_completed += 1
                                    case "CANCELLED":
                                        count_cancelled += 1

                        # hiển thị kết quả thống kê theo đúng định dạng yêu cầu
                        print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
                        print(f"PENDING: {count_pending}")
                        print(f"DELIVERING: {count_delivering}")
                        print(f"COMPLETED: {count_completed}")
                        print(f"CANCELLED: {count_cancelled}")
                        print(f"Tổng số đơn hàng: {len(order_list)}")    
              
        case "4":
             print("Thoát chương trình")
             break
        case _ :
             print("Vui lòng nhập 1 - 4")


# KHỞI TẠO danh_sách_đơn_hàng = ["GE001 - PENDING", "GE002 - DELIVERING", "GE003 - CANCELLED"]
# KHỞI TẠO danh_sách_trạng_thái_hợp_lệ = ["PENDING", "DELIVERING", "CANCELLED"]

# VÒNG LẶP VÔ HẠN (Vòng lặp Menu chính):
#     HIỂN THỊ giao diện Menu chính gồm 4 lựa chọn (1. Hiển thị, 2. Cập nhật, 3. Thống kê, 4. Thoát)
#     NHẬP lựa_chọn_chính từ bàn phím

#     KIỂM TRA lựa_chọn_chính:

#         TRƯỜNG HỢP "1": // HIỂN THỊ DANH SÁCH ĐƠN HÀNG
#             NẾU độ dài của danh_sách_đơn_hàng bằng 0:
#                 IN "Hiện không có đơn hàng nào"
#             NGƯỢC LẠI:
#                 IN "Danh sách đơn hàng hiện tại :"
#                 VỚI mỗi chỉ_mục từ 0 đến (độ dài danh_sách_đơn_hàng - 1):
#                     IN (chỉ_mục + 1) + ". " + danh_sách_đơn_hàng[chỉ_mục]

#         TRƯỜNG HỢP "2": // CẬP NHẬT DANH SÁCH ĐƠN HÀNG (MENU CON)
#             VÒNG LẶP VÔ HẠN (Vòng lặp Menu con):
#                 HIỂN THỊ giao diện Menu con (1. Thêm, 2. Sửa, 3. Xóa, 4. Quay lại)
#                 NHẬP lựa_chọn_con từ bàn phím

#                 KIỂM TRA lựa_chọn_con:

#                     TRƯỜNG HỢP "1": // Thêm đơn hàng mới
#                         NHẬP tên_đơn_hàng_mới (loại bỏ khoảng trắng, chuyển thành CHỮ HOA)
#                         NẾU tên_đơn_hàng_mới bằng rỗng:
#                             IN "Không được để trống"
#                             TIẾP TỤC vòng lặp con (bỏ qua các bước dưới)
#                         NẾU tên_đơn_hàng_mới có chứa khoảng trắng:
#                             IN "Mã đơn không được chứa kí tự cách"
#                             TIẾP TỤC vòng lặp con

#                         NHẬP trạng_thái_mới (loại bỏ khoảng trắng, chuyển thành CHỮ HOA)
#                         NẾU trạng_thái_mới bằng rỗng:
#                             IN "Không được để trống"
#                             TIẾP TỤC vòng lặp con
#                         NẾU trạng_thái_mới KHÔNG NẰM TRONG danh_sách_trạng_thái_hợp_lệ:
#                             IN "Chỉ nhập trạng thái PENDING / DELIVERING / CANCELLED"
#                             TIẾP TỤC vòng lặp con

#                         GÁN đơn_hàng_hoàn_chỉnh = tên_đơn_hàng_mới + " - " + trạng_thái_mới
#                         IN "Đã nhập " + đơn_hàng_hoàn_chỉnh + " vào danh sách!"
#                         THÊM đơn_hàng_hoàn_chỉnh vào cuối danh_sách_đơn_hàng

#                     TRƯỜNG HỢP "2": // Sửa đơn hàng theo vị trí
#                         NHẬP vị_trí_chuỗi từ bàn phím (loại bỏ khoảng trắng)
#                         NẾU vị_trí_chuỗi KHÔNG PHẢI LÀ CHỮ SỐ NGUYÊN:
#                             IN "Vị trí không hợp lệ!"
#                             TIẾP TỤC vòng lặp con

#                         GÁN vị_trí_số = chuyển vị_trí_chuỗi thành số nguyên
#                         NẾU vị_trí_số < 1 HOẶC vị_trí_số > độ dài của danh_sách_đơn_hàng:
#                             IN "Không tồn tại đơn hàng ở vị trí này!"
#                             TIẾP TỤC vòng lặp con

#                         GÁN chỉ_mục_cần_sửa = vị_trí_số - 1
#                         IN "Bạn đang sửa đơn hàng: " + danh_sách_đơn_hàng[chỉ_mục_cần_sửa]

#                         NHẬP mã_đơn_mới (loại bỏ khoảng trắng, chuyển thành CHỮ HOA)
#                         NẾU mã_đơn_mới bằng rỗng:
#                             IN "Mã đơn hàng không được để trống!"
#                             TIẾP TỤC vòng lặp con

#                         NHẬP trạng_thái_mới (loại bỏ khoảng trắng, chuyển thành CHỮ HOA)
#                         NẾU trạng_thái_mới KHÔNG NẰM TRONG danh_sách_trạng_thái_hợp_lệ:
#                             IN "Trạng thái không hợp lệ!"
#                             TIẾP TỤC vòng lặp con

#                         GÁN danh_sách_đơn_hàng[chỉ_mục_cần_sửa] = mã_đơn_mới + " - " + trạng_thái_mới
#                         IN "Cập nhật đơn hàng thành công!"

#                     TRƯỜNG HỢP "3": // Xóa đơn hàng theo vị trí
#                         NHẬP chuỗi_cần_xóa từ bàn phím (loại bỏ khoảng trắng)
#                         NẾU chuỗi_cần_xóa chỉ toàn ký tự chữ cái (Alpha):
#                             IN "Nhập sai định dạng"
#                             TIẾP TỤC vòng lặp con
#                         NẾU chuỗi_cần_xóa < "0" HOẶC chuỗi_cần_xóa > dạng chuỗi của(độ dài danh_sách_đơn_hàng):
#                             IN "không tìm thấy"
#                             TIẾP TỤC vòng lặp con

#                         NẾU chuỗi_cần_xóa không rỗng:
#                             GÁN chỉ_mục_cần_xóa = chuyển chuỗi_cần_xóa thành số nguyên
#                             // Lưu ý: vị trí này đang tương đương chỉ mục index trực tiếp trong code hiện tại của bạn
#                             IN "Đã xóa : " + danh_sách_đơn_hàng[chỉ_mục_cần_xóa]
#                             XÓA phần tử tại vị trí chỉ_mục_cần_xóa khỏi danh_sách_đơn_hàng

#                     TRƯỜNG HỢP "4": // Quay lại menu chính
#                         IN "Quay lại menu"
#                         THOÁT vòng lặp con (break)

#                     TRƯỜNG HỢP MẶC ĐỊNH (Còn lại):
#                         IN "Vui lòng nhập từ 1 - 4"

#         TRƯỜNG HỢP "3": // THỐNG KÊ ĐƠN HÀNG THEO TRẠNG THÁI
#             GÁN count_pending = 0
#             GÁN count_delivering = 0
#             GÁN count_completed = 0
#             GÁN count_cancelled = 0

#             VỚI MỖI đơn_hàng TRONG danh_sách_đơn_hàng:
#                 GÁN mảng_tách = tách đơn_hàng bằng chuỗi " - "
#                 NẾU độ dài của mảng_tách bằng 2:
#                     GÁN trạng_thái = mảng_tách[1] (loại bỏ khoảng trắng)

#                     KIỂM TRA trạng_thái:
#                         TRƯỜNG HỢP "PENDING":
#                             TĂNG count_pending lên 1 đơn vị
#                         TRƯỜNG HỢP "DELIVERING":
#                             TĂNG count_delivering lên 1 đơn vị
#                         TRƯỜNG HỢP "COMPLETED":
#                             TĂNG count_completed lên 1 đơn vị
#                         TRƯỜNG HỢP "CANCELLED":
#                             TĂNG count_cancelled lên 1 đơn vị

#             IN "===== THỐNG KÊ ĐƠN HÀNG ====="
#             IN "PENDING: " + count_pending
#             IN "DELIVERING: " + count_delivering
#             IN "COMPLETED: " + count_completed
#             IN "CANCELLED: "