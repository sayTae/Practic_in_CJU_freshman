## 모듈 ##
from cProfile import label
from tkinter import *
import random

## 함수 선언 ##
def dog_random():
    int = str(random.randint(2, 13))
    dog = "dog" + int + ".gif"
    return dog

## 메인 코드 ##
window = Tk()

photo_dog = PhotoImage(file = f"images/GIF/{dog_random()}")
photo_dog2 = PhotoImage(file = f"images/GIF/{dog_random()}")
photo_dog3 = PhotoImage(file = f"images/GIF/{dog_random()}")
photo_dog4 = PhotoImage(file = f"images/GIF/{dog_random()}")

# photo = PhotoImage(file = "C:\Users\Cju\Desktop\eee\images\GIF\dog.gif")

label1 = Label(
    window, 
    image = photo_dog
)
label2 = Label(
    window, 
    image = photo_dog2
)
label3 = Label(
    window, 
    image = photo_dog3
)
label4 = Label(
    window, 
    image = photo_dog4
)

label1.pack(side=LEFT)
label2.pack(side=RIGHT)
label3.pack(side=LEFT)
label4.pack(side=RIGHT)


window.mainloop()

