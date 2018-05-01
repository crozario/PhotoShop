import query_database as qd

logged_in = False
login_name = ""
quit = False

class MenuItem():
    def __init__(self, num, item):
        self.num = num
        self.item = item
    
    def print_item(self):
        print("{} - {}".format(self.num, self.item))


# class PhotographerMenu():
#     list_influenced_photographers = MenuItem(1, )

class ComputeSalesMenu():
    list_total_sales_per_customer = MenuItem(1, "List total sales per customer")
    list_total_sales_per_photographer = MenuItem(2, "List total sales per photographer")
    list_total_sales_by_photo_type = MenuItem(3, "List total sales by photo type")
    go_back = MenuItem(4, "Go Back")
    quit_application = MenuItem(5, "Quit Application")

    def print_menu(self):
        self.list_total_sales_per_customer.print_item()
        self.list_total_sales_per_photographer.print_item()
        self.list_total_sales_by_photo_type.print_item()
        self.go_back.print_item()
        self.quit_application.print_item()


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
    model_info = MenuItem(5, "Model Info")
    compute_sales = MenuItem(6, "Compute Sales")
    quit_application = MenuItem(7, "Quit Application")
    

    def print_menu(self):
        if logged_in:
            self.sign_out.print_item()
        else:
            self.sign_in.print_item()
        
        self.photo_info.print_item()
        self.photographer_info.print_item()
        self.transaction_info.print_item()
        self.model_info.print_item()
        self.compute_sales.print_item()
        self.quit_application.print_item()

             

def get_input():
    print("* - Choose a Number for an action:", end=' ')
    stdin = input()

    return int(stdin)

def check_logged_in():
    global logged_in, login_name
    if logged_in:
        print("* - Logged in as:", login_name)
    else:
        print("* - Not logged in")

def menu():
    global quit
   
    # check_logged_in()
    

    main_menu = MainMenu()
    photo_menu = PhotoMenu()
    compute_sales_menu = ComputeSalesMenu()

    while quit == False:
        check_logged_in()
        main_menu.print_menu()

        stdin = get_input()

        if stdin == main_menu.sign_in.num and not logged_in:
            pass
        elif stdin == main_menu.sign_out.num and logged_in:
            pass
        elif stdin == main_menu.photo_info.num:
            pass
        elif stdin == main_menu.photographer_info.num:
            pass
        elif stdin == main_menu.transaction_info.num:
            pass
        elif stdin == main_menu.model_info.num:
            pass
        elif stdin == main_menu.compute_sales.num:
            print("hello")
            compute_sales_menu.print_menu()

            stdin = get_input()

            while not quit or not stdin == compute_sales_menu.go_back:
                compute_sales_menu.print_menu()
        elif stdin == main_menu.quit_application.num:
            quit = True
        else:
            continue

    

def main():

    conn = qd.connect_to_database()

    menu()

    print("Goodbye")

    qd.disconnect_from_database(conn)
          
if __name__ == "__main__":
    main()