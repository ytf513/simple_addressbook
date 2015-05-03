# coding=utf8
# Author:   Alex Yean
# Date:     2014-12-24
# 电话簿搜索:(1)db:sieyuan table:person sql:sqlstr="select id,name,phone from person  where id regexp '.*%s.*' or name regexp'.*%s.*' or phone regexp '.*%s.*'" % (search,search,search)
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
from tornado.escape import json_encode
import re

from tornado.options import define,options,parse_command_line
define("port",default=8800,help="run one the given port",type=int)
db=torndb.Connection("127.0.0.1:3306","sieyuan",user="python",password="python")
result=[]
class AjaxGet(tornado.web.RequestHandler):
    #ajax get 方法；返回一个字符串
    def get(self):
        search=self.get_argument("search")
        #self.set_header("Content-Type", "text/html;charset=utf-8")
        sqlstr="select id,name from person where id regexp '.*%s.*' or name regexp '.*%s.*' limit 10" % (search,search)
        result=db.query(sqlstr)
        #res="\n".join([("%s %s") % (i["name"],i["id"]) for i in result])
        res=[("%s %s") % (i["name"],i["id"]) for i in result]
        #self.write(json_encode({"data:":res}).encode('utf-8'))
        print res[0]
        self.write({"data":res})
        #self.write(res) #TypeError: write() only accepts bytes, unicode, and dict objects


class SearchPage(tornado.web.RequestHandler):
    def get(self):
        self.render('address.html',title='Sieyuan Address',result=result)

class SearchResult(tornado.web.RequestHandler):
    def get(self):
        search=self.get_argument("search")
        #去除特殊字符
        search=re.sub('[.*=?% \'&]','',search)
        sqlstr="select id,name,phone from person  where id regexp '.*%s.*' or name regexp'.*%s.*' or phone regexp '.*%s.*' or dept regexp '.*%s.*'" % (search,search,search,search)
        #self.write(search)
        #sqlstr="select id,name,phone from person  where id like '%22%' or name like '%22%' or phone like '%22%'"  
        result=db.query(sqlstr)
        print self.request.remote_ip 
        #print result[0]
        self.render('address.html',title='Sieyuan通讯录',result=result)

def main():
    parse_command_line()
    settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static") 
    }#配置静态文件路径
    app=tornado.web.Application(
        [(r'/',SearchPage),
        (r'/s',SearchResult),
        (r'/ajaxGet',AjaxGet)],
        **settings
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__=='__main__':
    main()
