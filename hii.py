"""var1 = 598
print( var1, type(var1))
var2 =6.70
print(var2 , type(var2))
var3 = 3 +5j
print(var3 , type(var3))
var4 = "abcdefghijklmnopqrstuvwxyz"
print(var4,type(var4))
var5 ='''
hiiiii
heyyyyyy
hellooooooo
welcome to pythonnnnn
'''
print(var5,type(var5))
var6 = '''
hiiiii
heyyyyyy
hellooooooo
welcome to pythonnnnn
'''
print(var6,type(var6))
nums =[10,8.2,3+5j ,"hgfjf"]
print(nums,type(nums))
print("hellooo")
num_a =int(input("enter anything"))
print(num_a,type(num_a))
print(int(var2))
print(var1,id(var1))
print(var2,id(var2))
print(var3,id(var3))
print(var4,id(var4))
print(var5,id(var5))
print( 7/3)
"""
'''print("A"<"  abc")
sum=0
for i in range(1,6):
    print(i , end =".. ")
    sum=sum+i
print(sum)'''

#print k even no.s
'''k=int(input("enter no.:"))
for i in range(2,k,2):
    print(i)
for i in range(1,17):
    temp=i
    while temp%2==0:
        temp/=2
    if temp!=1:
        continue
    print(i)'''
#printing patterns
"""1 2 3 4 5 6 7 8 9 ....m
1 2 3 4 5 6 7 8 9 ....m
1 2 3 4 5 6 7 8 9 ....m
1 2 3 4 5 6 7 8 9 ....m
1 2 3 4 5 6 7 8 9 ....m
.. for n rows
"""
#code
'''n=int(input())
m=int(input())
for i in range(1,n+1):
    for j in range(1,m+1):
        print(j,end=" ")
    print("")
'''
"""pattern 2 print 
1
1 2
1 2 3
1 2 3 4
n no. for n rows"""
#code:
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print("")
#2nd method
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(j,end=" ")
        else:
            break
    print("")
    '''
'''print
       *
     * *
   * * *
   
 * * * *'''
#code
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("")
'''
'''print
* * * *
* * *
* *
*
'''
#coden=int(input())
'''for i in range(1,n+1):
    for j in range(n+1):
        if j>=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
    '''
'''print
*
* *
* * *
* * * *'''
#code
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")'''
#function defination uses parameters
#function call uses arguments
'''def to_sum(a,b):
   
    sum=a+b
    print(sum)
a=int(input("first no."))
b=int(input("second no."))
to_sum(a,b)
def greet():
    print("helllo")
greet()'''



'''recursion is the process of calling the function inside the function.
It uses stack but recursion without definig parameter and incrementing
or decrementing the value can cause an infinite loop'''
'''def myfun1(x):
    if x==0:
        return
    print(x)
    myfun1(x-1)
y=30
myfun1(y)

def myfun2(x):
    if x==0:
        return
    myfun2(x-1)
    print(x)
z=30
myfun2(z)
#factorial of n 
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
factorial = fact(8)
print(factorial)


#fibonacci series
def fibo(x):
    if x==2 or x==1:
        return 1
    return fibo(x-1)+fibo(x-2)
fibonacci=fibo(10)
print(fibonacci)'''

#sum of all elements of a list
'''
n=int(input("enter the length of list"))
mylist=input().split()
sum=0
for i in range(n):
    sum+=int(mylist[i])
    mylist[i]=int(mylist[i])
print("sum of list is :",sum)
minEle=mylist[0]
maxEle=mylist[0]
for val in mylist:
    print(val,end=" ")
    if val<minEle:
        minEle=val
    if val>maxEle:
        maxEle=val
print("minEle is :",minEle , "maxEle is:",maxEle)
'''
#mean , mode and median of a list
#mean
'''n=int(input())
mylist=input().split()
sum=0
for val in mylist:
    sum=sum+int(val)
print(sum/n)
'''
#median
'''
n=int(input())
mylist=input().split()
for i in range(n):
    mylist[i]=int(mylist[i])
mylist.sort()
if n%2!=0:
    print(mylist[n//2])
else:
    ele1=mylist[n//2-1]
    ele2=mylist[n//2]
    print((ele1+ele2)/2)
print(mylist)'''
#list comprehension
#element for item in sequence
'''
mylist=[ele for ele in range(0,25,5)]
print(mylist)
listb=[ele*2 for ele in range(0,25,5)]
print(listb)
lista =[ele for ele in input().split()]
print(lista)
sum=""
for i in range(len(lista)):
    sum=sum+lista[i]
print(sum)'''
#2D lists
#2d list is a list of lists 
#eg 3*3 matrix as a 2d list
'''grid=[[1,2,3],[4,5,6],[7,8,9]]
print(grid,sep="/n")
print(grid[0])
print(grid[1])
print(grid[2])
#orr 2 access a particular element
for i in range(len(grid)):
    for j in range(len(grid)):
        print(grid[i][j])
'''
#traverse a grid and take input
'''grid=[]
n=int(input("no. of rows"))
m=int(input("no. of columns"))
for i in range(n):
    templist=input().split()
    for j in range(m):
        templist[j]=int(templist[j])
    grid.append(templist)
print(grid)
'''
#shortcut for input and then trace of a matrix is included

n=int(input("enter no. of rows"))
m=int(input("enter no. of columns"))
grid=[]
for i in range(n):
    grid.append([int(item)for item in input().split()])
print(grid)
trace=0
'''for j in range(n):
    for k in range(n):
        if k==j:
            trace= trace +grid[j][k]
print(trace)'''
            #or
'''
for j in range(n):
    trace=trace+grid[j][j]
print(trace)'''


#to find transpose of a matrix
for i in range(n):
    for j in range(i,n):
        if i!=j:
            grid[i][j],grid[j][i]=grid[j][i],grid[i][j]

print(grid)