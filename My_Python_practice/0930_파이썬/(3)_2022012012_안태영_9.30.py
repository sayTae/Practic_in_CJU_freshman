## 모듈 ##
from tkinter import *
from tkinter import messagebox
import random

## 함수 선언 ##
def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠? ^^")
    
def dog_random():
    number = str(random.randint(2, 13))
    dog = "dog" + number + ".gif"
    return dog
                        
## 메인 코드 ##
window = Tk()

photo = PhotoImage(file = f"images\gif/{dog_random()}")
photo2 = PhotoImage(file = f"images\gif/{dog_random()}")

button1 = Button(
    window, 
    image = photo, 
    command = myFunc
)
button2 = Button(
    window, 
    image = photo2, 
    command = myFunc
)

button1.pack(side=LEFT)
button2.pack()


window.mainloop()