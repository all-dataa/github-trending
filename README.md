# project
全自动的 github trends 爬虫邮件发送

# how to use
## linux deploy
进入虚拟环境 ```source [yourenv]/bin/activate```

将程序挂在后台运行  ```nohup python app.py > output.log 2>&1 & ```

查看进程运行成功  ```ps aux | grep python```

关闭进程  ```kill [进程id]```

# log
- [x] 9/26，确定做 github && hugging face 每日自动化实时爬虫+社群AI发送/邮件推送 的功能
- [x] 9/28，获取邮件美化建议：找个html邮件模板套一下，简单又好看
- [x] 10/8，优化爬取失败的重爬机制，更鲁棒