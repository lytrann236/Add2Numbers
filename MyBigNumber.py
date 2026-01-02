class MyBigNumber:
    """
    Lớp thực hiện cộng hai số lớn dưới dạng chuỗi[cite: 12].
    """
    def sum(self, stn1, stn2):
        # Giả định dữ liệu đầu vào luôn đúng [cite: 23]
        result = []
        carry = 0 # Biến nhớ
        
        # Lấy độ dài lớn nhất của 2 chuỗi
        max_len = max(len(stn1), len(stn2))
        
        # Duyệt từ phải sang trái (giống cách học sinh làm) [cite: 13, 22]
        for i in range(1, max_len + 1):
            # Lấy từng chữ số từ phải sang trái, nếu hết thì coi là 0 [cite: 13]
            d1 = int(stn1[-i]) if i <= len(stn1) else 0
            d2 = int(stn2[-i]) if i <= len(stn2) else 0
            
            # Thực hiện phép cộng chữ số và số nhớ [cite: 14]
            current_sum = d1 + d2 + carry
            
            # Ghi lại lịch sử thực hiện (Logging/Print) [cite: 15]
            print(f"Bước {i}: Lấy {d1} cộng {d2} được {d1 + d2}. Cộng tiếp với nhớ {carry} được {current_sum}. "
                  f"Ghi {current_sum % 10}, nhớ {current_sum // 10}.")
            
            # Lưu chữ số hàng đơn vị vào kết quả và cập nhật biến nhớ [cite: 18, 21]
            result.append(str(current_sum % 10))
            carry = current_sum // 10
            
        # Nếu sau cùng vẫn còn nhớ thì thêm vào đầu [cite: 21]
        if carry > 0:
            result.append(str(carry))
            print(f"Bước cuối: Còn nhớ {carry}, viết thêm {carry} vào kết quả.")
            
        # Đảo ngược lại để được kết quả đúng
        return "".join(result[::-1])