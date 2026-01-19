import tkinter as tk
import turtle

def create():
    t.clear()

    rule= ruleentry.get()
    itera=int(iterentry.get())
    angle=int(angleentry.get())
    step=int(stepentry.get())
    
    s="F"
    
    for i in range(itera):
        new = ""
        for ch in s:
            if ch=="F":
                new+=rule
            else:
                new+=ch
        s=new

    for ch in s:
        if ch=="F":
            t.forward(step)
        elif ch=="+":
            t.right(angle)
        elif ch=="-":
            t.left(angle)

a=tk.Tk()
a.title("L-System Generator")

canvas=tk.Canvas(a,width=700,height=400)
canvas.pack()

screen=turtle.TurtleScreen(canvas)
t= turtle.RawTurtle(screen)
t.speed(0)

tk.Label(a,text="Rule").pack()
ruleentry=tk.Entry(a)
ruleentry.pack()

tk.Label(a,text="Iterations").pack()
iterentry=tk.Entry(a)
iterentry.pack()

tk.Label(a,text="Angle").pack()
angleentry=tk.Entry(a)
angleentry.pack()

tk.Label(a,text="Step Size").pack()
stepentry = tk.Entry(a)
stepentry.pack()

tk.Button(a,text="CREATE",command=create).pack()
root.mainloop()
