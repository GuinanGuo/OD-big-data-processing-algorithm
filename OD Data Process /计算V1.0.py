import csv


city_number = dict()  # 存储城市的人数
city_da = dict()  # 存储城市的计算总和
city_jl = dict()  # 存储城市的距离总和
line_num = 2
None_da = '' #空数据信息
num_noneDate = 0 #空数据的条数
num_totalDate = 0 #数据总条数
with open('1busnod_20171114.csv', 'r')as f:
    f_csv = csv.reader(f)  # 读取csv
    for i in f_csv:  # 循环每一行
        # print(i)
        da_line = i[0].split('\t')  # 通过制表符分割每一列的数据
        # print(da_line)
        if da_line[0] == '日期':  # 如果是第一行直接跳出
            continue
        num_totalDate += 1
        o_city = da_line[2]
        d_city = da_line[6]
        peop_num = int(da_line[-3])  # 人数
        tim = int(da_line[-2])  # 时间
        jl = int(da_line[-1])  # 距离
        if tim == jl == 0: # 用来判断距离和时间是不是空值
            num_noneDate += 1
            print(f'第{line_num}行：', end='')
            print(da_line)
            None_da += f'第{line_num}行:\t' + '\t'.join(da_line) + '\n'
            line_num += 1
            continue

        d = peop_num * tim  # 计算人数*时间
        j = peop_num * jl # 计算人数*距离
        try:
            city_number[o_city] += peop_num  # 加入该行的人数
            city_da[o_city] += d  # 加入计算该行的结果
            city_jl[o_city] += j  # 加入计算该行的结果
        except:
            city_number[o_city] = peop_num  # 初始化第一次记录该城市的人数
            city_da[o_city] = d  # 初始化第一次记录该城市的计算结果
            city_jl[o_city] = j  # 初始化第一次记录该城市的计算结果
        line_num += 1

print()

# 把结果接到txt文件中
with open('result.txt', 'w')as f:
    #
    print(f'总数据有{num_totalDate}条\n'+
          f'空数据有{num_noneDate}条\n'+
          f'空数据占比{round(num_noneDate / num_totalDate,2)}\n')
    print('城市\t平均时间\t平均距离')
    f.write(None_da +
            f'\n总数据有{num_totalDate}条'+
            f'\n空数据有{num_noneDate}条'+
            f'\n空数据占比{round(num_noneDate / num_totalDate, 5)}\n'+
            '\n城市 \t平均时间\t平均距离\n') # 写入空数据
    for k, v in city_number.items():  # 循环每个城市进行计算
        print(f'{k}:\t{round(city_da[k] / v, 2)}\t{round(city_jl[k] / v, 2)}')
        f.write(f'{k}:\t{round(city_da[k] / v, 2)}\t{round(city_jl[k] / v, 2)}\n')  # 写入平均时间和距离
