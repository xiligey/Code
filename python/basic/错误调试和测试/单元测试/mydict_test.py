# coding=utf-8
import unittest

from mydict import Dict


class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    # 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。
    # 这两个方法会分别在每调用一个测试方法的前后分别被执行
    def setUp(self):
        print 'setUp...'

    def tearDown(self):
        print 'tearDown...'


if __name__ == '__main__':
    unittest.main()
"""
运行单元测试

一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：

if __name__ == '__main__':
    unittest.main()
这样就可以把mydict_test.py当做正常的python脚本运行：

$ python mydict_test.py
另一种更常见的方法是在命令行通过参数-m unittest直接运行单元测试：

$ python -m unittest mydict_test
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。
"""
