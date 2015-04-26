# isdhw
def f(a,i):
    b=0
    c=False
    low=0
    high=len(a)-1
    while(low<(high-1)):
        mid=int((low+high)/2)
        if(a[high]==i):
            b=high
            c=True
            break
        if(a[low]==i):
            b=low
            c=True
            break
        if(a[mid]==i):
            b=mid
            c=True
            break
        elif(a[mid]>i):
            high=mid
        elif(a[mid]<i):
            low=mid
    if(c):
        return(b)

    else:
        return(0)
stu=input("请输入要被查找的序列，并以逗号隔开，例如 1,2,3,4 按照从大到小顺序：")
stu1=eval(stu)
stu2=list(stu1)
a=stu2
i=int(input("请输入你要查找到数："))
b=f(a,i)
if b==0:
    print('没有找到')
else:
    print("找到了，你要找的数在列表中的第{0}个位置".format(b))
    


