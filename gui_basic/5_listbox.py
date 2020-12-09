from tkinter import *

root = Tk()
root.title("Minho's App")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(3, "수박")
listbox.insert(END, "참외")
listbox.insert(END, "복숭아")
listbox.pack()


def btncmd():
    listbox.delete(END) #0이면 맨 앞부터 삭제, END면 맨 뒤부터 삭제
    print("리스트에는", listbox.size(), "개가 있어요")
    print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2))
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()