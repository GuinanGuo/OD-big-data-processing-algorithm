

with open('人数.txt', 'r')as f:  # 打开文件
    data_peop_num = f.read()  # 读取
data_201711 = dict()  # 初始化筛选的201711数据
for d in data_peop_num.split('\n'):
    data = d.split('\t')  # 按\t区分出每个列
    if data[0] == '日期':  # 判断第一行
        continue
    if data[0] == '2001':
        data_201711[data[2]] = data[-1]  # 将id作为键，人数作为值
with open('比例.txt', 'r')as f:  # 打开文件
    data_bl = f.read()  # 读取
direct = dict()  # 初始化区的数据
# print(data_201711)
f_ = open('各格网每个产业的人数.txt', 'w')  # 打开新文件写入
c = ['网格ID', '网格x坐标', '网格y坐标', '行业:农林牧渔_人数', 'Domain_1_人数', 'Domain_2_人数', 'Domain_3_人数', 'Domain_4_人数', 'city	district', 'town', 'town_code']
f_.write('\t'.join(c) + '\n')  # 写入标题一栏
print('\t'.join(c))
num = 0
num1 = 0
for d in data_bl.split('\n'):
    da = d.split('\t')  # 按\t区分出每个列
    if da[0] == '网格ID':  # 判断第一行
        continue
    try:
        n3 = round(int(data_201711[da[0]]) * float(da[3]), 2)  # 人数乘对应的比例，保留俩位数
        d1 = round(int(data_201711[da[0]]) * float(da[4]), 2)  # 人数乘对应的比例，保留俩位数
        d2 = round(int(data_201711[da[0]]) * float(da[5]), 2)  # 人数乘对应的比例，保留俩位数
        d3 = round(int(data_201711[da[0]]) * float(da[6]), 2)  # 人数乘对应的比例，保留俩位数
        d4 = round(int(data_201711[da[0]]) * float(da[7]), 2)  # 人数乘对应的比例，保留俩位数
        num1 +=1
    except:
        continue

    num += 1
    num_ = [str(n3), str(d1), str(d2), str(d3), str(d4)]   # 人数
    da[3:8] = num_  # 把比例替换人数
    print('\t'.join(da))
    f_.write('\t'.join(da) + '\n')  # 写入数据到result1.txt
    try:
        daa = list()  # 初始化对应加完的列表
        # if num1 == 1:
        #     direct[da[9]] = [0, 0, 0, 0, 0]
        for i, v in enumerate(direct[da[9]]):  # enumerate()返回列表每一行的索引和值用i，v接收
            daa.append(float(num_[i]) + v)  # 把上一次小区的值每隔对应加上这行的人数值
        direct[da[9]] = daa  # 把相同的区数据相加后替换
    except:
            direct[da[9]] = [n3, d1, d2, d3, d4]  # 第一个区进入的时候该区人数赋值

f_.close()  # 关闭文件
print()
print(f'总数据条数{num}')
print(f'能配对的格网个数{num1}')
# print(direct)
f_2 = open('每个区的各产业人数.txt', 'w')  # 打开新文件写入
f_2.write(f'总数据条数{num}'+f'\n能配对的格网个数{num1}\n\n')
f_2.write('district\t第一产业:农林牧渔_人数\t第二和第三产业总人数\n')  # 写入标题一栏
print('district\t第一产业:农林牧渔_人数\t第二和第三产业总人数')
for k, v in direct.items():  # .items()返回字典的键和对应的值， 用k，v接收
    n = float(v[0])  # 第一产业人数
    z_num = 0  # 初始化总人数
    for i in v:
        z_num += float(i)  # 加上每个行业人数
    ds = z_num - n  # 第二和第三产业的人数
    da_line = [str(k), str(n), str(ds)]
    print('\t'.join(da_line))
    f_2.write('\t'.join(da_line) + '\n')  # 写入文件
f_2.close()  # 关闭文件