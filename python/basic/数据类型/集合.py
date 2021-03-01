# 检查列表中的有重复的元素
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

# 集合的运算
set1 = set(['yellow', 'red', 'blue', 'green', 'black'])
set2 = set(['red', 'brown'])
print(set1.intersection(set2))  # 交集
print(set1.difference(set2))  # 差集

# {}创建集合
set3 = {'yellow', 'red', 'blue', 'green', 'black'}
print(type(set3))
