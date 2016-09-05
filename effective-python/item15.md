# 环境变量和闭包

根据原书的内容，我们从一个问题说起：

## 问题描述

我们要对一组数进行排序，但是优先把预先提供的数排在前面，举一个例子，对于[8,3,1,2,5,4,7,6]，我们要把[2,3,5,7]优先排到前面，怎么做呢？

可以直接利用python中的**sort**解决这个问题：

```python
def sort_priority(values, group):

    def helper(x):
        if x in group:
            return (0, x)  # 优先排在前面
        return (1, x)

    values.sort(key=helper)

>>>
values = [8,3,1,2,5,4,7,6]
group = [2,3]

sort_priority(values, group)

print(values)
>>> [2,3,1,4,5,6,7,8]
```

函数中套一个函数，这种方式被叫做闭包，这个闭包函数决定了怎么排序，而sort的key参数恰好接受了这样一个值，这边需要注意一下，tuple的排序是先比较第一个再比较后面的，以此类推。

好了，如果我们的需求变一变，我除了想知道排序的结果，我还想知道group中的数字是否在需要排序的数组中。好的，引出一个变量**found**。

```python
def sort_priority2(values, group):
    found = False
    def helper(x):
        if x in group:
            found = True # group中有values中的数
            return (0, x)
        return (1, x)

    values.sort(key=helper)
    return found
```

看似很机智， 但是运行一下，我们发现结果不是我们期待的。found的值依然是False!!!!

好了，不卖关子了，这里面有一个变量的作用域的问题。闭包中的found只在闭包函数中有效，出了函数，就被外面的found覆盖了。因此，即使group中有values中的数，得到的结果依然是False.

```python
def sort_priority2(values, group):
    found = False  # Scope: 函数sort_priority2中
    def helper(x):
        if x in group:
            found = True # Scope: helper中，出不了helper
            return (0, x)
        return (1, x)

    values.sort(key=helper)
    return found
```

那我们怎么解决下这个问题呢？核心也就是把found从闭包中解救出来，好在python3提供了一个关键词解决方案: nonlocal:


```python
def sort_priority2(values, group):
    found = False
    def helper(x):
        nonlocal found # 直接使用外层函数的found
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    values.sort(key=helper)
    return found
```

这种方法虽然巧妙但是如果函数很长，容易造成混乱，其实可以直接用 类 来替代方法。

那么python2怎么办呢？有一个讨巧的方法使用列表：

```python
def sort_priority2(values, group):
    found = [False] # 列表
    def helper(x):
        if x in group:
            found[0] = True # 可以把值送到外面去
            return (0, x)
        return (1, x)

    values.sort(key=helper)
    return found
```

## 想法
局部变量和全局变量这些概念是在编程初期学的，可是很多时候，这些基础还是会被遗忘。


