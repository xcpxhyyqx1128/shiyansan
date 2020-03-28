import tkinter as tk
import pickle
from tkinter import messagebox


class usr_login2(tk.Frame):
    def __init__(self, parent, root):
        window = tk.Tk()
        window.title('防控办负责人登录界面')
        window.geometry('450x300')

        tk.Label(window, text='Username:').place(x=50, y=150)
        tk.Label(window, text='Password:').place(x=50, y=190)

        var_usr_name = tk.StringVar()
        var_usr_name.set('MrZhangxd@python.com')
        var_usr_pwd = tk.StringVar()
        entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
        entry_usr_name.place(x=160, y=150)

        entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
        entry_usr_pwd.place(x=160, y=190)

        btn_login = tk.Button(window, text='Login', command=usr_login)
        btn_login.place(x=170, y=230)
        btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
        btn_sign_up.place(x=270, y=230)

        def usr_login():
            usr_name = var_usr_name.get()
            usr_pwd = var_usr_pwd.get()
            try:
                with open('usrs_info,pickle', 'rb') as usr_file:
                    usrs_info = pickle.load(usr_file)
            except FileNotFoundError:
                with open('usrs_info', 'wb') as usr_file:
                    usrs_info = {'admin': 'admin'}
                    pickle.dump(usrs_info, usr_file)
            if usr_name in usrs_info:
                if usr_pwd == usrs_info[usr_name]:
                    tk.messagebox.showinfo(title='Welcome', message='How are you?' + usr_name)

                else:
                    tk.messagebox.showinfo(message='Error,your password is wrong,try again.')
            else:
                is_sign_up = tk.messagebox.askyesno('Welcome', 'You hava not sign up yet.Sign up today?')

                if is_sign_up:
                    usr_sign_up()

        print("这是一个弹出提示框")
        messagebox.showinfo("提示", "提交成功")

        window.mainloop()










