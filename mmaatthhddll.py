import cmath, math

def solve():

    while True:
        try:
            a = float(input("x^2의 계수의 값을 입력하세요: "))
            b = float(input("x의 계수의 값을 입력하세요: "))
            c = float(input("상수항의 값을 입력하세요: "))
        except Exception:
            print("입력값을 확인하세요. 숫자만 입력 가능합니다. 다시 시도하세요.")
            continue
        if a == 0:
            print("이차방정식이 성립하지 않습니다.다시 시도하세요")
            continue

        D = b**2 - 4*a*c  # 판별식 계산

        if D == 0:
            x = -b / (2 * a)  # 중근
            print(f"방정식의 해는 중근인 {x}입니다.")
        elif D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            print(f"방정식의 해는 {x1}와 {x2}입니다.")
        else:
            real_part = -b / (2 * a)
            imaginary_part = cmath.sqrt(-D) / (2 * a)
            x1 = complex(real_part, imaginary_part)
            x2 = complex(real_part, -imaginary_part)
            print(f"방정식의 해는 허수인 {x1}와 {x2}입니다.")
        break    
        
def r_continue():
    r = input("계속하시겠습니까? (y/n): ")
    if r.lower() == 'y':
        solve()
        r_continue()
    elif r.lower() == 'n':
        print("프로그램을 종료합니다.")
    else:
        print("잘못된 입력입니다. y 또는 n을 입력하세요.")

print("ax^2 + bx + c = 0 형태의 방정식을 풀겠습니다.")
solve()
r_continue()

