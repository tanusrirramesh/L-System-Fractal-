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

root=tk.Tk()

canvas=tk.Canvas(root,width=400,height=400)
canvas.pack()

screen=turtle.TurtleScreen(canvas)
t= turtle.RawTurtle(screen)
t.speed(0)


ruleentry = tk.Entry(root)
ruleentry.insert(0,"F+F")
ruleentry.pack()

iterentry=tk.Entry(root)
iterentry.insert(0,"4")
iterentry.pack()

tk.Button(root, text="CREATE",command=generate).pack()
root.mainloop()
