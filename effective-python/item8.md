# 在列表表达式中避免使用两个以上的表达式

在上一篇文章中，我们体会到了列表表达式的优势。我们来看一个实际问题：

对于下面的matrix：

```python
maxtrix = [[1,2,3], [4,5,6], [7,8,9]]
```

如果我们想把其中所有的元素都找出来组成一个一维列表，很容易想到:

```python
flat = [x for row in matrix for x in row]
```

虽然有两个表达式，但看上去易读性还是挺好的。

此时，又有一个需求：把其中给matrix中的每一个元素求平方数，那我们可以这样写：

```python
squared = [[x ** 2 for x in row] for row in matrix]
```

倘若如果这个matrix再多一个维度，变成这样：

```python
high_matrix = [
    [[1,2,3], [4,5,6]]
    ......
]
```

此时想把这个matrix中的每个元素都找出来形成新的列表，就需要3个for循环了。如果我们再加上**if**逻辑, 有时候我们会把一个列表表达式弄的十分复杂。所以还不如化繁为简。

## 想法
不要在一个列表表达式中使用2个以上的for或者if表达式，为了增强可读性，直接用for，if展开多行来写。