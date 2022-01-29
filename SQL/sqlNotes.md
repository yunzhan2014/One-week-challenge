# 数据库相关的内容

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

