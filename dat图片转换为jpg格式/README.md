# dat图片解码
在检查微信缓存中“FileStorage”文件夹时发现了其目录下的“Image”文件夹，想到可能是使用过程中缓存的聊天图片等，但是打开文件夹发现都是dat文件，用图片浏览器打开也提示无法查看。



想到可能是进行了加密处理，便去网上查了一下资料，现在把解密过程描述如下。

需要的工具：Python 16进制编辑器--wxMEdit

1. 原理描述

原理很简单，就是按字节对接收到的图片文件进行了异或处理保存为dat文件，查看时再解码，并且使用的加密代码几乎是一样的，只要我们弄到了加密的字节码，使用其对dat文件进行异或操作保存为png文件便可以查看了。

2. 获取加密字节码 工具----16进制编辑器

将其中一个文件夹的dat文件通过16进制编辑器打开，记录其开头两个16进制的值，随机挑选一部分dat文件打开，查看开头两个16进制的值并对比，一般来说是一样的，这两个值是解密的关键。

<img src="https://images.gitee.com/uploads/images/2021/1005/004435_848184d8_9732815.png" width="700"/>

我这里开头的两个值几乎都是3F 18，同时我们了解到网络中传输的图片多为jpg格式，而jpg格式的图片开头两个16进制的值通常为FF D8，我们打开计算器，将这两个值[3F18 XOR FFD8]异或一下，得到两个16进制的值，通常来说应该是一样的，那么这个16进制的值就是解码的关键了。



本机的结果是C0，那么我们只需要将dat文件的所有数据都与C0异或便可以得到解密数据了，同时把数据保存为png格式便可以使用看图软件直接查看了。

 3. 编程实现批量dat图片批量解密

1) 获取指定路径下的所有dat文件，进入for循环等待处理

2) 按次序读入dat文件，按byte对其数据与C0进行异或

3) 将异或后的数据保存下来，后缀改为png，输出到指定文件夹

 


解码效果图
图片解码的代码如下：


```py
def imageDecode(f,fn):
    dat = open(f, "rb")
    out = output_path + fn + ".png"
    png = open(out, "wb")
    for now in dat:
        for nowByte in now:
            newByte = nowByte ^ 0xC0 #修改为自己的解密码
            png.write(bytes([newByte]))
    dat.close()
    png.close()
```

鉴于Python环境不是那么普遍，更新一下使用MATLAB实现dat图片解密的代码:


```py
dat = fopen('1b0882eb7706dfedc7d7becefd1ee2df.dat','rb');% 需要解码的dat文件
A = fread(dat);% 将dat文件的数据读取出来
A = uint8(A);
B = bitxor(A,uint8(243)); % 此处243就是解密字节码的十进制数值，需要更换为自己的解密码
png = fopen('Test2.png','wb'); % 将处理后的数据写入png格式文件，解密成功
fwrite(png,B);
fclose(png);
fclose(dat); % 将上述打开的文档关闭掉
```


