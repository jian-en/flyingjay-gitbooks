# 使用Generator而不是返回一个List

在[Item 9](item9.md)中介绍过用generator来处理较大的数据集，而不是一次性加载到内存中逐行处理。我们再来看一个与此相关的问题：

# 问题描述

给定一个字符串，返回这个字符串中所有的单词首字母的索引, 下面是第一版的思路:

```python
def index_words(text):
    result = []  # 1. 初始化一个数组来装载所有元素
    if text:     # 2. 如果字符串不为空，则索引0是第一个单词的开始
        result.append(0)
    for index, letter in enumerate(text):  # 3. 遍历整个字符串
        if letter == '':                   # 4. 如果index位置的字符为空
            result.append(index + 1)       # 5. 则会在index + 1 的位置出现一个新单词
```

上述的解决方案确实可以解决问题，但是有几个问题：

1. 需要引入一个结果列表，完全遍历整个字符串
2. 当text特别大的时候，这是很吃内存的

引入[item9](item9.md)中的**yield**关键词：

这是第二版的思路:

```python
def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == '':
            yield index + 1
```

上面的函数就变成了一个生成器函数，它不是一次把结果放到内存中，而是一个一个吐出来。对待这个函数返回的对象可以像对待列表一样。最重要的一点使用**yield**很清晰地陈述了问题的解决方案，而不需要引入result变量。

## 想法

yield是神器！
