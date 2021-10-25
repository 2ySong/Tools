## 如何解决Clion中文乱码问题

按照如下操作勾选

![image-20211021220112738](https://gitee.com/song-zhangyao/mapdepot1/raw/master/typora/202110212201669.png)

并在CMakeLists.txt文件中添加如下代码：

```
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -fexec-charset=GBK")
```

