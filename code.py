import tkinter as tk
import turtle

def generate():
    t.clear()

    rule= ruleentry.get()
    itera=int(iterentry.get())
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
            t.forward(10)
        elif ch=="+":
            t.right(90)
        elif ch=="-":
            t.left(90)

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
