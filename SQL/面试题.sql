
CREATE TABLE students (
    id  INT NOT NULL AUTO_INCREMENT,
    stu_name CHAR(15) NOT NULL,
    sex CHAR(8) NULL,
    age INT NULL,
    PRIMARY KEY (id)
  ) ENGINE = InnoDB;

INSERT INTO students (stu_name, sex, age)
VaLUES('张三', '女', 15),
('王五', '女', 16),
('李四', '女', 16);

SELECT age, COUNT(age) as number
FROM students
WHERE sex='女'
GROUP BY age;

## SELECT age, COUNT(DISTINCT age) as num
FROM students
WHERE sex='女';