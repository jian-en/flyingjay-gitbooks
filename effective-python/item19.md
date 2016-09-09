# 用关键词参数提供可选行为

和很多其他的程序语言一样，构造函数的时候我们按照位置传递参数。

```python
def remainder(number, divisor):
    return number % divisor
```

使用起来要按照顺序来传参，当然也可以传递参数名:

```python
remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

# 以上使用方法都正确
# 以下错误皆有问题
remainder(number=20, 7)  # 位置参数应该在关键词参数前
remainder(20, number=7)  # 给number赋值两次

```

但是这种使用方法有一个问题，就是每次使用都需要读文档确定位置和参数的对应关系。所以使用关键词参数更好！这样使用起来比较方便，且有一个很好的附加功能，就是能够有默认参数:

```python
def remainder(number, divisor=2):  # 如果不传，即使用默认值
    return number % divisor
```

# 想法

多使用关键词参数，可以提供更多便利，且方便函数的扩展。
