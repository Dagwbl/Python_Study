#encoding:utf8
import csv
import random
import time
import shutil,os
from tkinter import messagebox

Studentsfile = 'Students.csv'
Students_edfile = 'Students_ed.csv'

def reset_nd():
    with open(Students_edfile,'w') as New_file:
        jud = messagebox.askyesno('Warning','Are you sure reset named file? This operation is irreversible.')
        if jud:
            messagebox.showinfo('Tips','The file has been reset, now you can begin a new lap.')
        else:
            pass

def inquire_ed():
    counter1 = 0
    counter2 = 0
    surplus = 0
    list1 =[]
    list2 = []
    with open(Studentsfile,'r',newline = '') as students:
        reader = csv.reader(students)
        for j in reader:
            # print(row)
            if j:
                counter1+=1
                list1.append(j)
    with open(Students_edfile,'r',encoding = 'utf-8') as students_ed:
        reader_ed = csv.reader(students_ed)
        for y in reader_ed:
            if y:
                counter2+=1
                list2.append(y)

    surplus = counter1-counter2
    return list1,list2,counter1,counter2,surplus

# def unname_person():
#     unname_list = []
#     with open(Studentsfile,'r') as students:
#         reader = csv.reader(students)
#         with open(Students_edfile,'r',encoding = 'utf-8') as students_ed:
#             reader_ed = csv.reader(students_ed)
#             for row in reader:
#                 if row not in reader_ed:
#                     unname_list.append(row)
#                 else:
#                     continue
#     return unname_list

def students_num():
    list1,list2,counter1,counter2,surplus = inquire_ed()
    str0 = 'There are '+str(counter1)+' students in this class.'
    messagebox.showinfo('Students number',str0)

def surplus_num():
    list1,list2,counter1,counter2,surplus = inquire_ed()
    messagebox.showinfo('Surplus number',str(surplus))

def Named():
    list1,list2,counter1,counter2,surplus = inquire_ed()
    print(counter1,counter2,surplus)
    # print(list2)
    if surplus == 0:
        bool_1 = messagebox.askyesno('Tips','Everyone has been called.\nDo you want to reset data?(y/n)')
        if bool_1 == True:
            reset_nd()
        else:
            pass
    else:
        flag = True
        while flag:
            lucky = random.randint(0,counter1-1)
            lucky_person = list1[lucky]
            print(lucky)
            print(lucky_person)
            if  lucky_person not in list2:
                with open(Students_edfile,'a',encoding = 'utf-8',newline = '') as pointed:
                    writer = csv.writer(pointed)
                    writer.writerow(lucky_person)
                    list2.append(lucky_person)
                    flag = False

def replacefile(filename):
    filename = filename
    shutil.move(Studentsfile,'Students_old.csv')
    shutil.move(Students_edfile,'Students_ed_old.csv')
    shutil.copy(filename,Studentsfile)

