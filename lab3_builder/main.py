from mysqlbuilder import MySQLBuilder
from postrgresbuilder import PostrgresBuilder
from query import Query


if __name__ == '__main__':
    mysqlBuilder = MySQLBuilder()
    mysqlBuilder.select("image", ["title", "description"])
    mysqlBuilder.where("title == 'index'")
    print(mysqlBuilder.getSql())
    mysqlBuilder.reset()
    print(mysqlBuilder.getSql())


    postrgresBuilder = PostrgresBuilder()
    postrgresBuilder.select("book", ["title", "author", "year"])
    postrgresBuilder.where("year == 2000")
    postrgresBuilder.where("AND (author = 'test author' OR author = 'test author2')")
    postrgresBuilder.limit(5)
    print(postrgresBuilder.getSql())

