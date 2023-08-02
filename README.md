<br>

## 简介

<br>
<br>
基于PyQt5和openai_api的chatgpt3.5 windows桌面应用 2023-6
<br>
<br>
<br>
搞到gpt3.5账号->去openai官网搞到api-keys->根据openai官网的python api文档->套一个pyqt5的壳玩玩
<br>
<br>
            openai_api-keys网站：https://platform.openai.com/account/api-keys
<br>
<br>
学习书籍参考 1.明日科技-Python 从入门到精通 
            2.明日科技-PyQt从入门到精通
<br>
<br>
<br><br>

## 文件说明

<br>
1. chat.py：主内容文件 包含api输入窗口和对话窗口<br><br>
2. chat3.ui：对话窗口的ui设计界面 可用QT designer附件打开 再用PYUIC转换为py代码<br><br>
3. logkey.ui：api输入界面 同上<br><br>
4. main.py：openai库最简单prompt调用3.5模型示例<br><br>
5. mrsoft.db：主要存放api的密匙 和记录登录界面的两个勾选窗口是否被勾选<br><br>
<br>
<br>
<br>

## 大概想法

<br>
因为openai规定免费用户调用api次数1分钟只有3-4次好像 <br><br>
所以每当按下send发送后先run一个线程计时10秒冷却开关 <br><br>
然后再run第二个线程发送信息给openai官网 防止阻塞在主页面卡顿卡死<br><br>
<br>
<br>
            完整安装包下载地址：<br>
            https://pan.baidu.com/s/1fcsfhmIeYG336LTR4XGL9w?pwd=w0ci    提取码: w0ci 
<br>
<br>
<img src="https://github.com/hhhhhhos/PyQt5_openai_chatgpt3.5_Windows/assets/71121770/0574371a-1b39-4967-b42d-4a16561f4fda" width=300px>

<img src="https://github.com/hhhhhhos/PyQt5_openai_chatgpt3.5_Windows/assets/71121770/c29bfd28-1827-4544-8be3-8abaca4e8eb9" width=300px>
<br>
<img src="https://github.com/hhhhhhos/PyQt5_openai_chatgpt3.5_Windows/assets/71121770/90dc28d5-94e7-4495-b371-a06ade349cb0" width=300px>
<br>
<img src="https://github.com/hhhhhhos/PyQt5_openai_chatgpt3.5_Windows/assets/71121770/5d352e41-0b44-44e9-91f3-4ad8a2397516" width=600px>











## Thanks

感谢 
