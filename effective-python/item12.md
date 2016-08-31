# 在for或者while后面跟一个else，你知道是什么意思吗？

**else**这个关键字最常出现在if语句或者try语句中，首先if...else语句很好理解，表示两个分支选择其一运行。然而当我们把else和for这样的循环语句放在一起时，会是什么意思呢？

```python
for i in range(10):
    print(i)
else:
    print('I am done')

>>>
0
1
...
I am done
```

输出结果很容易能猜出来，但是为什么要这样写呢？不需要else我们也可以达到一样的效果啊。有一个地方不一样，就是else共享for语句中的局部变量的，可能可以达到一些特别的效果。但是如果写成这样呢？


```python
for i in range(10):
    print(i)
    if i == 3:
        break
else:
    print('I am done')
>>>
0
1
2
3
```

此时，else语句被break强行跳出了，那么就不会执行。

What??

感觉不符合正常思维啊，所以尽管python提供了这么一个else，但是作者建议还是少用，其实能用到else语句的都可以用更易读的代码重写。

## 想法
有些代码设计时，给了很多所谓**方便**关键词，但怎么用好？在于使用者。
