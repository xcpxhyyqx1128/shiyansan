import pymysql
import xlwt
##1、连接数据库并查询对应的表数据
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='000000', database="yiqing",charset="utf8")
curs = conn.cursor()

sql = '''select * from infotable'''
curs.execute(sql)
rows = curs.fetchall()

##2、初始化 Excel
w = xlwt.Workbook(encoding='utf-8')
style = xlwt.XFStyle()  # 初始化样式
font = xlwt.Font()  # 为样式创建字体
font.name = "微软雅黑"
style.font = font  # 为样式设置字体
ws = w.add_sheet("信息", cell_overwrite_ok=True)

##3、写入 Excel 表
title = "id,number,name,college,mail,area,is_heat,,is_maybe,is_sure,type"
title = title.split(",")
for i in range(len(title)):
    ws.write(0, i, title[i], style)
    # 开始写入数据库查询到的数据
    for i in range(len(rows)):
       row = rows[i]
       for j in range(len(row)):
           if row[j]:
               item = row[j]
               ws.write(i + 1, j, item, style)


##4、保存到本地
# 写文件完成，开始保存xls文件
path = 'daochu.xls'
w.save(path)
conn.close()
