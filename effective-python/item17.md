# 遍历参数时，我们需要注意的

直接上来一个问题吧

## 问题描述

给定一组数据，计算每个数据占总数的百分比，举个例子：给定的是中国每一个省一年的GDP数量，返回每个省GDP的占比。这是一个很常见的需求。

```python
def normalize(numbers):
    total = sum(numbers)  # 求和
    result = []
    for value in numbers:
        percent = 100 * value / total  # 分别计算每一个数的占比，如果是python2需要用100.0
    return result
```

我们把问题的复杂度变大，如果给定这个世界所有城市的GDP数量，需要计算其占比。那么该怎么办？自然联想到之前说过的：使用generator生成器。好的，我们从一个文件中载入数据，yield每一行的数据：

```python
def read_gdps(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_gdps('world_cities_gdp.txt')
percentages = normalize(it)
print(percentages)

>>>
[]
```

很奇怪为什么是空呢？仔细观察一下就会发现，生成器对象其实是stateful的，也就是遍历一次就不能再继续使用了。sum()函数将其遍历一次，然后用**for**循环语句自然获取不到任何值。怎么改进呢？

第一种方案，直接把生成器遍历一次保存在内存:

```python
def normalize(numbers):
    numbers = list(numbers) # 用list将generater转成list对象
    total = sum(numbers)
    .....
```

上述方案其实还没有解决那个根本性问题，依然会将大量数据加载到内存。

第二种方案, 传入函数来不断获取一个新的Iterator对象:

```python
def normalize_func(get_iter):
    total = sum(get_iter())  # 返回新的迭代器对象
    result = []
    for value in get_iter():  # 也是一个新的迭代器对象
        percent = 100 * value / total
        result.append(percent)

percentages = normalize_func(lambda: read_gdps(path))  # 传入函数
```

引入了lambda的写法不是很优雅, 其实自己可以按照迭代器对象的协议制定相应的迭代器。

第三种方案:

```python
class ReadGdps(object):

    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):   #  protocol 迭代器对象
        with open(self.data_path) as f:
            for line in f:
                yield line

gdps = ReadGdps(path)
percentages = normalize(gdps)
```

上述方式直接生成了一个迭代器对象，传入后每一次使用都会重新读取文件。

## 想法

遍历大文件需要用迭代器，用类写法更加易读且方便管理。
