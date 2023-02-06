# Tối thiểu hoá Otomat hữu hạn đơn định - Minimization DFA
## 1. Tải các thư viện cần thiết.
Bài làm sử dụng 2 thư viện để hỗ trợ vẽ hình của Otomat và hiển thị bảng chuyển trạng thái.


```
pip install -r requirements.txt
```
## 2. Định dạng dữ liệu

Dữ liệu vào ở file `input.json`, dữ liệu ra ở file `output.json`

Dữ liệu ở `input.json` có dạng:
```
{
    "states": danh sách các trạng thái,
    "alphabets": danh sách các chữ cái,
    "start": trạng thái đầu,
    "finals": danh sách các trạng thái kết,
    "transitions": {
        Có dạng hashmap: trạng thái: {chữ cái: trạng thái}. Ví dụ
        
        "q0": {"0": "q1", "1": "q5"},
        "q1": {"0": "q6", "1": "q2"},
        "q2": {"0": "q0", "1": "q2"},
        "q3": {"0": "q2", "1": "q6"},
        "q4": {"0": "q7", "1": "q5"},
        "q5": {"0": "q2", "1": "q6"},
        "q6": {"0": "q6", "1": "q4"},
        "q7": {"0": "q6", "1": "q2"}
    }
}
```
Dữ liệu ra ở file output.json cũng có dạng tương tự.

Ngoài ra còn có 2 file là `dfa_input.pdf` và `dfa_output.pdf` là 2 file pdf chứa hình ảnh của Otomat nhập vào và ra.

## 3. Chạy chương trình
```
python minDFA.py
```