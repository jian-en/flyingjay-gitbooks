# 使用辅助性方法

Python的简洁性常常会让开发者直接写出一行代码解决很多逻辑的事情，看上去十分狂抓酷炫，但实际上对于可读性，readability，是一种很大的伤害。接下来用一个实际的例子阐释，怎么进行这方面的代码重构。

# 问题描述

从url中解析出来一个形如'red=5&blue=7&green='的参数字符串，这样一个rgb颜色查询需要代码准确解析出red，blue，green的值分别是多少？

# 第一版代码

直接使用**urlparse**包中的**parse_qs**方法, 直接获取即可, 为统一起见，均采用python2写法，python3中的parse_qs方法从urllib.parse中引入,print方法进行相应的改造.

```python
from urlparse import parse_qs
# from urllib.parse import parse_qs # python3
my_values = parse_qs(qs, keep_blank_values=True)  # 保留空值
print 'Red', my_values.get('red')
print 'Green', my_values.get('green')
print 'Opacity', my_values.get('opacity')

>>> Red ['5']
>>> Green ['']
>>> Opacity None
```

问题很明显, 如果不传递某种颜色的值，我们一般希望它是0，而不是None或者[''], 那自然就想到使用默认值的方式，但是如果传了['']的数组需要把数组中第一个元素取出来做判断，这时候就用上了**or**这样方便的关键词.

# 增加默认值

```python
red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0

>>> Red '5'
>>> Green 0
>>> Opacity 0
```

Hooray, 所有的默认值都加上了,但是代码还有一个小问题。就是Red的值是'5', 这是一个字符串类型，我们需要integer类型帮助我们做之后的运算。

# 统一输出格式

```python
red = int(my_values.get('red', [''])[0] or 0)
green = int(my_values.get('green', [''])[0] or 0)
opacity = int(my_values.get('opacity', [''])[0] or 0)

>>> Red 5
>>> Green 0
>>> Opacity 0

```

好的，问题已经解决了。大功告成了！但是不要急，现在的代码如果找另一个开发者过来看，很可能结果是：我不知道这些取第一个索引意味着什么？换句话说，可读性太差！这个时候就是该呼唤重构了！

# 用if...else...进行第一次重构

```python
red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0

green = my_values.get('green', [''])
green = int(green[0]) if green[0] else 0

opacity = my_values.get('opacity', [''])
opacity = int(opacity[0]) if opacity[0] else 0


>>> Red 5
>>> Green 0
>>> Opacity 0
```

这样的重构尽量保证测试一直存在，否则我们不知道自己是否沿着正确的方向前进。看起来不错，我们用了**if...else**语句替代**or**这样生硬的逻辑（永远记着代码越接近自然语言越有可读性）。但是我们在之前的代码风格中提到过，单行的if...else语句其实会牺牲可读性，那好我们再来一次，把它变成多行。

# 多行if...else...再重构一次

```python
red = my_values.get('red', [''])
if red[0]:
    red = int(red[0])
else:
    red = 0

green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0

opacity = my_values.get('opacity', [''])
if opacity[0]:
    opacity = int(opacity[0])
else:
    opacity = 0

>>> Red 5
>>> Green 0
>>> Opacity 0
```

是不是突然感觉清楚多了，但是问题很明显。方法太长了，而且可扩展性太弱，如果我们增加一个颜色标识，又得多加5行代码，秉承Do not Repeat Yourself的原则，把相似代码抽离出来。

# 使用辅助性方法

```python
def get_first_int(values, key, default=0):

    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

red = get_first_int(my_values, 'red')
green = get_first_int(my_values, 'green')
opacity = get_first_int(my_values, 'opacity')


>>> Red 5
>>> Green 0
>>> Opacity 0
```

完美的呈现了问题的解，这种小型辅助性方法帮助程序实现高可复用性。

# 想法

总结一下，就是下面几点：

1. 能用**if...else**解决少用**or**
2. 尽量把**if...else**放到多行，增加可读性
3. 相似代码在重构时想想是否能够用辅助性方法抽离 
