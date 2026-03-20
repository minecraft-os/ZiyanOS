from tkinter import *
import os
from PIL import Image,ImageTk
from tkinter import messagebox
import tkinter.ttk as t
import tkinter.font as tkFont


def callback():
    ask=messagebox.askyesno("","是否重启系统？")
    if ask=="Yes":
        pecmdkill = os.system("pecmd kill pecmd.exe")
    elif ask=="No":
        pass


root=Tk()
root.geometry("1000x500")
root.title("自演操作系统 - 桌面")
root.resizable(False,False)
root.protocol('WM_DELETE_WINDOW',callback)
root.iconbitmap("images/Icons/apps.ico")


#获取屏幕的高度和宽度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#初始化位置
cur_x=screen_width//3.5
cur_y=screen_height//3.2
root.geometry("%dx%d+%d+%d"%(1000,500,cur_x,cur_y))


#创建背景
img0=Image.open("images/background/img1.jpg")
img=ImageTk.PhotoImage(img0)

background=Label(root,image=img)
background.pack()

#创建设置标签
setimg=Image.open("images/Icons/settings.png")
setigs=ImageTk.PhotoImage(setimg)

def opset():
    setting=Toplevel(root)
    setting.geometry("500x300")
    setting.title("设置")
    setting.resizable(False,False)
    setting.wm_attributes("-topmost",True)
    setting.wm_attributes("-toolwindow",True)

    # 获取屏幕的高度和宽度
    screen_width = setting.winfo_screenwidth()
    screen_height = setting.winfo_screenheight()

    # 初始化位置
    cur_x = screen_width // 3.5
    cur_y = screen_height // 3.2
    setting.geometry("%dx%d+%d+%d" % (500, 300, cur_x, cur_y))


    #打开分区工具
    def opdisk():
        opdsk=os.system("start Apps/Diskgenius/Diskgenius.exe")

    fqimg0=Image.open("images/Icons/DiskGenius_128.png")
    fqimg=ImageTk.PhotoImage(fqimg0)

    fqimgbut=Button(setting,image=fqimg,border=0,command=opdisk)
    fqimgbut.image=fqimg
    fqimgbut.place(x=0,y=0)


    # 定义字体
    ft = tkFont.Font(family='Consolas', size=20, weight='bold')

    # 样式配置
    style = t.Style()
    style.configure('My.TButton', font=ft, width=10)


    fqbut=t.Button(setting,text="分区工具",style='My.TButton',command=opdisk)
    fqbut.place(x=50,y=0)




    #桌面模式
    def desktop():
        open_Desktop=os.system("start Apps/Desktop/home.exe")
        root.destroy()

    desktopimg0=Image.open("images/Icons/home.png")
    desktopimg=ImageTk.PhotoImage(desktopimg0)


    deskimg=Button(setting,image=desktopimg,border=0,command=desktop)
    deskimg.image=desktopimg
    deskimg.place(x=0,y=59)

    deskbt=t.Button(setting,text="启动桌面模式",style='My.TButton',command=desktop)
    deskbt.place(x=50,y=60)

    #更多设置
    def all_settings():
        oteset=os.system("start Apps/SystemSettings/UI_Settings.exe")
        setting.destroy()

    controlpanimg=Image.open("images/Icons/control.png")
    control=ImageTk.PhotoImage(controlpanimg)
    all_setimg=Button(setting,image=control,border=0,command=all_settings)
    all_setimg.image=control
    all_setimg.place(x=0,y=110)

    all_set=t.Button(setting,text="更多设置",style='My.TButton',command=all_settings)
    all_set.place(x=50,y=115)

    #更改背景
    def update_back():
        background=Toplevel(root)
        background.geometry("300x200")
        background.title("背景设置")
        background.resizable(False,False)
        background.wm_attributes("-topmost",True)
        background.wm_attributes("-toolwindow",True)

        def updates():
            messagebox.showinfo("你选择了：", zx1.get())


        zx1=Entry(background,font=("微软雅黑",12))
        zx1.place(x=50,y=50)

    update_backim=Image.open("images/Icons/personalize.png")
    update_backg=ImageTk.PhotoImage(update_backim)

    update_backgroundbut=Button(setting,image=update_backg,border=0,command=update_back)
    update_backgroundbut.image=update_backg
    update_backgroundbut.place(x=0,y=168)

    update_backgroundbt=t.Button(setting,text="更改背景",style='My.TButton',command=update_back)
    update_backgroundbt.place(x=50,y=168)



sets=Button(root,image=setigs,border=0,command=opset)
sets.place(x=50,y=20)

#创建浏览器标签
def opbroswer():
    opero=os.system("start Apps/360ChromeX/360ChromeX.exe")
broswerig=Image.open("images/Icons/Chrome.png")
broswer=ImageTk.PhotoImage(broswerig)

open_browser=Button(root,image=broswer,border=0,command=opbroswer)
open_browser.place(x=280,y=20)

mainloop()