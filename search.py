# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.messagebox
import pickle
import pymssql
#连接到数据库

def connect():
    connect = pymssql.connect('DESKTOP-IDILIBA',user='kkk',password='123456',database='test') #服务器名,账户,密码,数据库名
    if connect:
        print("连接成功!")
    else:
        print("failed")
connect()
#窗口
self=tk.Tk()
self.title('飞行器数据查询系统')
self.geometry('450x300')
canvas=tk.Canvas(self,width=300,height=500)
photo=tk.PhotoImage(file='F:/fei.png')
canvas.create_image(0,0,anchor='nw',image=photo)
canvas.pack(side='top')
photos=tk.PhotoImage(file='F:/ci.png')
canvas.create_image(0,0,anchor='w',image=photos)
canvas.pack(side='top')

#标签 标题,用户名,密码
tk.Label(self,text='空军航空大学',fg='blue',font=('楷体',22, 'bold')).place(x=140,y=10)
tk.Label(self,text='用户名:',font=('楷体')).place(x=100,y=150)
tk.Label(self,text='密码:',font=('楷体')).place(x=100,y=190)
aa=tk.StringVar() #初始化为空
tk.Entry(self,textvariable=aa).place(x=160,y=150)
bb=tk.StringVar() #初始化为空
tk.Entry(self,textvariable=bb,show='*').place(x=160,y=190)
#登录函数
def usr_log_in():
    #connect=connect()
    #输入框获取用户名密码
    #usr_name=var_usr_name.get()
    usr_name=aa.get()
    usr_pwd=bb.get()
   # usr_pwd=var_usr_pwd.get()
    #从本地字典获取用户信息，如果没有则新建本地数据库
    try:
        with open('usr_info.pickle','rb') as usr_file:
            usrs_info=pickle.load(usr_file)
    except FileNotFoundError:
        with open('usr_info.pickle','ab') as usr_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    #判断用户名和密码是否匹配
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='welcome',message='欢迎您：'+usr_name)
            plane()
        else:
            tk.messagebox.showerror(message='密码错误')
    #用户名密码不能为空
    elif usr_name=='' or usr_pwd=='' :
        tk.messagebox.showerror(message='用户名或密码为空')
    #不在数据库中弹出是否注册的框
    else:
        is_signup=tk.messagebox.askyesno('欢迎','您还没有注册，是否现在注册')
        if is_signup:
            usr_sign_up()

#注册函数限定
def zhuce_it():
    #确认注册时的相应函数
    def signfx():
        #获取输入框内的内容
        nn=new_name.get()
        np=new_pwd.get()
        npf=new_pwd_confirm.get()
 
        #本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open('usr_info.pickle','rb') as usr_file:
                exist_usr_info=pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info={}           

        #检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            tk.messagebox.showerror('错误','用户名已存在')
        elif np =='' or nn=='':
            tk.messagebox.showerror('错误','用户名或密码为空')
        elif np !=npf:
            tk.messagebox.showerror('错误','密码前后不一致')
        elif len(np)<6:
            tk.messagebox.showerror('错误','密码不能少于六位')
        #注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn]=np
            with open('usr_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tk.messagebox.showinfo('欢迎您','注册成功')
        #注册成功关闭注册框
            window_sign_up.destroy()
            
#新建注册界面
    auser=tk.Toplevel(self)
    auser.geometry('350x200')
    auser.title("用户注册")
#用户名变量及标签、输入框
    new_name=tk.StringVar()
    tk.Label(auser,text='用户名：').place(x=10,y=10)
    tk.Entry(auser,textvariable=new_name).place(x=150,y=10)
#密码变量及标签、输入框
    new_pwd=tk.StringVar()
    tk.Label(auser,text='请输入密码：').place(x=10,y=50)
    tk.Entry(auser,textvariable=new_pwd,show='*').place(x=150,y=50)    
#重复密码变量及标签、输入框
    new_pwd_confirm=tk.StringVar()
    tk.Label(auser,text='请再次输入密码：').place(x=10,y=90)
    tk.Entry(auser,textvariable=new_pwd_confirm,show='*').place(x=150,y=90)    
#确认注册按钮及位置
    bt_confirm_sign_up=tk.Button(auser,text='确认注册',command=signfx)
    bt_confirm_sign_up.place(x=150,y=130)
#退出的函数
def out_it():
    out_it=tk.messagebox.askyesno('提示','您确定退出程序吗？')
    if out_it:
      self.destroy()
#新建飞机数据查询界面
def plane():
    pla=tk.Toplevel(self)
    pla.geometry('500x300')
    pla.title("飞机数据CX")
    af=tk.StringVar()
    tk.Label(pla,text='飞机名称:').place(x=10,y=50)
    #数据库内查询数据
    def lookup():
        #chicken=input('查询数据：')
        chicken=af.get()
        connects = pymssql.connect('DESKTOP-IDILIBA',user='kkk',password='123456',database='test') #服务器名,账户,密码,数据库名
        cursor = connects.cursor()
        cursor.execute("select * from C_test02 where name='%s' " % chicken)
        for row in cursor:
            '''print(row)'''
        tk.messagebox.showinfo(message=row)
        cursor.close()
        connects.close()   
    '''pla=tk.Toplevel(self)
    pla.geometry('500x300')
    pla.title("飞机数据CX")
    af=tk.StringVar()
    tk.Label(pla,text='飞机名称:').place(x=10,y=50)'''
    tk.Entry(pla,textvariable=af).place(x=200,y=50)
#查询按钮及其位置
    bt_find=tk.Button(pla,text='查询',command=lookup)
    bt_find.place(x=200,y=80)
'''#数据库内查询数据
    def Lookup():
        chicken=af.get()
        cursor = conn.cursor()
        cursor.execute("select * from C_test02 where name='%s' " % chicken)
        for row in cursor:
            print(row)

        cursor.close()
        connect.close()
   '''
#登录,注册
tk.Button(self,text='登录',command=usr_log_in).place(x=140,y=230)
tk.Button(self,text='注册',command=zhuce_it).place(x=210,y=230)
tk.Button(self,text='退出',command=out_it).place(x=280,y=230)

self.mainloop()

