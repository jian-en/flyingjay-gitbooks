# 了解你使用的Python版本

python现在有两个版本，严格来说是python2和python3; 比如我们在命令行中敲入python，其实就是python2版本（不论是python2.5, 2.6还是2.7)，python3有自己一套独立的环境，也就是在命令行中敲入**python3**，想要查看python的版本很简单:

```python
python --version
python3 --version
```
在代码中查看python的版本也是可以的:

```python
import sys
print(sys.version_info)
print(sys.version)
```

因为python2现在已经不加入新功能了，社区的重心都在转向python3，因此建议开发者下一个新项目都能用python3来开发。
现有的支持python2到python3平滑转移的项目有：

* [six](https://pythonhosted.org/six/)  因为2 * 3等于6，所以这个包的名字叫做six, 我们下载的包很多都有这个依赖，原因是都做了python2，python3的兼容:

"Six provides simple utilities for wrapping over differences between Python 2 and Python 3. It is intended to support codebases that work on both Python 2 and 3 without modification. six consists of only one Python file, so it is painless to copy into a project."

* [2to3](https://docs.python.org/2/library/2to3.html)  有点像一个翻译，可以直接把python2代码翻译成python3的

"2to3 is a Python program that reads Python 2.x source code and applies a series of fixers to transform it into valid Python 3.x code. The standard library contains a rich set of fixers that will handle almost all code."

# 想法
以后我们的小项目可以尝试着向python3转移，尝试多了解一些python3的新特性。
