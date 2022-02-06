## 함수부
def add_data(friend): # 선형 리스트에 추가
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

def delete_data(position):
    katok[position] = None
    kLen = len(katok)
    for i in range(position+1, kLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[kLen-1])
## 전역변수부
katok = [] # 선형 리스트

##메인코드부
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

#katok.append(None)
#katok[0] = '다현'

#katok.append(None)
#katok[1] = '정현'
print(katok)

add_data('다현')
print(katok)

#katok.append(None)
#katok[6] = katok[5]
#katok[5] = None
#katok[5] = katok[4]
#katok[4] = None
#katok[4] = katok[3]
#katok[3] = None
#katok[3] = '미나'
print(katok)

insert_data(3, '미나')
print(katok)