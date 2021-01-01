# -*- coding:utf-8 -*-
import Tkinter as tk
from PIL import ImageTk, Image

class Kiosk():
    def __init__(self):
        #main window setting
        self.__window=tk.Tk()
        self.__window.title("Kiosk")
        self.__window.attributes('-fullscreen', True)
        self.__window.configure(cursor='none')
        self.__window.bind('<Escape>', self.typeESC)
        self.__window.bind('<Alt-Return>', self.typeALTENT)

        #image load
        self.__img1 = ImageTk.PhotoImage(Image.open('1.png'))
        self.__img2 = ImageTk.PhotoImage(Image.open('2.png'))
        self.__img3 = ImageTk.PhotoImage(Image.open('3.png'))
        self.__img4 = ImageTk.PhotoImage(Image.open('4.png'))
        self.__img5 = ImageTk.PhotoImage(Image.open('5.png'))
        self.__img6 = ImageTk.PhotoImage(Image.open('6.png'))

        #button setting
        tk.Button(self.__window,width=370 ,height= 400, command = lambda: self.click(1), image = self.__img1).place(x=100,y=40)
        tk.Button(self.__window,width=370 ,height= 400, command = lambda: self.click(2), image = self.__img2).place(x=600,y=40)
        tk.Button(self.__window,width=370 ,height= 400, command = lambda: self.click(3), image = self.__img3).place(x=100,y=500)
        tk.Button(self.__window,width=370 ,height= 400, command = lambda: self.click(4), image = self.__img4).place(x=600,y=500)
        tk.Button(self.__window,width=370 ,height= 400, command = lambda: self.click(5), image = self.__img5).place(x=100,y=960)
        tk.Button(self.__window,width=370 ,height= 400, command = lambda: self.click(6), image = self.__img6).place(x=600,y=960)

        tk.Button(self.__window, width=10, height=5, text = "결제", font=("궁서체",20), command = self.buy).place(x=800,y=1600)

        #listbox setting
        self.__drinkList=tk.Listbox(self.__window, width=30, height=25)
        self.__drinkList.place(x=100,y=1420)

        #start GUI
        tk.mainloop()

    def typeESC(self, event):
        self.__window.attributes('-fullscreen', False)

    def typeALTENT(self, event ):
        self.__window.attributes('-fullscreen', True)

    def click(self, num):
        account = tk.Tk()
        account.title("ACCOUNT")
        account.geometry("400x270+370+1420")
        account.configure(cursor='none')
        account.resizable(False,False)
        tk.Button(account, width=5, height=5, text = "담기", font=("궁서체",20), command = lambda: self.addDrink(num, account)).place(x=50,y=50)
        tk.Button(account, width=5, height=5, text = "취소", font=("궁서체",20), command = lambda: self.cancel(account)).place(x=200,y=50)

    def cancel(self, root):
        root.destroy()

    def addDrink(self, num, root):
        if num==1:
            self.__drinkList.insert(0, "아메리카노")
        elif num==2:
            self.__drinkList.insert(0, "카페라떼")
        elif num==3:
            self.__drinkList.insert(0, "카푸치노")
        elif num==4:
            self.__drinkList.insert(0, "카페모카")
        elif num==5:
            self.__drinkList.insert(0, "블루베리 스무디")
        elif num==6:
            self.__drinkList.insert(0, "프라페 커피")
        root.destroy()

    def buy(self):
        self.__drinkList.delete(0, tk.END)





def main():
    Kiosk()

if __name__=="__main__":
    main()










