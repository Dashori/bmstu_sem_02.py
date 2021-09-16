##Лабораторная работа 4
##Вариант 1

##На плоскости заданы множество точек А и множество прямых В.
##Найти две такие различные точки из А, что проходящая через них
##прямая параллельная наибольшему количеству прямых из B.

from tkinter import *
from tkinter import messagebox
from math import *
import numpy as np
from tkinter import Tk, Canvas,Frame, BOTH

window=Tk()
window.title('')
window.geometry('1000x600')

current_entry = None

##функция для определения положения мышки для ввода

def on_focus(evt):
    global current_entry
    current_entry = evt.widget

def on_click(x):
    if current_entry is not None:
        current_entry.insert('insert',x)

##проверка на валидность данных точек
        
def check_points(line): 
    
    line=str(line)
    line_sep=line.split()
    line_1=[]

    if len(line)==0:
        messagebox.showerror('Ошибка','Проверьте валидность данных для точек')
    try:
        for i in range(len(line_sep)):
            line_1.append(float(line_sep[i]))
            if float(line_sep[i]) < 0 or float(line_sep[i]) > 420:
                messagebox.showerror('Ошибка','Проверьте границы интервалов точек')
                line_1=[]
            
    except:
        messagebox.showerror('Ошибка','Проверьте валидность данных тояек')
        line_1=[]
        
    if len(line_1)%2 == 1:
        messagebox.showerror('Ошибка','Каждая точка задается 2-мя координатами')
        line_1=[]
        
    return line_1

def check_lines(line): ##проверка на валидность данных прямых
    
    line=str(line)
    line_sep=line.split()
    line_1=[]

    if len(line)==0:
        messagebox.showerror('Ошибка','Проверьте валидность данных для прямых')
        line_1=[]
    try:
        for i in range(len(line_sep)):
            line_1.append(float(line_sep[i]))
            if float(line_sep[i]) < 0 or float(line_sep[i]) > 420:
                messagebox.showerror('Ошибка','Проверьте границы интервалов прямых')
                line_1=[]
                
    except:
        messagebox.showerror('Ошибка','Проверьте валидность данных для прямых')
        line_1=[]
        
    if len(line_1)% 4 != 0:
        messagebox.showerror('Ошибка','Каждая прямая задается 2-мя точками')
        line_1=[]
        
    return line_1


def result(p,l):

    global x_l, y_l, x_p

    arr_count=[]
    count = 0
    
    arr_x=check_points(p)
    arr_y=check_lines(l)

    ##добавлямем в массив точек точки с графики
    for i in range(len(x_p)):
        arr_x.append(x_p[i])
    
    ##сделаем массив с коэффициентами k прямых
    
    arr_k=[]
    
    for i in range(0,len(arr_y)-3,4):
        if arr_y[i]!=arr_y[i+2]:
            k_y=(arr_y[i+1]-arr_y[i+3])/(arr_y[i]-arr_y[i+2])
            arr_k.append(k_y)
        else:
            arr_k.append(0)
    for i in range(0, len(x_l)-1, 2):
        if abs(x_l[i] - x_l[i+1])>=0.00001:
            k_y=(y_l[i+1]-y_l[i])/(x_l[i+1]-x_l[i])
            k_y=round(k_y,2)
            arr_k.append(k_y)
        else:
            arr_k.append(0)
            
            
    print(arr_k)
        
    max_count=0
    max_k=0

    ##найдем нужную прямую по двум точкам
    
    for i in range(len(arr_x)-3):
        count=0
        if arr_x[i]!=arr_x[i+2]:
            k_x=(arr_x[i+1]-arr_x[i+3])/(arr_x[i]-arr_x[i+2])
        else:
            k_x=0
            
        for j in range(len(arr_k)):
            if abs(k_x-arr_k[j]) < 0.01:
                count += 1
        if count >= max_count or max_count == 0:
            max_count = count
            max_k=k_x
            
            max_x_1=arr_x[i]
            max_y_1=arr_x[i+1]
            max_x_2=arr_x[i+2]
            max_y_2=arr_x[i+3]
  
    print(max_x_1)
    print(max_y_1)
    print(max_x_2)
    print(max_y_2)

    
    if max_count == 0:
        messagebox.showerror('Ошибка','Решение не найдено')
    else:
        result_canvas(arr_x, arr_y,max_x_1,max_y_1,max_x_2,max_y_2, max_k)

def paint_points(event):
    
    global c1, x_p
     
    x1, y1 = (event.x - 3), (event.y - 3)
    x2, y2 = (event.x + 3), (event.y + 3)
    
    if event.x < 40 or event.x > 460:
        return event
    if event.y < 40 or event.y > 460:
        return event
    
    x_p.append(event.x-40 )
    x_p.append(event.y-40)

    c1.create_oval(x1, y1, x2, y2, fill = 'pink')
    
    return event


def paint_lines(event):
 
    global c1, x_l, y_l, count

    x1, y1 = (event.x - 3), (event.y - 3)
    x2, y2 = (event.x + 3), (event.y + 3)

    if event.x < 40 or event.x > 460:
        return event
    if event.y < 40 or event.y > 460:
        return event

    x_l.append(event.x-40)
    y_l.append(event.y-40)
  
    c1.create_oval(x1, y1, x2, y2, fill='purple')

    if len(x_l) % 2 == 0 :
        c1.create_line(x_l[count]+40,y_l[count]+40, x_l[count+1]+40, y_l[count+1]+40, fill='purple', width=3)
        count += 2;
    return event
    
def draw():
    
    global c1
    
    c1=Canvas(window, width=1000, height=1000)
    

    for line in range(0,500 ,20):
        c1.create_line([(line, 0), (line, 500)], fill='black')
        
    for line in range(0,500, 20):
        c1.create_line([(0, line), (500, line)], fill='black')

    c1.create_line(40,40,40,480,fill='grey', width=3)
    c1.create_text(40,480,text='V', fill= 'black')
    c1.create_text(30,470,text='Y', fill= 'black')
    
    c1.create_line(40,40,480,40,fill="grey",width=3)
    c1.create_text(480,40,text='>', fill="black")
    c1.create_text(470,30,text='X', fill="black")

    for line in range(0,440, 20):
        if line % 6 == 0:
            c1.create_text(30+line,30, 
                  text=str(line),
                  justify=CENTER, font=('Times 10'))
            if line != 0:
                c1.create_text(30,30+line,
                      text=str(line),
                      justify=CENTER,font=('Times 10'))
            c1.create_line(40+line,35,40+line,45,fill='black',width=3)
            c1.create_line(35,40+line,45,40+line,fill='black',width=3)

    c1.pack()

##функция для прорисовки искомой прямой и точек
    
def result_canvas(arr_x, arr_y,max_x_1,max_y_1,max_x_2,max_y_2,max_k):
    
    global c1, x_p, x_l , y_l

    max_x_1+=40
    max_x_2+=40
    max_y_1+=40
    max_y_2+=40
    print(max_k)
    c1.create_line(max_x_1, max_y_1, max_x_2, max_y_2, fill='green', width=4)
    c1.create_oval(max_x_1+3, max_y_1+3, max_x_1-3, max_y_1-3, fill='red')
    c1.create_oval(max_x_2+3, max_y_2+3, max_x_2-3, max_y_2-3, fill='red') 
    c1.pack()
    
##функция для очистки поля графического ввода    
def draw_clean():
    
    global c1, x_p, x_l , y_l, count
    
    c1.delete('all')
    
    x_p=[]
    y_l=[]
    x_l=[]
    count = 0

    for line in range(0,500 ,20):
        c1.create_line([(line, 0), (line, 500)], fill='black')
        
    for line in range(0,500, 20):
        c1.create_line([(0, line), (500, line)], fill='black')

    c1.create_line(40,40,40,480,fill='grey', width=3)
    c1.create_text(40,480,text='V', fill= 'black')
    c1.create_text(30,470,text='Y', fill= 'black')
    
    c1.create_line(40,40,480,40,fill="grey",width=3)
    c1.create_text(480,40,text='>', fill="black")
    c1.create_text(470,30,text='X', fill="black")

    for line in range(0,440, 20):
        if line % 6 == 0:
            c1.create_text(30+line,30, 
                  text=str(line),
                  justify=CENTER, font=('Times 10'))
            if line != 0:
                c1.create_text(30,30+line,
                      text=str(line),
                      justify=CENTER,font=('Times 10'))
            c1.create_line(40+line,35,40+line,45,fill='black',width=3)
            c1.create_line(35,40+line,45,40+line,fill='black',width=3)
    c1.pack()

x_p=[]
y_l=[]
x_l=[]

count=0
draw()

input_points_l=Label(text='Введите через пробел координаты точек:', font=('Times'))
input_points_l.place(x=550,y=50)

input_points=Entry(width=50)
input_points.place(x=550,y=80)
input_points.bind('<FocusIn>', on_focus)
input_points.insert(0,[100,100,140,140,20,40])

input_lines_l=Label(text='''Введите через пробел координаты прямых
                                                  по двум точкам:''', font=('Times'))
input_lines_l.place(x=540,y=115)

input_lines=Entry(width=50)
input_lines.place(x=550,y=160)
input_lines.bind('<FocusIn>', on_focus)
input_lines.insert(0,[100,100,200,200,300,300,400,400])


##Кнопки для цифр,-, очистка полей и выход из приложения

but_1= Button(text='1',font=('Times'),command= lambda: on_click('1'), bg='grey',fg='white')
but_2= Button(text='2',font=('Times'),command= lambda: on_click('2'), bg='grey',fg='white')
but_3= Button(text='3',font=('Times'),command= lambda: on_click('3'), bg='grey',fg='white')
but_4= Button(text='4',font=('Times'),command= lambda: on_click('4'), bg='grey',fg='white')
but_5= Button(text='5',font=('Times'),command= lambda: on_click('5'), bg='grey',fg='white')
but_6= Button(text='6',font=('Times'),command= lambda: on_click('6'), bg='grey',fg='white')
but_7= Button(text='7',font=('Times'),command= lambda: on_click('7'), bg='grey',fg='white')
but_8= Button(text='8',font=('Times'),command= lambda: on_click('8'), bg='grey',fg='white')
but_9= Button(text='9',font=('Times'),command= lambda: on_click('9'), bg='grey',fg='white')
but_0= Button(text='0',font=('Times'),command= lambda: on_click('0'),bg='grey',fg='white')

but_point= Button(text='.',font=('Times'),command= lambda: insert('.'),bg='grey',fg='white')
but_minus= Button(text='-',font=('Times'),command= lambda: on_click('-'),bg='grey',fg='white')

but_clean_1= Button(text='C',font=('Times'),command= lambda: input_points.delete(0,'end'))
but_clean_2= Button(text='C',font=('Times'),command= lambda: input_lines.delete(0,'end'))
but_exit = Button(text='Exit',font=('Times'),command= lambda: window.destroy(),bg='grey',fg='white')

but_clean_1.place(x=850,y=80,width=20, height=20)
but_clean_2.place(x=850,y=160,width=20, height=20)
but_exit.place(x=550,y=400,width=110, height=45)

but_1.place(x=715,y=340,width=45, height=45)
but_2.place(x=765,y=340,width=45, height=45)
but_3.place(x=815,y=340,width=45, height=45)

but_4.place(x=715,y=280,width=45, height=45)
but_5.place(x=765,y=280,width=45, height=45)
but_6.place(x=815,y=280,width=45, height=45)

but_7.place(x=715,y=220,width=45, height=45)
but_8.place(x=765,y=220,width=45, height=45)
but_9.place(x=815,y=220,width=45, height=45)

but_0.place(x=715,y=400,width=45, height=45)
but_point.place(x=765,y=400,width=45, height=45)
but_minus.place(x=815,y=400,width=45, height=45)


but_draw=Button(text='Clean', font=('Times'), command= lambda : draw_clean() , bg='grey', fg='white')
but_draw.place(x=550,y=340,width=110, height=45)

but_res=Button(text = 'Result',font=('Times'),command= lambda: result(input_points.get(), input_lines.get()) , bg='grey',fg='white')
but_res.place(x=550,y=280,width=110, height=45)

draw_points_button=Button(text='Draw points',font=('Times'),command = lambda: window.bind('<Button-1>', paint_points))
draw_points_button.place(x=160,y=520,width=90)
    
draw_lines_button=Button(text='Draw lines', font=('Times'), command = lambda: window.bind('<Button-1>', paint_lines))
draw_lines_button.place(x=260,y=520,width=90)   


window.mainloop()

