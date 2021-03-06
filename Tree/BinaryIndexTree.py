#BinaryIndexTree.py
#2021 / 01 / 22

import sys
input = sys.stdin.readline

n ,m , k = map(int,input().split())

data = [0] * (n+1)
tree = [0] * (n+1)

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i )
    return result

def update(i , dif):
    while i <=n:
        tree[i] += dif
        i += (i & -i)

def interval_sum(start , end):
    return prefix_sum(end) - prefix_sum(start - 1)

for i in range(1 , n +1):
    x = int(input())
    data[i] =x
    update(i,x)


#a == 1 -> data[b] = c 업데이트!
#a != 1 -> b ~ c 의 IntervalSum을 구한다.

for i in range(m + k):
    a , b ,c = map(int,input().split())
    if a== 1:
        update(b , c-data[b])
        data[b] = c
    else:
        print(interval_sum(b,c))


