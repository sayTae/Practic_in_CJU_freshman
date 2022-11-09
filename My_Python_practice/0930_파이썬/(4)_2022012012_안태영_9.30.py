## 모듈 ##
from tkinter import *
from tkinter import messagebox
from turtle import window_width

## 함수 선언 ##
def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("", "체크버튼이 꺼졌어요")
    else:
        messagebox.showinfo("", "체크버튼이 켜졌어요")

## 메인 코드 ##
window = Tk()
chk = IntVar()

cb1 = Checkbutton(
    window,
    text = "클릭하세요",
    variable = chk,
    command = myFunc
)

cb1.pack()


window.mainloop()
