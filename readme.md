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
      * ![创建一个新的项目，方便学习Python](imgs/%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E6%96%B0%E7%9A%84%E9%A1%B9%E7%9B%AE%EF%BC%8C%E6%96%B9%E4%BE%BF%E5%AD%A6%E4%B9%A0Python.PNG)
      * ![如何运行Python文件](imgs/%E5%A6%82%E4%BD%95%E8%BF%90%E8%A1%8CPython%E6%96%87%E4%BB%B6.png)
      * ![输出testPython的第一条运行结果](imgs/%E8%BE%93%E5%87%BAtestPython%E7%9A%84%E7%AC%AC%E4%B8%80%E6%9D%A1%E8%BF%90%E8%A1%8C%E7%BB%93%E6%9E%9C.PNG)
    * 页面布局介绍
      * 文件导航区域，就是查找、定位、打开项目文件的区域。
      * 文件编辑区域，能够编写当前选中的文件里的代码。
      * 控制台区域，用于输出程序执行内容，跟踪代码调试的执行。
    * 基本使用和配置
      * Pycharm左下侧有个如图示的图标，这是终端，点击后，输入python进入python环境，与命令提示符的终端效果一样。
        * ![Pycharm里的终端，与cmd+r整出来的结果一样](imgs/Pycharm%E9%87%8C%E7%9A%84%E7%BB%88%E7%AB%AF%EF%BC%8C%E4%B8%8Ecmd%2Br%E6%95%B4%E5%87%BA%E6%9D%A5%E7%9A%84%E7%BB%93%E6%9E%9C%E4%B8%80%E6%A0%B7.PNG)
      * 点击左上侧文件的设置，在文件和代码模板中可设置编码格式，如项目创建时间，作者名，文件名以及项目名称，之后可以根据公司的要求，设置更多编码格式
        * ![设置编码格式](imgs/%E8%AE%BE%E7%BD%AE%E7%BC%96%E7%A0%81%E6%A0%BC%E5%BC%8F.PNG)
        * ![设置编码格式后创建的文件的顶部可看到之前设置的格式](imgs/%E8%AE%BE%E7%BD%AE%E7%BC%96%E7%A0%81%E6%A0%BC%E5%BC%8F%E5%90%8E%E5%88%9B%E5%BB%BA%E7%9A%84%E6%96%87%E4%BB%B6%E7%9A%84%E9%A1%B6%E9%83%A8%E5%8F%AF%E7%9C%8B%E5%88%B0%E4%B9%8B%E5%89%8D%E8%AE%BE%E7%BD%AE%E7%9A%84%E6%A0%BC%E5%BC%8F.PNG)
## 四、Python
* 4.1 注释
  * 1. 注释介绍
    * 在工作编码的过程中，如果一段代码的逻辑比较复杂，不是特别容易理解，可以适当地添加注释，以辅助自己活其他编码人员解读代码。
    * 注：注释是给程序员看的，是为了让程序员方便阅读代码，解释器会忽略注释。使用自己熟悉的语言，适当地对代码进行注释，说明该程序员有良好的编码习惯。
  * 2. 注释的分类
    * 在Python中支持单行注释和多行注释。
    * **单行注释**
      * 一般情况下注释写在代码的上面，只对当前行有效，shift+3或Ctrl+/(这是快捷键方法)都可，有时也会写在代码后面，但比较少，绝对不能写在前面。
      * ![单行注释](imgs/%E5%8D%95%E8%A1%8C%E6%B3%A8%E9%87%8A.PNG)
    * **多行注释**
      * 用三个单引号(''')开始，三个单引号(''')结束。
      * ![多行注释](imgs/%E5%A4%9A%E8%A1%8C%E6%B3%A8%E9%87%8A.PNG)
* 4.2 变量以及数据类型
  * 1. 变量的定义
    * 对于重复使用，并且需要经常修改的数据，可以定义为变量，来提高编程效率。
    * 定义变量的语法为：变量名=变量值(这里的=的意思是赋值，这点跟js里一样)
    * 定义变量后可以使用变量名来访问变量值。
      * ```
          print("Who says, you're not perfect")
          print("Who says, you're not worth it")
          print("Who says, you're the only one that's hurting")
          print("Trust me that's the price of beauty")
          print("Who says, you're not pretty")
          print("Who says, you're not beautiful")
        
          # 使用变量
          whosays="Who says,you're not perfect"
          print(whosays)
        ```
      * ![使用变量结果](imgs/%E4%BD%BF%E7%94%A8%E5%8F%98%E9%87%8F%E7%BB%93%E6%9E%9C.PNG)
      * ![应用场景：给变量img赋值图片地址，输出就是该地址，具体是啥粘贴到网页查看即可](imgs/%E7%BB%99%E5%8F%98%E9%87%8Fimg%E8%B5%8B%E5%80%BC%E5%9B%BE%E7%89%87%E5%9C%B0%E5%9D%80%EF%BC%8C%E8%BE%93%E5%87%BA%E5%B0%B1%E6%98%AF%E8%AF%A5%E5%9C%B0%E5%9D%80%EF%BC%8C%E5%85%B7%E4%BD%93%E6%98%AF%E5%95%A5%E7%B2%98%E8%B4%B4%E5%88%B0%E7%BD%91%E9%A1%B5%E6%9F%A5%E7%9C%8B%E5%8D%B3%E5%8F%AF.PNG)
    * 说明：
      * 变量即可以变化的量，可以随时进行修改。
      * 程序就是用来处理的，而变量就是用来存储数据的。
  * 2. 变量的类型
    * 程序中：在Python里为了应对不同的业务需求，也把数据分为不同的类型，基本数据类型和高级数据类型
      * 基本数据类型：
        * Numbers(数字)，**最需要掌握的就是int和float**
          * int(有符号整型)，就是整数。
          * long(长整型，也可以代表八进制和十六进制)，Python3.x中，已不使用，它是Python2的
          * float(浮点型)，就是小数。
          * complex(复数)，在爬虫中不用，但有实数和虚数的就是复数，eg:c=a+bj
        * 布尔类型：True&False
        * String(字符串)，就是让单或双引号圈起来的内容。
      * 高级数据类型：
        * List(列表)，用列表描述很多个数据。
          * 应用场景：当获取到了很多数据的时候，可以将它们存储到列表中，并直接使用到列表访问。
        * Tuple(元组)，与List类似，用一个数据代表很多个数据的集合。
        * Dictionary(字典)，
  * 3. 查看数据类型
    * 在python中，只要定义一个变量，并且它有数据，那么它的类型就已经确定了，不需要开发者主动地说明他的类型，系统会自动识别，意思就是**变量没有类型，数据才有类型**。
    * 如果临时想要查看一个变量存储的数据类型，可以使用type方法来查看变量存储的数据类型。格式：type(变量名)
      * ![type(变量名)来查看变量存储的数据类型](imgs/type%28%E5%8F%98%E9%87%8F%E5%90%8D%29%E6%9D%A5%E6%9F%A5%E7%9C%8B%E5%8F%98%E9%87%8F%E5%AD%98%E5%82%A8%E7%9A%84%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B.PNG)
* 4.3 标识符和关键字
  * 计算机编程语言中，标识符，也叫变量名，它是用户编程时使用的名字，用于给变量、常量、函数、语句块等命名，已建立起名称与使用之间的关系，但须注意以下三点。
    * 标识符/变量名由字母、下划线和数字组成，且绝对不能以数字开头。
      * ![数字不能是变量名的开头](imgs/%E6%95%B0%E5%AD%97%E4%B8%8D%E8%83%BD%E6%98%AF%E5%8F%98%E9%87%8F%E5%90%8D%E7%9A%84%E5%BC%80%E5%A4%B4.PNG)
    * 严格区分大小写。
      * ![严格区分大小写](imgs/%E4%B8%A5%E6%A0%BC%E5%8C%BA%E5%88%86%E5%A4%A7%E5%B0%8F%E5%86%99.PNG)
    * 不能使用关键字。是Python中已经写好的，有特殊功能的，比如，for，False，True，while等。
      * ![不能使用既定的关键字来定义变量名](imgs/%E4%B8%8D%E8%83%BD%E4%BD%BF%E7%94%A8%E6%97%A2%E5%AE%9A%E7%9A%84%E5%85%B3%E9%94%AE%E5%AD%97%E6%9D%A5%E5%AE%9A%E4%B9%89%E5%8F%98%E9%87%8F%E5%90%8D.PNG)
      * ![一些关键字](imgs/%E4%B8%80%E4%BA%9B%E5%85%B3%E9%94%AE%E5%AD%97.PNG)
    * 1. 命名规范
      * 标识符命名，要做到顾名思义。尽量取一个有意义的名字，做到让人一眼就能看出其用途和功能，也是为了提高代码可读性和效率的方式。比如，想定义一个人名，就用name；想定义一种动物，就用那个动物的英文单词cat，puppy，fish等。
      * 遵守一些命名规范。
        * 驼峰命名法，又分为大驼峰命名法和小驼峰命名法。
          * (1). 大驼峰命名法(lower camel case)：每一个单词的首字母都采用大写字母，例如：FirstName、LastName，UpperCamelCase等。
          * (2). 小驼峰命名法(upper camel case)：第一个单词以小写字母开始，第二个单词首字母大写，例如：userName、submitForm，lowerCamelCase等。
        * 还有一种就是用下划线来连接两个单词，如，current_state，user_name等。Python的命令瑰色遵循PEP8标准。
    * 2. 关键字
      * 关键字的概念。是指一些具有特殊功能的标识符，是已经被python官方使用了的，所以不允许开发者自己定义和关键字相同名字的标识符。
      * ![一些关键字](imgs/%E4%B8%80%E4%BA%9B%E5%85%B3%E9%94%AE%E5%AD%97.PNG)
* 4.4 类型转换
  * ![类型转换的一些方法](imgs/%E7%B1%BB%E5%9E%8B%E8%BD%AC%E6%8D%A2%E7%9A%84%E4%B8%80%E4%BA%9B%E6%96%B9%E6%B3%95.PNG)
  * 转换为整型
    * string --> int
    * float --> int
    * boolean  --> int
      * True会被转换为数字1，False会被转换为数字0.
    * string --> int
      * 在这里需要注意一点，转换字符串为整型时，字符串中不可有非法字符，如小数点。在两种情况下，会导致转换失败，一个是像图片里一样的小数字符串 ；另一个是含有字母的字符串，因为都包含非法字符，不能转换为整型。
        * ![报错原因是字符串中有一些非法字符，在这里就是小数点](imgs/%E6%8A%A5%E9%94%99%E5%8E%9F%E5%9B%A0%E6%98%AF%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E6%9C%89%E4%B8%80%E4%BA%9B%E9%9D%9E%E6%B3%95%E5%AD%97%E7%AC%A6%EF%BC%8C%E5%9C%A8%E8%BF%99%E9%87%8C%E5%B0%B1%E6%98%AF%E5%B0%8F%E6%95%B0%E7%82%B9.PNG)
        * ![字符串无法转为整型的第二个原因，不能有字母](imgs/%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%97%A0%E6%B3%95%E8%BD%AC%E4%B8%BA%E6%95%B4%E5%9E%8B%E7%9A%84%E7%AC%AC%E4%BA%8C%E4%B8%AA%E5%8E%9F%E5%9B%A0%EF%BC%8C%E4%B8%8D%E8%83%BD%E6%9C%89%E5%AD%97%E6%AF%8D.PNG)
  * 转换为浮点数
    * string --> float，在爬虫时，获取的大部分都是String类型，但实际上需要的是对应的float类型，因此需要进行类型转换。
    * int --> float
  * 转换为字符串，将当前的数据和其他的数据进行拼接时，会用到。举个例子的话，在一个网页最底部，翻到下一页时，其对应的网址会跟着发生改变，代表翻到了第几页，就是页码和域名的拼接，此时就可能需要将int转换为string来进行拼接。只是强制转换为字符串的方法与前几个有所不同，想要转换为string类型使用str()即可，string()这方法不合法。且打印出转换后的结果没有用引号包裹，这是因为Pycharm在显示时进行了优化，用type方法，可以查看到确实成功转换了。
    * int --> string
    * float --> string
    * boolean --> string
  * 转换为布尔值
    * int --> boolean，如果对非零的整型进行bool类型的转换，那么全是True，甚至负数也是True；在整数的范围内，0强制类型转换为bool类型的结果是False。
    * float --> boolean，与int一样，只要是非零，无论正负，强制转换为bool类型的结果都是True；如果是0.0，转换结果就是False。
    * string --> boolean，只要字符串中有内容，在强制类型转换为bool类型是，就会返回True，就算是空格转换结果也是True，也就是非空即是True。值得注意的是，无论是单双引号不影响前面那句话。
    * list --> boolean，只要列表中有数据，强制类型转换为bool类型时，返回的结果就是True；若列表中没有任何数据，强制类型转换结果为False。
    * tuple -- boolean，只要元组中有数据，在强制类型转换为bool类型时，就会返回True；但若元组中没有数据，就会返回False。
    * dictionary --> boolean，只要字典中有数据，在强制类型转换为bool类型时，返回结果就是True；否则，返回False。
* 4.5 运算符
  * 1. 算术运算符 
    * ```
        a=5
        b=2
        
        # + 加
        print(a+b)  #7
        
        # - 减
        print(a-b)  #3
        
        # * 乘
        print(a*b)  #10
        
        # / 除
        print(a/b)  #2.5
        
        # // 取整除，就是取整数部分，它的结果有且只有一种就是int类型
        print(a // b)   #2
        
        # % 取余，就是整除后剩下来的那个
        print(a%b)  #1
        
        # ** 指数，就是a的b次幂
        print(a**b) #25
        
        # () 小括号，提高运算优先级
        print(a*(a+b))  #35
      ```
    * 注意：混合运算时，优先级顺序为**(指数运算)高于*(乘)、/(除)、%(取余)、//(取整除)高于+、-，为了避免歧义，建议使用()来处理运算符优先级。
    * 并且不同类型的数字进行混合运算时，整数将会转换为浮点数进行运算。
    * 扩展：
      * 可以用 +(加法) 进行两个字符串的拼接，但只限于相同数据类型之间，字符串和整型显然是不能使用加法来实现拼接的，若硬要实现，需要将int类型转换为string类型。
        * 乘法运用在字符串中就会把字符串的内容重复N次。
          * ```
              a='初听只当戏，再听已懂曲中意。'
              print(a*3)  #初听只当戏，再听已懂曲中意。初听只当戏，再听已懂曲中意。初听只当戏，再听已懂曲中意。
            ``` 
  * 2. 赋值运算符，就是把等号右边的结果赋值给左边的变量。示例如下：
    * ```
        # 为单个变量赋值
        a=8
        print(a)
      
        # 同时为多个变量赋值，按下面的例子，将数据23先赋值给变量c，再将以获取数据的变量c赋值给变量b。
        b=c=23
        print(b)    #23
        print(c)    #23
      
        # 多个变量赋值，用逗号进行分隔，同时给多个变量赋值不同的数据。
        d,e,f=67,'身着长衫轻摇纸扇',False
        print(d)    #67
        print(e)    #身着长衫轻摇纸扇
        print(f)    #False
      ```
  * 3. 复合赋值运算符，用在元组和列表结合操作上。
    * +=，加法赋值运算符
      * ```
         a=1
         # += 加法赋值运算符
         # a=a+2
         a += 2   #等于a=a+2
         print(a)    #3
        ```
    * -=，减法赋值运算符
      * ```
         b=2
         # -= 减法赋值运算符
         # b=b-3
         b -= 3
         print(b)    #-1
        ```
    * *=，乘法赋值运算符
      * ```
         c=2
         # *= 乘法赋值运算符
         # c=c*0
         c *= 0
         print(c)    #0
        ```
    * /=，除法赋值运算符
      * ```
         # /= 除法赋值运算符
         d=5
         d=d/4
         # d /= 4
         print(d)    #1.25
        ```
    * //=，取整除赋值运算符
      * ```
         # //= 取整除赋值运算符
         e=7
         # e=e//3
         e //= 3
         print(e)    #2
        ```
    * %=，取模赋值运算符
      * ```
         # %= 取模赋值运算符
         f=8
         # f=f%5
         f %= 5
         print(f)    #3
        ```
    * **=，幂赋值运算符
      * ```
         # **= 幂赋值运算符
         g=2
         # f=f**3
         g **=3
         print(g)    #8
        ```
  * 4. 比较运算符返回的都是布尔类型的数据
    * ==，是判断==两边的变量是否一致
    * !=，是判断!=两边的变量是否不一致
      * 扩展：<> Python2使用的是这个，Python3中已不再使用它来表示不等式，若坚持使用会报Python3.13不再支持该种写法的错。
    * >，判断>左边的变量是否大于右边的变量
    * >=，判断>=左边的变量是否大于或等于右边的变量
    * <，判断<左边的变量是否小于右边的变量
    * <=，判断<=左边的变量是否小于或等于右边的变量
  * 5. 逻辑运算符
    * and，与，and两端的结果必须都是True，才会返回True，只要有一端不满足该条件，返回的结果就是False。
    * or，或，or的两端中，有一端满足结果为True的情况下，最终会返回True，但必须有一端返回的就是True，否则返回的依旧是False。
    * not，非，取反
    * 性能提升：
      * and   短路与，and两端的条件都必须满足才可执行，有一端不满足则不会执行。
        * ![and的有一端不满足条件则不打印](imgs/and%E7%9A%84%E6%9C%89%E4%B8%80%E7%AB%AF%E4%B8%8D%E6%BB%A1%E8%B6%B3%E6%9D%A1%E4%BB%B6%E5%88%99%E4%B8%8D%E6%89%93%E5%8D%B0.png)
      * or    短路或，or前面那一端的结果是False才会考虑后面那一端的执行，若or前面结果是True，后面的将不会执行，所以想要使用or，还想执行语句或其他代码，那就写在or的前面
        * ![or只要有一端满足True即可，但若or前面的是True后面的就不执行了](imgs/or%E5%8F%AA%E8%A6%81%E6%9C%89%E4%B8%80%E7%AB%AF%E6%BB%A1%E8%B6%B3True%E5%8D%B3%E5%8F%AF%EF%BC%8C%E4%BD%86%E8%8B%A5or%E5%89%8D%E9%9D%A2%E7%9A%84%E6%98%AFTrue%E5%90%8E%E9%9D%A2%E7%9A%84%E5%B0%B1%E4%B8%8D%E6%89%A7%E8%A1%8C%E4%BA%86.png)
* 4.6 输入输出
  * 1. 输出
    * 普通输出，就是print()，若有int和string类型的话，需要将int类型转换为string类型，会比较麻烦
    * 格式化输出，会在scrapy框架中用到，爬虫后会生成json文件，可以放到excel文件或mysql又或者放到redis数据库中。在Python中最常用的就是%s和%d，%d代表数值，%s代表字符串的缩写。具体例子如下：
      * ```
        age=29
        name='谷江山'
        print('大家好，我是729声工场的配音演员%s，今年%d岁' % (name,age))
        ```
  * 2. 输入
    * 不同于前端，Python中input是一个函数，在前端它是一个可以输入内容的输入框标签，就是这个<input/>。调用input函数，运行py文件可以在控制台输入内容，点击回车键，输入的内容可以打印出来。
      * ![调用input函数并赋值给一个变量，运行py文件后可以在控制台输入相关内容](imgs/%E8%B0%83%E7%94%A8input%E5%87%BD%E6%95%B0%E5%B9%B6%E8%B5%8B%E5%80%BC%E7%BB%99%E4%B8%80%E4%B8%AA%E5%8F%98%E9%87%8F%EF%BC%8C%E8%BF%90%E8%A1%8Cpy%E6%96%87%E4%BB%B6%E5%90%8E%E5%8F%AF%E4%BB%A5%E5%9C%A8%E6%8E%A7%E5%88%B6%E5%8F%B0%E8%BE%93%E5%85%A5%E7%9B%B8%E5%85%B3%E5%86%85%E5%AE%B9.png)
* 4.7 流程控制语句
  * 1. if判断语句
    * if语句是用来进行判断的，其格式为：
      * if 要判断的条件：
            满足条件时，要做的事
      * ![满足条件才会执行if下面的代码](imgs/%E6%BB%A1%E8%B6%B3%E6%9D%A1%E4%BB%B6%E6%89%8D%E4%BC%9A%E6%89%A7%E8%A1%8Cif%E4%B8%8B%E9%9D%A2%E7%9A%84%E4%BB%A3%E7%A0%81.png)
      * ![条件未满足，则不会执行](imgs/%E6%9D%A1%E4%BB%B6%E6%9C%AA%E6%BB%A1%E8%B6%B3%EF%BC%8C%E5%88%99%E4%B8%8D%E4%BC%9A%E6%89%A7%E8%A1%8C.png)
    * 需要注意的一个点是，调用input方法，返回的是一个字符串类型，若在控制台输入的是一个int，就会报错，此时就需要将input返回的强制转换为int类型，再进行比较。
  * 2. if else
    * 当满足判断条件时，执行if下代码，当不满足判断条件时，执行else下代码。
  * 3. elif
    * elif的功能，用if-else写法会导致穿透现象，在下面的案例中，如果输入了76，会把中等、及格都打印出来，因此这是个错误写法，不要这么写。用elif还有一个好处就是一旦某一条件成立，则后面的elif及else都不会再去判断了，减少了判断次数。
      * elif的使用格式如下：
        * ```
            # elif相当于前端的switch判断，使用elif可以避免穿透现象
            score=int(input('please enter your score.'))
            if score>=90:
                print('优秀')
            # 否则如果，成绩大于80，就打印良好；
            elif score>=80:
                print('良好')
            # 否则如果，成绩大于70，就打印中等；
            elif score>=70:
                print('中等')
            # 否则如果，成绩大于60，就打印及格；
            elif score>=60:
                print('及格')
            # 否则打印不及格
            else:
                print('不及格')
          ```
        * 说明：
          * 当条件一满足时，执行事件一，随后整个循环结束；
          * 当条件一不满足时，判断条件二，若第二行条件满足，则执行事件二，随后整个循环结束；
          * 当条件一不满足，且条件二页不满足时，判断条件三，若满足，则执行事件三，随后整个循环结束，
          * 以此类推，到最后一个条件。
        * ![用ifelse语句来判断会导致穿透现象，因此这是个错误示范](imgs/%E7%94%A8ifelse%E8%AF%AD%E5%8F%A5%E6%9D%A5%E5%88%A4%E6%96%AD%E4%BC%9A%E5%AF%BC%E8%87%B4%E7%A9%BF%E9%80%8F%E7%8E%B0%E8%B1%A1%EF%BC%8C%E5%9B%A0%E6%AD%A4%E8%BF%99%E6%98%AF%E4%B8%AA%E9%94%99%E8%AF%AF%E7%A4%BA%E8%8C%83.png)
        * ![用elif来避免if循环时会出现的穿透现象](imgs/%E7%94%A8elif%E6%9D%A5%E9%81%BF%E5%85%8Dif%E5%BE%AA%E7%8E%AF%E6%97%B6%E4%BC%9A%E5%87%BA%E7%8E%B0%E7%9A%84%E7%A9%BF%E9%80%8F%E7%8E%B0%E8%B1%A1.png)
  * 4. for
    * 在Python中for循环可以遍历任何序列的项目，如一个列表或一个字符串。
    * for循环的格式：
      * ```
          for 变量 in 要遍历的数据:
              方法体
        ```
      * 像前端里的forEach方法，这里的c时字符串中一个又一个的字符串变量，country代表要遍历的数据。
        * ![使用for循环遍历字符串并打印结果](imgs/%E4%BD%BF%E7%94%A8for%E5%BE%AA%E7%8E%AF%E9%81%8D%E5%8E%86%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%B9%B6%E6%89%93%E5%8D%B0%E7%BB%93%E6%9E%9C.png)
        * ![遍历一个列表中的元素](imgs/%E9%81%8D%E5%8E%86%E4%B8%80%E4%B8%AA%E5%88%97%E8%A1%A8%E4%B8%AD%E7%9A%84%E5%85%83%E7%B4%A0.png)
        * ![遍历range方法返回的元素的长度，来获取元素的下标](imgs/%E9%81%8D%E5%8E%86range%E6%96%B9%E6%B3%95%E8%BF%94%E5%9B%9E%E7%9A%84%E5%85%83%E7%B4%A0%E7%9A%84%E9%95%BF%E5%BA%A6%EF%BC%8C%E6%9D%A5%E8%8E%B7%E5%8F%96%E5%85%83%E7%B4%A0%E7%9A%84%E4%B8%8B%E6%A0%87.png)
  * 5. range
    * ![range(数字)方法返回的结果是一个可遍历的对象，且这个对象默认是从0开始到这个数字之前的那个数字](imgs/range%28%E6%95%B0%E5%AD%97%29%E6%96%B9%E6%B3%95%E8%BF%94%E5%9B%9E%E7%9A%84%E7%BB%93%E6%9E%9C%E6%98%AF%E4%B8%80%E4%B8%AA%E5%8F%AF%E9%81%8D%E5%8E%86%E7%9A%84%E5%AF%B9%E8%B1%A1%EF%BC%8C%E4%B8%94%E8%BF%99%E4%B8%AA%E5%AF%B9%E8%B1%A1%E9%BB%98%E8%AE%A4%E6%98%AF%E4%BB%8E0%E5%BC%80%E5%A7%8B%E5%88%B0%E8%BF%99%E4%B8%AA%E6%95%B0%E5%AD%97%E4%B9%8B%E5%89%8D%E7%9A%84%E9%82%A3%E4%B8%AA%E6%95%B0%E5%AD%97.png)
    * ![若range方法中的第一个参数有指定从哪个数字开始，那就从那个数字开始到第二个参数的前一个数字为止，依旧是左闭右开的区间](imgs/%E8%8B%A5range%E6%96%B9%E6%B3%95%E4%B8%AD%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%8F%82%E6%95%B0%E6%9C%89%E6%8C%87%E5%AE%9A%E4%BB%8E%E5%93%AA%E4%B8%AA%E6%95%B0%E5%AD%97%E5%BC%80%E5%A7%8B%EF%BC%8C%E9%82%A3%E5%B0%B1%E4%BB%8E%E9%82%A3%E4%B8%AA%E6%95%B0%E5%AD%97%E5%BC%80%E5%A7%8B%E5%88%B0%E7%AC%AC%E4%BA%8C%E4%B8%AA%E5%8F%82%E6%95%B0%E7%9A%84%E5%89%8D%E4%B8%80%E4%B8%AA%E6%95%B0%E5%AD%97%E4%B8%BA%E6%AD%A2%EF%BC%8C%E4%BE%9D%E6%97%A7%E6%98%AF%E5%B7%A6%E9%97%AD%E5%8F%B3%E5%BC%80%E7%9A%84%E5%8C%BA%E9%97%B4.png)
    * ![range方法传递三个参数及其对应的意义与作用](imgs/range%E6%96%B9%E6%B3%95%E4%BC%A0%E9%80%92%E4%B8%89%E4%B8%AA%E5%8F%82%E6%95%B0%E5%8F%8A%E5%85%B6%E5%AF%B9%E5%BA%94%E7%9A%84%E6%84%8F%E4%B9%89%E4%B8%8E%E4%BD%9C%E7%94%A8.png)
* 4.8 高级数据类型
  * 1. 字符串高级
    * 字符串的常见操作有：
      * 获取长度：len，获取字符串的长度。
      * 查找内容：find，查找指定内容在字符串中是否存在，若存在就返回该内容在字符串中第一次出现的开始位置索引值，若不存在，则返回-1.
      * 判断：startswith,endswith，判断字符串是否以谁谁谁开头/结尾。
      * 计算出现次数：count，返回str在start和end之间在mystr里出现的次数。
      * 替换内容：replace，替换字符串中指定的内容，如果指定次数count，则替换不会超过count次。
      * 切割字符串：split，通过参数的内容切割字符串。
      * 修改大小写：upper,lower，将字符串中的大小写互换。
      * 空格处理：strip，去空格。
      * 字符串拼接：join，字符串拼接。
  * 2. 列表高级
    * 列表的增删改查
      * 增-向列表中添加元素，主要是三种方法，append、insert、extend
        * append，在列表末端/最后添加新元素
          * ```
              food_list=['火锅','麻辣烫','酸菜馅饺子']
              print(food_list)    #['火锅', '麻辣烫', '酸菜馅饺子']
              food_list.append('兰州牛肉面')
              print(food_list)    #['火锅', '麻辣烫', '酸菜馅饺子', '兰州牛肉面']
            ```
        * insert，向指定位置插入元素，insert方法的参数，第一个是索引位置，代表要插入的位置的下标；第二个是对象，就是要插入的元素内容。想要插入到哪个位置，就写那个位置的索引值。
          * insert(index-索引,object-对象)
          * ```
              man_list=['Osborn','Sariel','Jesse']
              print(man_list)     #['Osborn', 'Sariel', 'Jesse']
              man_list.insert(1,'Evan')
              print(man_list)     #['Osborn', 'Evan', 'Sariel', 'Jesse']
              man_list.insert(3,'Charlie')
              print(man_list)     #['Osborn', 'Evan', 'Sariel', 'Charlie', 'Jesse']
            ```
        * extend，合并两个列表，通过extend，可以将另一个列表中的元素逐一添加到列表中。extend方法的参数必须是可以迭代的数据，比如字符串、列表、元组、字典等，绝对不可以是int和float，但他俩是单个值不是系列值，也不可以遍历，所以想要变成可迭代就转为string或调用range方法。
          * 另外扩展的一点是，可迭代对象甚至可以是一个空值，比如空列表、空字符串等，因为它们可以用for循环来进行遍历。
          * ```
              num_list=[1,2,3]
              num_list2=[4,5,6]
              num_list.extend(num_list2)
              print(num_list)     #[1, 2, 3, 4, 5, 6]
            ```
      * 删-删除列表中已有元素，常用的方法有三种，del、pop、remove：
        * del，根据下标进行删除，若爬取的数据中，有不想要的个别数据，就可以通过下标的方式来删除。需要注意的是del是python语句，不是列表的方法，所以无法通过listName.del()的方式被调用。
          * ![del-根据下标删除元素](imgs/del-%E6%A0%B9%E6%8D%AE%E4%B8%8B%E6%A0%87%E5%88%A0%E9%99%A4%E5%85%83%E7%B4%A0.png)
        * pop，删除最后一个元素
          * ![pop-删除列表中最后一个元素](imgs/pop-%E5%88%A0%E9%99%A4%E5%88%97%E8%A1%A8%E4%B8%AD%E6%9C%80%E5%90%8E%E4%B8%80%E4%B8%AA%E5%85%83%E7%B4%A0.png)
        * remove，根据元素的值进行删除
          * ![remove-remove方法中传递想要删除的元素值作为参数](imgs/remove-remove%E6%96%B9%E6%B3%95%E4%B8%AD%E4%BC%A0%E9%80%92%E6%83%B3%E8%A6%81%E5%88%A0%E9%99%A4%E7%9A%84%E5%85%83%E7%B4%A0%E5%80%BC%E4%BD%9C%E4%B8%BA%E5%8F%82%E6%95%B0.png)
      * 改-修改列表中元素的值，通过下标来修改
        * ```
            cityList=['北京','上海','深圳','兰州','西安']
            print(cityList)     #['北京', '上海', '深圳', '兰州', '西安']
            # 需求：将西安改为沈阳
            # 方法：通过下标来修改元素值
            cityList[4]='沈阳'
            print(cityList)     #['北京', '上海', '深圳', '兰州', '沈阳']
            # 需求：将深圳改为天水  
            cityList[2]='天水'
            print(cityList)     #['北京', '上海', '天水', '兰州', '沈阳']
          ```
      * 查-查询列表中指定元素是否存在，主要包含以下两个方法，in和not in：
        * Python中查找元素的常用方法为如下两种
        * in(存在)，若指定元素存在于列表中，则返回True，否则返回False。
          * ![in-指定元素存在于列表中](imgs/in-%E6%8C%87%E5%AE%9A%E5%85%83%E7%B4%A0%E5%AD%98%E5%9C%A8%E4%BA%8E%E5%88%97%E8%A1%A8%E4%B8%AD.png)
          * ![in-指定元素不存在于列表中](imgs/in-%E6%8C%87%E5%AE%9A%E5%85%83%E7%B4%A0%E4%B8%8D%E5%AD%98%E5%9C%A8%E4%BA%8E%E5%88%97%E8%A1%A8%E4%B8%AD.png)
        * not in(不存在)，若指定元素不存在于列表中，则返回True，否则返回False。
          * ![not in-指定元素不在列表中，返回True](imgs/not%20in-%E6%8C%87%E5%AE%9A%E5%85%83%E7%B4%A0%E4%B8%8D%E5%9C%A8%E5%88%97%E8%A1%A8%E4%B8%AD%EF%BC%8C%E8%BF%94%E5%9B%9ETrue.png)
          * ![not in-指定元素存在于列表中，返回False](imgs/not%20in-%E6%8C%87%E5%AE%9A%E5%85%83%E7%B4%A0%E5%AD%98%E5%9C%A8%E4%BA%8E%E5%88%97%E8%A1%A8%E4%B8%AD%EF%BC%8C%E8%BF%94%E5%9B%9EFalse.png)
  * 3. 元组高级
    * python中元组和列表类似，不同之处就在于元组只可读不可改，元组用小括号，而列表用中括号。增删改查中，在元组中能做到的只有查。
      * 尝试增：
        * ![尝试调用append方法增加，结果报错](imgs/%E5%B0%9D%E8%AF%95%E8%B0%83%E7%94%A8append%E6%96%B9%E6%B3%95%E5%A2%9E%E5%8A%A0%EF%BC%8C%E7%BB%93%E6%9E%9C%E6%8A%A5%E9%94%99.png)
        * ![insert方法增加，失败](imgs/insert%E6%96%B9%E6%B3%95%E5%A2%9E%E5%8A%A0%EF%BC%8C%E5%A4%B1%E8%B4%A5.png)
        * ![extend方法增加，失败](imgs/extend%E6%96%B9%E6%B3%95%E5%A2%9E%E5%8A%A0%EF%BC%8C%E5%A4%B1%E8%B4%A5.png)
      * 尝试删
        * ![del 删除，删不了](imgs/del%20%E5%88%A0%E9%99%A4%EF%BC%8C%E5%88%A0%E4%B8%8D%E4%BA%86.png)
        * ![pop方法删除，删不了](imgs/pop%E6%96%B9%E6%B3%95%E5%88%A0%E9%99%A4%EF%BC%8C%E5%88%A0%E4%B8%8D%E4%BA%86.png)
        * ![remove方法删除，删不了](imgs/remove%E6%96%B9%E6%B3%95%E5%88%A0%E9%99%A4%EF%BC%8C%E5%88%A0%E4%B8%8D%E4%BA%86.png)
      * 尝试改
        * ![尝试修改Tuple中元素值，结果肯定是失败的，元组中元素只可读不可改](imgs/%E5%B0%9D%E8%AF%95%E4%BF%AE%E6%94%B9Tuple%E4%B8%AD%E5%85%83%E7%B4%A0%E5%80%BC%EF%BC%8C%E7%BB%93%E6%9E%9C%E8%82%AF%E5%AE%9A%E6%98%AF%E5%A4%B1%E8%B4%A5%E7%9A%84%EF%BC%8C%E5%85%83%E7%BB%84%E4%B8%AD%E5%85%83%E7%B4%A0%E5%8F%AA%E5%8F%AF%E8%AF%BB%E4%B8%8D%E5%8F%AF%E6%94%B9.png)
    * 定义只有一个数据的元组，**必须在唯一的元素后写一个逗号**，这说明该元组有且只有一个元素/数据。
      * ![定义只有一个元素的元组时，必须在唯一的元素后加一个逗号，否则类型将不是Tuple类型](imgs/%E5%AE%9A%E4%B9%89%E5%8F%AA%E6%9C%89%E4%B8%80%E4%B8%AA%E5%85%83%E7%B4%A0%E7%9A%84%E5%85%83%E7%BB%84%E6%97%B6%EF%BC%8C%E5%BF%85%E9%A1%BB%E5%9C%A8%E5%94%AF%E4%B8%80%E7%9A%84%E5%85%83%E7%B4%A0%E5%90%8E%E5%8A%A0%E4%B8%80%E4%B8%AA%E9%80%97%E5%8F%B7%EF%BC%8C%E5%90%A6%E5%88%99%E7%B1%BB%E5%9E%8B%E5%B0%86%E4%B8%8D%E6%98%AFTuple%E7%B1%BB%E5%9E%8B.png)
  * 4. 切片
    * 切片是指对操作的对象只截取其中一部分的操作，字符串、列表、元组都支持切片操作。可能觉得有点像range()，确实类似于range方法，但切片的话不用写range()，有特定写法。
    * 语法：[起始:结束:步长]，也可以简化成[起始:结束]。
    * 注：选取的区间是从‘起始’位开始，到‘结束’前一位结束，不包含结束位本身，依旧是左闭右开的区间，步长表示选取间隔。
  * 5. 字典高级
    * 增-增加元素
      * 还是通过[]来进行新增元素的操作，利用key的特点，key的特点就是，key值若存在于字典中，那根据操作的不同会变成修改或查询的操作，但若key值不存在于字典中，又做了赋值的操作，那就会变成新增元素的操作。
        * ![字典高级-利用key新增元素](imgs/%E5%AD%97%E5%85%B8%E9%AB%98%E7%BA%A7-%E5%88%A9%E7%94%A8key%E6%96%B0%E5%A2%9E%E5%85%83%E7%B4%A0.png)
    * 删-删除元素
      * 删除元素有del和clear()两种方法，del还有可以删除指定元素和删除整个字典两种用法。
        * del
          * 删除指定元素，其格式为del dicName['keyName']，即可删除指定的元素。
          * 删除整个字典，其格式为del dicName，此操作会将整个字典清除掉，且不保留字典对象，若输出，会出现该dicName为定义的错。
          * ![字典高级-del，删除字典，连字典对象都不保留](imgs/%E5%AD%97%E5%85%B8%E9%AB%98%E7%BA%A7-del%EF%BC%8C%E5%88%A0%E9%99%A4%E5%AD%97%E5%85%B8%EF%BC%8C%E8%BF%9E%E5%AD%97%E5%85%B8%E5%AF%B9%E8%B1%A1%E9%83%BD%E4%B8%8D%E4%BF%9D%E7%95%99.png)
        * clear()-调用clear方法即可清空指定的字典，但只是把字典内的数据全部清除掉，会保留字典对象/字典结构，调用clear方法，输出dicName会返回一个空字典/对象。
          * ![字典高级-调用clear方法来清空字典，但保留字典结构](imgs/%E5%AD%97%E5%85%B8%E9%AB%98%E7%BA%A7-%E8%B0%83%E7%94%A8clear%E6%96%B9%E6%B3%95%E6%9D%A5%E6%B8%85%E7%A9%BA%E5%AD%97%E5%85%B8%EF%BC%8C%E4%BD%86%E4%BF%9D%E7%95%99%E5%AD%97%E5%85%B8%E7%BB%93%E6%9E%84.png)
    * 改-修改元素
      * 在[]中输入想要修改的key值，并赋值其对应的value值，且修改不像是查询，不可以调用get方法来进行，因为get方法是用来获取元素的，而不是修改。说句题外话，也可以调用__setitem__方法来修改元素值，方法中第一个参数位置传递要修改的key值，第二个参数位置传value值，这个方法是修改dic时使用的。
    * 查-查看元素
      * 除了使用key查找元素，还可以使用get方法来获取数据。
        * 通过元素的key值查找元素的value值的格式是```dicName['key值']```，但这个key值并非要用引号括起来，若当初设置的时候没用引号，获取的时候也就不用。用[]的方式获取元素的value值时，不能输入不存在的key值，否则会报keyerror的错，当然也不能用.的方式来访问dic的数据，这样会报属性错误的错；
          * ![当想要获取字典中不存在的key值时，会报keyError的错，来代表改键值对不存在](imgs/%E5%BD%93%E6%83%B3%E8%A6%81%E8%8E%B7%E5%8F%96%E5%AD%97%E5%85%B8%E4%B8%AD%E4%B8%8D%E5%AD%98%E5%9C%A8%E7%9A%84key%E5%80%BC%E6%97%B6%EF%BC%8C%E4%BC%9A%E6%8A%A5keyError%E7%9A%84%E9%94%99%EF%BC%8C%E6%9D%A5%E4%BB%A3%E8%A1%A8%E6%94%B9%E9%94%AE%E5%80%BC%E5%AF%B9%E4%B8%8D%E5%AD%98%E5%9C%A8.png)
          * ![在Python中不可以用这种方式获取value值，前端或许可以，但Python绝对不行](imgs/%E5%9C%A8Python%E4%B8%AD%E4%B8%8D%E5%8F%AF%E4%BB%A5%E7%94%A8%E8%BF%99%E7%A7%8D%E6%96%B9%E5%BC%8F%E8%8E%B7%E5%8F%96value%E5%80%BC%EF%BC%8C%E5%89%8D%E7%AB%AF%E6%88%96%E8%AE%B8%E5%8F%AF%E4%BB%A5%EF%BC%8C%E4%BD%86Python%E7%BB%9D%E5%AF%B9%E4%B8%8D%E8%A1%8C.png)
        * 通过get方法来获取元素的value值的话，将key值作为get方法的参数传进去即可，但也要注意不能传递不存在的key值，虽然不报错，会返回None值，但也无法获取任何数据。
    * 字典的遍历
      * 只遍历key，调用dicName的keys()，也可以省略，写成for 变量名 in dicName
        * ![遍历字典-只遍历并输出字典的key](imgs/%E9%81%8D%E5%8E%86%E5%AD%97%E5%85%B8-%E5%8F%AA%E9%81%8D%E5%8E%86%E5%B9%B6%E8%BE%93%E5%87%BA%E5%AD%97%E5%85%B8%E7%9A%84key.png)
      * 只遍历value，调用dicName的value()，专门用来获取字典中的value，它不像keys方法一样能被省略，一旦省略就会默认为获取字典中的key。
        * ![遍历字典-只遍历并输出字典的value](imgs/%E9%81%8D%E5%8E%86%E5%AD%97%E5%85%B8-%E5%8F%AA%E9%81%8D%E5%8E%86%E5%B9%B6%E8%BE%93%E5%87%BA%E5%AD%97%E5%85%B8%E7%9A%84value.png)
      * 遍历key和value，需要在变量名的位置写上key和value，缺一不可，在这里调用dicName的items方法，来获取字典的key和value。
        * ![遍历字典-调用items方法获取字典中的key和value，并遍历字典中的key和value](imgs/%E9%81%8D%E5%8E%86%E5%AD%97%E5%85%B8-%E8%B0%83%E7%94%A8items%E6%96%B9%E6%B3%95%E8%8E%B7%E5%8F%96%E5%AD%97%E5%85%B8%E4%B8%AD%E7%9A%84key%E5%92%8Cvalue%EF%BC%8C%E5%B9%B6%E9%81%8D%E5%8E%86%E5%AD%97%E5%85%B8%E4%B8%AD%E7%9A%84key%E5%92%8Cvalue.png)
      * 遍历字典的元素，并以元组的形式输出，还是调用dicName的items方法，但在变量名的位置写入一个变量名即可，这样就可以遍历字典的键值对，输出元组类型的数据。
        * ![遍历字典-调用items方法获取获取字典中元素，并输出，输出的结果数据类型为元组](imgs/%E9%81%8D%E5%8E%86%E5%AD%97%E5%85%B8-%E8%B0%83%E7%94%A8items%E6%96%B9%E6%B3%95%E8%8E%B7%E5%8F%96%E8%8E%B7%E5%8F%96%E5%AD%97%E5%85%B8%E4%B8%AD%E5%85%83%E7%B4%A0%EF%BC%8C%E5%B9%B6%E8%BE%93%E5%87%BA%EF%BC%8C%E8%BE%93%E5%87%BA%E7%9A%84%E7%BB%93%E6%9E%9C%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B%E4%B8%BA%E5%85%83%E7%BB%84.png)
* 4.9 函数
  * 1. 定义函数
    * 格式：
      * ```
        def 函数名():
          代码
        ```
    * 定义好函数后，函数体内的代码并不会执行，若想要执行函数体内的内容，需要手动调用函数。每次调用函数时，函数都会从头开始执行一次，当函数体中的代码执行完毕后，意味着调用结束。
  * 2. 调用函数
    * 定义了函数之后，就相当于有了一个具有某些功能的代码，想要让这些代码能够执行，就需要调用它，调用函数很简单，函数名()即可。
    * ![定义函数与调用函数](imgs/%E5%AE%9A%E4%B9%89%E5%87%BD%E6%95%B0%E4%B8%8E%E8%B0%83%E7%94%A8%E5%87%BD%E6%95%B0.png)
  * 3. 函数参数
    * 为了让一个函数更加通用，即想让它计算哪两个数的和，就让它计算哪两个的和，在定义函数时，就可以让函数接收数据，就解决了这个问题，可以将一个函数使用地更灵活。
    * ![未使用参数和使用参数的结果展示](imgs/%E6%9C%AA%E4%BD%BF%E7%94%A8%E5%8F%82%E6%95%B0%E5%92%8C%E4%BD%BF%E7%94%A8%E5%8F%82%E6%95%B0%E7%9A%84%E7%BB%93%E6%9E%9C%E5%B1%95%E7%A4%BA.png)
    * 注：
      * 在定义函数时，小括号里写等待赋值的变量名，是用来接收参数用的，简称形参。
      * 在调用函数时，小括号里写真正需要进行运算的数据，必须保证与定义函数时传递的形参数保持一致，是用来传递给函数用的，简称实参。
  * 4. 函数返回值
    * “返回值”介绍
      * 简单来说，返回值就是程序中函数完成一件事后，最后还给调用者的结果。
    * 带有返回值的函数
      * 想要在函数中把结果返回给调用者，就需要在函数中使用return
        * ```
            def sum(a,b):
            return a+b
            sum=sum(166,512)
            print(sum)      #678
          ```
    * 保存函数的返回值
  * 5. 局部变量
    * 是指在函数内部定义的变量，特点是其作用域范围是函数内部，而无法在函数的外部使用。
      * ![局部变量，在函数外部打印在函数内部定义的变量时会报错](imgs/%E5%B1%80%E9%83%A8%E5%8F%98%E9%87%8F%EF%BC%8C%E5%9C%A8%E5%87%BD%E6%95%B0%E5%A4%96%E9%83%A8%E6%89%93%E5%8D%B0%E5%9C%A8%E5%87%BD%E6%95%B0%E5%86%85%E9%83%A8%E5%AE%9A%E4%B9%89%E7%9A%84%E5%8F%98%E9%87%8F%E6%97%B6%E4%BC%9A%E6%8A%A5%E9%94%99.png)
  * 6. 全局变量
    * 是指定义在函数外部的变量，其可以在函数的外部以及在函数的内部使用。但在现实开发中，要在满足条件的情况下，尽量使用作用域最小的那个变量范围。因为全局变量是通用且重复的，有时需要避免重复书写。
* 4.10 文件
  * 1. 文件的打开与关闭
    * 打开/创建文件
      * 在Python，使用open函数，可以打开一个已经存在的文件，或创建一个新文件，open(文件路径,访问模式)
      * 示例如下：
        * ```file=open('test.txt','w')```
        * ![未创建文件的情况下，只写文件路径，不写访问模式会报错](imgs/%E6%9C%AA%E5%88%9B%E5%BB%BA%E6%96%87%E4%BB%B6%E7%9A%84%E6%83%85%E5%86%B5%E4%B8%8B%EF%BC%8C%E5%8F%AA%E5%86%99%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%EF%BC%8C%E4%B8%8D%E5%86%99%E8%AE%BF%E9%97%AE%E6%A8%A1%E5%BC%8F%E4%BC%9A%E6%8A%A5%E9%94%99.png)
        * ![同样未创建文件的情况下，写了访问模式，不但不会报错，还会将文件创建好](imgs/%E5%90%8C%E6%A0%B7%E6%9C%AA%E5%88%9B%E5%BB%BA%E6%96%87%E4%BB%B6%E7%9A%84%E6%83%85%E5%86%B5%E4%B8%8B%EF%BC%8C%E5%86%99%E4%BA%86%E8%AE%BF%E9%97%AE%E6%A8%A1%E5%BC%8F%EF%BC%8C%E4%B8%8D%E4%BD%86%E4%B8%8D%E4%BC%9A%E6%8A%A5%E9%94%99%EF%BC%8C%E8%BF%98%E4%BC%9A%E5%B0%86%E6%96%87%E4%BB%B6%E5%88%9B%E5%BB%BA%E5%A5%BD.png)
    * 文件路径
      * 绝对路径：是指绝对位置，完整地描述了目标文件的所在地，将所有目录的层级关系一目了然的呈现出来。
        * 如：C:\Users\田园，从电脑的盘符开始，一级一级的到达目标文件的所在地，表示的就是一个绝对路径。
      * 相对路径：是从当前文件所在的文件夹开始的路径。
        * test.txt，在当前文件夹里查找test.txt文件。
        * ./test.txt，也是在当前文件夹里查找test.txt文件，./表示当前文件夹。
        * ../test.txt，从当前文件夹的上一级文件夹里查找test.txt文件，../表示上一级文件夹。
        * demo/test.txt，先在当前文件夹里找到demo文件夹，并在该文件夹中查找test.txt文件。
    * 访问模式：
      * r:以**只读**方式打开文件。文件的指针将会放在文件的开头，若文件不存在，则报错，```这是默认模式``。
      * w:打开一个只用于**写入**的文件。若该文件已存在，则将其覆盖。但若不存在，则创建新文件。
      * a(append):打开一个文件用于**追加**，若该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容会被写入到已有内容之后；但若该文件不存在，则创建新文件进行写入。
      * r+:打开一个文件用于读写，文件指针将会放在文件的开头。
      * w+:打开一个文件用于读写。若该文件已存在，则将其覆盖；若不存在，则创建新文件。
      * a+:打开一个文件用于读写，若该文件已存在，文件指针将会放在文件的结尾，在文件打开时，会是追加模式；但若该文件不存在，则创建新文件用于读写。
      * rb:以二进制格式打开一个文件，用于只读，文件指针将会放在文件的开头。
      * wb:以二进制格式打开一个文件只用于写入，若该文件已存在，则将其覆盖，但若文件不存在，则创建新文件。
      * ab:以二进制格式打开一个文件用于追加，若该文件已存在，则文件指针将会放在文件的结尾。也就是说，新的内容会被写入到已有内容之后，但若该文件不存在，则创建新文件进行写入。
      * rb+:以二进制格式打开一个文件用于读写，文件指针将会放在文件的开头。
      * wb+:以二进制格式打开一个文件用于读写，若该文件已存在，则将其覆盖；但若该文件不存在，则创建新文件。
      * ab+:以二进制格式打开一个文件用于读写，若该文件已存在，文件指针将会放在文件的结尾；但若该文件不存在，则创建新文件用于读写。
    * 关闭文件
      * 为避免CPU过载，也要记得关闭一些用完的文件。调用close方法关闭即可，关闭文件是一个良好的习惯。调用close方法关闭后，文件看起来并未被关闭，且文件也没有被删除，但其实确实已经关闭了，是被吃掉了内存的。
  * 2. 文件的读写
    * 写数据(write)
      * 使用write()可以完成向文件写入数据的操作。
      * demo：新建一个file_write_test.py文件，向其中写入代码：
      * ![创建新文件file_write_test.py文件，并调用write方法向其中输入数据](imgs/%E5%88%9B%E5%BB%BA%E6%96%B0%E6%96%87%E4%BB%B6file_write_test.py%E6%96%87%E4%BB%B6%EF%BC%8C%E5%B9%B6%E8%B0%83%E7%94%A8write%E6%96%B9%E6%B3%95%E5%90%91%E5%85%B6%E4%B8%AD%E8%BE%93%E5%85%A5%E6%95%B0%E6%8D%AE.png)
      * 除了上图所示，创建新文件并写入文件以外，还有访问模式为a的情况，意思是append，也就是追加，用a模式访问文件，就会在旧数据后面追加新的数据。
        * ![以w方式和以a模式的区别](imgs/%E4%BB%A5w%E6%96%B9%E5%BC%8F%E5%92%8C%E4%BB%A5a%E6%A8%A1%E5%BC%8F%E7%9A%84%E5%8C%BA%E5%88%AB.png)
    * 读数据(read)
      * 创建新文件，并设置访问模式为r，也就是只读取，并且调用read方法，来读取文件中的内容就可以获取到想要的内容。
        * ![访问模式为r，并调用read方法，意为读取数据](imgs/%E8%AE%BF%E9%97%AE%E6%A8%A1%E5%BC%8F%E4%B8%BAr%EF%BC%8C%E5%B9%B6%E8%B0%83%E7%94%A8read%E6%96%B9%E6%B3%95%EF%BC%8C%E6%84%8F%E4%B8%BA%E8%AF%BB%E5%8F%96%E6%95%B0%E6%8D%AE.png)
      * 但read方法有效率低下的问题，当数据量庞大时，read方法就不会适用，此时可以调用readline方法，它是一行一行读取数据的。
        * ![read方法读取效率较低，可以调用readline方法，这样输出的虽只有一行数据，但提升了效率](imgs/read%E6%96%B9%E6%B3%95%E8%AF%BB%E5%8F%96%E6%95%88%E7%8E%87%E8%BE%83%E4%BD%8E%EF%BC%8C%E5%8F%AF%E4%BB%A5%E8%B0%83%E7%94%A8readline%E6%96%B9%E6%B3%95%EF%BC%8C%E8%BF%99%E6%A0%B7%E8%BE%93%E5%87%BA%E7%9A%84%E8%99%BD%E5%8F%AA%E6%9C%89%E4%B8%80%E8%A1%8C%E6%95%B0%E6%8D%AE%EF%BC%8C%E4%BD%86%E6%8F%90%E5%8D%87%E4%BA%86%E6%95%88%E7%8E%87.png)
      * 当然，一行一行读取数据有时效率也不高，因此可以调用readlines方法，用于多行读取，会将所有的数据都读取到，返回的是一个列表，列表的元素就是一行一行的数据，
  * 3. 序列化和反序列化
    * 通过文件操作，可以将字符串导入到一个本地文件，但若是一个对象(如列表、元组、字典等)，就无法直接写入到一个文件里，需要对这个对象进行序列化，才能写入到文件中。
    * 序列化就是设计一套协议，按照某种规则，把内存中的数据转换为字节序列，保存到文件，反之从文件的字节序列恢复到内存中，就是反序列化。
      * 对象--->字节序列 ===>序列化
      * 字节序列--->对象 ===>反序列化
    * Python中提供了JSON这个模块用来实现数据的序列化和反序列化。
    * JSON模块
      * JSON(Javascript Object Notation，JS对象简谱)是一种能够轻量级的数据交换标准，JSON的本质是字符串。
    * 使用JSON实现序列化
      * JSON提供了dump和dumps两种方法，将一个对象进行序列化。
        * ![默认情况下，只能将字符串写入到文件中，其他的像列表字典等都不可以](imgs/%E9%BB%98%E8%AE%A4%E6%83%85%E5%86%B5%E4%B8%8B%EF%BC%8C%E5%8F%AA%E8%83%BD%E5%B0%86%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%86%99%E5%85%A5%E5%88%B0%E6%96%87%E4%BB%B6%E4%B8%AD%EF%BC%8C%E5%85%B6%E4%BB%96%E7%9A%84%E5%83%8F%E5%88%97%E8%A1%A8%E5%AD%97%E5%85%B8%E7%AD%89%E9%83%BD%E4%B8%8D%E5%8F%AF%E4%BB%A5.png)
      * dumps()：dumps方法的作用是把对象转换成字符串，它本身不具备将数据写入到文件的功能，需要write方法做协助。
        * ```
            file2=open('test2.txt','w')
            nameList=['Osborn','Evan','Sariel','Charlie','Jesse']
            import json
            name=json.dumps(nameList)
            # 可以看到调用dumps方法转换后的结果是字符串类型的数据
            print(type(name))   #<class 'str'>
            # 将转换后的数据写入到文件中
            file2.write(name)
            file2.close() #要记得关闭文件，以免内存泄漏
          ```
      * dump()：dump方法的作用也是把对象转换成字符串，但它不像dumps，需要write方法的协助，它可以一步到位。
        * ```
            file3=open('test3.txt','w')
            nameList=['Luke','Artem','Richard','Marius']
            import json
            # 调用dump方法，第一个参数为想要转换为字符串的数据，第二个参数就是想要将输入写入进去的那个指定的文件的变量名
            # 这一步骤就相当于dumps的name=json.dumps(nameList)和file2.write(name)这两步操作，dump给简化了，一步到位
            names=json.dump(nameList,file3) 
            file3.close()
          ```
    * 使用JSON实现返反序列化
      * JSON也提供了loads和load两种方法，来实现json字符串转为python对象/对象类型的数据的操作。
        * loads()：
          * ```
              file4=open('test3.txt','r')
              # 读取文件中的数据
              content=file4.read()
              print(content)      #["Luke", "Artem", "Richard", "Marius"]
              # 转换前，读取到的数据是字符串类型的数据
              print(type(content))    #<class 'str'>
              import json
              # 调用loads方法，将json字符串转换为python对象
              loaded=json.loads(content)
              print(loaded)   #['Luke', 'Artem', 'Richard', 'Marius']
              # 转换后，json字符串类型的数据已变为python的list类型
              print(type(loaded))     #<class 'list'>
            ```
        * load()：
          * ```
              file4=open('test3.txt','r')
              import json
              # 调用loaded方法，一步到位将json字符串转换为python对象
              loaded=json.load(file4)
              print(loaded)       #['Luke', 'Artem', 'Richard', 'Marius']
              print(type(loaded)) #<class 'list'>
            ```
* 4.11 异常
  * 1. 读取文件异常
    * 程序在运行过程中，由于我们的编码不规范，或其他一些客观原因，导致程序无法继续运行，此时，程序就会出现异常，若不对其异常进行处理，程序可能会由于异常直接终端掉。为保证程序的健壮性(我本人更想称之为流畅性、合法性)，在程序设计里提出异常处理的概念。
    * 读取文件异常
      * 在读取文件时，若该文件不存在，则会报出FileNotFoundError错误。
      * ![创造一个异常](imgs/%E5%88%9B%E9%80%A0%E4%B8%80%E4%B8%AA%E5%BC%82%E5%B8%B8.png)
  * 2. try...except语句
    * 如上图所示，一个文件不存在的情况下，设置访问模式为r的话就会报错，所以，try...except语句类似于前端中promise的try...catch语句，就是若有错误的话及时拦截。
      * ![用try...except语句解决异常情况，与前端里promise的trycatch类似](imgs/%E7%94%A8try...except%E8%AF%AD%E5%8F%A5%E8%A7%A3%E5%86%B3%E5%BC%82%E5%B8%B8%E6%83%85%E5%86%B5%EF%BC%8C%E4%B8%8E%E5%89%8D%E7%AB%AF%E9%87%8Cpromise%E7%9A%84trycatch%E7%B1%BB%E4%BC%BC.png)

