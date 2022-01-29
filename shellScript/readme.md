# Liunx 命令行

## 文件管理

lsof 万物皆文件

### 创建
touch
vim
>> 追加
> >直接创建

创建 软链接和硬链接

### 查看
less
more
head
tail
cat


2. 查看增量增长的日志

```bash
tail -f **.log 查看增量增长的文件
tail -f **.log | grep **关键词**
```

> 相关指令：more less cat header


### 删除

rm 


### 更改文件权限

chmod
chown


### 进行文件的压缩和解压缩

tar


## 设备管理

### 网络管理

ifconfig
netstat 
iptables
tcpdump

### 磁盘存储
mount
umount

du

df 
### 内存管理
free

## 程序监视和管理

top/htop
ps -ef
sar
lsof

kill -9 
killall

## 工具

### 字符串工具

sed
awk
cut

### 

