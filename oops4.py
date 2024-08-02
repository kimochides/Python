class Cart:
    def __init__(self):
        self.items={}
    def Additem(self,item_name,price,quantity=1):
        #if item already exisits, then increment the quantity
        if item_name in self.items:
            self.items[item_name]['quantity']+=quantity
        else:
            self.items[item_name]={'price':price,'quanity':quantity}
        print(f"Added {quantity} of {item_name} to the cart.")

    def Removeitem(self,item_name,quantity):
        #in case you try to remove more quantity of an item than it is already present
        if item_name in self.items:
            if self.items[item_name]['quantity']<=quantity:
                del self.items[item_name]
                print(f"Removed all {item_name} from the cart.")
        #decrement the quantity after removal
            else:
                self.items[item_name]['quantity']-=quantity
                print(f"Removed {quantity} of {item_name} from the cart.")
        else:
            print(f"{item_name} not found in the cart.")
    def calculate_total(self):
        total_price=0
        for item in self.items.values():
            total_price+=item['price']*item['quantity']
        return total_price
    def display_cart(self):
        if not self.items:
            print("The cart is empty.")
        else:
            print("Your Cart:")
            for item_name,details in self.items.items():
                print(f"{item_name}:{details['price']} x {details['quantity']}")

#example usage
cart=Cart()
cart.Additem("Apple",50,5)
cart.Additem("Banana",40,3)
cart.display_cart()

cart.Removeitem("Banana",2)
cart.display_cart()

cart.Additem("Orange",29,2)
cart.display_cart()

cart.Removeitem("Banana",2)
cart.display_cart()