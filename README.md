﻿# project
全自动的 github trends 爬虫邮件发送

# how to use
## linux deploy
进入虚拟环境 ```source tenv/bin/activate```

将程序挂在后台运行  ``` nohup python -u app.py > output.log 2>&1 &```

web3信息流：```nohup python -u web3_app.py > web3.log 2>&1 &```

查看进程运行成功  ```ps aux | grep python```

关闭进程  ```kill [进程id]```

我进行测试查看效果 ```nohup python -u test.py > output2.log 2>&1 &```

获取有多少用户邮箱 ```wc -l emails.txt``` 结果 +1 就是最终的订阅用户数

# log
- [x] 9/26，确定做 github && hugging face 每日自动化实时爬虫+社群AI发送/邮件推送 的功能
- [x] 9/28，获取邮件美化建议：找个html邮件模板套一下，简单又好看
- [x] 10/8，优化爬取失败的重爬机制，更鲁棒
- [x] 10/22，用户56，群内集中复盘遇到的问题+接下来的措施
- [x] 10/25，我的后台爬虫原来是每天最大尝试次数 12 次，我以为一定会成功的，结果 GG，今天 daily.py 成功发送的。我还没找到原因，难道就是这玄妙的网络墙吗？接下来设置每天最大尝试次数是 6，我挂着后台程序跑 5 天，看看效果。当天失败的话，就当天转人工跑 daily.py。顺便，今天加的日本妹子很靓丽hhh
- [x] 10/26，晚上看完毒液3的电影来了灵感，原来的定时代码失效了，搜索写了个更简洁的，明天观察下。做自己的产品真 tm 爽呀~
- [x] 10/28，给代码加入稳健的日志，所有运行记录以及错误都会计入日志，解决原来的问题
- [x] 10/31，今天用户满78啦，今天一天就来了 6 个用户，金钱 +60，代码稳健跑 4 天
    - [x] 我的下一步目标，到达 100 就采用新的定价 19.9，只要能拉 2 个人我就多送他 1 年服务
- [x] 11/1，在宿舍孵化出 Web3信息流 产品2，晚上成交卖了一单
- [x] 11/2，目前 83+5=88 个用户了    
- [x] 11/5，晚上和林博聊天，我们两个人相互安利自己的产品，我玩了玩他的 swanlab，在他安利后我用户+4，现在用户98
    - [x] 从林博获取灵感：关注某个具体开源项目的更新动态，
    （1）几个主流的开源项目最近在关注什么，（2）跟我是竞争对手的开源项目，在关注什么，（3）跟我是生态关系的开源项目，在关注什么
    本质就是个情报系统
- [x] 11/5，产品破百，发了个9.9红包，心怀感恩