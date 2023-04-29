a = int(input())
for i in range(a):
    l=list(map(int, input().split()))
    avg=(sum(l)-l[0])/l[0]
    cnt=0
    for i in range(l[0]):
        if  l[i + 1]>avg:
            cnt+=1
    print(f'{cnt/l[0]*100:.3f}%')