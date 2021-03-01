from functools import reduce

print(list(map(str, [1, 2, 3, 4, 5])))  # 要list一下map结果才能显示
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 80))
