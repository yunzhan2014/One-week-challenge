# python知识点

## 类库

1. [tinyDB  非关系型数据库](https://tinydb.readthedocs.io/en/latest/getting-started.html)
2. [click   命令行工具箱](https://click-docs-zh-cn.readthedocs.io/zh/latest/#)
3. [OS      系统相关的](https://www.geeksforgeeks.org/python-os-path-expanduser-method/)
4. [pathlib 专注于路径](https://docs.python.org/zh-cn/3.10/library/pathlib.html)
5. [python-docx](https://juejin.cn/post/7035867058642354207)
6. [pyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation)

### 创建虚拟环境的几种方法

1. venv python原生的方式
2. conda 整体创建
3. virtualenv

### 位置参数和关键值参数，以及*和**参数的用法

### 正反斜杠的问题

> 路径上的应用，首先告诉大家，用于路径上，python是不区分正("/")反("\")斜杠的。
但是呢，反斜杠本身属于转义符，如果"\"后正好有个n，那就会识别为换行符。

> 所以一般我们这样：
r"E:\Python\Lib\site_packages" ，r告诉字符串，这个里面的反斜杠不需要转义。
"E:\\Python\\Lib\\site_packages" ，我把每个反斜杠都转义。
"E:/Python/Lib/site_packages" ，全是正斜杠，不需要转义。
>正则表达式里的反斜杠
正则表达式为什么不同，因为正则表达式要经过两次转义：先经过字符串转义，再来正则表达式自己的转义。
正则表达式想要匹配反斜杠的话，需要写成这样：
"\\\\"，第一次转义为"\\"，第二次转义为"\"。
r"\\"，告诉python，第一次不转义了，直接进行第二次转义。

[在Python的string前面加上‘r’， 是为了告诉编译器这个string是个raw string，不要转意backslash '\ ' 。 例如，\n 在raw string中，是两个字符，\和n， 而不会转意为换行符。由于正则表达式和 \ 会有冲突，因此，当一个字符串使用了正则表达式后，最好在前面加上'r'。](https://blog.csdn.net/orzlzro/article/details/6645909)
> [参考1](https://blog.csdn.net/qq_38161040/article/details/88387537)  
> [参考2](https://www.polarxiong.com/archives/Python-os-path-join-%E4%BA%A7%E7%94%9F%E7%9A%84%E6%96%9C%E6%9D%A0%E5%9C%A8Windows%E5%92%8CLinux%E4%B8%8B%E7%9A%84%E4%B8%8D%E5%90%8C%E8%A1%A8%E7%8E%B0%E5%92%8C%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95.html)  

### 列表的长度在迭代中的变化

[Leetcode 283. 移动零](https://leetcode-cn.com/problems/move-zeroes/)

