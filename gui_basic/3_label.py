from tkinter import *

root = Tk()
root.title("Minho's App")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/button1.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2 #함수내에서의 변수는 전역변수가 아니므로 변수가 삭제되는것을 방지하기위해 global함수로 선언한다.
    photo2 = PhotoImage(file="gui_basic/button2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()