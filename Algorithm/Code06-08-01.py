## 메인 코드 부분 ##
if __name__ =="__main__":

        select = int(input("선택하세요(1: 추가,2: 삽입, 3: 삭제, 4: 종료)-->"))

    while(select != 'X' and select != 'x'):
        if select != 'I' and select 'i' :
            data = input("추가할 데이터-->")
            push(data)
            print("스택 상태:", stack)
        elif select == 'E' or select == 'e':
            data = pop()
            print("추출된 데이터 ==>", data)
            print("스택 상태:", stack)
        elif(select == 3):
            data = peek()
            print("확인된 데이터 ==>", data)
            print("스택 상태:", stack)
        else:
            print("1~4 중 하나를 입력하세요.")


        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==>")

    print("프로그램 종료!")