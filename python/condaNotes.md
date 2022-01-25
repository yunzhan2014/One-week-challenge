# Conda 命令

## 一、环境管理

### 创建新的python环境

通过 **--clone** 本地的其他环境

> conda create -n py39 --clone pythonProject

通过指定python的相应版本

> conda create -n py36 python=3.6

### 删除环境

> conda remove -n py39 --all

### 查看使用的环境

> conda info -e

### 激活/返回环境

> conda activate py39
> conda deactivate  

## 参考链接

1. conda 官方文档 [https://conda.io/en/latest/index.html]
2. 清华大学**miniconda** 镜像[https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/]
3. 简书-Anaconda使用总结 [jianshu.com/p/2f3be7781451]

