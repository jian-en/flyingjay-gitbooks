# 使用zip来并行地处理迭代对象

## 问题描述
先描述一下问题，对于这样一组数据，我们想求得最大的长度的字符串元素的位置以及内容：

```python
names = ['hello', 'fujianhaha', 'a']
```

## 问题分析

我们既然比较的是字符串长度，那么需要构建这样一个数组来记录字符串的长度：

```python
letters = [len(n) for n in names]
```

这时候，我们就有一个求解的方式：

```python
longest_name = None
max_letters = 0
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        max_letters = count
        longest_name = name
```

这种方式虽然还行，但是不够简介，引入zip之后：

```python
longest_name = None
max_letters = 0
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
```

用这种方式并行处理两个迭代对象，相对来说是简介而清楚的。这边尤其注意，Python2中的zip和Python3中的zip实际上是不一样的。Python2中的zip会直接求出结果，而python3中的zip生成的是一个迭代器，换言之，更节省内存使用。

## 想法
zip是一个比较小巧的工具，特别对于两个相关性比较大的列表，并行执行会清楚很多。
