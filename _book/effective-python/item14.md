# 在函数中宁可直接抛出异常不要返回None

这其实是一种设计函数的理念，在函数中如果出现异常怎么处理，举一个简单的例子：

```python
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

上面这种写法其实是把潜在的错误在函数内部消化掉了，结果外层代码的逻辑需要判断是否为None, 如果直接用:

```python
result = division(a, b)
if result is not None: # 这种写法OK
    pass

# 但是经常我们会写成这样
if result:
    pass
```

如果是后一种写法的话，会出现的一个问题是：如果是 **division(0, 8)**，那么结果就是0，此时if result: 就会被跳过去，因此None 和 0在一起就会发生歧义。

## 想法
那么比较好的处理方法就是：不要自己定义返回值，直接跑出异常，让上层代码按照自己的逻辑处理可能发生的异常。但是需要在函数定义中明确的说明可能出现的异常。
