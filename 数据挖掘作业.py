import time

# 列表测试
# 初始化一个10000 * 10000的二维列表
list_data = [[0] * 10000 for _ in range(10000)]

# 记录开始时间
start_time_list = time.time()

# 进行10000 * 10000轮数据修改
for i in range(10000):
    for j in range(10000):
        list_data[i][j] = 1

# 记录结束时间
end_time_list = time.time()

# 计算列表修改所用时间
list_time = end_time_list - start_time_list

# 元组测试
# 初始化一个10000 * 10000的二维元组
tuple_data = tuple(tuple(0 for _ in range(10000)) for _ in range(10000))

# 记录开始时间
start_time_tuple = time.time()

# 由于元组不可变，需要重新创建元组来模拟修改
for i in range(10000):
    new_row = tuple(1 for _ in range(10000))
    tuple_data = tuple(new_row if index == i else row for index, row in enumerate(tuple_data))

# 记录结束时间
end_time_tuple = time.time()

# 计算元组修改所用时间
tuple_time = end_time_tuple - start_time_tuple

# 输出结果
print(f"使用列表修改数据所用时间: {list_time} 秒")
print(f"使用元组修改数据所用时间: {tuple_time} 秒")