#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# 显示高度
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.- 0.2, 1.03*height, '%s' % int(height))

plt.rcParams['font.sans-serif']=['STSong']     ## 中文宋体
#各学院填报统计
name_list = ['文学院','历院','教院','心理学院','马院','社管院','法学院','经济学院','商学院',
                     '外国语学院','音乐学院','舞蹈学院','美术学院','体育学院','数统院','计工院','物电院',
                     '化工院','生科院','地环院','教技院','传媒学院','旅游学院','国交院',
                     '敦煌学院','哲学学院']
num_list = [20,20,10,5,19,30,4,3,8,2,9,10,16,17,5,8,9,13,15,24,21,24,5,7,24,31,]
num_list2 = [5,0,2,1,2,3,0,0,1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
x = list(range(len(num_list)))
total_width, n = 0.8, 2
width = total_width / n
plt.bar(x, num_list, width=width, label='已填报', fc='b')
for i in range(len(x)):
    x[i] += width
plt.bar(x, num_list2, width=width, label='未填报', tick_label=name_list, fc='g')
plt.title('各学院填报统计')
plt.xticks(rotation=270)
plt.legend()
plt.show()





# 显示高度
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.- 0.2, 1.03*height, '%s' % int(height))

plt.rcParams['font.sans-serif']=['STSong']     ## 中文宋体
#化工院填报统计
name_list = ['已填报','未填报',]
num_list = [29, 5]
autolabel(plt.bar(range(len(num_list)), num_list, color='rgb', tick_label=name_list))
plt.title('化工院填报统计')
plt.xticks(rotation=270)
plt.show()


# 显示高度
def autolabel(rects1, rects2):
    i = 0
    for rect1 in rects1:
        rect2 = rects2[i]
        i += 1
        height = rect1.get_height() + rect2.get_height()
        plt.text(rect1.get_x()+rect1.get_width()/2. - 0.1, 1.03*height, '%s' % int(height))


name_list = ['学生', '教师',]
num_list = [140, 47,]
num_list2 = [5, 2,]
z1 = plt.bar(range(len(num_list)), num_list, label='已填报', fc='b')
z2 = plt.bar(range(len(num_list)), num_list2, bottom=num_list, label='未填报', tick_label=name_list, fc='g')
autolabel(z1, z2)
plt.title('学生教师填报情况统计')
plt.legend()
plt.show()


# 显示高度
def autolabel(rects1, rects2):
    i = 0
    for rect1 in rects1:
        rect2 = rects2[i]
        i += 1
        height = rect1.get_height() + rect2.get_height()
        plt.text(rect1.get_x()+rect1.get_width()/2. - 0.1, 1.03*height, '%s' % int(height))


name_list = ['学生', '教师',]
num_list = [145, 55,]
num_list2 = [3, 1,]
z1 = plt.bar(range(len(num_list)), num_list, label='未确诊', fc='b')
z2 = plt.bar(range(len(num_list)), num_list2, bottom=num_list, label='已确诊', tick_label=name_list, fc='g')
autolabel(z1, z2)
plt.title('学生教师确诊情况统计')
plt.legend()
plt.show()

name_list = ['计工院', '化工院', '数统院', '地环院']
num_list = [20, 15, 19, 28]
num_list2 = [0, 0, 0, 0]
x = list(range(len(num_list)))
total_width, n = 0.8, 2
width = total_width / n
plt.bar(x, num_list, width=width, label='已填报', fc='b')
for i in range(len(x)):
    x[i] += width
plt.bar(x, num_list2, width=width, label='未填报', tick_label=name_list, fc='g')
plt.legend()
plt.show()



name_list = ['学生未确诊','学生确诊','教师未确诊','教师确诊',]
num_list = [145, 5, 57, 1, ]
colors = ['green', 'yellow',]
# 保证圆形
plt.axes(aspect=1)
plt.title("确诊情况统计")
plt.pie(x=num_list, labels=name_list, autopct='%3.1f %%')
plt.show()


name_list = ['学生未确诊','学生确诊','教师未确诊','教师确诊',]
num_list = [5, 2, ]
colors = ['green', 'yellow',]
# 圆形
plt.figure(1, figsize=(6, 6))
#决定分割部分，及其与其它部分之间的间距
expl = [0, 0, 0, 0.1]
plt.title("确诊情况统计")
plt.pie(x=num_list, explode=expl, labels=name_list, autopct='%3.1f %%', colors=colors, shadow=True)
plt.show()
