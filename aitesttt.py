def input_matrix(rows, cols, name):
    # 사용자가 행렬의 각 값을 입력하도록 하는 함수
    print(f"{name} 행렬의 값을 입력하세요:")
    matrix = []  # 입력받은 행렬을 저장할 리스트
    for i in range(rows):  # 각 행에 대해 반복
        row = []  # 한 행의 값을 저장할 리스트
        for j in range(cols):  # 각 열에 대해 반복
            # 사용자에게 값을 입력받음
            val = int(input(f"{name}[{i+1}][{j+1}] 값: "))
            row.append(val)  # 입력받은 값을 행에 추가
        matrix.append(row)  # 완성된 행을 행렬에 추가
    return matrix  # 완성된 행렬 반환

def multiply_matrices(A, B):
    # 두 행렬 A와 B를 곱하는 함수
    result = []  # 결과 행렬을 저장할 리스트
    rows_A = len(A)  # A의 행 개수
    cols_A = len(A[0])  # A의 열 개수 (B의 행 개수와 같아야 함)
    cols_B = len(B[0])  # B의 열 개수
    for i in range(rows_A):  # 결과 행렬의 각 행에 대해 반복
        row = []  # 결과 행렬의 한 행
        for j in range(cols_B):  # 결과 행렬의 각 열에 대해 반복
            sum = 0  # 곱셈 결과를 누적할 변수
            for k in range(cols_A):  # 곱셈 및 덧셈 연산
                # A의 i번째 행과 B의 j번째 열의 곱을 누적
                sum += A[i][k] * B[k][j]
            row.append(sum)  # 계산된 값을 행에 추가
        result.append(row)  # 완성된 행을 결과 행렬에 추가
    return result  # 결과 행렬 반환

# 첫 번째 행렬의 크기 입력
rows_A = int(input("첫 번째 행렬의 행 개수: "))
cols_A = int(input("첫 번째 행렬의 열 개수: "))

# 두 번째 행렬의 크기 입력
rows_B = int(input("두 번째 행렬의 행 개수: "))
cols_B = int(input("두 번째 행렬의 열 개수: "))

# 행렬 곱셈이 가능한지 확인
if cols_A != rows_B:
    print("행렬 곱셈이 불가능합니다. (첫 번째 행렬의 열 개수와 두 번째 행렬의 행 개수가 같아야 합니다.)")
else:
    # 두 행렬의 값을 입력받음
    A = input_matrix(rows_A, cols_A, "A")
    B = input_matrix(rows_B, cols_B, "B")

    # 행렬 곱셈 수행
    result = multiply_matrices(A, B)

    # 결과 출력
    print("행렬 곱셈 결과:")
    for row in result:
        print(row)