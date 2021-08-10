N = int(input())
cnt = N
if N==1:
    print("")
i=2
while True:
    if N%i==0:
        print(i)
        N=N//i
    else:
        i+=1
    if i>cnt:
        break