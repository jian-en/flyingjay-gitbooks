# 用列表推导式替代map, filter方法

Python通过借鉴其他语言，引入了一些函数式编程的思想。map, filter就是两个方便的方法，但很多时候我们既可以用列表推导式，又可以用map，filter时。我们改选择哪一个呢？

## 问题实例

### 问题一

求一组数的平方数:

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [x ** 2 for x in a]
print(squares)
```

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = map(lambda x: x ** 2, a)
print(squares)
```

### 问题二

我们接着列举，求同样这组数中的偶数的平方数:

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_squares = [x ** 2 for x in a if x % 2 == 0]
print(even_squares)
```

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_squares = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))
print(even_squares)
```

这时候我们明显可以感觉到map, filter写起来有点费脑子，因为嵌套比较多。而等价的列表推导式做法却很干净，清爽。

## 拓展

其实dictionary, set数据类型也可以用推导式，把**[]**改成**{}**就好。

## 想法

map, filter虽好，但是引入了lambda这样的噪音。直接上列表推导式就好!
