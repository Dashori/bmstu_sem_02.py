##Лабораторная работа 3
##Уточнение корней уравнения методом секущих


from tkinter import *
from tkinter import messagebox 
from math import *
from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np

def derived(x):
    return cos(x)

def clear():
    input_start.delete(0,'end')
    input_finish.delete(0,'end')
    input_step.delete(0,'end')
    input_eps.delete(0,'end')

def secant_method(a,b,eps):
    count=0
    a_0=a
    b_0=b
    while abs(a-b)>eps:
        t=b
        b=b-(((b-a)*sin(b))/(sin(b)-sin(a)))
        a=t
        count+=1
        
    if (b - b_0 <= 0.00001) and ((b -a_0) >= 0.0001):
        b=round(b,6)
        return b,count
    else:
        return 'no',0
    
def result_roots():
    
    start=input_start.get()
    finish=input_finish.get()
    step=input_step.get()
    eps=input_eps.get()
    flag=0
    count=0
    roots=[]
    iterations=[]
    try:
        start=float(start)
        finish=float(finish)
    except:
        messagebox.showerror('Ошибка','Проверьте валидность данных для отрезка')
        flag=1
        
       
        
    if finish < start:
        messagebox.showerror('Ошибка','Конец отрезка должен быть больше, чем начало')
        flag=1

    try:
        step=float(step)
        eps=float(eps)
        if eps<0 or eps>1:
            messagebox.showerror('Ошибка','Точность должна быть в промежутке от 0 до 1')
            flag=1
        if step<0 or step>3:
            messagebox.showerror('Ошибка','Шаг должен быть в промежутке от 0 до 3х')
            flag=1
    except:
        messagebox.showerror('Ошибка','Проверьте валидность данных для шага и точности')
        flag=1           
    if flag==1:
        return roots, iterations,flag
    
    while start < finish:
        if start+step >= finish:
            current=secant_method(start,finish,eps)
            start += step
            roots.append(current[0])
            iterations.append(current[1])
            
        else:
            current=secant_method(start,start+step,eps)            
            start+=step
            roots.append(current[0])
            iterations.append(current[1])

    return roots, iterations,flag


def res_wd():

    a=result_roots()
    roots=a[0]
    iterations=a[1]
    if a[2]==1:
        return 1
    flag=0
    num_roots=[]
    j=1
    for i in roots:
        if i!='no':
            flag=1
            num_roots.append(j)
            j+=1
        else:
            num_roots.append(0)
            
    if flag==1:
        start=float(input_start.get())
        step=float(input_step.get())
        
        window = Toplevel()
        window.title('Result')
        window.geometry('700x500')
        y_0=50
        
        num_label=Label(window,text='Номер корня')
        num_label.place(x=20,y=20)

        piece_label=Label(window, text='Отрезок ')
        piece_label.place(x=150,y=20)

        root_label=Label(window, text='Корень')
        root_label.place(x=260,y=20)

        func_label=Label(window,text='Значение функции')
        func_label.place(x=340,y=20)

        iteration_label=Label(window, text='Количество итераций')
        iteration_label.place(x=460,y=20)

        error_label=Label(window, text='Код ошибки')
        error_label.place(x=600,y=20)

        
        
        for i in range(len(num_roots)):
            if roots[i]!='no':
                
                res_num_label=Label(window,text=num_roots[i])
                res_num_label.place(x=50,y=y_0)
                                        
                
                piece_1=Label(window,text='{:3.2g}'.format(start+step*i))
                piece_1.place(x=150,y=y_0)
                
                
                piece_2=Label(window,text='{:3.2g}'.format(start+step*(i+1)))
                piece_2.place(x=190,y=y_0)
                
                res_label=Label(window,text=roots[i])
                res_label.place(x=260,y=y_0)

                func=Label(window,text='{:^3.3g}'.format(sin(roots[i])))
                func.place(x=350,y=y_0)

                iter_label=Label(window,text=iterations[i])
                iter_label.place(x=515,y=y_0)

                error=Label(window,text='0')
                error.place(x=635,y=y_0)
                y_0+=50

        window.mainloop()
    else:
        messagebox.showerror('Ошибка','Корни не найдены')
        
        

def graph_wd():
    res=result_roots()
    res_roots=res[0]
    if res[2]==1:
        return 1
    
    res=res[0]
    
    x = np.linspace(float(input_start.get()),float(input_finish.get()),500000)


    plt.cla()
    plt.title('$sin(x)$')
    plt.grid(True)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    
    plt.plot(x,np.sin(x))

     
    extr_list_x = []
    extr_list_y = []
    
    for i in range(1,499999):
        if abs(derived(x[i]))<0.0001 and derived(x[i])*derived(x[i+1])<0 :         
            extr_list_x.append(x[i])
            extr_list_y.append(sin(x[i]))
    res_roots_y=[]
    res_roots_1=[]
        
  
    for i in range(len(res_roots)):
        if res_roots[i]!='no':
            res_roots_y.append(sin(float(res_roots[i])))
            res_roots_1.append(res_roots[i])
 
    
            
    plt.scatter(extr_list_x,extr_list_y,color = 'red',label='Extremums')
    plt.scatter(res_roots_1,res_roots_y,color='green',label='Roots')
    plt.legend(loc = 'lower left')
    plt.show()


window=Tk()
window.title('Secant method')
window.geometry('500x400')


sin_label=Label(text='Уточнение корней методом секущих функции y=sin(x)')
sin_label.place(x=90,y=20)

input_a_label=Label(text='Начало отрезка')
input_a_label.place(x=45,y=80)

input_start=Entry(width=15)
input_start.place(x=40,y=110)
input_start.insert(0,-11)

input_b_label=Label(text='Конец отрезка')
input_b_label.place(x=155,y=80)

input_finish=Entry(width=15)
input_finish.place(x=150,y=110)
input_finish.insert(0,10)

input_step_label=Label(text='Шаг')
input_step_label.place(x=295,y=80)

input_step=Entry(width=15)
input_step.place(x=260,y=110)
input_step.insert(0,2)

input_eps_label=Label(text='Точность')
input_eps_label.place(x=385,y=80)


input_eps=Entry(width=15)
input_eps.place(x=370,y=110)
input_eps.insert(0,0.0001)


result=Button(text='Найти корни',width=20, command= lambda: res_wd())
result.place(x=60,y=180)

graph=Button(text='Построить график',width=20, command= lambda: graph_wd())
graph.place(x=260,y=180)

clear_bt=Button(text='Очистить все поля',width=20, command= lambda:clear() )
clear_bt.place(x=160,y=220)
window.mainloop()
