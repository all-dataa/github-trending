﻿# project
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
- [x] 10/22，用户56，群内集中复盘遇到的问题+接下来的措施
- [x] 10/25，我的后台爬虫原来是每天最大尝试次数 12 次，我以为一定会成功的，结果 GG，今天 daily.py 成功发送的。我还没找到原因，难道就是这玄妙的网络墙吗？接下来设置每天最大尝试次数是 6，我挂着后台程序跑 5 天，看看效果。当天失败的话，就当天转人工跑 daily.py。顺便，今天加的日本妹子很靓丽hhh