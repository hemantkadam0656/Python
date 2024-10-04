import json

def load_order():
    try:
        with open("bacekyDetails.py", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_order(orderId):
    with open('bacekyDetails.py', 'w') as file:
        return json.dump(orderId, file)
       
        
def NewOrder(orderId):
    Name = input("Pls enter your Name : ")
    number = int(input("Pls enter your contact number : "))
    Order = input("Enter your Order : ")
    orderId.append({"Name": Name, "number": number, "order": Order,})
    save_order(orderId)
   

def OrderList(orderId):
     for index, order in enumerate(orderId,start=1):
        print(f"Order {index} : {order['order']}")


def OrderDetails(ordernumber,orderId):
        for index, order in enumerate(orderId,start=1):
            try:
                print(index)
                print(ordernumber)
                if ordernumber == index:                   
                    print(f"Order {index}: Customer Name : {order['Name']}  \n Cutomer Number : {order['number']} \n Customer Order : {order['order']}")
                    break
                else:
                    print(f"Order {ordernumber} Not found!")
            except ValueError:
                print(f"Oops! Value not found.")
                
def CustomerDetails(orderId,*args ):
        for index, order in enumerate(orderId,start=1):
            if args:
                if order['Name'] == args[0] and order['number'] == args[1] :             
                    print(f"Order {index}: Customer Name : {order['Name']}  \n Cutomer Number : {order['number']} \n Customer Order : {order['order']}")
                else:                 
                    print(f"Sorry ! Customer not found")

def main():
    orderId = load_order()
    while(True):
        print("\n-------------------------------")
        print("** Bakery Managemant Dash Board **")
        print("---------------------------------")
        print("1.OrderList")
        print("2.create New Order")
        print("3.Order Details")
        print("4.Customer Details")
        print("5.Exit")
        print("-------------------------------")
        choice = int(input("Enter your option : "))
        # orderId = input("Enter Your Order Id : ")
        match choice:
            case 1 :
                OrderList(orderId)
            case 2 :
                
                NewOrder(orderId)
            case 3 :
                ordernumber = input("Enter order number : ")
                OrderDetails(ordernumber,orderId)
            case 4:
                customerName = input("Enter Customer Name :")
                customerNumber = int(input("Enter Customer Number :"))
                CustomerDetails(orderId,customerName, customerNumber)
            case _:
                print("Invalid Option ! Pls Select correct One ")
            
 
if __name__ == '__main__':
    main()
