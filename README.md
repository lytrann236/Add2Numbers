# MyBigNumber - Dự án Cộng 2 Số Lớn

## 1. Giới thiệu
Đây là bài làm cho yêu cầu phát triển hàm cài đặt thuật toán cộng 2 số lớn (được biểu diễn dưới dạng chuỗi) theo thuật toán cộng của học sinh Tiểu học. Dự án được phát triển bằng ngôn ngữ Python.

## 2. Chức năng chính
- Cài đặt lớp `MyBigNumber` với phương thức `sum(stn1, stn2)` để tính tổng hai chuỗi số lớn.
- Ghi nhận lại lịch sử chi tiết của từng bước phép toán (Dùng lệnh Print/Log).
- Ví dụ: `sum("1234", "897")` sẽ thực hiện cộng từng hàng đơn vị, hàng chục... và in ra lịch sử từng bước.

## 3. Cấu trúc thư mục
Dự án tuân thủ khuyến khích tách biệt mã nguồn chính và mã nguồn kiểm thử:
- `MyBigNumber.py`: Chứa mã nguồn chính của dự án.
- `test_unit.py`: Chứa các Unit Test để kiểm tra tính chính xác của hàm.
- `README.md`: Hướng dẫn chi tiết về dự án.

## 4. Cách sử dụng và Chạy thử
Để đảm bảo bạn có thể thực hiện lại đúng như tác giả đã làm, hãy làm theo các bước sau:

### Bước 1: Clone dự án từ GitHub
```bash
git clone [https://github.com/lytrann236/Add2Numbers.git](https://github.com/lytrann236/Add2Numbers.git)
cd Add2Numbers

### Bước 2: Chạy các Test Case (Unit Testing)
Dự án sử dụng Unit Testing để kiểm thử mã nguồn. Bạn chạy lệnh sau để xem quá trình tính toán và kiểm tra kết quả:
```bash
python test_unit.py