# isdhw
#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from dbconn import db_cursor


def write_grade(stu_no, cou_no, grade):
    """��дѧ��stu_no��ӿγ̱��Ϊcou_no�ĳɼ�"""

    with db_cursor() as cur : # ȡ�ò������ݵ��α꣬��Ϊcur

        s = 'SELECT sn, name FROM student WHERE no=%(stu_no)s'
        cur.execute(s, dict(stu_no=stu_no))
        stu = cur.fetchone() # ����ȡ��һ�е����ݣ�������(sn, name)
        print(stu)                   # ���û��һ�����ݷ��أ��򷵻ص���None
        if stu is None : 
            print('�Ҳ���ѧ��(%s)' % stu_no)
            return

        s = 'SELECT sn, name FROM course WHERE no=%(cou_no)s'
        cur.execute(s, dict(cou_no=cou_no))
        cou = cur.fetchone() # ����ȡ��һ�е�����
        if cou is None :
            print('�Ҳ����γ�(%s)' % cou_no)
            return

        s = """
        UPDATE course_grade SET
           grade = %(grade)s
        WHERE stu_sn = %(stu_sn)s AND cou_sn= %(cou_sn)s
        """
        cur.execute(s, dict(stu_sn=stu[0],
                    cou_sn=cou[0],
                    grade=grade))
        if cur.rowcount == 0:
            # rowcount, ���һ��ִ��SQL�������漰������
            # ���ѧ���Ϳγ̶��ҵ��������ٸ���һ����
            # ��֮��û�ҵ��ɸ��µģ������Ҫ����һ���µ�
            s = """
            INSERT INTO course_grade (stu_sn, cou_sn, grade)
                VALUES (%(stu_sn)s, %(cou_sn)s, %(grade)s)
            """
            cur.execute(s, dict(stu_sn=stu[0],
                                cou_sn=cou[0],
                                grade=grade))
            print('���%s��%s�ɼ�%.2f' % (stu[1], cou[1], grade))
        else:
            print('����%s��%s�ɼ�%.2f' % (stu[1], cou[1], grade))
            

def list_grades(stu_no):
    """��ӡ��ѧ��Ϊstu_noѧ�������пγ̳ɼ������տγ̺Ŵ�С��������"""
    with db_cursor() as cur : 
        s = 'SELECT sn,name FROM student WHERE no=%(stu_no)s'
        cur.execute(s, dict(stu_no=stu_no))
        stu = cur.fetchone()
        b=[101,102,103]
        for i in range(0,len(b)):
            s = 'SELECT grade FROM course_grade WHERE stu_sn=%(a)s AND cou_sn=%(c)s'
            cur.execute(s, dict(a=stu[0],c=b[i]))
            stu1 = cur.fetchone()
            s = 'SELECT name FROM course WHERE sn=%(d)s'
            cur.execute(s, dict(d=b[i]))
            stu2 =cur.fetchone()
            if stu1==None:
                print('%s��%s�εĳɼ�������'%(stu[1],stu2[0]))
            else:
                print('%s��%s�ɼ���%d'%(stu[1],stu2[0],stu1[0]))
    # TODO: ����3 ʵ�ָú���
    # ��ʾ��
    #  1. д��SQL��SELECT��䣬��ʹ��executeִ�У�
    #  2. ����fetchall()ȡ��ȫ���������һ���еĽ��в���
    # ���磺
    #   for row in cur:
    #      ....
    # ��
    #   for row in cur.fetchall()
    #      ....
    

def delete_grades(stu_no, cou_no):
    """ɾ��ѧ��Ϊstu_noĳ�ſγ̵ĳɼ����ÿγ̱���Ϊcou_no"""
    with db_cursor() as cur :
        a=['S002','S003','S004']
        b=['C01','C02','C03']
        if((stu_no in a) and (cou_no in b)):
            s = 'SELECT sn,name FROM student WHERE no=%(stu_no)s'
            cur.execute(s, dict(stu_no=stu_no))
            stu = cur.fetchone()
            s = 'SELECT sn FROM course WHERE no=%(cou_no)s'
            cur.execute(s, dict(cou_no=cou_no))
            stu1 = cur.fetchone()
            s = """DELETE
                   FROM course_grade
                   WHERE stu_sn=%(stu_no)s AND cou_sn=%(cou_no)s"""
            cur.execute(s, dict(stu_no=stu[0],cou_no=stu1[0]))
            print("ɾ���ɹ�")
        else:
            print("û�и�ѧ���Ż��߿γ̺�")
    # TODO: ����4 ʵ�ָú���
    # д����Ӧ��SQL��䣬��ִ�У�
    # ע�⣬���û�иÿγ̻��ѧ��Ӧ���Ѻõ���ʾ

  
if __name__ == '__main__':

    write_grade('S004', 'C01', 88.5)
    write_grade('S004', 'C02', 76.0)
    write_grade('S004', 'C03', 68.0)

    print('[1]' + '==' * 20)
    list_grades('S002')

    print('[2]' + '==' * 20)
    delete_grades('S004', 'C02')
    delete_grades('S004', 'C10')

    print('[3]' + '==' * 20)
    list_grades('S004')

