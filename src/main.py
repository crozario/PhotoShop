import query_database as qd

logged_in = False
login_name = ""
quit = False

class MenuItem():
    def __init__(self, num, item):
        self.num = num
        self.item = item
    
    def print_item(self):
        print(self.num, self.item)


class PhotoMenu():
    list_all_photos = MenuItem(1, "List All Photo's")
    list_photos_bought = MenuItem(2, "List Photo's Bought")
    list_photos_not_bought = MenuItem(3, "List Photo's Not Bought")

    def print_menu(self):
        self.list_all_photos.print_item()
        self.list_photos_bought.print_item()
        self.list_photos_not_bought.print_item()


class MainMenu():
    sign_in = MenuItem(1, "Sign In")
    sign_out = MenuItem(1, "Sign Out")
    photo_info = MenuItem(2, "Photo Info")
    photographer_info = MenuItem(3, "Photographer Info")
    transaction_info = MenuItem(4, "Transaction Info")

    def print_menu(self):
        if logged_in:
            self.sign_out.print_item()
        else:
            self.sign_in.print_item()
        
        self.photo_info.print_item()
        self.photographer_info.print_item()
        self.transaction_info.print_item()

    def check_selection(stdin):
        if stdin == self.sign_in.num and not logged_in:
            pass
        elif stdin == self.photo_info.num:
            photo_menu = PhotoMenu()
             

def get_input():
    stdin = input()

    return stdin

def check_logged_in():
    global logged_in, login_name
    if logged_in:
        print("-Logged in as-", login_name)
    else:
        print("-Not logged in-")

def menu():
   
    # check_logged_in()
    

    main_menu = MainMenu()
    photo_menu = PhotoMenu()
    

    while not quit:
        main_menu.print_menu()

        if main_menu.


        stdin = get_input()

    

def main():

    conn = qd.connect_to_database()

    menu()

    qd.disconnect_from_database(conn)
          
if __name__ == "__main__":
    main()