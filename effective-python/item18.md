# 用*来搜集参数 

## 问题描述

需要log一些信息，message放一个string来描述信息，values则收集所有的参数，在我们不知道python强大的功能之前，我们可能会这样写:

```python
def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print('%s:%s' % (message, values_str))


log('My numbers are', [1, 2])
log('No values', None)

>>>
My numbers are: 1,2
No values
```

这样写有什么问题呢？

如果没有参数需要多传一个None或者空数组(被作者定义为 visual noise)

解决这个问题的思路很简单，使用星号。

```python
def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print('%s:%s' % (message, values_str))


log('My numbers are', 1, 2)  # 直接手机所有参数不需要数组
log('No values')

log('My numbers are', *[1,2])  # 拆解参数传入 与上面等价

>>>
My numbers are: 1,2
No values
My numbers are: 1,2
```

## 想法

星号这种语法是相当方便的，当参数过多，我们可以用其来搜集所有这些参数，进入函数他们就统一变成了tuple类型，但要注意，这种类型的参数瞄定的是参数的位置。
