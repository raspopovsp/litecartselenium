from sqlalchemy import create_engine
import pymysql

pymysql.install_as_MySQLdb()  # Костылим MySQL для Python3


def fetchall(req):
    engine = create_engine("mysql://root:@localhost/litecartdb")
    result = engine.execute(req)

    res = result.fetchall()
    result.close()
    return res


def execute(req):
    engine = create_engine("mysql://root:@localhost/litecartdb")
    result = engine.execute(req)
    result.close()
