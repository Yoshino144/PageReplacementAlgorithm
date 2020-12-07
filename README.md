页面置换算法 图形界面

开发环境：

```
Windows 10 20H2 + Python3.8 
```

基础Python库：

```
Pillow == 8.0.1
PyQt5 == 5.15.1
PyQtChart == 5.15.1
pyinstaller == 4.1
```

目录

```
├── README.md             // 帮助
├── GUI.py                // 主界面
├── NEW_GUI.py            // 比较界面
├── data                  // 数据文件
│   ├── ico.ico           // 图标
│   ├── ico.png           // 图标
│   ├── mieba.png         // 图标
│   ├── start.png         // 启动图
├── FIFO.py               // 先进先出算法算法
├── OPT.py                // 理想型淘汰算法
├── LRU.py                // 最近最久未使用算法
```



##### （一）手动输入模式

###### 1.数据

页面数据：1 2 3 4 5 2 1 2 3 4 1 2 3 2 3 2 3

内存块数：3

 

###### 2.先进先出算法 FIFO 手动：

 ![image-20201207110310377](https://raw.githubusercontent.com/Yoshino144/page_replacement_algorithm/master/img/8.png)        

 

###### 3.最近最久未使用算法 LRU手动：

 ![image-20201207110316425](https://raw.githubusercontent.com/Yoshino144/page_replacement_algorithm/master/img/7.png)

 

###### 4.理性淘汰型算法 OPT手动：

 

 ![image-20201207110321255](https://raw.githubusercontent.com/Yoshino144/page_replacement_algorithm/master/img/6.png)

##### （二）随机生成模式

###### 1.数据

(1)随机数量：100

(2)随机范围：1 30

(3)内存块数：20

 

###### 2.先进先出算法 FIFO 随机：

 

 ![image-20201207110327653](https://raw.githubusercontent.com/Yoshino144/page_replacement_algorithm/master/img/5.png)

###### 3.最近最久未使用算法 LRU手动：

 

 ![image-20201207110334841](https://raw.githubusercontent.com/Yoshino144/page_replacement_algorithm/master/img/4.png)

###### 4.理性淘汰型算法 OPT手动：

 ![image-20201207110340647](https://raw.githubusercontent.com/Yoshino144/page_replacement_algorithm/master/img/3.png)

 

##### （三）算法比较模式

###### 1.数据

(1)随机数量：1000

(2)随机范围：1 15

(3)内存块数：5

 

###### 2.缺页率模式：

 

 ![image-20201207110346544](https://raw.githubusercontent.com/Yoshino144/page_replacement_algorithm/master/img/2.png)

###### 3.平均缺页率模式：

![image-20201207110351263](https://raw.githubusercontent.com/Yoshino144/page_replacement_algorithm/master/img/1.png)