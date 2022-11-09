from cProfile import label
from tkinter import *

window= Tk()

# 이 부분에서 화면을 구성하고 시작 #
# window.title("윈도우창 연습을 실시한다! 캬하핰")
# window.geometry("400x100")
# window.resizable(width = FALSE, height = FALSE)

label1 = Label(window, text = "첫 번째 내용입니다.")
label2 = Label(window, text = "두 번째 내용입니다.", font=("궁서체",30), fg="blue")
label3 = Label(window, text = "세 번째 내용입니다.", bg="magenta", width=20, height=5, anchor=SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()