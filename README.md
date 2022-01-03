# One-week-challenge

一周的时间能做多少事情，人生许多困顿和力所不及，我想都可以用一周又一周的时间去改变，毕竟虚度的光阴也是这样悄悄流逝的

## week 1  12月19日-12月25日

### 数据库相关的内容

1. 面试吃了不会sql做增和删除的亏，之前只是学习了怎样查表。

```sql
CREATE  TABLE gradtable(
id int  NOT  NULL AUTO_INCREMENT,
st_name char(50) NOT  NULL,
class char(5) NULL,
course char(50) NULL,
score int  NULL,
PRIMARY  KEY (id)
) ENGINE = InnoDB;

INSERT  INTO gradtable(st_name,course, score)
VALUES('张三','语文',87);
INSERT  INTO gradtable(st_name,course, score)
VALUES('李四','语文',86),
('李四','数学', 98),
('李四','英语', 90);
INSERT  INTO gradtable(st_name,course, score)
VALUES('王五','语文',85),
('王五','英语', 91);
  
# 查询一个每个学生所有科目的平均值，降序排列
SELECT st_name, AVG(score) AS avg_socre
from gradtable
GROUP BY st_name
ORDER BY avg_socre DESC;

## 更新 张三的成绩
UPDATE gradtable
SET score =  89
WHERE st_name =  '张三';
```

2. 这个案例忘记了COUNT()的使用方法

```sql
## 创建表
CREATE TABLE students (
    id  INT NOT NULL AUTO_INCREMENT,
    stu_name CHAR(15) NOT NULL,
    sex CHAR(8) NULL,
    age INT NULL,
    PRIMARY KEY (id)
  ) ENGINE = InnoDB;

## 插入数据
INSERT INTO students (stu_name, sex, age)
VaLUES('张三', '女', 15),
('王五', '女', 16),
('李四', '女', 16);

SELECT age, COUNT(age) as number
FROM students
WHERE sex='女'
GROUP BY age;

## 采用DISTINCT 关键字进行筛选

SELECT age, COUNT(DISTINCT age) as num
FROM students
WHERE sex='女';
```

### Liunx命令

1. 查询某个程序运行的情况

```shell
ps -ef 查看所有进程
top 也可以查看 
```

2. 查看增量增长的日志

```bash
tail -f **.log 查看增量增长的文件
tail -f **.log | grep **关键词**
```

> 相关指令：more less cat header

### 数据驱动

## YAML 格式

### 学习材料

* [Yaml 官网](https://yaml.org/)
    能看到各种python yaml库，以及yaml新特性更新

* [菜鸟驿站]（）

### Vim

分别更改这些配对标点符号中的文本内容。
> ci’、ci”、ci(、ci[、ci{、ci< -

分别删除这些配对标点符号中的文本内容。
> di’、di”、di(或dib、di[、di{或diB、di< -

分别复制这些配对标点符号中的文本内容。
> yi’、yi”、yi(、yi[、yi{、yi< -

分别选中这些配对标点符号中的文本内容。
> vi’、vi”、vi(、vi[、vi{、vi< -

## python知识点

### 类库

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
