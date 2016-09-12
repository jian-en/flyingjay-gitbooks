# 使用None和Docstring来控制动态默认变量

先说一下什么是动态默认变量，我们先说一个场景：打log。如果不传相应的时间，那么默认就是当下的时间，函数可能会写成这样：

```python
from datetime import date
def log(message, when=datetime.now()):
    print('%s:%s' % (when, message))
```

但是，万万没想到，这是有问题的：

```python
log('hello')
log('hello')  # 这两次调用其实显示的时间都是一个
```

原因在于函数在第一次载入的时候，datetime.now()已经运行了，获取了默认值，之后都不会再动态赋值。

为了达到动态赋值的效果，我们可以这样做：

```python
def log(message, when=None):  # 动态的值用None替代
    """Log a message with a timestamp

    Args:
        message: str
        when: datetime of now
        defaults to now
    """
    when = datetime.now() if when is None else when  # 如果不传值，则用默认
    print('%s:%s' % (when, message))
```

这样就对了，在调用的时候才运行一次。我们再说一个例子，解析json，如果json有问题返回一个默认值：

```python
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default
```

这会出现什么问题呢？同样道理函数只被加载一次：

```python
foo = decode('bad data')
foo['stuff'] = 5

bar = decode('bad again')
bar['meep'] = 1

print('Foo:', foo)
print('Bar:', bar)
>>>
Foo: {'stuff': 5, 'meep': 1}
Bar: {'stuff': 5, 'meep': 1}
```

为什么Foo和Bar是一样的？因为其实我们改变的是同一个默认值。当然，也可以用None + docstring的形式解决。

# 想法
默认参数只在加载的时候运行了一次，多思考自己是否用正确了。
