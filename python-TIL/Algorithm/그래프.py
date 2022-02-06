## 함수
class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.gragh = [[ 0 for _ in range(size)] for _ in range(size)]

## 전역
G = None

## 메인
G = Graph(4)
G.gragh[0][1] = 1; G.gragh[0][2]=1; G.gragh[0][3] = 1

for row in range(4):
    for col in range(4):
        print(G.gragh[row][col], end=' ')
    print()