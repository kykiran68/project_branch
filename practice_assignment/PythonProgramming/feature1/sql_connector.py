import sqlite3
from faker import Faker
"""
pip install faker
"""
fk = Faker()

def initial_connection(db_file='students.db'):
    con = sqlite3.connect(db_file)
    return con

def execute_query(query):
    con = initial_connection()
    con.execute(query)
    print("table created successfully")
    con.close()

def insert_query(query):
    con = initial_connection()
    con.execute(query)
    print("data inserted successfully")
    con.commit()
    con.close()

def select_query(query):
    con = initial_connection()
    data = con.execute(query)
    #con.close()
    return data

# create_table = """create table studentinfo(firstname text, lastname text, email text, phone int
# )
# """

# print(dir(fk))
# for i in range(50):
#     f_name = fk.first_name()
#     l_name = fk.last_name()
#     email =  fk.email()
#     phone =  8768878644
#     print(f_name, l_name, email, phone)
#     insert_query_cmd = f"""insert into studentinfo(firstname, lastname, email, phone) values
#     ('{f_name}', '{l_name}', '{email}', {phone})
#     """
#     #execute_query(create_table)
#     insert_query(insert_query_cmd)

# select_query_details = """select * from studentinfo where firstname='Jason'"""
#
# data = select_query(select_query_details)
# for val in data:
#     print(val)
