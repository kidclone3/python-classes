# Homework 7: Dynamic Programming

> Bùi Khánh Duy - 20001898
> 

# I.  Lý thuyết phương pháp

***Trình bày (ngắn gọn) ý tưởng, những yếu tố cơ bản và các bước trong thiết kế giải thuật bằng phương pháp quy hoạch động.***

Phương pháp quy hoạch động là một kỹ thuật giải quyết các bài toán tối ưu bằng cách chia bài toán thành các bài toán con nhỏ hơn, giải quyết các bài toán con này và kết hợp lại để tìm ra lời giải cho bài toán ban đầu. Ý tưởng cơ bản của phương pháp quy hoạch động là sử dụng kết quả của các bài toán con để giải quyết bài toán lớn hơn, với mục đích tối ưu hóa hàm mục tiêu.

Các yếu tố cơ bản của phương pháp quy hoạch động bao gồm:

- Tối ưu hóa hàm mục tiêu: Phương pháp quy hoạch động được sử dụng để giải quyết các bài toán tối ưu, trong đó cần tìm ra lời giải tốt nhất cho hàm mục tiêu.
- Chia bài toán thành các bài toán con: Bài toán ban đầu được chia thành các bài toán con nhỏ hơn, có thể được giải quyết độc lập với nhau.
- Lưu trữ kết quả tính toán: Kết quả tính toán của các bài toán con được lưu trữ để sử dụng trong các bài toán lớn hơn.

Các bước trong thiết kế giải thuật bằng phương pháp quy hoạch động bao gồm:

1. Xác định cấu trúc của bài toán và đặt ra mục tiêu tối ưu.
2. Chia bài toán thành các bài toán con nhỏ hơn.
3. Xác định hàm truy xuất và lưu trữ kết quả tính toán của các bài toán con.
4. Thiết lập quy tắc cập nhật kết quả tính toán của các bài toán con.
5. Giải quyết bài toán ban đầu bằng cách kết hợp các kết quả tính toán của các bài toán con.
6. Kiểm tra và tối ưu hóa giải thuật để đảm bảo tính đúng đắn và hiệu quả của giải thuật.

Các bước trên sẽ được lặp lại cho đến khi đạt được lời giải tối ưu cho bài toán ban đầu.

# II. Lập trình

***Viết chương trình cho các thuật toán đã phân tích và xây dựng (theo bài giảng).***

### 1. Bài toán tìm dãy con đơn điệu tăng dài nhất (longest increasing subsequence)

**Đặt vấn đề:** Bài toán này là gì?

Bài toán đưa ra yêu cầu tìm một dãy con của một dãy số đã cho, sao cho các phần tử trong dãy con này tăng dần theo thứ tự và chiều dài của dãy con này là lớn nhất

**Ví dụ:** cho dãy `A = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}` 

Dãy con đơn điệu tăng dài nhất của dãy số này là {1, 2, 5, 6}. Các dãy con khác như `{1, 4, 5, 6}` hoặc `{1, 2, 3, 5}` là các kết quả khác cho đầu vào này.

**Đặt bài toán:** Cho mảng `A` có độ dài $n$, được đánh số từ $0$ đến $n-1$.

**Phương pháp giải:**

- Cách thông thường: Các bước như sau:
    1. Tạo thêm 2 mảng phụ để tính toán, gọi là mảng `B` để lưu phần tử nhỏ nhất xuất hiện trước phần tử đang xét, và mảng `C` để tính độ dài của dãy con tăng dài nhất tại vị trí $i$.
    2. Sử dụng 2 vòng for để tính toán: Tại vị trí thứ $i$, ta sẽ duyệt ngược các phần tử trước đó, để tìm ra 1 phần tử thoả mãn 2 tiêu chí sau:
        1. `A[j] < A[i]`
        2. `C[j] max`
        
        Với $j \in [0, i-1]$
        
    3. Lấy ra mảng dãy con tăng dài nhất bằng cách xuất phát từ vị trí có giá trị lớn nhất của mảng `C`.
    
    **Code:**
    

### 2. Bài toán xếp balo 0-1 (0-1 knapsack)

### 3. Bài toán đường đi trong bảng số (path in numeric table)