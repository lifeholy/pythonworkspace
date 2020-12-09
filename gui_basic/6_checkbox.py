from tkinter import *

root = Tk()
root.title("Minho's App")
root.geometry("640x480")


chkvar = IntVar()
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.select() #기본으로 선택
chkbox.deselect() #기본으로 해제
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.select() #기본으로 선택
chkbox2.deselect() #기본으로 해제
chkbox2.pack()


def btncmd():
    print("오늘하루 : ", chkvar.get()) #0:체크해제, 1:체크
    print("일주일동안 : ",chkvar2.get()) #0:체크해제, 1:체크

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()