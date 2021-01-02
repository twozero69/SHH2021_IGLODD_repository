# -*- coding:utf-8 -*-
import Tkinter as tk
from PIL import ImageTk, Image
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json, time
import playsound as ps

client_id='IGLODDer'
mqtt_client = AWSIoTMQTTClient(client_id)
mqtt_client.configureEndpoint("a1lm27anwcfzhd-ats.iot.ap-northeast-2.amazonaws.com", 8883)
mqtt_client.configureCredentials("/home/pi/certs/root-CA.crt", "/home/pi/certs/IGLODDer.private.key", "/home/pi/certs/IGLODDer.cert.pem")
mqtt_client.configureOfflinePublishQueueing(-1)
mqtt_client.configureDrainingFrequency(2)
mqtt_client.configureConnectDisconnectTimeout(10)
mqtt_client.configureMQTTOperationTimeout(5)
mqtt_client.connect()
mqtt_client.publish("IGLODDer/status", '{"status":"connect"}', 0)


class Kiosk():
    def __init__(self):
        #variable
        self.__number=1

        #main window setting
        self.__window=tk.Tk()
        self.__window.title("Kiosk")
        self.__window.attributes('-fullscreen', True)
        self.__window.configure(cursor='none')
        self.__window.bind('<Escape>', self.typeESC)
        self.__window.bind('<Alt-Return>', self.typeALTENT)

        #image load
        self.__img1 = ImageTk.PhotoImage(Image.open('amer.png'))
        self.__img2 = ImageTk.PhotoImage(Image.open('lat.png'))
        self.__img3 = ImageTk.PhotoImage(Image.open('pucc.png'))
        self.__img4 = ImageTk.PhotoImage(Image.open('moca.png'))
        self.__img5 = ImageTk.PhotoImage(Image.open('smoo.png'))
        self.__img6 = ImageTk.PhotoImage(Image.open('pra.png'))

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
        payloads={
            "number": self.__number
        }
        mqtt_client.publish("IGLODDer/number", json.dumps(payloads), 0)
        time.sleep(1)
        self.__number+=1

        for string in self.__drinkList.get(0,tk.END):
            payloads={
                "order": string
            }
            mqtt_client.publish("IGLODDer/order", json.dumps(payloads), 0)
            time.sleep(1)

        self.__drinkList.delete(0, tk.END)


def main():
    Kiosk()

if __name__=="__main__":
    main()










