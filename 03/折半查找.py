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
stu=input("������Ҫ�����ҵ����У����Զ��Ÿ��������� 1,2,3,4 ���մӴ�С˳��")
stu1=eval(stu)
stu2=list(stu1)
a=stu2
i=int(input("��������Ҫ���ҵ�����"))
b=f(a,i)
if b==0:
    print('û���ҵ�')
else:
    print("�ҵ��ˣ���Ҫ�ҵ������б��еĵ�{0}��λ��".format(b))
    


