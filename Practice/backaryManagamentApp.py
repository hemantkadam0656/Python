import json

def load_order():
    try:
        with open("bacekyDetails.py", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
  
        
def NewOrder(orderId):
    Name = input("Pls enter your Name : ")
    number = int(input("Pls enter your contact number : "))
    Order = input("Enter your Order : ")
    orderId.append({"Name": Name, "number": number, "order": Order,})
   

def OrderList():
     pass

def OrderDetails(orderId):    
    pass


def CustomerDetails(orderId):
    pass



def main():
    orderId = load_order()
    while(True):
        print("\n-----------------------------")
        print("Bakery Managemant Dash Board")
        print("-----------------------------")
        print("1.OrderList")
        print("2.create New Order")
        print("3.Order Details")
        print("4.Exit")
        print("------------------------------")
        choice = int(input("Enter your option : "))
        # orderId = input("Enter Your Order Id : ")
        match choice:
            case 1 :
                OrderList()
            case 2 :
                
                NewOrder(orderId)
            case 3 :
                orderId = int(input("Enter your new Order Id : "))
                OrderDetails(orderId)
            case 4:
                break
            case _:
                print("Invalid Option ! Pls Select correct One ")
            
 
if __name__ == '__main__':
    main()
