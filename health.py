import time

import pymysql

def database_not_ready_yet(error, checking_interval_seconds):
    print('Database initialization has not yet finished. Retrying over {0} second(s). The encountered error was: {1}.'
          .format(checking_interval_seconds,
                  repr(error)))
    time.sleep(checking_interval_seconds)

print('Waiting until the database is ready to handle connections....')
database_ready = False
while not database_ready:
    db_connection = None
    try:
        db_connection = pymysql.connect(host="db",
                                        port=3306,
                                        db="easy2make",
                                        user="root",
                                        password="root",
                                        charset='utf8mb4',
                                        connect_timeout=5)
        print('Database connection made.')
        db_connection.ping()
        print('Database ping successful.')
        database_ready = True
        print('The database is ready for handling incoming connections.')
    except pymysql.err.OperationalError as err:
        database_not_ready_yet(err, 2)
        print(err)
    except pymysql.err.MySQLError as err:
        database_not_ready_yet(err, 2)
        print(err)
    except Exception as err:
        database_not_ready_yet(err, 2)
        print(err)
    finally:
        if db_connection is not None and db_connection.open:
            db_connection.close()