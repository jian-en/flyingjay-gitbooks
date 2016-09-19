# 函数是一等公民：传递函数参数

许多Python内置的方法都支持传递函数参数，比如**sort**:

```python
names = ['Galeo', 'fujian', 'Fe']
names.sort(key=lambda x: len(x))
print(names)
>>>
['Fe', 'Galeo', 'fujian']
```

Python中函数是没有状态的，因此直接函数很方便，上面我们用lambda自己定义了一个函数，当然还有更加复杂的情况，再举一列：

defaultdict 这个含有默认值字典，也会接受一个默认函数：

```python
def log_missing():
    print('Key added')
    return 0

current = {'green': 12, 'blue': 3}

from collections import defaultdict
result = defaultdict(log_missing, current)
print(result['green'])
print(result['gre'])

>>>
12
Key added
0
```

这个函数就在没有对应键值的时候调用，但是问题来了，传递的函数是没有状态的，如果我想记录到底有多少键值不存在？也就是保留相应状态，那么可以有这么几个方法：

1. 把这个函数变成闭包函数，用**nonlocal**将计数器暴露出来；

2. 设计一个类，类中可以保留这样的变量，把类方法传递给defaultdict；

3. 设计一个类，在类中定义**__call__**方法，那么这个类实例就可以直接传入；

## 想法
函数是一等公民，传递函数参数很方便，但是函数参数都是无状态的，如果想记录状态，可以改为闭包函数或者类函数。
