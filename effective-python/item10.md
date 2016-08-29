# enumerate比range更好用

最开始学习Python时，大家肯定会对range这个BIF（Built In Function）影响深刻，因为它可以方便地帮助我们生成一个数组。但是习惯了range后，我们经常会写出这样的代码：

```python
for i in range(len(a_list)):
    item_content = a_list[i]
    print('%d:%s' % (i + 1, item_content))
```

为什么会写成这样呢？因为我们不仅想获取每个元素的内容，而且想获取这个元素的序列号是多少。此时引入了i，并且又要兼容**数组从0开始编号**的逻辑。

此时我们就应该弃暗投明，Python给我们提供了另一个好用的BIT: enumerate。此时，上面那段代码可以写成这样的形式。


```python
for i, item_content in enumerate(a_list):
    print('%d:%s' % (i + 1, item_content))
```

此时，大家明白了，enumerate不仅会列举a_list中每一个元素，而且会附带上它的索引。如果我们想让索引从某个数开始计数，可以写成这样：


```python
for i, item_content in enumerate(a_list, 1):
    print('%d:%s' % (i, item_content))
```

这时候，就会从1开始计数了。

## 想法
只有range的写法感觉像C语言的写法，Python这种高级语言能够更好地表达我们的想法。
