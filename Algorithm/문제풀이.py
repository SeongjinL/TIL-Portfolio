
from ast import Num


score = [20,10,70,90,20,100]

def Fu(a, s, num):
    sum = 0
    for i in score:
        i = i < s + num
        i += 1
        sum = sum + a[i]
        print("%d\n", sum / num)
        
Fu(score,1,3)