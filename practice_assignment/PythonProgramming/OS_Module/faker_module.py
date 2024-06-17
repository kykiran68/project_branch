from faker import Faker

fk = Faker()
for i in range(10):
    print("first name :", fk.first_name())
    print("last name :", fk.last_name())
    print("email :", fk.email())
    print("username :", fk.user_name())
    print("password :", fk.password())
    print("Company :", fk.company())
    print("Address :", fk.address())
    print("_"*40)

print(dir(fk))
