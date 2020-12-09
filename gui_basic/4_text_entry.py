from tkinter import *

root = Tk()
root.title("Minho's App")
root.geometry("640x480")

text = Text(root, width=30, height=5)
text.pack()

text.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0,"한 줄만 입력해요")


def btncmd():
    print(text.get("1.0", END)) # 1:첫번째 라인, 0: 0번째 컬럼
    print(e.get())

    text.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()