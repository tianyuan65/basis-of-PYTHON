## PYTHON
## 一、PYTHON环境的安装
* 1.1 下载PYTHON
    * 去官网找，下载符合电脑的。官网：https://www.python.org/
* 1.2 安装
    * ![click to install](imgs/点击安装即可.PNG)
    * 安装时，不选择自动安装，选择自定义安装，将pip等全部勾选后，点击next，并勾选**Add Python 3.x to Path**，也就是选中添加环境变量后，再继续安装。
* 1.3 测试是否安装成功
    * 在命令提示符，输入python，可查看版本，并查看是否安装成功。
* 1.4 手动配置Python
    * 若未按照上一个步骤进行，可手动配置。桌面上右键点击此电脑，点击属性，继续点击高级系统设置，点击环境变量，选中USER的用户变量中的Path后，点击编辑，再点击新建，填写好路径即可添加到下载python的盘中。记得点击三个确定。
## 二、pip的使用
* pip是一个现代的、通用的Python包管理工具。提供了对Python包的查找、下载、安装、卸载的功能，便于我们对Python的资源包进行管理。相当于学习前端时的npm和yarn。
* 2.1 安装
    * 安装Python是，会自动下载并安装pip。
* 2.2 配置
    * 在Windows命令行里，输入```pip -V```，即可查看pip版本。
        * ![查看pip版本](imgs/my%20pip%20version.PNG)
    * 但若在命令行里，运行```pip -V```，出现如下提示：
        * ![未安装pip](imgs/没勾选Add%20Python%20balabala.PNG)
    * 可能是因为在安装Python的过程中未勾选**Add Python 3.x to Path**选项的缘故，需要手动昂配置pip环境变量，具体步骤看一，只不过要正确输入路径，下面是我的路径。
        * ![我的pip和Python本身的路径](imgs/我的pip和Python本身的路径.PNG)
* 2.3 使用pip管理Python包
    * pip install <包名>：安装指定的包，包大还是包小，等一会儿出现Successfully installed巴拉巴拉，即意味着安装成功。前提是没有输错字母。
        * ![安装一个简单的包](imgs/打开pip所在路径，并在其中安装ipython.PNG)
    * pip uninstall <包名>：卸载/删除指定的包
    * pip list ：显示已经安装的包，可查看已安装成功的包。
        * ![展示已安装成功的所有包](imgs/查看安装成功的包.PNG)
    * pip freeze：显示已经安装的包，并以指定的格式显示，会把依赖的第三方也给展示出来。
* 2.4 修改pip下载源
    *   运行pip install命令会从网站上下载指定的python包，默认是从https://files.pythonhosted.org/ 网站上下载。这是国外的网站，遇到网络不稳定的情况时，可能会下载失败，因此可以通过命令，修改pip现在软件时的源。
    * 格式： ```pip install 包名 -i 国内源地址```(这个-绝对不能省略)
    * 示例：
        * ```pip install ipython -i https://pypi.mirrors.ustc.edu.cn/simple/```，就是从中国科技大学(ustc)的服务器上下载requests(给予python的第三番文本框架)
    * 国内常用的pip下载源列表：
        * 阿里云：https://mirrors.aliyun.com/pypi/simple/
        * 中国科技大学：https://pypi.mirrors.ustc.edu.cn/simple/
        * 豆瓣：https://pypi.douban.com/simple/  (老师推荐使用)
        * 清华大学：https://pypi.tuna.tsinghua.edu.cn/simple/
        * 中国科学技术大学：https://pypi.mirrors.ustc.edu.cn/simple/
## 三、运行Python程序
* 3.1 终端运行
    * 1. 直接在python解析器中书写代码，缺点是无法保存到本地或硬盘中。
        * ![win+r,cmd输入python，在其解析器上直接书写代码，单双引号皆可](imgs/直接在python解析器上书写代码.PNG)
        * 如何退出python环境，就是上面那个环境
            * 1. exit()
            * 2. Ctrl+z
    * 2. 使用ipython解析器编写代码
        * 使用pip命令，可以快速安装ipython，不要写在python根目录下，直接在当前目录编写即可。但这两种方法有个共同的缺点，就是无法保存文件到本地或硬盘当中，不利于二次开发。
            * ```pip install ipython -i https://pypi.douban.com/simple```
            * 成功安装ipython后，在当前目录下输入ipython进入ipython的环境中，即可编写代码。
            * ![下载ipython源，并使用其解析器编写代码](imgs/使用ipython解析器编写代码.PNG)
* 3.2 运行python文件
    * 使用python指令，运行后缀为.py的python文件
        * ![cmd+r，命令提示符下输入文件路径来运行python文件](imgs/命令提示符下输入文件路径即可运行py文件.PNG)
* 3.3 Pycharm(最常用)
    * 上述两种方法能够使用并提高编码速度，但面对更复杂的要求就显得无比麻烦。一般情况下，需要借助工具来辅助我们快速地搭建环境，编写代码以及运行程序。
    * IDE的概念
        * IDE(Integrated Development Environment)又称为集成开发环境。解释一下就是，有一款图形化界面的软件，它集成了编辑代码，编译代码，分析代码，执行代码以及调试代码等功能。在Python开发中，最常用的IDE是Pycharm。除了Pycharm还有我在学前端是常用的VSCode、WenStorm等，但Pycharm是最常用的。
    * pycharm是由捷克公司JetBrains开发的一款IDE，提供代码分析、图形化调试器、集成测试器、集成版本控制系统等，主要用于编写Python代码。下载社区版，因为这个免费。
        * 下载地址：https://www.jetbrains.com/pycharm/download/?section=windows
        * Pycharm的安装
            * 双击安装文件
            * 自定义安装路径，但我没自定义
            * 编辑设置(全部选中)
            * 安装完成后双击
            * 可设置主题，左下角设置->设置->外观中可选择喜欢的主题
* 3.4 Pycharm的使用介绍
    * 运行Pycharm，选择新建项目，创建一个新的Python工程。到此我是用VSCode书写的代码和笔记，鉴于已经有了一个有关Python的文件夹，在Pycharm就直接打开已有文件夹了。
    * 从这儿开始是在Pycharm写的笔记。创建或打开一个项目或文件夹后，选择'Pure Python'创建一个新的纯Python工程项目，Location表示该项目的保存路径，Interpreter用来指定Python解释器的版本。
      * ![创建一个新的项目，方便学习Python](imgs/%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E6%96%B0%E7%9A%84%E9%A1%B9%E7%9B%AE%EF%BC%8C%E6%96%B9%E4%BE%BF%E5%AD%A6%E4%B9%A0Python.PNG)
    * 右键项目，选择新建，再选择Python文件，即可创建一个python文件，命名为testPython，写好代码后，右键选择运行XXX文件即可，或者左下侧有个三角形，点那个也是运行，但要明确运行的文件。
      * ![创建一个新的项目，方便学习Python.PNG](imgs/%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E6%96%B0%E7%9A%84%E9%A1%B9%E7%9B%AE%EF%BC%8C%E6%96%B9%E4%BE%BF%E5%AD%A6%E4%B9%A0Python.PNG)
      * ![如何运行Python文件.png](imgs/%E5%A6%82%E4%BD%95%E8%BF%90%E8%A1%8CPython%E6%96%87%E4%BB%B6.png)
      * ![输出testPython的第一条运行结果.PNG](imgs/%E8%BE%93%E5%87%BAtestPython%E7%9A%84%E7%AC%AC%E4%B8%80%E6%9D%A1%E8%BF%90%E8%A1%8C%E7%BB%93%E6%9E%9C.PNG)
    * 页面布局介绍
      * 文件导航区域，就是查找、定位、打开项目文件的区域。
      * 文件编辑区域，能够编写当前选中的文件里的代码。
      * 控制台区域，用于输出程序执行内容，跟踪代码调试的执行。

## 四、Python

