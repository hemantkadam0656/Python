def add(firstName: str | list[str] , lastName: str):  
    for item in firstName:
        if type(item) == str:
            return item + " " + lastName

        

    



fname = ["Hemant", "Kadam"]
lname = ""

name = add(fname,lname)
print(name)