from pymongo import MongoClient
from bson import ObjectId

#Database connection ( used Mongodb client for database)

client = MongoClient("mongodb+srv://AppFun:AppFun@cluster0.vakdbhi.mongodb.net/")

db = client["User_AppFun"]

userDetails = db["user"]

# Defined variable in globle scope to take inputs from diferent function. 

message = ""


# Defined function of main function to take user details 

def user_list():
    for user in userDetails.find():
        print(f"user-id: {str(user["_id"])} Name : {user["name"]} age: {user["age"]}" )

def add_user(name,age,password):
    userDetails.insert_one({"name":name, "age":age, "password":password})

def remove_id(user_id):
    userDetails.delete_one({'_id':ObjectId(user_id)})
    message = "user succesfully removed from list"
    user_message(message)

def update_user_details(user_id,new_name,new_age,new_password):
    userDetails.update_one({'_id':ObjectId(user_id)},
                           {'$set':{"name":new_name , "age": new_age, "password": new_password}})

def user_message(message):
    print(f"Message :{message}") 


# Main function started from here :- 
def main():
    while True:
        print("\n User List App")
        print("1.Add user")
        print("2.remove User")
        print("3.Update User Details")
        print("4.User Message")
        print("5.All User List")
        print("6.Exit from App")
        choice = int(input("Enter your choice:- "))

        match choice:
            case 1:
                name = input("Enter user name: ")
                age = input("Enter user age: ")
                password = input("Enter user password: ")
                add_user(name,age,password)
            case 2:
                user_id = input("Enter user id to remove: ")
                remove_id(user_id)
            case 3:
                user_id = input("Enter user id to update: ")
                new_name = input("Enter user name: ")
                new_age = input("Enter user age: ")
                new_password = input("Enter user password: ")
                update_user_details(user_id,new_name,new_age,new_password)
            case 4:
                print("\n Select any One message for account ")
                print("1.would you want to make your account private")
                print("2.would you want to make your account Public")
                print("3.Not Intertested")
                print("4.Exit")
                select_msg = int(input("Select your option: "))

                match select_msg:
                    case 1:
                        message = "Congratulation ! your account is private."
                        user_message(message)
                    case 2:
                        message = "Congratulation ! your account is open for public."  
                        user_message(message)
                    case 3:
                        message = "Thanks for connecting with us!"
                        user_message(message)
                        break
                    case 4:
                        break
                    case _:
                        print("Invalid Selection")

            case 5:
                user_list()                               
            case 6:
                break
            case _:
                print("Invalid choice,Select new option")

if __name__ == "__main__":
    main()