# git 学习笔记

## 把本地的工程建立好后与github进行连接，并把mater分支合入到main分支，然后删除远程库的master分支

1. 与github远程仓库建立链接 

> git remote add origin [URL]

2. 把本地的 **master** 分支推到github上
>push -u orgin master

3. 如果推送失败的话，需要用下面这两条命令进行修复
> git config --global --unset http.proxy   
git config --global --unset https.proxy

4. 完成推送后，先从远程仓库获取main版本，并切换至**main**
> git pull   
git checkout main

5. 进行本地的**master**和**main**的融合
>git merge master

6. 融合了两个版本后，将main分支提交至远程仓库
> git push orgin main

7. 提交成功后，删除远程的**master**版本（这里先进行一下查看）
>git brance -a             # 查看所有的分支版本   
git remote orgin --delete master          #删除远程仓库的**master**分支

8. 查看确认删除后，删除本地master分支
> git brance -a   
git brance -d master

以上，就完成了所有操作