#encoding:utf8
import csv
import random
import time

def Named():
    with open('Students.csv','r') as students:
        reader = csv.reader(students)
        # print(reader)
        list1 =[]
        for row in reader:
            # print(row)
            list1.append(row)
        allnum = len(list1)
    # print(list1)

    with  open('Students_ed.csv','r',encoding = 'utf-8') as students_ed:
        reader2 = csv.reader(students_ed)
        list2 = []
        for row in reader2:
            if row:
                list2.append(row)
        ednum = len(list2)

    flag =True
    jud = allnum-1-ednum
    # print(allnum,ednum,jud)
    if jud ==0:
        print("Everyone has been called.")
        text = input('DO you want reset data?(y/n) ' )
        if text =='y':
            with open('Students_ed.csv','w') as New_file:
                print('The file has been reset, now you can begin a new lap.')
        else:
            print('Have a nice day')
    else:
        print(str(jud) +' others have not been called.')
        while flag:
            lucky = random.randint(1,44)
            lucky_person = list1[lucky]
            # print(lucky)
            # print(lucky_person)

            if  lucky_person not in list2:
                message = 'The lucky person is '+ lucky_person[2]
                print(message)
                with open('Students_ed.csv','a',encoding = 'utf-8') as pointed:
                    fieldnames = ['Sequence','ID','Name']
                    writer = csv.DictWriter(pointed,fieldnames = fieldnames)
                    writer.writerow({'Sequence':lucky_person[0],'ID':lucky_person[1],'Name':lucky_person[2]})
                flag = False
            else :
                continue
time.sleep(1)
while True:
    key = input('Please input command\nc    name\nq    quit\nr    reset\n')
    if key == 'c':
        Named()
    elif key == 'r':
        text = input('DO you want reset data?(y/n) ' )
        if text =='y':
            with open('Students_ed.csv','w') as New_file:
                print('The file has been reset, now you can begin a new lap.')
    elif key == 'q':
        print('Exiting...')
        time.sleep(2)
        break
    else:
        print('Invalid command\n')
        time.sleep(1)
        print('Please enter again. \n')
        pass