## About Simple_Addressbook
这是一个简单的通讯录系统，可以只输入工号、姓名、部门或者电话任一信息，进行快速搜索功能。
- 自动填充；
- 参数化查询，防止SQL注入攻击；
- 去除特殊字符，防止查询失败，比如:=?*等

## 所用技术

- 使用Python,基于Tornado Web框架;
- 后台数据库：Mysql
- 前台使用Jquery,Jquery UI Autocomplete

## 怎么使用（Usage）

1. git clone 或者下载代码，配置环境（Jquery、安装Tornado等）；

2. 配置数据库
    - 默认db:sieyuan,table:person
    - 可以从csv导入数据库，csv格式如下：工号;姓名;部门;职位;性别;手机;E-mail.
      ` load data infile 'people.csv'  into table person  fields terminated by '; '  optionally enclosed by '"' escaped by '"'  lines terminated by '\r\n';`

3. 安装torndb，tornado中访问Mysql的模块

4. 修改参数address.py
    db=torndb.Connection("127.0.0.1:3306",dbName,user=userName,password=Password)

5. 运行`python address.py`,默认Port=8800

## Continue：后续新增功能

1. 用户新增功能；
2. 用户修改、删除功能；
3. ... 


 
