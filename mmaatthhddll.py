import cmath

print("ax^2 + bx + c = 0 형태의 방정식을 풀겠습니다.")
a = float(input("x^2의 계수의 값을 입력하세요: "))
b = float(input("x의 계수의 값을 입력하세요: "))
c = float(input("상수항의 값을 입력하세요: "))

D = b**2 - 4*a*c  # 판별식 계산
if D == 0:
    x = -b / (2 * a)  # 중근
    print(f"방정식의 해는 중근인 {x}입니다.")
elif D > 0:
    x1 = (-b + cmath.sqrt(D)) / (2 * a)
    x2 = (-b - cmath.sqrt(D)) / (2 * a)
    print(f"방정식의 해는 {x1}와 {x2}입니다.")
else:
    real_part = -b / (2 * a)
    imaginary_part = cmath.sqrt(-D) / (2 * a)
    x1 = complex(real_part, imaginary_part)
    x2 = complex(real_part, -imaginary_part)
    print(f"방정식의 해는 허수인 {x1}와 {x2}입니다.")