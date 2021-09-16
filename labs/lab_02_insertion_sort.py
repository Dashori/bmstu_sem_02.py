##Лабораторная работа 2
##Сортировка вставками

from tkinter import *
from tkinter import messagebox 
from random import *
import time

numbers='0123456789'


def define(el):             ##функция для определения элемент
    el1=list(str(el))       ##разбиение вставляемого элемента на список для проверки
    minus=0                 ##есть ли минус
    point=0                 ##point-количество точек  элементе
    kol=0                   ##kol-количество цифр в элементе
    if len(el1)==0:
        return 1
    if el1[0]=='-':      ##проверка является ли элемент отрицаельным числом
        minus=1
    for i in range(len(el1)):
        if el1[i]=='.':               ##проверка является ли элемент числом  типа float
            return 1   
        if el1[i] in numbers:             ##подсчет количества цифр в элементе
            kol=kol+1
    if el1[0]!='.' or el1[len(el1)-1]!='.':
        point==2
            
    if point==0 and minus==0 and len(el1)==kol:      ##если число целое и положительное
        el=int(el)
        if el>0:
            return 0
    else:                                   
        return 1    


def insertion(line_1): ##сортировка вставками
    for i in range(len(line_1)):
        j = i - 1 
        key = line_1[i]
        while line_1[j] > key and j >= 0:
            line_1[j + 1] = line_1[j]
            j -= 1
        line_1[j + 1] = key
    return line_1
    
def check(line): ##проверка на валидность данных
    line_sep=line.split()
    line_1=[]

    if len(line)==0:
        messagebox.showerror('Ошибка','Проверьте валидность данных')
        return 1
    try:
        for i in range(len(line_sep)):
            line_1.append(float(line_sep[i]))
    except:
        messagebox.showerror('Ошибка','Проверьте валидность данных ')
        line_1=[]        
    if len(line_1)>10:
        messagebox.showerror('Ошибка','Максимально количество элементов 10')
    else:        
        if len(line_1)<11:            
            line_1=insertion(line_1)
        output_array.config(state='normal')
        for i in range(len(line_1)):
            output_array.insert('end','{:^g}'.format(line_1[i]))
            output_array.insert('end','   ')
        output_array.config(state='readonly')
        input_array.config(state='readonly')
            
def time_check(n): ##функция для подсчета времени
    arr=[uniform(-1000000,1000000) for x in range(n)]
    
    t0= time.time()
    arr_sort=insertion(arr)
    t1 = (time.time() - t0)  * 1e6  ##время сортировки рандомного массива
    
    t0=time.time()
    arr_sort=insertion(arr_sort)
    t2=(time.time()-t0) * 1e6  ##время сортировки упорядоченного массива
    
    arr_reverse=arr_sort[::-1]

    t0=time.time()
    insertion(arr_reverse)
    t3=(time.time()-t0) * 1e6   ##время сортировки обратно упорядоченного массива

    return t1,t2,t3

def time_table(n1,n2,n3):  ##функция заполняющая таблицу времени
    
    if define(n1)==0 and define(n2)==0 and define(n3)==0:
        
        n1=int(n1)
        
        arr_1=(time_check(n1))

        arr_1_rand.config(text='{:.3f}'.format(arr_1[0]))

        arr_1_sort.config(text='{:.3f}'.format(arr_1[1]))

        arr_1_reverse.config(text='{:.3f}'.format(arr_1[2]))
        
        n2=int(n2)
        arr_2=(time_check(n2))

        arr_2_rand.config(text='{:.3f}'.format(arr_2[0]))

        arr_2_sort.config(text='{:.3f}'.format(arr_2[1]))

        arr_2_reverse.config(text='{:.3f}'.format(arr_2[2]))
        
        n3=int(n3)
        arr_3=(time_check(n3))
        
        arr_3_rand.config(text='{:.3f}'.format(arr_3[0]))

        arr_3_sort.config(text='{:.3f}'.format(arr_3[1]))

        arr_3_reverse.config(text='{:.3f}'.format(arr_3[2]))

    else:
        messagebox.showerror('Ошибка','Проверьте валидность данных')


def clear_1():  ##функция отчистки для первого массива
    output_array.config(state='normal')
    output_array.delete(0,'end')
    input_array.config(state='normal')
    input_array.delete(0,'end')
    output_array.config(state='readonly')
        
def clear_tabl(): ##функция отчистки таблицы
    arr_1_rand.config(text='')
    arr_1_sort.config(text='')
    arr_1_reverse.config(text='')
    
    arr_2_rand.config(text='')
    arr_2_sort.config(text='')
    arr_2_reverse.config(text='')
    
    arr_3_rand.config(text='')
    arr_3_sort.config(text='')
    arr_3_reverse.config(text='')
    
    size_1.delete(0,'end')
    size_2.delete(0,'end')
    size_3.delete(0,'end')

window=Tk()
window.title('Сортировка вставками')
window.geometry('600x400')

N0=Label(text='Введите элементы массива через пробел:')
N0.place(x=50,y=40)

input_array=Entry(width=45)
input_array.place(x=290,y=40)

input_sort=Button(text='Отсортировать',command = lambda: check(input_array.get()))
input_sort.place(x=50,y=70)

clear_sort_1=Button(text='Отчистить', command= lambda: clear_1())
clear_sort_1.place(x=150,y=70)

output_array=Entry(width=45)
output_array.config(state='readonly')
output_array.place(x=290,y=80)


random_array=Label(text='Случайный массив', width=20)
random_array.place(x=35,y=170)

ordered_array=Label(text='Упорядоченный массив',width=20)
ordered_array.place(x=50,y=200)

reverse_array=Label(text='Обратно упорядоченный массив')
reverse_array.place(x=51,y=230)

##лейблы и окна ввода для кол-ва чисел

N1_label=Label(text='N1 =')
N2_label=Label(text='N2 =')
N3_label=Label(text='N3 =')

N1_label.place(x=250,y=145)
N2_label.place(x=330,y=145)
N3_label.place(x=410,y=145)

size_1=Entry(width=5)
size_2=Entry(width=5)
size_3=Entry(width=5)

size_1.place(x=280,y=145)
size_2.place(x=360,y=145)
size_3.place(x=440,y=145)

##лейблы для вывода результатов таблицы

arr_1_rand=Label(text='')
arr_1_rand.place(x=270,y=170)

arr_1_sort=Label(text='')
arr_1_sort.place(x=270,y=200)

arr_1_reverse=Label(text='')
arr_1_reverse.place(x=270,y=230)


arr_2_rand=Label(text='')
arr_2_rand.place(x=350,y=170)

arr_2_sort=Label(text='')
arr_2_sort.place(x=350,y=200)

arr_2_reverse=Label(text='')
arr_2_reverse.place(x=350,y=230)

arr_3_rand=Label(text='')
arr_3_rand.place(x=420,y=170)

arr_3_sort=Label(text='')
arr_3_sort.place(x=420,y=200)

arr_3_reverse=Label(text='')
arr_3_reverse.place(x=420,y=230)


generate=Button(text='Сформировать таблицу ', command= lambda: time_table(size_1.get(),size_2.get(),size_3.get()))
generate.place(x=50,y=140)

clear=Button(text='Очистить', command= lambda: clear_tabl() )
clear.place(x=50,y=260)

window.mainloop()
