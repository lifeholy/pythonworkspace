from tkinter import *

root = Tk()
root.title("1st GUI")
root.geometry("640x480")
#root.geometry("640x480+100+300") #가로크기 * 세로크기 + x좌표 + y좌표

#root.resizable(False,False) #크기변경 불가

#위젯
#버튼만들기
def btncmd():
    print("버튼이 클릭되었어요")

btn1 = Button(root, text="버튼1", command=btncmd) #root는 버튼 넣는 위치
btn1.pack()
btn2 = Button(root, padx=5, pady=10, text="버튼222222222222222", command=btncmd) #버튼크기는 텍스트의 크기에 연동
btn2.pack()
btn3 = Button(root, padx=10, pady=4, text="버튼3", command=btncmd)
btn3.pack()
btn4 = Button(root, width=10, height=3, text="버튼444444444444", command=btncmd) #버튼크기 절대값 지정
btn4.pack()
btn5 = Button(root, fg="red", bg="yellow", padx=10, pady=4, text="버튼3", command=btncmd)
btn5.pack()

photo = PhotoImage(file="gui_basic/button.png")
btn6 = Button(root, image=photo, command=btncmd)
btn6.pack()


btn7 = Button(root, text="동작하는버튼", command=btncmd)
btn7.pack()

root.mainloop()