# def myFunc(p1=1, p2=2, p3=3):
# 	ret = p1 + p2 + p3
# 	return ret

# print("매개변수 없이 호출 =>", myFunc())
# print("매개변수가 1개로 호출 =>", myFunc(1))
# print("매개변수가 2개로 호출 =>", myFunc(1,2))
# print("매개변수가 3개로 호출 =>", myFunc(1,2,3))


# def addNumber(num):
# 	if num < 2:
# 		return 1
# 	return num + addNumber(num -1)

# print(addNumber(100)) 



# from tkinter import *

# window = Tk()
# window.title("연습 문제")
# window.geometry("400x100")
# window.resizable(width=FALSE, height=FALSE)

# label1 = Label(window, text="COOKBOOK~~파이썬을 학습 중...", font=("궁서체", 15), fg="red")

# label1.pack()

# window.mainloop()
 	

# from tkinter import *
# from tkinter import messagebox

# def click_button():
# 	messagebox.showinfo("버튼", "버튼을 눌렀어요.")

# window = Tk()

# button1 = Button(window, text="여기를 클릭", command=click_button)

# button1.pack()

# window.mainloop()


# from tkinter import *

# def clickMouse(event):
# 	txt = str(event.y) + "," + str(event.x) + "에서 클릭 됨"
# 	label1.configure(text=txt)

# window = Tk()
# window.geometry("400x400")

# label1 = Label(window, text="이곳이 바뀜")
# window.bind("<Button>", clickMouse)

# label1.pack(expand=1, anchor=CENTER)

# window.mainloop()


# from tkinter import *
# from tkinter import ttk

# window = Tk()
# # window.iconbitmap('python.ico')

# baseTab = ttk.Notebook(window)

# tabDog = ttk.Frame(baseTab)
# baseTab.add(tabDog, text="강아지")

# tabCat = ttk.Frame(baseTab)
# baseTab.add(tabCat, text="고얌미")


# baseTab.pack(expand=1, fill="both")


# photoDog = PhotoImage(file = "0930_파이썬/images/GIF/dog7.gif")
# labelDog = Label(tabDog, image=photoDog)
# labelDog.pack()

# photoCat = PhotoImage(file = "0930_파이썬/images/GIF/cat5.gif")
# labelCat = Label(tabCat, image=photoCat)
# labelCat.pack()

# window.mainloop()


