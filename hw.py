from random import randint
'''print('----TASk1----')
k=int(input())
n=[]
m=[]
for i in range(k):
    n.append(randint(0,1000))
    m.append(randint(0,26*n[i]**2))
print(n,m)
for i in range(k):
    d=19*m[i]+(n[i]+239)*(n[i]+366)/2
    print (d)

print('----TASk2----')
pl=str(input())
x=randint(1,1000)
print('total rides:', x)
if pl=='School':
    if x//2==0:
        print('NO')
    else:
        print('YES')
elif pl=='Home':
    if x//2==0:
        print('YES')
    else:
        print('NO')
else:
    print("wrong")
print('----TASk3----')    
n= int(input())
max=[]
cnt=[]
for i in range (n):
  max.append(int(input()))
  cnt.append(0)
k=int(input())
for i in range (k):
  read=int(input())
  cnt[read-1]+=1
for i in range (n):
  if cnt[i]>max[i]:
    print('YES')
  else:
    print('NO')
    
print('----TASk4----')
a=[int(i) for i in input().split()]
b=a[:4]
b.sort
if a[5]>a[4]:
    print(b[-1]*a[5]+b[-2]*a[4])
else:
    print(b[-1]*a[4]+b[-2]*a[5])

print('----TASk5----')
print('input asleep time and awake time')
a=[int(i) for i in input().split()]
time= a[1]-a[0]
if time>12:
    time= time-12
print (time)

print('----TASk6----')
print('введите A B C T')
a=[int(i) for i in input().split()]
if a[3]>a[0]:
    print(30*((a[3]-a[0])*a[2] + a[0]*a[1]))
else:
    print(a[3]*a[1])
    '''



