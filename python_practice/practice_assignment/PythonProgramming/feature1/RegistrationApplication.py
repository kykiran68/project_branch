from sql_connector import *

class Registration:
    def __init__(self, table_name, db_name='registration.db'):
        self.table_name = table_name
        self.db_name = db_name
        self.con = initial_connection(db_file=db_name)

    def create_registration_table(self):
        # check the table exist or not
        check_table_query = f"""select name from sqlite_master where type='table' and name='{self.table_name}'"""
        response = self.con.execute(check_table_query)
        if not response.fetchall():
            create_table_query = f"""create table {self.table_name}(
            first_name text, last_name text, username text, password text,
            email text, phone text, address text)"""
            self.con.execute(create_table_query)
        else:
            print("Table already exist")

    def user_singup(self):
        self.create_registration_table()
        first_name = input("Please enter first name :")
        last_name = input("Please enter Last name :")
        username = input("Please enter unique username :")
        password = input("Please enter password :")
        email = input("Please enter the email :")
        phone = input("Please enter the phone number :")
        address = input("Please enter the address :")
        insert_query = f"""insert into {self.table_name} (first_name, last_name, username, password,
        email, phone, address) values ('{first_name}', '{last_name}', '{username}',
        '{password}', '{email}', '{phone}', '{address}')        
        """
        print(insert_query)
        self.con.execute(insert_query)
        self.con.commit()


    def dummy_user_signup(self, num_of_user):
        self.create_registration_table()
        for i in range(num_of_user):
            first_name = fk.first_name()
            last_name = fk.last_name()
            username = fk.user_name()
            password = "userpassword"
            email = fk.email()
            phone = fk.phone_number()
            address = fk.address()
            insert_query = fr"""insert into {self.table_name} (first_name, last_name, username, password,
            email, phone, address) values ('{first_name}', '{last_name}', '{username}',
            '{password}', '{email}', '{phone}', '{address}')        
            """
            print(insert_query)
            self.con.execute(insert_query)
            self.con.commit()

    def login(self, username, password):
        select_query = f"""select username, password from {self.table_name} where username='{username}'"""
        user_details = self.con.execute(select_query)
        user_info = user_details.fetchall()
        print()
        flag = False
        for data in user_info:
            if data[0] == username and data[1] == password:
                flag = True
                break
            else:
                continue

        if flag:
            print("Login Successful")
        else:
            print("Access Denied, Wrong Username Password")

if __name__ == "__main__":
    obj = Registration("signup")
    while True:
        print("### Welcome to Registration Application ###")
        print("1. Registration \n"
              "2. Login")
        user_input = input("Please select your option :")
        if user_input == '1':
            print("1. Single user \n"
                  "2. multiple user\n")
            user_reg = input("Please select the choice :")
            if user_reg == '1':
                obj.user_singup()
            elif user_reg == '2':
                num_of_user= int(input("Please enter number of users :"))
                obj.dummy_user_signup(num_of_user)
        elif user_input == '2':
            username = input("Please enter username :")
            password = input("Please enter the password :")
            obj.login(username, password)
