from tkinter import *

root = Tk()
root.title("Minho's App")
root.geometry("640x480")

label1 = Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="불고기버거", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치킨버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="라이스버거", value=3, variable=burger_var)
btn_burger4 = Radiobutton(root, text="맛있는버거", value=4, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()
btn_burger4.pack()

label1 = Label(root, text="음료수를 선택하세요").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="환타", value="환타", variable=drink_var)
btn_drink4 = Radiobutton(root, text="물", value="물", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()
btn_drink4.pack()
 


def btncmd():
    print(burger_var.get()) #선택된 값의 value값을 반환
    print(drink_var.get()) #선택된 값의 value값을 반환

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()