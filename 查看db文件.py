# import sqlite3

# # 连接到数据库
# conn = sqlite3.connect('UserDatabase.db')  # 将 'your_database.db' 替换为你的数据库文件名

# # 创建游标对象
# cursor = conn.cursor()

# # 查询数据库中的所有表
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()

# # 遍历所有表
# for table in tables:
#     print(f"Data in {table[0]} table:")
#     # 查询每个表中的所有数据
#     cursor.execute(f"SELECT * FROM {table[0]}")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#     print("\n")  # 打印一个空行以分隔不同的表数据

# # 提交事务（如果进行了更改）
# # conn.commit()

# # 关闭游标和连接
# cursor.close()
# conn.close()



import sqlite3
import csv

# 连接到数据库
conn = sqlite3.connect('UserDatabase.db')  # 将 'UserDatabase.db' 替换为你的数据库文件名

# 创建游标对象
cursor = conn.cursor()

# 查询数据库中的所有表
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# 遍历所有表
for table in tables:
    table_name = table[0]
    print(f"Data in {table_name} table:")
    
    # 查询每个表中的所有数据
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    
    # 为每个表创建一个 CSV 文件
    csv_file_name = f"UserDatabase/{table_name}.csv"
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # 获取列名
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [column[1] for column in cursor.fetchall()]
        csv_writer.writerow(columns)  # 写入列名
        
        # 写入数据
        for row in rows:
            csv_writer.writerow(row)
    
    print(f"Data saved to {csv_file_name}")
    print("\n")  # 打印一个空行以分隔不同的表数据

# 关闭游标和连接
cursor.close()
conn.close()