## 함수
def countdown(n):
    if n == 0:
        print('발싸!')
    else:
        print(n)
        countdown(n-1)

countdown(5)