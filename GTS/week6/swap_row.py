import numpy as np
def swap_row(v: np.ndarray, i: int, j: int):
    if len(v.shape) == 1:
        v[i][j], v[j][i] = v[j][i], v[i][j]
    else:
        v[i], v[j] = v[j], v[i]

# np.argmax(A:np.ndarray) -> vị trí của phần tử lớn nhất
# np.argmax(np.abs(A):np.ndarray) -> vị trí của phần tử có || lớn nhất
# np.argmax(abs(a[i])) # mảng 2 chiều 
a = np.array([[10, 9, 3], [0., 7., -11.], [8,5,4]])
i = 1
k = 2
print(np.argmax(abs(a[i,k:])))