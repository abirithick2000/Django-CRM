import mysql.connector


database=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345'
)

cursorobject=database.cursor()
cursorobject.execute('CREATE DATABASE rithick')

print('ALL DONE!')
