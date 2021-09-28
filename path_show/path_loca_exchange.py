import math
f = open('C:\\Users\\Administrator\\Desktop\\jiyi.txt')
lines = f.read().splitlines()#消除换行符
#lines = f.readlines()  #存在换行符的形式

#Reading Original Path from the text and save as list ori_path
ori_path = list();
item2 = list()
for line in lines:
    ori_path.append(line)#lines的每行数据为line为一个字符串
    #line = line[0:]
    items = line.split(' ')#将line按照空格打断，字符串list组成一个新的list
    item2.append(items)#将line的list再组成一个新的list

#depart x and y coordinates into two columns
x_column = list()
y_column = list()
for item in item2:
    x_column.append(item[0]) #提取出x坐标作为一列
    y_column.append(item[1]) #提取出y坐标作为一列
x_column_trans = list()
y_column_trans = list()

#对x，y坐标做平移变换
for x in x_column:
    x = float(x)-250;
    x_column_trans.append(x)

for y in y_column:
    y = float(y)-100;
    y_column_trans.append(y)

#rotate x，y for a better position
angel = 45;#degree
pi = 3.1415926535897932;
angel_rad = pi/180*angel;
rotate_center = [0,0]

x_rotate = list();
y_rotate = list();
for i in range(len(x_column)):
    x_r = (float(x_column_trans[i]) - 0) * math.cos(angel_rad) - (float(y_column[i]) - 0) * math.sin(angel) + 0
    y_r = (float(y_column_trans[i]) - 0) * math.sin(angel_rad) + (float(y_column[i]) - 0) * math.cos(angel) + 0
    x_rotate.append(x_r);
    y_rotate.append(y_r);

print(ori_path)
print(items)
print(item2)
print(x_column)
print(y_column)
print(x_column_trans)
print(y_column_trans)
print(x_rotate)
print(y_rotate)