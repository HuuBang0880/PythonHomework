import pyodbc
from tabulate import tabulate
# import pandas as pd

# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=DESKTOP-SQM34MJ;'
#                       'Database=QLMonAn;'
#                       'Trusted_Connection=yes;')
# cursor = conn.cursor()
# cursor.execute("select * from dbo.monan");
# for i in cursor:
#     print(i)
# conn.close()

# connString = 'Driver={SQL Server};Server=DESKTOP-SQM34MJ;Database=QLMonAn;Trusted_Connection=yes;'

# def get_Connection():
#     conn = pyodbc.connect(connString)
#     return conn

# def close_Connection(conn):
#     if conn:
#         conn.close()

# def get_all_dish():
#     try:
#         conn = get_Connection()
#         cursor = conn.cursor()
#         cursor.execute("select * from dbo.monan")
#         print(list(cursor))
#         close_Connection(cursor)

#     except (Exception, pyodbc.Error) as error:
#         print("Đã có lỗi: ", error)

# get_all_dish()


connString = 'Driver={SQL Server};Server=.;Database=QLSinhVien;Trusted_Connection=yes;'

def get_Connection():
    conn = pyodbc.connect(connString)
    return conn

def close_Connection(conn):
    if conn:
        conn.close()

def get_all_Student():
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        cursor.execute("select * from dbo.SinhVien, dbo.Lop where dbo.SinhVien.MaLop = dbo.Lop.Id")
        print("Danh sách sinh viên:")
        # print(f"Mã số\t\tHọ tên\t\t\tMã lớp\tLớp")
        # for row in cursor:
        #     print(f"{row[0]:1}\t{row[1]:23}\t{row[2]:10}\t{row[4]}")
        print(tabulate(cursor, headers= ["Mã số", "Họ tên", "IDClass", "IDClass", "Lớp"], numalign= "center"))
        close_Connection(cursor)

    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi: ", error)

def get_student_by_classid(class_id):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        params = (class_id)
        cursor.execute("SELECT dbo.SinhVien.ID, dbo.SinhVien.HoTen, dbo.Lop.Id, TenLop FROM dbo.SinhVien, dbo.Lop where dbo.SinhVien.MaLop = dbo.Lop.Id and dbo.Lop.Id = %s" %(params))
        print(tabulate(cursor, headers= ["Mã số", "Họ tên", "Mã lớp" , "Lớp"], numalign= "center"))
        close_Connection(cursor)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi: ", error)

def get_student_by_id(class_id):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        params = (class_id)
        cursor.execute("SELECT dbo.SinhVien.ID, dbo.SinhVien.HoTen, dbo.Lop.Id, TenLop FROM dbo.SinhVien, dbo.Lop where dbo.SinhVien.MaLop = dbo.Lop.Id and dbo.SinhVien.Id = %s" %(params))
        print(tabulate(cursor, headers= ["Mã số", "Họ tên", "Mã lớp" , "Lớp"], numalign= "center"))
        close_Connection(cursor)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi: ", error)


#get_all_Student()
get_student_by_classid(2)
# get_student_by_id(2)
