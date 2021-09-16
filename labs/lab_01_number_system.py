##Лабораторная работа 1
##Нужно создать интерфейс для перевода чисел
##из 3сс в 10сс и обратно


from tkinter import *
from tkinter import messagebox 
  
third='012.'
def three(x): ##функция для перевода из 3сс в 10
    out.delete(0,'end')
    before=0 ##считаем количество чисел до точки
    after=0 ##считаем количество чисел после точки
    znak='' ## Переменная для запоминания знака
    flag=0 ## Переменная для запоминания есть ли знак
    count=0 ## Переменная для подсчета кол-ва чисел
    point=0 ## Переменная для подсчета точек в числе
    if x[0]=='.':
        flag=1
    if x[0]=='+':
        znak='+'
        x=x[1:]
    elif x[0]=='-':
        znak='-'
        x=x[1:]
    if len(x)<1:
        flag=1
        
    count_p=x.count('.') ##кол-во точек в числе
    for i in range(len(x)):
        if x[i] not in third:
            flag=1
            break
        if x[i] in third and x[i]!='.':
            before+=1
        if x[i]=='.':
            break
    for i in range(before+1,len(x)):
        if x[i] not in third:
            flag=1
            break        
    if flag==0 and count_p<=1:
        after=len(x)-1-before        
        num_before=x[:before] ##число до точки
        num_after=x[before+1:] ##число после точки
        num_before=num_before[::-1] ##перевернутое число до точки для расчетов
        k=1 
        num_b=0
        for i in range(len(num_before)):
            cur=int(num_before[i])*k
            num_b=num_b+cur
            k=k*3
        k=1/3
        num_a=0
        for i in range(len(num_after)):
            cur=int(num_after[i])*k
            num_a=num_a+cur
            k=k/3
        num_10=num_a+num_b
        if znak=='+':
            znak=''
        num_10=float(num_10)
        out.insert(0,znak)
        out.insert(1,'{:^g}'.format(num_10))
        
    else:
        k=lambda: messagebox.showerror('Ошибка','Введите корректное число в 3сс: ')
        k()
        out.insert(0,'')
    
tenth='0123456789.'
def ten(y):
    out.delete(0,'end')
    div=0
    mod=0
    before=0
    num_3='' ##Результат перевода в 3сс
    znak='' ## Переменная для запоминания знака
    flag=0 ## Переменная для запоминания есть ли знак
    count=0 ## Переменная для подсчета кол-ва чисел
    point=0 ## Переменная для подсчета точек в числе
    if y[0]=='.':
        flag=1
    if y[0]=='+':
        znak='+'
        y=y[1:]
    elif y[0]=='-':
        znak='-'
        y=y[1:]
    if len(y)<1:
        flag=1
    count_p=y.count('.')
    for i in range(len(y)):
        if y[i] not in tenth:
            flag=1
            break
        if y[i] in tenth and y[i]!='.':
            before+=1
        if y[i]=='.':
            break
    for i in range(before+1,len(y)):
        if y[i] not in tenth:
            flag=1
            break
    num_b=''
    num_a=''
    if flag==0 and count_p<=1:
        after=len(y)-1-before
        num_before=y[:before] ##число до точки
        num_after=float('0'+y[before:]) ##число после точки
        num_before=int(num_before)
        while num_before>=3:
            mod=str(num_before%3)
            num_before=num_before//3
            num_b+=mod
        
        num_b=num_b[::-1]
        num_b=str(num_before)+num_b
        for i in range(7):
            num_after=num_after*3
            num_after=str(num_after)
            num_a+=num_after[0]
            num_after='0'+num_after[1:]
            num_after=float(num_after)
        num_3=num_b+'.'+num_a
        if znak=='+':
            znak=''
        num_3=float(num_3)
        out.insert(0,znak)
        out.insert(1,'{:^g}'.format(num_3))
    else:
        k=lambda: messagebox.showerror('Ошибка','Введите корректное число в 10сс: ')
        k()
        out.insert(0,'')
        
window = Tk()
window['bg']='grey'
window.title("Перевод чисел из 10-oй системы в 3-yю и обратно")
window.geometry('350x420')

##МЕНЮ
main_menu=Menu(window)
window.config(menu=main_menu)

step_menu=Menu(main_menu,tearoff=0)
step_menu.add_command(label='3 -> 10',command=lambda: three(ent.get()))
step_menu.add_command(label='10 -> 3',command= lambda: ten(ent.get()))
main_menu.add_cascade(label='Заданные действия',menu=step_menu)
main_menu.add_separator()

clear_menu=Menu(main_menu,tearoff=0)
clear_menu.add_command(label='Очистить поле ввода',command=lambda: ent.delete(0,'end'))
clear_menu.add_command(label='Очистить поле вывода',command= lambda: out.delete(0,'end'))

clear_menu.add_command(label='Очистить все поля',command=lambda: (out.delete(0,'end'),ent.delete(0,'end')))
main_menu.add_cascade(label='Очистка полей',menu=clear_menu)

main_menu.add_command(label='Информация',command= lambda: messagebox.showinfo('Информация',
'''Цель программы: перевод чисел из 10-ой системы счисления в 3-ную и обратно
Автор: Чепиго Дарья ИУ7-24Б
'''))


input_num=Label(window,width=20,text='Введите число : ',bg='grey')
ent = Entry(width=40,bg='gray50')
but_3 = Button(text='3 -> 10',command= lambda: three(ent.get()),width=7, height=1, bg='grey',fg='white')
but_10= Button(text='10 -> 3',command= lambda: ten(ent.get()),width=7, height=1, bg='grey',fg='white')
out_num=Label(window,width=20,text='Полученное число : ',bg='grey')
out=Entry(width=40,bg='grey')

##циферки и знаки
def insert_n(x):
    ent.insert('end',x)
    
def exit_program():
    window.destroy()
    
##Кнопки для цифр, + -, очистка полей и выход из приложения 
but_1= Button(text='1',command= lambda: insert_n('1'),width=4, height=3, bg='grey',fg='white')
but_2= Button(text='2',command= lambda: insert_n('2'),width=4, height=3, bg='grey',fg='white')
but__3= Button(text='3',command= lambda: insert_n('3'),width=4, height=3, bg='grey',fg='white')  
but_4= Button(text='4',command= lambda: insert_n('4'),width=4, height=3, bg='grey',fg='white')
but_5= Button(text='5',command= lambda: insert_n('5'),width=4, height=3, bg='grey',fg='white')
but_6= Button(text='6',command= lambda: insert_n('6'),width=4, height=3, bg='grey',fg='white')
but_7= Button(text='7',command= lambda: insert_n('7'),width=4, height=3, bg='grey',fg='white')
but_8= Button(text='8',command= lambda: insert_n('8'),width=4, height=3, bg='grey',fg='white')
but_9= Button(text='9',command= lambda: insert_n('9'),width=4, height=3, bg='grey',fg='white')
but_0= Button(text='0',command= lambda: insert_n('0'),width=4, height=3, bg='grey',fg='white')
but_point= Button(text='.',command= lambda: insert_n('.'),width=4, height=3, bg='grey',fg='white')
but_plus= Button(text='+',command= lambda: insert_n('+'),width=4, height=1, bg='grey',fg='white')
but_minus= Button(text='-',command= lambda: insert_n('-'),width=4, height=1, bg='grey',fg='white')
but_clean= Button(text='C',command= lambda: (ent.delete(0,'end'),out.delete(0,'end')),width=3, height=2, bg='grey',fg='white')
but_bite= Button(text='<-',command= lambda: ent.delete(len(ent.get())-1,len(ent.get())),bg='grey',fg='white',width=2,height=2)
but_exit=Button(text='Exit',command= lambda: exit_program(),bg='grey',fg='white',width=7)

input_num.place(x=100,y=10)
ent.place(x=50,y=30)
out_num.place(x=100,y=60)
out.place(x=50,y=80)
but_3.place(x=190,y=170)
but_10.place(x=190,y=200)
but_1.place(x=60,y=225)
but_2.place(x=100,y=225)
but__3.place(x=140,y=225)
but_4.place(x=60,y=170)
but_5.place(x=100,y=170)
but_6.place(x=140,y=170)
but_7.place(x=60,y=115)
but_8.place(x=100,y=115)
but_9.place(x=140,y=115)
but_0.place(x=60,y=281)
but_point.place(x=100,y=281)
but_plus.place(x=140,y=281)
but_minus.place(x=140,y=311)
but_exit.place(x=190,y=311)
but_clean.place(x=220,y=115)
but_bite.place(x=190,y=115)

window.mainloop()
