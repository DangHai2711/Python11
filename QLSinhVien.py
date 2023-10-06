# import pyodbc

# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER = LAPTOP-VKBUP5Q2\LOCALDB#C7B135D0; DATABASE = QLSinhVien; UID=sa;PWD=sa;Encrypt=no')
# cursor = conn.cursor()
# cursor.execute("SELECT @@version")
# conn.close()
# db_version = cursor.fetchone()
# print("Bạn đang dùng hệ quản trị CSDL SQL server phiên bản ", db_version)

import pyodbc

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\MSSQLLocalDB;DATABASE=QLSinhVien;UID=mon;PWD=27112003;')
cursor = cnxn.cursor()
cursor.execute("select * from SinhVien")
rows = cursor.fetchall()
for row in rows:
    print (row)