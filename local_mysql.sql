show tables;
# 排序语句
select prod_name from products;
select prod_name,prod_id,prod_price FROM products;
SELECT * FROM products;
SELECT vend_id FROM products;
SELECT distinct vend_id FROM products;
SELECT prod_name,prod_price FROM products ORDER BY prod_price DESC, prod_name DESC;
SELECT * FROM customers;
SELECT cust_id,cust_name, cust_country FROM customers where cust_email IS NULL;
SELECT prod_name,prod_price FROM products WHERE (vend_id=1003 OR vend_id=1002)
 AND prod_price<=10;
SELECT vend_id, prod_name, prod_price FROM products 
WHERE vend_id IN (1002,1003) AND prod_price<10 ORDER BY prod_name;


###################
# 12章 聚集函数
###################

## 所有货物的平均价格
SELECT AVG(prod_price) AS avg_price FROM products;

## 供货商1003的货物平均价格
SELECT vend_id, AVG(prod_price) AS avg_price FROM products
WHERE vend_id = 1003;

## 供货商1003不同品类货物的平均价格
SELECT vend_id, AVG(DISTINCT prod_price) AS avg_price
FROM products
WHERE vend_id = 1003;

## COUNT(*) 忽略空值，COUNT(column) 则不统计空值
SELECT COUNT(*) AS cust_num FROM customers;
SELECT COUNT(cust_email) AS cust_num FROM customers;

########################
## 13章 分组数据
## GROUP BY 和 HAVING
########################

# 显示每个供货商的供货数
SELECT vend_id, COUNT(*) AS num_prods FROM products
GROUP BY vend_id;
# ROLLUP 显示总数
SELECT vend_id, COUNT(*) AS num_prods FROM products
K=GROUP BY vend_id WITH ROLLBACK;

## HAVING 是先分组再过滤，WHERE 是直接过滤
SELECT cust_id, COUNT(*) AS orders FROM orders
GROUP BY cust_id
HAVING COUNT(*) >= 2;

## 同时使用 WHERE 和 HAVING
SELECT vend_id, COUNT(*) AS num_prods FROM products
WHERE prod_price >= 10
GROUP BY vend_id 
HAVING COUNT(*) >= 2;

## 使用 ORDER BY 对分组查询后的结果进行排序
SELECT order_num, SUM(quantity*item_price) AS ordertotal
FROM orderitems
GROUP BY order_num
HAVING SUM(quantity*item_price)>=50
ORDER BY ordertotal;

######################
## 子查询
######################

/*这三条语句是组合查询购买了‘TNT2’的客户信息*/

SELECT order_num FROM orderitems
WHERE prod_id = 'TNT2';

SELECT cust_id FROM orders
WHERE order_num = 20005 OR order_num = 20007;

SELECT * FROM customers
WHERE cust_id = 10001 OR cust_id = 10004;

/*利用子查询来组合这三条语句如下所示,其实就是层层嵌套,
使用 WHERE IN 来构造*/
SELECT * FROM customers
WHERE cust_id in (SELECT cust_id 
                    FROM orders
                    WHERE order_num IN (SELECT order_num 
                                        FROM orderitems
                                        WHERE prod_id = 'TNT2'));

/*对客户10001所有订单数的查询*/
SELECT COUNT(*)  orderstotal
FROM orders
WHERE cust_id = 10001;

/* 作为计算字段的子查询*/
SELECT cust_name, cust_country, (SELECT COUNT(*) FROM orders
                                WHERE customers.cust_id = orders.cust_id)
                                AS orderstotal
FROM customers
ORDER BY orderstotal;

#################################
## 15 联结表 内部联结  叉联结（笛卡尔积）
#################################

/* 等值联结 也成为 内部联结，INNER JOIN*/
SELECT vend_name, prod_name, prod_price
FROM products, vendors
WHERE vendors.vend_id = products.vend_id
ORDER BY vend_name;

SELECT vend_name, prod_name, prod_price
FROM vendors INNER JOIN products
ON vendors.vend_id = products.vend_id
ORDER BY vend_name;

/*连接多个表找出订单2005中所有prod_id|vend_name|prod_price|quantity，这里采用三种方式实现
1.通过逐条查询
2.将逐条查询改为子查询语句
3.用联结表的方式进行,待定留成作业*/

SELECT prod_name, vend_name, prod_price, quantity
FROM orderitems, vendors, products
WHERE vendors.vend_id = products.vend_id
        AND orderitems.prod_id = products.prod_id
        AND orderitems.order_num = 20005;



##############################
## 16章 高级联结
## 自联结
## 自然链接
## 外部连接（左联和右联）
##############################

## 自联结
SELECT prod_id, prod_name FROM products
WHERE vend_id = (SELECT vend_id FROM products WHERE prod_id = 'DTNTR' );

SELECT p1.prod_id, p1.prod_name 
FROM products as p1, products AS p2
WHERE p2.prod_id = 'DTNTR'
        AND p1.vend_id = p2.vend_id;

## 自然联结：自动匹配同名的列，不用指定匹配的列






