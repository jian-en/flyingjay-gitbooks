# 用关键词参数增加函数的清晰度

给函数传参数能够用关键词参数(keyword args)或者位置参数(positional args)，但是位置参数不明确，举一个简单例子:

```python
hello('hello world', 1, True, False)
```

对于上面的调用，我们怎么知道哪一个参数是做什么呢？很难！因此有一种方法可以帮助我们强制外部传关键词参数：

python3中:

```python
def hello(arg1, arg2, *, kw_arg1=False, kw_arg2=True):
    pass
```

用\*可以合理的隔离出关键词参数, 这个时候想要给关键词参数赋值必须用关键词参数, 否则报错。python2只能用另一种讨巧的方法, \*\*kwarg:

```python
def hello(arg1, arg2, **kwargs):
    pass
```

用kwargs收集所有关键词参数即可。

# 想法

使用关键词参数来增加函数调用的可读性。
