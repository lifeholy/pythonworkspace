from tkinter import *

root = Tk()
root.title("1st GUI")
#root.geometry("640x480")
root.geometry("640x480+100+300") #가로크기 * 세로크기 + x좌표 + y좌표

root.resizable(False,False) #크기변경 불가

#위젯

root.mainloop()