## 一、GitHub 术语解释

为了大家进一步了解和使用 GitHub，我们一起来看看 GitHub 的常用术语，也可以说是基本概念：

#### **Repository**：

简称Repo，可以理解为“仓库”，我们的项目就存放在仓库之中。也就是说，如果我们想要建立项目，就得先建立仓库；有多个项目，就建立多个仓库。

#### **Issues**：

可以理解为“问题”，举一个简单的例子，如果我们开源一个项目，如果别人看了我们的项目，并且发现了bug，或者感觉那个地方有待改进，他就可以给我们提出Issue，等我们把Issues解决之后，就可以把这些Issues关闭；反之，我们也可以给他人提出Issue。

#### **Star**：

可以理解为“点赞”，当我们感觉某一个项目做的比较好之后，就可以为这个项目点赞，而且我们点赞过的项目，都会保存到我们的Star之中，方便我们随时查看。在 GitHub 之中，如果一个项目的点星数能够超百，那么说明这个项目已经很不错了。

#### **Fork**：

可以理解为“拉分支”，如果我们对某一个项目比较感兴趣，并且想在此基础之上开发新的功能，这时我们就可以Fork这个项目，这表示复制一个完成相同的项目到我们的 GitHub 账号之中，而且独立于原项目。之后，我们就可以在自己复制的项目中进行开发了。

#### **Pull Request**：

可以理解为“提交请求”，此功能是建立在Fork之上的，如果我们Fork了一个项目，对其进行了修改，而且感觉修改的还不错，我们就可以对原项目的拥有者提出一个Pull请求，等其对我们的请求审核，并且通过审核之后，就可以把我们修改过的内容合并到原项目之中，这时我们就成了该项目的贡献者。

#### **Merge：**

可以理解为“合并”，如果别人Fork了我们的项目，对其进行了修改，并且提出了Pull请求，这时我们就可以对这个Pull请求进行审核。如果这个Pull请求的内容满足我们的要求，并且跟我们原有的项目没有冲突的话，就可以将其合并到我们的项目之中。当然，是否进行合并，由我们决定。

#### **Watch：**

可以理解为“观察”，如果我们Watch了一个项目，之后，如果这个项目有了任何更新，我们都会在第一时候收到该项目的更新通知。

#### **Gist：**

如果我们没有项目可以开源或者只是单纯的想分享一些代码片段的话，我们就可以选择Gist。不过说心里话，如果不翻墙的话，Gist并不好用。

## 二、Git 初体验及其常用命令介绍

接下来介绍 Git 的命令操作，包含 init、add 等，在 Git 中，所有的命令都是以git开头，例如，git init其作用就是初始一个 Git 仓库。

为了方便演示，我们先在D盘的CoderLife目录下创建一个名为demo的子目录，并在其中新建一个名为hit.txt的文件，接下来我们的 Git 操作都是基于此目录和文件的。

![img](https://pic2.zhimg.com/50/v2-30263746fb2b0bc3f37b560c2d3df05d_720w.jpg?source=1940ef5c)![img](https://pic2.zhimg.com/80/v2-30263746fb2b0bc3f37b560c2d3df05d_1440w.jpg?source=1940ef5c)

此外，在这里还要强调一点，那就是：在我们进行任何的git操作之前，我们都得先切换到 Git 的仓库目录。

换言之，我们得到先进入到（我们定义的）Git 仓库的最顶层文件目录下，然后从此目录中进入 Git Bash，这样之后的操作才能顺利进行。

如果是 Linux 操作系统，则可以直接cd到仓库目录。

以博主为例，选择demo目录作为 Git 仓库，然后进入demo目录之中，点击鼠标右键，再选择Git Bash Here，即可打开 Git Bash 的命令行窗口。

![img](https://pica.zhimg.com/50/v2-ff4b6b4436077764af5ce83ee41f76dc_720w.jpg?source=1940ef5c)![img](https://pica.zhimg.com/80/v2-ff4b6b4436077764af5ce83ee41f76dc_1440w.jpg?source=1940ef5c)

如上图所示，Git 会自动定位到进入的位置，如我们选择的demo目录，这也是为什么我们需要先进入到 Git 仓库的最顶层目录下，然后再打开 Git Bash 的原因。下面，我们结合 Git 的常用命令演示一下 Git 的相关操作。

#### **第 1 个命令：git status**

在命令行窗口的光标处，输入git status命令，查看仓库的状态：

![img](https://pic3.zhimg.com/50/v2-41af87497f490ee0e93147921a3dfa4c_720w.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-41af87497f490ee0e93147921a3dfa4c_1440w.jpg?source=1940ef5c)

如上图所示，结果显示demo不是一个 Git 仓库，这是很正常的反应，因为我们还没有在计算机中声明demo为 Git 仓库，之前说demo是 Git 仓库只是我们口头上的说的，计算机当然不会认可。

#### **第 2 个命令：git init**

在命令行窗口的光标处，输入git init命令，初始化 Git 仓库：

![img](https://pic2.zhimg.com/50/v2-2d758c4a4090bce9fb8d4d0447f88546_720w.jpg?source=1940ef5c)![img](https://pic2.zhimg.com/80/v2-2d758c4a4090bce9fb8d4d0447f88546_1440w.jpg?source=1940ef5c)

如上图所示，结果显示已经初始化demo为一个空的 Git 仓库啦！在这里大家可以会有些疑问，因为我们在建立demo目录的同时也在里面新建了一个名为hit.txt的文件，怎么初始化仓库之后，demo目录就变成空的了呢？这个问题稍后解惑，我们重新输入git status命令检查一下仓库的状态：

![img](https://pic4.zhimg.com/50/v2-0215d2df12ba1ceb300c4fe7f512b890_720w.jpg?source=1940ef5c)![img](https://pic4.zhimg.com/80/v2-0215d2df12ba1ceb300c4fe7f512b890_1440w.jpg?source=1940ef5c)

如上图所示，在我们初始化仓库之后，demo目录已经成为一个 Git 仓库了，并且默认进入 Git 仓库的master分支，即主分支。在这里，我们需要注意的是Untracked fies提示，它表示demo仓库中有文件没有被追踪，并提示了具体没有被追踪的文件为hit.txt，还提示了我们可以使用git add命令操作这个文件，简直不要太好。

#### **第 3 个命令：git add**

在命令行窗口的光标处，输入git add hit.txt命令，将hit.txt文件添加到 Git 仓库：

![img](https://pic3.zhimg.com/50/v2-6932af42aa149c735cd429ae5d8b350a_720w.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-6932af42aa149c735cd429ae5d8b350a_1440w.jpg?source=1940ef5c)

如上图所示，如果没有报错，就说明命令已经执行啦！接下来，输入git status命令查看仓库状态：

![img](https://pic4.zhimg.com/50/v2-7658f1c05af7c4dfd277d85889026275_720w.jpg?source=1940ef5c)![img](https://pic4.zhimg.com/80/v2-7658f1c05af7c4dfd277d85889026275_1440w.jpg?source=1940ef5c)

如上图所示，已经显示Initial commit初始化提交了，同时已经没有Untracked files提示了，这说明文件hit.txt已经被添加到 Git 仓库了，而在我们没有进行git add操作之前，文件hit.txt并不被 Git 仓库认可，因此才会出现提示初始化仓库为空的现象。在这里，需要声明一点，那就是：git add命令并没有把文件提交到 Git 仓库，而是把文件添加到了「临时缓冲区」，这个命令有效防止了我们错误提交的可能性。

#### **第 4 个命令：git commit**

在命令行窗口的光标处，输入git commit -m "text commit"命令，将hit.txt文件提交到 Git 仓库：

![img](https://pic1.zhimg.com/50/v2-7bae7e33584a12b55dbaf6268769afe1_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-7bae7e33584a12b55dbaf6268769afe1_1440w.jpg?source=1940ef5c)



如上图所示，我们成功将文件hit.txt提交到了 Git 仓库，其中commit表示提交，-m表示提交信息，提交信息写在双引号""内。接下来，再输入git status命令查看仓库状态：

![img](https://pica.zhimg.com/50/v2-341e2394a657effef0c38f445bbe9bb6_720w.jpg?source=1940ef5c)![img](https://pica.zhimg.com/80/v2-341e2394a657effef0c38f445bbe9bb6_1440w.jpg?source=1940ef5c)

如上图所示，结果显示nothing to commit, working tree clean，这表示已经没有内容可以提交了，即全部内容已经提交完毕。

#### **第 5 个命令：git log**

在命令行窗口的光标处，输入git log"命令，打印 Git 仓库提交日志：

![img](https://pica.zhimg.com/50/v2-365628061daef5e1b857f4337990981e_720w.jpg?source=1940ef5c)![img](https://pica.zhimg.com/80/v2-365628061daef5e1b857f4337990981e_1440w.jpg?source=1940ef5c)

如上图所示，显示了我们的提交记录，提交记录的内容包括Author提交作者、Date提交日期和提交信息。

通过以上的操作，我们会发现一个现象，那就是：在每个git操作之后，我们基本都会输入git status命令，查看仓库状态。

这也从侧面说明了git status命令使用的频率之高，也建议大家在操作 Git 仓库的时候多使用git status命令，这能帮助我们实时了解仓库的状态，显然非常有用。

#### **第 6 个命令：git branch**

在命令行窗口的光标处，输入git branch命令，查看 Git 仓库的分支情况：

![img](https://pic3.zhimg.com/50/v2-229c8f677bea969708a39a4c853ba98f_720w.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-229c8f677bea969708a39a4c853ba98f_1440w.jpg?source=1940ef5c)

如上图所示，显示了仓库demo中的分支情况，现在仅有一个master分支，其中master分支前的*号表示“当前所在的分支”，例如* master就意味着我们所在的位置为demo仓库的主分支。输入命令git branch a，再输入命令git branch，结果如下图所示：

![img](https://pic1.zhimg.com/50/v2-ce8506d523068e526e5b9164846f18f5_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-ce8506d523068e526e5b9164846f18f5_1440w.jpg?source=1940ef5c)

如上图所示，我们创建了一个名为a的分支，并且当前的位置仍然为主分支。

#### **第 7 个命令：git checkout**

在命令行窗口的光标处，输入git checkout a命令，切换到a分支：

![img](https://pic1.zhimg.com/50/v2-ce8506d523068e526e5b9164846f18f5_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-ce8506d523068e526e5b9164846f18f5_1440w.jpg?source=1940ef5c)

如上图所示，我们已经切换到a分支啦！也可以通过命令git branch查看分支情况：

![img](https://pic2.zhimg.com/50/v2-3b28d0015bd823222db84211c034741e_720w.jpg?source=1940ef5c)![img](https://pic2.zhimg.com/80/v2-3b28d0015bd823222db84211c034741e_1440w.jpg?source=1940ef5c)

在这里，我们还有一个更简单的方法来查看当前的分支，即通过观察上图中用红色框圈起来的部分。此外，我们也可以在创建分支的同时，直接切换到新分支，命令为git checkout -b，例如输入git checkout -b b命令：

![img](https://pic3.zhimg.com/50/v2-bd7b115a3f411746658bf44eb78b00f9_720w.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-bd7b115a3f411746658bf44eb78b00f9_1440w.jpg?source=1940ef5c)

如上图所示，我们在a分支下创建b分支（b为a的分支），并直接切换到b分支。

#### **第 8 个命令：git merge**

切换到master分支，然后输入git merge a命令，将a分支合并到master分支：

![img](https://pic2.zhimg.com/50/v2-807514785bdbb725053f4e30458bf5f5_720w.jpg?source=1940ef5c)![img](https://pic2.zhimg.com/80/v2-807514785bdbb725053f4e30458bf5f5_1440w.jpg?source=1940ef5c)

如上图所示，我们已经将a分支合并到主分支啦！此外，在这里需要注意一点，那就是：在合并分支的时候，要考虑到两个分支是否有冲突，如果有冲突，则不能直接合并，需要先解决冲突；反之，则可以直接合并。



#### **第 9 个命令：git branch -d & git branch -D** 

在命令行窗口的光标处，输入git branch -d a命令，删除a分支：

![img](https://pica.zhimg.com/50/v2-e22b97be855bf2c358db3c158d9cdc3f_720w.jpg?source=1940ef5c)![img](https://pica.zhimg.com/80/v2-e22b97be855bf2c358db3c158d9cdc3f_1440w.jpg?source=1940ef5c)

如上图所示，我们已经将分支a删除啦！不过有的时候，通过git branch -d命令可以出现删除不了现象，例如分支a的代码没有合并到主分支等，这时如果我们一定要删除该分支，那么我们可以通过命令git branch -D进行强制删除。

#### **第 10 个命令：git tag**

在命令行窗口的光标处，输入git tag v1.0命令，为当前分支添加标签：

![img](https://pic1.zhimg.com/50/v2-341de31e1046fe7dbd0f7d5d823a198c_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-341de31e1046fe7dbd0f7d5d823a198c_1440w.jpg?source=1940ef5c)

如上图所示，我们为当前所在的a分支添加了一个v1.0标签。通过命令git tag即可查看标签记录：

![img](https://pic3.zhimg.com/50/v2-7f4bbacebd1903677fb9e3235edbf36f_720w.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-7f4bbacebd1903677fb9e3235edbf36f_1440w.jpg?source=1940ef5c)

如上图所示，显示了我们添加标签的记录。通过命令git checkout v1.0即可切换到该标签下的代码状态：

![img](https://pic3.zhimg.com/50/v2-36840bbe7c7f25a4afd62580348a1550_720w.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-36840bbe7c7f25a4afd62580348a1550_1440w.jpg?source=1940ef5c)

如上图所示，我们已经成功切换到a分支的v1.0标签啦！

## 三、利用 SSH 完成 Git 与 GitHub 的绑定

现在，我们已经对 GitHub 有了一定的了解，包括创建仓库、拉分支，或者通过Clone or download克隆或者下载代码；我们也下载并安装了 Git，也了解了其常用的命令。

But，无论是 GitHub，还是 Git，我们都是单独或者说是独立操作的，并没有将两者绑定啊！也就是说，我们现在只能通过 GitHub 下载代码，并不能通过 Git 向 GitHub 提交代码。

因此，在本篇博文中，我们就一起完成 Git 和 GitHub 的绑定，体验通过 Git 向 GitHub 提交代码的能力。不过在这之前，我们需要先了解 SSh（安全外壳协议），因为在 GitHub 上，一般都是通过 SSH 来授权的，而且大多数 Git 服务器也会选择使用 SSH 公钥来进行授权，所以想要向 GitHub 提交代码，首先就得在 GitHub 上添加 SSH key配置。

#### **第 1 步：生成 SSH key**

我们要想生成SSH key，首先就得先安装 SSH，对于 Linux 和 Mac 系统，其默认是安装 SSH 的，而对于 Windows 系统，其默认是不安装 SSH 的，不过由于我们安装了 Git Bash，其也应该自带了 SSH. 可以通过在 Git Bash 中输入ssh命令，查看本机是否安装 SSH：

![img](https://pic1.zhimg.com/50/v2-23abbd2b8bfbc1ae2d2291d3aa6b274f_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-23abbd2b8bfbc1ae2d2291d3aa6b274f_1440w.jpg?source=1940ef5c)

如上图所示，此结果表示我们已经安装 SSH 啦！接下来，输入ssh-keygen -t rsa命令，表示我们指定 RSA 算法生成密钥，然后敲三次回车键，期间不需要输入密码，之后就就会生成两个文件，分别为id_rsa和id_rsa.pub，即密钥id_rsa和公钥id_rsa.pub. 对于这两个文件，其都为隐藏文件，默认生成在以下目录：

Linux 系统：~/.ssh

Mac 系统：~/.ssh

Windows 系统：C:\Documents and Settings\username\\.ssh

Windows 10 ThinkPad：C:\Users\think\.ssh

密钥和公钥生成之后，我们要做的事情就是把公钥id_rsa.pub的内容添加到 GitHub，这样我们本地的密钥id_rsa和 GitHub 上的公钥id_rsa.pub才可以进行匹配，授权成功后，就可以向 GitHub 提交代码啦！

#### **第 2 步：添加 SSH key**

![img](https://pic2.zhimg.com/50/v2-d8157e3f5ba22ce64a4bdab14f2c7739_720w.jpg?source=1940ef5c)![img](https://pic2.zhimg.com/80/v2-d8157e3f5ba22ce64a4bdab14f2c7739_1440w.jpg?source=1940ef5c)

如上图所示，进入我们的 GitHub 主页，先点击右上角所示的倒三角▽图标，然后再点击Settins，进行设置页面；点击我们的头像亦可直接进入设置页面：

![img](https://pic1.zhimg.com/50/v2-ea4f291447727e84434b87254a497c12_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-ea4f291447727e84434b87254a497c12_1440w.jpg?source=1940ef5c)

如上图所示，进入Settings页面后，再点击SSH and GPG Keys进入此子界面，然后点击New SSH key按钮：

![img](https://pica.zhimg.com/50/v2-4ef2ed875603194788cf0b99fa975220_720w.jpg?source=1940ef5c)![img](https://pica.zhimg.com/80/v2-4ef2ed875603194788cf0b99fa975220_1440w.jpg?source=1940ef5c)

如上图所示，我们只需要将公钥id_rsa.pub的内容粘贴到Key处的位置（Titles的内容不填写也没事），然后点击Add SSH key 即可。

#### **第 3 步：验证绑定是否成功**

在我们添加完SSH key之后，也没有明确的通知告诉我们绑定成功啊！不过我们可以通过在 Git Bash 中输入ssh -T git@github.com进行测试：

![img](https://pic3.zhimg.com/50/v2-aa1938b4970cd5ccddd82406f58aee83_720w.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-aa1938b4970cd5ccddd82406f58aee83_1440w.jpg?source=1940ef5c)

如上图所示，此结果即为Git 与 GitHub 绑定成功的标志。

## 四、通过 Git 将代码提交到 GitHub

到这一步我们已经完成了本地 Git 与远程 GitHub 的绑定，这意味着我们已经可以通过 Git 向 GitHub 提交代码啦！

但是在进行演示之前，我们需要先了解两个命令，也是我们在将来需要经常用到的两个命令，分别为 push 和 pull 。

#### push

push：该单词直译过来就是“推”的意思，如果我们本地的代码有了更新，为了保持本地与远程的代码同步，我们就需要把本地的代码推到远程的仓库，代码示例：

```text
git push origin master
```

#### pull

pull：该单词直译过来就是“拉”的意思，如果我们远程仓库的代码有了更新，同样为了保持本地与远程的代码同步，我们就需要把远程的代码拉到本地，代码示例：

```text
git pull origin master
```

此外，在之前我们讲到过pull request，在这里，估计大家就能更好的理解了，它表示：如果我们fork了别人的项目（或者说代码），并对其进行了修改，想要把我们的代码合并到原始项目（或者说原始代码）中，我们就需要提交一个pull request，让原作者把我们的代码拉到 ta 的项目中，至少对于 ta 来说，我们都是属于远程端的。

一般情况下，我们在push操作之前都会先进行pull操作，这样不容易造成冲突。

#### **提交代码**

对于向远处仓库（GitHub）提交代码，我们可以细分为两种情况：

第一种：本地没有 Git 仓库，这时我们就可以直接将远程仓库clone到本地。通过clone命令创建的本地仓库，其本身就是一个 Git 仓库了，不用我们再进行init初始化操作啦，而且自动关联远程仓库。我们只需要在这个仓库进行修改或者添加等操作，然后commit即可。

接下来，以博主的 GitHub 账号中的 CSBook 项目为例，进行演示。

首先，进入 GitHub 个人主页：

![img](https://pic2.zhimg.com/50/v2-9ad79b3a791bc683dc0a03d4623f7d11_720w.jpg?source=1940ef5c)![img](https://pic2.zhimg.com/80/v2-9ad79b3a791bc683dc0a03d4623f7d11_1440w.jpg?source=1940ef5c)

如上图所示，点击 mybatis-tutorial 项目：

![img](https://pic3.zhimg.com/50/v2-345a4e0b557f69ecc9d4e6b302773f46_720w.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-345a4e0b557f69ecc9d4e6b302773f46_1440w.jpg?source=1940ef5c)



如上图所示，进入mybatis-tutorial项目后，点击Clone or download，复制上图所示的地址链接。然后，进入我们准备存储 Git 仓库的目录，例如下面我们新建的GitRepo目录， 从此目录进入 Git Bash：

![img](https://pic4.zhimg.com/50/v2-bd26ef496de8c9b8dcc4f381f52b1b82_720w.jpg?source=1940ef5c)![img](https://pic4.zhimg.com/80/v2-bd26ef496de8c9b8dcc4f381f52b1b82_1440w.jpg?source=1940ef5c)



接下来，输入

```text
git clone https://github.com/guobinhit/mybatis-tutorial.git 
```

命令，其中clone后面所接的链接为我们刚刚复制的远程仓库的地址：

![img](https://pic1.zhimg.com/50/v2-98531ed02dddc6d49a63f25e44bae1a4_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-98531ed02dddc6d49a63f25e44bae1a4_1440w.jpg?source=1940ef5c)

如上图所示，我们已经把远程的mybatis-tutorial仓库clone到本地啦！下面，我们看看clone到本地的仓库内容与远程仓库的内容，是否完全一致：

![img](https://pic3.zhimg.com/50/v2-a5d885d3467bc4c4e54348e0697dd619_720w.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-a5d885d3467bc4c4e54348e0697dd619_1440w.jpg?source=1940ef5c)

如上图所示，显示我们已经把远程仓库mybatis-tutorial的内容都clone到本地啦！接下来，为了方便演示，我们直接把之前重构的「史上最简单的 MyBatis 教程」里面的mybatis-demo项目的代码复制过来：

![img](https://pic1.zhimg.com/50/v2-b8d40ee86db0a3db8a0f4d417b59037c_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-b8d40ee86db0a3db8a0f4d417b59037c_1440w.jpg?source=1940ef5c)

如上图所示，我们已经把mybatis-demo项目里面的主要内容src目录和web目录复制过来啦！接下来，从此目录进入 Git Bash，然后输入git status命令查看仓库状态：

![img](https://pic3.zhimg.com/50/v2-93386740f30fc5c749f800e5bb71ca4a_720w.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-93386740f30fc5c749f800e5bb71ca4a_1440w.jpg?source=1940ef5c)

如上图所示，mybatis-tutorial已经是一个 Git 仓库了，而且在输入git status命令后显示有两个文件未被追踪，也就是我们刚刚复制过来的两个文件没有提交。通过「Git 初体验及其常用命令介绍」，我们已经知道了在真正提交代码之前，需要先进行git add操作：

![img](https://pic2.zhimg.com/50/v2-cedb6cfa064b3370b0957e9eeab725cd_720w.jpg?source=1940ef5c)![img](https://pic2.zhimg.com/80/v2-cedb6cfa064b3370b0957e9eeab725cd_1440w.jpg?source=1940ef5c)

如上图所示，我们已经将src目录add并commit到mybatis-tutorial仓库啦！接下来，我们将web目录提交到仓库，然后输入git log命令查看仓库日志：

 ![img](https://pic3.zhimg.com/80/v2-d8508c5c15e39ec868ec4a6a88d07344_1440w.jpg?source=1940ef5c)

再输入git status命令查看仓库状态：

![img](https://pic3.zhimg.com/50/v2-94ae3d85f07be17ad35d24d05b40bb06_720w.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-94ae3d85f07be17ad35d24d05b40bb06_1440w.jpg?source=1940ef5c)

如上图所示，我们已经将mybatis-tutorial仓库里面新添加的两个目录都提交啦！下面，我们将本地仓库的内容push到远程仓库，输入git push origin master命令：

![img](https://pic2.zhimg.com/50/v2-52245f01d75b17216142ae090381e39b_720w.jpg?source=1940ef5c)![img](https://pic2.zhimg.com/80/v2-52245f01d75b17216142ae090381e39b_1440w.jpg?source=1940ef5c)

如上图所示，在第一次向远程仓库提交代码的时候，需要输入账号及密码进行验证，验证成功后，显示如下结果：

![img](https://pic1.zhimg.com/50/v2-fc46faa29abd6533b9b0c32f5bb1debe_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-fc46faa29abd6533b9b0c32f5bb1debe_1440w.jpg?source=1940ef5c)

然后，刷新 GitHub 中mybatis-tutorial仓库：

![img](https://pic1.zhimg.com/50/v2-35ede403564e8b5ddb370fa231f92e25_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-35ede403564e8b5ddb370fa231f92e25_1440w.jpg?source=1940ef5c)



如上图所示，我们已经将项目（仓库）中新添加的内容提交到了远程仓库。接下来，返回 GitHub 个人主页：

![img](https://pic3.zhimg.com/50/v2-50f370d747c2d22f5d518139aacbdb66_720w.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-50f370d747c2d22f5d518139aacbdb66_1440w.jpg?source=1940ef5c)

观察上图，我们会发现一个现象，那就是：mybatis-tutorial仓库的概要中新增了一个Java语言的标记。对于这个仓库语言的标记，其来源有两个，一是在我们创建仓库时就指定语言；二是在我们提交或者新建代码后由 GitHub 自动识别该语言。

以上介绍了向 GitHub 提交代码时的第一种情况，即：

第一种：本地没有 Git 仓库，这时我们可以直接将远程仓库clone到本地。通过clone命令创建的本地仓库，其本身就是一个 Git 仓库了，不用我们再进行init初始化操作啦，而且自动关联远程仓库。我们只需要在这个仓库进行修改或者添加等操作，然后commit即可。

接下来，我们继续介绍向 GitHub 提交代码时可能遇到的第二种情况，即：

第二种：本地有 Git 仓库，并且我们已经进行了多次commit操作。

仍然以博主的开源项目为例，不过这次换成springmvc-tutorial项目进行演示。首先，建立一个本地仓库，命名为springmvc-tutorial：

![img](https://pica.zhimg.com/50/v2-db781e9d147fbad141a3e25124e7572a_720w.jpg?source=1940ef5c)![img](https://pica.zhimg.com/80/v2-db781e9d147fbad141a3e25124e7572a_1440w.jpg?source=1940ef5c)

如上图所示，进入该仓库，进入init初始化操作：

![img](https://pic1.zhimg.com/50/v2-93a1b4932f996da643621d66407c6514_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-93a1b4932f996da643621d66407c6514_1440w.jpg?source=1940ef5c)

然后，输入

```text
git remote add origin https://github.com/guobinhit/springmvc-tutorial.git
```

命令，关联远程仓库（在此，默认大家都知道如何获取远程仓库的地址），其中origin为远程仓库的名字：

![img](https://pic1.zhimg.com/50/v2-ea435870e321c2befd427ea6bc9b1a9b_720w.jpg?source=1940ef5c)![img](https://pic1.zhimg.com/80/v2-ea435870e321c2befd427ea6bc9b1a9b_1440w.jpg?source=1940ef5c)

输入git pull origin master命令，同步远程仓库和本地仓库：

![img](https://pica.zhimg.com/50/v2-5a0caecda20f89df85f250580686fb57_720w.jpg?source=1940ef5c)![img](https://pica.zhimg.com/80/v2-5a0caecda20f89df85f250580686fb57_1440w.jpg?source=1940ef5c)

再回到本地springmvc-tutorial仓库，看看我们是否已经把远程仓库的内容同步到了本地：

![img](https://pic2.zhimg.com/50/v2-bc4c9c8c62be0d85355f39e4727391ec_720w.jpg?source=1940ef5c)![img](https://pic2.zhimg.com/80/v2-bc4c9c8c62be0d85355f39e4727391ec_1440w.jpg?source=1940ef5c)

如上图所示，显然我们已经把远程springmvc-tutorial仓库里面仅有的README.md文件同步到了本地仓库。接下来，在本地仓库新建一个名为test.txt的测试文件：

![img](https://pica.zhimg.com/50/v2-b4ae6a7adbd1eae904003b4f7c0d5b36_720w.jpg?source=1940ef5c)![img](https://pica.zhimg.com/80/v2-b4ae6a7adbd1eae904003b4f7c0d5b36_1440w.jpg?source=1940ef5c)

输入git add和git commit命令，将文件test.txt添加并提交到springmvc-tutorial仓库：

![img](https://pic2.zhimg.com/50/v2-793f271d0f4869c94eebe758a3f5eef2_720w.jpg?source=1940ef5c)![img](https://pic2.zhimg.com/80/v2-793f271d0f4869c94eebe758a3f5eef2_1440w.jpg?source=1940ef5c)

再输入git push origin master命令，将本地仓库修改（或者添加）的内容提交到远程仓库：

![img](https://pica.zhimg.com/50/v2-6acb455e9035ac8d73ea8e9f9d1783bf_720w.jpg?source=1940ef5c)![img](https://pica.zhimg.com/80/v2-6acb455e9035ac8d73ea8e9f9d1783bf_1440w.jpg?source=1940ef5c)

如上图所示，我们已经将本地仓库的内容同步到了远程仓库。下面，我们进入远程springmvc-tutorial仓库的页面，看看我们的提交结果：

![img](https://pic3.zhimg.com/50/v2-4c192aa5e2a5f118f0c5191f46d43c0c_720w.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-4c192aa5e2a5f118f0c5191f46d43c0c_1440w.jpg?source=1940ef5c)

如上图所示，我们已经将「通过 Git 将代码提交到 GitHub」的第二种情况演示完毕。

此外，在这个例子中，我们将远程仓库命名为origin，本地仓库名为springmvc-tutorial，其实两者的名字咱们可以随意取，一般来说，我们习惯性将远程仓库命名为origin，不过在需要关联多个远程仓库的时候，就需要我们再取别的名字啦！

最后，再强调一遍：在我们向远程仓库提交代码的时候，一定要先进行pull操作，再进行push操作，防止本地仓库与远程仓库不同步导致冲突的问题，尤其是第二种提交代码的情况，很容易就出现问题。

