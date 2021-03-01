import collections

# collections是一个内置的集合模块,提供了许多有用的集合类
# 1.namedtuple,可用来表示点坐标
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y, type(p), type(p.x))

# 2.deque,使用list存储时插入数据较慢,deque是为了实现高效插入和删除的双向列表,适合用于队列和栈
q = collections.deque(['a', 'b', 'c', 'a'])
q.append('x')  # 尾部添加
q.appendleft('y')  # 头部添加
q.pop()  # 尾部删除
q.popleft()  # 头部删除
print(q)

# 3.defaultdict,字典中如果引用的key不存在,返回默认值
dd = collections.defaultdict(lambda: 'none')
dd['a'] = 1
print(dd['a'], dd['b'])

# 4.OrderdDict,保持key的顺序
d = collections.OrderedDict([('name', 'xilige'), ('age', 22), ('birthday', '1994-09-27')])
print(d, type(d), d.keys(), d.items())

# 5.Counter,一个简单的计数器
c = collections.Counter()
for ch in 'svgfoifkqnfbfhjadjdshdoq;wngfbvhgqhpqjjsfoyjnwqeqwj':
    c[ch] += 1

print(c)
