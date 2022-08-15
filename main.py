import math
import pathlib

class Student:
    def __init__(self, ten, tuoi, diem):
        self.ten = ten
        self.tuoi = tuoi
        self.diem = diem

class Danhsach:
    def __init__(self, students):
        self.students = students

def read_student():
    ten = input('\t\t[?] Nhap ten: ')
    tuoi = input(select_in_range('\t\t[?] Nhap tuoi: ',1, math.inf))
    diem = input(select_in_range('\t\t[?] Nhap diem: ',1,math.inf))
    student = Student(ten, tuoi, diem)
    return student

def read_students():
    students = []
    total_student = select_in_range('\t- So luong sinh vien muon nhap: ', 1, math.inf)
    for i in range(total_student):
        print('\t- Nhap sinh vien thu', i+1)
        student = read_student()
        students.append(student)
    return students

def print_student(student):
    print(student.ten, student.tuoi, student.diem)

def print_students(students):
    for i in range(len(students)):
        print('\t'+"| {} | {} | {} | {} |".format(str(i+1).center(4), students[i].ten.center(20), students[i].tuoi.center(6), students[i].diem.center(10)))
    print('\t'+"".center(53, "-"))

def write_student_to_txt(student, file):
    line = student.ten    + '|' + \
                str(student.tuoi) + '|' + \
                str(student.diem) +'\n'
    file.write(line)

def write_students_to_txt(students, file):
    # with open('data.txt', 'a') as file:
    for i in range(len(students)):
        write_student_to_txt(students[i], file)

def read_students_from_txt(file):
    students = []
    # with open('data.txt', 'r') as file:
    for line in file:
        info = line.replace('\n', '').split('|')
        students.append(Student(*info))
    return students

def read_danhsach():
    students = read_students()
    danhsach = Danhsach(students)
    return danhsach

def write_danhsach_txt(danhsach):
    with open('data.txt', 'w') as file:
        write_students_to_txt(danhsach.students, file)
    print('\n\t>>>[!] Sao luu thanh cong.', end='')
def read_danhsach_form_txt():
    with open('data.txt', 'r') as file:
        students = read_students_from_txt(file)
        danhsach = Danhsach(students)
    return danhsach

def print_danhsach(danhsach):
    setup_table()
    print_students(danhsach.students)


def show_menu():
    print('Danh sach thao tac:')
    print('-------------------------------------')
    print('|Option 1: Khoi tao danh sach       |')
    print('|Option 2: In danh sach             |')
    print('|Option 3: Them sinh vien           |')
    print('|Option 4: Xoa thong tin sinh vien  |')
    print('|Option 5: Sua thong tin sinh vien  |')
    print('|Option 6: Tim kiem                 |')
    print('|Option 7: Sap xep                  |')
    print('|Option 8: Sao luu                  |')
    print('|Option 9: Thoat                    |')
    print('-------------------------------------')

def select_in_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(prompt)
    choice = int(choice)
    return choice

def add_student(danhsach):
    total_student = select_in_range('\t- So luong sinh vien muon nhap: ', 1, math.inf)
    for i in range(total_student):
        print('\t\t[*] Nhap sinh vien thu', i+1)
        student = read_student()
        print('\t\t---------')
        danhsach.students.append(student)
    print('\n\t>>>[!] Thao tac them sinh vien thanh cong.')
    return danhsach

def remove_student(danhsach):
    print_students(danhsach.students)
    choice = select_in_range('[?] Nhap STT sinh vien muon xoa: ',1 ,len(danhsach.students))
    # del danhsach.students[choice-1] # cach 1
    # cach 2
    new_student_list = []
    for i in range(len(danhsach.students)):
        if i == choice-1:
            continue
        new_student_list.append(danhsach.students[i])
    danhsach.students = new_student_list
    print('\n\t>>>[!] Thao tac xoa thong tin sinh vien thanh cong.')
    return danhsach

def update_student(danhsach):
    print_students(danhsach.students)
    choice = select_in_range('\tNhap STT sinh vien muon sua: ',1, len(danhsach.students))
    new_student = read_student()
    for i in range(len(danhsach.students)):
        if i == choice-1:
            danhsach.students[i] = new_student
    print('\n\t>>>[!] Thao tac sua thong tin sinh vien da thanh cong.')
    return danhsach

def setup_table():
    print('\t'+"".center(53, "-"))
    print('\t'+"| {} | {} | {} | {} |".format("STT".center(4), "Ten".center(20), "Tuoi".center(6), "Diem".center(10)))
    print('\t'+"".center(53, "-"))
                
def find_student(danhsach):
    find_list = []
    find = input('\t[?] Nhap tu khoa tim kiem: ')
    for i in range(len(danhsach.students)):
        if find in danhsach.students[i].ten:
            find_list.append(danhsach.students[i])
    return find_list

def sort_function(danhsach):
    choice = select_in_range(('''\
\t[!] Chon Option sap xep:
\t[!] 1 - Sap xep theo ten ABC
\t[!] 2 - Sap xep theo tuoi tang dan
\t[!] 3 - Sap xep theo diem tang dan 
\t Chon (1->3):'''),1,3)
    li = danhsach.students.copy()
    if choice == 1:
        for i in range(len(li)):
            for j in range(i+1,len(li)):
                s1 = li[i].ten.split(' ')[-1]
                s2 = li[j].ten.split(' ')[-1]
                if s1 > s2:
                    li[i],li[j] = li[j],li[i]
        setup_table()
        print_students(li)
    elif choice == 2:
        for i in range(len(li)):
            for j in range(i+1,len(li)):
                s1 = int(li[i].tuoi)
                s2 = int(li[j].tuoi)
                if s1 > s2:
                    li[i],li[j] = li[j],li[i]
        setup_table()
        print_students(li)
    elif choice == 3:
        for i in range(len(li)):
            for j in range(i+1,len(li)):
                s1 = int(li[i].diem)
                s2 = int(li[j].diem)
                if s1 > s2:
                    li[i],li[j] = li[j],li[i]
        setup_table()
        print_students(li)
    
    
            
def main():
    
    p = pathlib.Path('data.txt')
    p.touch()

    danhsach = read_danhsach_form_txt()

    while True:
        show_menu()
        if len(danhsach.students) == 0:
            print('\n [!!!] Danh sach sinh vien chua khoi tao. Chon Option 1 de khoi tao danh sach !!!\n')
            choice = select_in_range('Chon option (1-8): ', 1, 1)
            if choice == 1:
                print('[1] Khoi tao danh sach.')
                danhsach = read_danhsach()
                write_danhsach_txt(danhsach)
                print(' Danh sach da duoc khoi tao.')
                input('\nPress Enter to continue.\n')
        else:
            print('\n\t[!] Danh sach da khoi tao. Vui long bo qua Option 1.!!!\n')
            choice = select_in_range('Chon option (1-8): ', 2, 9)
            if choice == 2:
                print('[2] In danh sach.')
                print_danhsach(danhsach)
                input('\nPress Enter to continue.\n')
            if choice == 3:
                print('[3] Them sinh vien.')
                danhsach = add_student(danhsach)
                input('\nPress Enter to continue.\n')
            if choice == 4:
                print('[4] Xoa thong tin sinh vien.')
                setup_table()
                danhsach = remove_student(danhsach)
                input('\nPress Enter to continue.\n')
            if choice == 5:
                print('[5] Sua thong tin sinh vien.')
                setup_table()
                danhsach = update_student(danhsach)
                input('\nPress Enter to continue.\n')
            if choice == 6:
                print('[6] Tim kiem.')
                student = find_student(danhsach)
                if len(student) > 0:
                    setup_table()
                    print_students(student)
                else:
                    print('\n\t>>>[!] Tu khoa tim kiem khong ton tai.')
                input('\nPress Enter to continue.\n')
            if choice == 7:
                print('[7] Sap xep.')
                sort_function(danhsach)
                input('\nPress Enter to continue.\n')
            if choice == 8:
                print('[8] Sao luu.')
                write_danhsach_txt(danhsach)
                print()
                input('\nPress Enter to continue.\n')
            if choice == 9:
                print('[9] Thoat.')
                break

main()
    
