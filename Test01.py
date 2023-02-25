from tkinter import *
import random

root=Tk()
root.title("Приложение")
root.geometry("1000x600")
root["bg"] = "white"

canvas = Canvas(root, width=1000, height=400)
canvas.pack()

lbl = None

def func():
    global lbl
    if lbl:
        lbl.destroy()
    canvas.delete("all")
    x1=random.randint(400,500)
    y1=random.randint(100,200)
    side = random.randint(5,100)
    rand = random.randint(1,3)
    if rand == 1:
        x1=850
        y1=150
        side = 130
        canvas.create_rectangle(x1,y1,x1+side,y1+side,fill="green")
        f9 = "Квадрат"
    elif rand == 2:
        canvas.create_oval(400,100,600,300,fill="red")
        f9 = "Круг"
    elif rand == 3:
        canvas.create_polygon(200, 50, 50, 350, 350, 350, outline="green", 
            fill='yellow', width=3)
        f9 = "Треугольник"
    lbl = Label(text='Выпало число '+str(rand)+". Фигура: "+(f9), font=("Consolas", 21, "bold"), bg="black", foreground="white")
    lbl.pack()

btn = Button(root,text="Press",width=30,height=2,command=func,bg='grey')
btn.place(relx=0.5,rely=0.9)
root.mainloop()
