# coding=utf-8
def feb(n_max):
    n, a, b = 0, 0, 1
    while n < n_max:
        yield b
        a, b = b, a + b
        n += 1


for i in feb(10):
    print(i)
