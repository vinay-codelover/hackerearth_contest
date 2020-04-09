s = input()
birth = input()
first_gift = int(input())
last_gift = int(input())
s = list(s)
s.sort()
for i in range(len(s)):
    if(s[i]==birth):
        left = s[0:i]
        right = s[i+1:]
        break
left.reverse()
l =[0 for j in range(len(s)-1)]
l[0] = first_gift
l[-1] = last_gift
for i in range(1,(len(l)//2)):
    l[i] = l[i-1]//i
    l[-(i+1)] =(l[-(i+1)+1])//(len(l)-(i+1))
print(' '.join(left+right))
print(' '.join(map(str,l)))
print(sum(l)) 
