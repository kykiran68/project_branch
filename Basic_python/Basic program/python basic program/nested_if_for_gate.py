gate1 = "found"
gate2 = "found"
gate3 = "not found"
if gate1 == "found":
     print("you entered to gate 1")
     if gate2 == "found":
         print("congrats! you opened gate 2")
         if gate3 == "found":
             print("Welcome to home you are successful")
         else:
             print("you are unsuccessful")
     else:
         print("you are unsuccessful")
else:
     print("you are unsuccessful")