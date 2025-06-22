import cmath, math

def solve():
    try:
        #  a,b,c값 입력
        a = int(input("x^2의 계수를 입력해 주세요.:"))
        b = int(input("x의 계수를 입력해 주세요.:"))
        c = int(input("상수항을 입력해 주세요.:"))
        if a == 0:
            print("a의 값이 0이 되면 이차방정식이 성립되지 않습니다.")
            r_return()
            return
            
        #판별식
        D = b**2 - 4*a*c
        #근의 형식 탐색
        if D == 0:
            x = -b/(2*a)
            print(f"이 방정식의 해는 중근으로 {x} 입니다.")
        elif D >0:
            x1 = (-b + math.sqrt(D))/(2*a)
            x2 = (-b - math.sqrt(D))/(2*a)
            print(f"이 방정식의 해는 {x1}, {x2} 입니다.")            
        else:
            x1 = (-b + cmath.sqrt(D))/(2*a)
            x2 = (-b - cmath.sqrt(D))/(2*a)
            print(f"이 방정식의 해는 허근인 {x1}, {x2} 입니다.")
    except ValueError:
        print("숫자만 입력 가능합니다. 값을 확앤해 주세요")
        r_return()
        return
    except Exception:
        print("예기치 못한 오류가 발생하였습니다. 다시 시도해 주세요.")
        r_return()
    r_return()  
            
            
def r_return():
    answer = input("프로그램을 다시 시작할까요? (y/n)").strip()
    if answer.lower() == "y":
        solve()
    elif answer.lower() == "n":
        print("프로그램을 종료합니다.")
    else:
        print("잘못된 입력입니다. 입력을 검토해 주세요.")
        r_return()
            
            
print("a^2 + bx + c = 0 꼴의 이차방정식의 근을 구하는 프로그램을 실행하겠습니다.")            
solve()        