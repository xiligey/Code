a = 10
while a > 0:
    print(a)
    a -= 1
    if a == 5:
        continue  # 跳过后边的代码 进入下一个循环
    if a == 3:
        pass  # 啥也不做 只是占位
    if a == 2:
        break # 跳出循环
