def find_horse_pivot(n, a):
    inf = 1e9
    row = [inf for i in range(n)] # find minimum point in each row
    col = [-inf for i in range(n)] # find maximum point in each column
    for i in range(n):
        for j in range(n):
            row[i] = min(row[i], a[i][j])
            col[j] = max(col[j], a[i][j])
    answer = []
    for i in range(n):
        for j in range(n):
            if a[i][j] == row[i] == col[j]:
                answer.append(a[i][j])
    return answer

if __name__ == '__main__':
    with open("input1.txt", 'r') as f:
        n = int(f.readline())
        a = [[int(x) for x in f.readline().split()] for i in range(n)]
    
    print("Horse pivot in matrix is: ", end = " ")
    print(find_horse_pivot(n, a))