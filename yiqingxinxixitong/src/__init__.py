from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
from tkinter import ttk
import smtplib
import time
import pymysql
import matplotlib.pyplot as plt
import xlwt


LARGE_FONT = ("Verdana", 20)


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.wm_title("疫情防控上报表")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # 循环功能界面
        for F in (StartPage,  PageTwo, PageThree, PageFour, PageFive):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # 四个页面的位置都是 grid(row=0, column=0), 位置重叠，只有最上面的可见！！

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # 切换，提升当前 tk.Frame z轴顺序（使可见）！！此语句是本程序的点睛之处


# 主页面
class StatPage(tk.Frame):
    '''主页'''

    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="疫情信息管理系统", font=LARGE_FONT)
        label.pack(pady=100)
        ft2 = tkFont.Font(size=16)
        Button(self, text="学生/教职工疫情上报", font=ft2, command=lambda: root.show_frame(PageOne), width=30, height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self, text="二级部门疫情汇总", font=ft2, command=lambda: root.show_frame(PageThree), width=30, height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self, text="疫情防控填报统计", font=ft2, command=lambda: root.show_frame(PageFour), width=30, height=2).pack()
        Button(self, text='退出系统', height=2, font=ft2, width=30, command=root.destroy, fg='white', bg='gray',
               activebackground='black', activeforeground='white').pack()


# 疫情上报
class PageTwo(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="学生/教职工疫情上报", font=LARGE_FONT)
        label.pack(pady=50)

        ft3 = tkFont.Font(size=14)
        ft4 = tkFont.Font(size=12)
        Label(self, text='所在学院：', font=ft3).pack(side=TOP)
        global e1
        e1 = StringVar()
        Entry(self, width=30, textvariable=e1, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='所在班级：', font=ft3).pack(side=TOP)
        global e2
        e2 = StringVar()
        Entry(self, width=30, textvariable=e2, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='学号/工号：', font=ft3).pack(side=TOP)
        global e3
        e3 = StringVar()
        Entry(self, width=30, textvariable=e3, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='姓名：', font=ft3).pack(side=TOP)
        global e4
        e4 = StringVar()
        Entry(self, width=30, textvariable=e4, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='电子邮箱：', font=ft3).pack(side=TOP)
        global e5
        e5 = StringVar()
        Entry(self, width=30, textvariable=e5, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='当前所在地：', font=ft3).pack(side=TOP)
        global e6
        e6 = StringVar()
        Entry(self, width=30, textvariable=e6, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='体温是否正常：', font=ft3).pack(side=TOP)
        global e7
        e7 = StringVar()
        Radiobutton(self, text='是', variable=e7, value=1, ).pack(side=TOP)
        Radiobutton(self, text='否', variable=e7, value=2, ).pack(side=TOP)
        Label(self, text='是否有疑似症状：', font=ft3).pack(side=TOP)
        global e8
        e8 = StringVar()
        Radiobutton(self, text='是', variable=e8, value=1, ).pack(side=TOP)
        Radiobutton(self, text='否', variable=e8, value=2, ).pack(side=TOP)
        Label(self, text='是否已确诊：', font=ft3).pack(side=TOP)
        global e9
        e9 = StringVar()
        Radiobutton(self, text='是', variable=e9, value=1, ).pack(side=TOP)
        Radiobutton(self, text='否', variable=e9, value=2, ).pack(side=TOP)
        Button(self, text="返回首页", width=8, font=ft4, command=lambda: root.show_frame(StartPage)).pack(pady=20)
        Button(self, text="提交", width=8, font=ft4, command=self.save).pack(side=TOP)

    def save(self):
        with open('student_infor.txt', 'a+') as student_infor:
            XueYuan = str(e1.get())
            BanJi = str(e2.get())
            Sno = str(e3.get())
            Name = str(e4.get())
            Tel = str(e5.get())
            Address = str(e6.get())
            Tem = str(e7.get())
            YiSi = str(e8.get())
            QueZheng = str(e9.get())
            student_infor.write(
                XueYuan + ' ' + BanJi + ' ' + Sno + ' ' + Name + ' ' + Tel + ' ' + Address + ' ' + Tem + ' ' + YiSi + ' ' + QueZheng + '\n')


# 疫情上报
class PageTwo(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="疫情上报", font=LARGE_FONT)
        label.pack(pady=50)

        ft3 = tkFont.Font(size=14)
        ft4 = tkFont.Font(size=12)
        Label(self, text='所在学院：', font=ft3).pack(side=TOP)
        global e1
        e1 = StringVar()
        Entry(self, width=30, textvariable=e1, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='职工号：', font=ft3).pack(side=TOP)
        global e3
        e3 = StringVar()
        Entry(self, width=30, textvariable=e3, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='姓名：', font=ft3).pack(side=TOP)
        global e4
        e4 = StringVar()
        Entry(self, width=30, textvariable=e4, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='电子邮箱：', font=ft3).pack(side=TOP)
        global e5
        e5 = StringVar()
        Entry(self, width=30, textvariable=e5, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='当前所在地：', font=ft3).pack(side=TOP)
        global e6
        e6 = StringVar()
        Entry(self, width=30, textvariable=e6, font=ft3, bg='Ivory').pack(side=TOP)
        Label(self, text='体温是否正常：', font=ft3).pack(side=TOP)
        global e7
        e7 = StringVar()
        Radiobutton(self, text='是', variable=e7, value=1, ).pack(side=TOP)
        Radiobutton(self, text='否', variable=e7, value=2, ).pack(side=TOP)
        Label(self, text='是否有疑似症状：', font=ft3).pack(side=TOP)
        global e8
        e8 = StringVar()
        Radiobutton(self, text='是', variable=e8, value=1, ).pack(side=TOP)
        Radiobutton(self, text='否', variable=e8, value=2, ).pack(side=TOP)
        Label(self, text='是否已确诊：', font=ft3).pack(side=TOP)
        global e9
        e9 = StringVar()
        Radiobutton(self, text='是', variable=e9, value=1, ).pack(side=TOP)
        Radiobutton(self, text='否', variable=e9, value=2, ).pack(side=TOP)
        Button(self, text="返回首页", width=8, font=ft4, command=lambda: root.show_frame(StartPage)).pack(pady=20)
        Button(self, text="提交", width=8, font=ft4, command=self.save).pack(side=TOP)

    def save(self):
        with open('student_infor.txt', 'a+') as student_infor:
            XueYuan = str(e1.get())
            Sno = str(e3.get())
            Name = str(e4.get())
            Tel = str(e5.get())
            Address = str(e6.get())
            Tem = str(e7.get())
            YiSi = str(e8.get())
            QueZheng = str(e9.get())
            student_infor.write(
                XueYuan + ' ' + Sno + ' ' + Name + ' ' + Tel + ' ' + Address + ' ' + Tem + ' ' + YiSi + ' ' + QueZheng + '\n')



# 疫情防控填报统计
class PageFour(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        label = tk.Label(self, text="疫情防控填报统计", font=LARGE_FONT)
        label.pack(pady=100)
        tree_data = ttk.Treeview()
        ft4 = tkFont.Font(size=12)
        # 滚动条

        scro = Scrollbar(self)

        scro.pack(side=RIGHT, fill=Y)
        lista = Listbox(self, yscrollcommand=scro.set, width=150)

        f = open('student_infor.txt', 'r')
        text = ("                                             %-16s%-16s%-16s%-16s%-16s%-16s%-16s%-16s%-16s" % (
        "所在学院", "所在班级", "学号", "姓名", "联系电话", "当前所在地", "体温是否正常", "是否有疑似症状", "是否已确诊"))

        li = []
        for i in f.readlines():
            j = i.split(' ')
            j[8] = j[8].replace('\n', '')
            li.append(j)
            li.sort(key=lambda x: x[8], reverse=False)
        for i in li:
            text1 = ("                %-16s%-16s%-16s%-16s%-16s%-16s%-16s%-16s%-16s" % (
            i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
            lista.insert(0, text1)
        f.close()
        lista.insert(0, text)
        lista.pack()
        Button(self, text="返回首页", width=8, font=ft4, command=lambda: root.show_frame(StartPage)).pack(pady=40)

# 高级查询功能
class PageFive(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        tk.Label(self, text="高级查询功能", font=LARGE_FONT).pack(pady=100)

        ft3 = tkFont.Font(size=14)
        ft4 = tkFont.Font(size=12)
        Label(self, text='学生/教师', font=ft3).pack(side=TOP)
        global e7
        e7 = StringVar()
        Radiobutton(self, text='学生', variable=e7, value=1, ).pack(side=TOP)
        Radiobutton(self, text='教师', variable=e7, value=2, ).pack(side=TOP)
        Label(self, text='是否确诊：', font=ft3).pack(side=TOP)
        global e8
        e8 = StringVar()
        Radiobutton(self, text='是', variable=e8, value=1, ).pack(side=TOP)
        Radiobutton(self, text='否', variable=e8, value=2, ).pack(side=TOP)
        Button(self, text="查询", width=8, font=ft4, command=self.modify).pack(pady=20)
        Button(self, text="画表", width=8, font=ft4, command=lambda: root.show_frame(StartPage)).pack()


if __name__ == '__main__':
    # 实例化Application
    app = Application()
    # 主消息循环
    app.mainloop()

