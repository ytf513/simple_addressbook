# coding=utf8
# Author:   Alex Yean
# Date:     2014-12-24
# 电话簿搜索:(1)db:sieyuan table:person sql:sqlstr="select id,name,phone from person  where id regexp '.*%s.*' or name regexp'.*%s.*' or phone regexp '.*%s.*'" % (search,search,search)
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options,parse_command_line
define("port",default=8800,help="run one the given port",type=int)
db=torndb.Connection("127.0.0.1:3306","sieyuan",user="python",password="python")
result=[]
class SearchPage(tornado.web.RequestHandler):
    def get(self):
        self.render('address.html',title='Sieyuan Address',result=result)

class SearchResult(tornado.web.RequestHandler):
    def get(self):
        search=self.get_argument("search")
        sqlstr="select id,name,phone from person  where id regexp '.*%s.*' or name regexp'.*%s.*' or phone regexp '.*%s.*'" % (search,search,search)
        #sqlstr="select id,name,phone from person  where id like '%22%' or name like '%22%' or phone like '%22%'"  
        result=db.query(sqlstr)
        #print sqlstr 
        self.render('address.html',title='Sieyuan result',result=result)

def main():
    parse_command_line()
    app=tornado.web.Application(
        [(r'/',SearchPage),(r'/s',SearchResult)],
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__=='__main__':
    main()
