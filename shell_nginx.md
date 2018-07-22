## shell

### linux cmd

常用的shell有: sh,bash,zsh

查看当前的shell类型: echo $SHELL
查看所有的shell类型: cat /etc/shells
改变当前的shell类型: chsh -s /bin/zsh 

(pwd;cd ..;pwd)

pwd;cd ..;pwd

man bash-builtins

$? 为执行命令的退出码 

echo $? 如果为0,说明执行成功

cd - 回到上一次的路径/回到OLDPWD对应的路径

### shell脚本

vim a.sh

#! /bin/sh 开头

改变a.sh的执行权限 : chmod a+x a.sh

/bin/sh a.sh 或者 ./a.sh 执行

source a.sh 或者 . a.sh 也执行

### shell变量

变量分 环境变量与本地变量

查看环境变量: env
打印环境变量: printenv

查看所有变量,包括本地变量: set

查找环境变量: env | grep "envname"
查找本地变量: set | grep "setname"

定义本地变量diner:
diner="tang"

将本地变量升级为环境变量: export diner

删除一个本地变量或者环境变量: unset diner

--------------------------------------------------
<br/>
<br/>

## nginx

1. nginx的三大功能是什么
  > 反向代理,负载均衡,静态资源服务器

2.什么是正向代理与反向代理

3.什么是负载均衡,nginx的负载均衡有几种策略?

### nginx配置文件相关
