import csv
f = open(r'G:\ResearchWork\G_extrac\jiyi-nowear.gcode','r')
lines = f.readlines()
#print(lines)

c = open('extract_infor_1.csv', 'w', newline="")
writer=csv.writer(c)


#删除单元间空格
def filterNan(item):
    return item != ''

#循环处理每一行
#line为字符串
#lines为总字符串列表
#items为单行字符串列表
#item为单行字符串
#item2为重组的单行字符串列表
for line in lines:
    line = line[0:]#引用字符串
    items = line.split(' ') #以空格区分拆分字符串 #将一个字符串转换为一个列表
    items = list(filter(filterNan, items))#清除空字符,提取的内容为“符号”，”字母+数字“，“单词“
    items = items[0:]
    item2 = list(range(8))

    #将头部为X，Y，Z和F的单元提出,并按序排列
    for item in items:
        if item[0] == 'X':
            item2[0]=item[0];
            item2[1]=item[1:];#不能写作item=item.qppend()

        elif item[0] == 'Y':
            item2[2] = item[0];
            item2[3] = item[1:];

        elif item[0] == 'Z':
            item2[4] = item[0];
            item2[5] = item[1:];

        elif item[0] == 'F':
            item2[6] = item[0];
            item2[7] = item[1:];

        elif item[0] == 'G':
            continue

        for i in range(8):
            if item2[i] == i:
                item2[i] = '';


    writer.writerow(item2)

f.close()
c.close()