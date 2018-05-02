import photoshop_database as pd

logged_in = False
login_name = ""
quit = False
count = 0
db = pd.PhotoShopDatabase()


class MenuItem():
    def __init__(self, num, item):
        self.num = num
        self.item = item
    
    def print_item(self):
        print("{} - {}".format(self.num, self.item))


class CustomerMenu():
    list_customers = MenuItem(1, "List customers")
    list_customers_that_spent_more_than_hundred = MenuItem(1, "List customers who spent more than $100")
    list_customers_who_bought_all_portraits_with_model = MenuItem(2, "List customers who bought portraits with specific model")
    go_back = MenuItem(3, "Go Back")
    quit_application = MenuItem(4, "Quit Application")

    def print_menu(self):
        self.list_customers.print_item()
        self.list_customers_that_spent_more_than_hundred.print_item()
        self.list_customers_who_bought_all_portraits_with_model.print_item()
        self.go_back.print_item()
        self.quit_application.print_item()


class PhotographerMenu():
    list_photographers = MenuItem(1, "List photographers")
    list_influenced_photographers_in_usa = MenuItem(2, "List photographers influenced in US")
    list_photographers_only_took_portrait = MenuItem(3, "List photographers only took portrait photos")
    update_photographer_name_of_photo = MenuItem(4, "Update photographer name of photo")
    rank_photographer_by_total_photo_cost = MenuItem(5, "Rank photographers by total prices of photos taken")
    go_back = MenuItem(5, "Go Back")
    quit_application = MenuItem(6, "Quit Application")

    def print_menu(self):
        self.list_photographers.print_item()
        self.list_influenced_photographers_in_usa.print_item()
        self.list_photographers_only_took_portrait.print_item()
        self.update_photographer_name_of_photo.print_item()
        self.go_back.print_item()
        self.quit_application.print_item()

class TransactionsMenu():
    list_transaction_with_more_than_three_photos = MenuItem(1, "List transactions which contains more than 3 photos")
    go_back = MenuItem(2, "Go Back")
    quit_application = MenuItem(3, "Quit Application")

    def print_menu(self):
        self.list_transaction_with_more_than_three_photos.print_item()
        self.go_back.print_item()
        self.quit_application.print_item()

class ModelMenu():
    list_models = MenuItem(1, "List model names")
    list_models_who_modeled_all_photos_for_photographer = MenuItem(2, "List models who modeled in all photos taken by photographer")
    go_back = MenuItem(3, "Go Back")
    quit_application = MenuItem(4, "Quit Application")

    def print_menu(self):
        self.list_models.print_item()
        self.list_models_who_modeled_all_photos_for_photographer.print_item()
        self.go_back.print_item()
        self.quit_application.print_item()

class ComputeSalesMenu():
    list_total_sales_per_customer = MenuItem(1, "List total sales per customer")
    list_total_sales_per_photographer = MenuItem(2, "List total sales per photographer")
    list_total_sales_by_photo_type = MenuItem(3, "List total sales by photo type")
    compute_top_n_dates = MenuItem(4, "Compute top n dates")
    go_back = MenuItem(5, "Go Back")
    quit_application = MenuItem(6, "Quit Application")

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
    delete_photo = MenuItem(4, "Delete Photo")
    go_back = MenuItem(5, "Go Back")
    quit_application = MenuItem(6, "Quit Application")

    def print_menu(self):
        self.list_all_photos.print_item()
        self.list_photos_bought.print_item()
        self.list_photos_not_bought.print_item()
        self.delete_photo.print_item()
        self.go_back.print_item()
        self.quit_application.print_item()


   
class MainMenu():
    sign_in = MenuItem(1, "Sign In")
    sign_out = MenuItem(1, "Sign Out")
    photo_info = MenuItem(2, "Photo Info")
    photographer_info = MenuItem(3, "Photographer Info")
    transaction_info = MenuItem(4, "Transaction Info")
    model_info = MenuItem(5, "Model Info")
    customer_info = MenuItem(6, "Customer Info")
    compute_sales = MenuItem(7, "Compute Sales")
    quit_application = MenuItem(8, "Quit Application")
    

    def print_menu(self):
        if logged_in:
            self.sign_out.print_item()
        else:
            self.sign_in.print_item()
        
        self.photo_info.print_item()
        self.photographer_info.print_item()
        self.transaction_info.print_item()
        self.model_info.print_item()
        self.customer_info.print_item()
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

def print_separator():
    global count
    num = 50
    if count % 2 == 0:
        print("*" * num)
    else:
        print("-" * num)

    count += 1

def menu():
    global quit
    
    # menus
    main_menu = MainMenu()
    photo_menu = PhotoMenu()
    photographer_menu = PhotographerMenu()
    transaction_menu = TransactionsMenu()
    model_menu = ModelMenu()
    customer_menu = CustomerMenu()
    compute_sales_menu = ComputeSalesMenu()


    while quit == False:
        print_separator()
        check_logged_in()
        main_menu.print_menu()

        stdin = get_input()

        if stdin == main_menu.sign_in.num and not logged_in:
            if quit == True:
                break
            print_separator()
            print("*IN SIGN IN MENU*")
        elif stdin == main_menu.sign_out.num and logged_in:
            if quit == True:
                break
            print_separator()
            print("*IN SIGN OUT MENU*")
        elif stdin == main_menu.photo_info.num:
            if quit == True:
                break
            print_separator()
            print("*IN PHOTO INFO MENU*")

            while quit == False:
                photo_menu.print_menu()
                stdin = get_input()          

                if photo_menu.list_all_photos.num == stdin:
                    db.list_all_photos()
                elif photo_menu.list_photos_bought.num == stdin:
                    db.list_photos_bought()
                elif photo_menu.list_photos_not_bought.num  == stdin:
                    db.list_photos_not_bought()
                elif photo_menu.delete_photo.num == stdin:
                    print("What is the PhotoID")
                    photo_id = int(input())
                    db.delete_photo(photo_id)
                elif photo_menu.go_back.num == stdin:
                    break
                elif photo_menu.quit_application.num == stdin:
                    quit = True
                else:
                    continue

        elif stdin == main_menu.photographer_info.num:
            if quit == True:
                break
            print_separator()
            print("*IN PHOTOGRAPHER INFO MENU*")

            while quit == False:
                photographer_menu.print_menu()
                stdin = get_input()          
                if photographer_menu.list_photographers.num == stdin:
                    db.list_photographers()
                elif photographer_menu.list_influenced_photographers_in_usa.num == stdin:
                    # stdin = input()
                    pass
                elif photographer_menu.list_photographers_only_took_portrait.num == stdin:
                    pass
                elif photographer_menu.update_photographer_name_of_photo.num  == stdin:
                    pass
                elif photographer_menu.rank_photographer_by_total_photo_cost.num == stdin:
                    break
                elif photographer_menu.go_back.num == stdin:
                    break
                elif photographer_menu.quit_application.num == stdin:
                    quit = True
                else:
                    continue

        elif stdin == main_menu.transaction_info.num:
            if quit == True:
                break
            print_separator()
            print("*IN TRANSACTION INFO MENU*")

            while quit == False:
                transaction_menu.print_menu()
                stdin = get_input()          

                if transaction_menu.list_transaction_with_more_than_three_photos.num == stdin:
                    pass
                elif transaction_menu.go_back.num == stdin:
                    break
                elif transaction_menu.quit_application.num == stdin:
                    quit = True
                else:
                    continue

        elif stdin == main_menu.model_info.num:
            if quit == True:
                break
            print_separator()
            print("*IN MODEL INFO MENU*")

            while quit == False:
                model_menu.print_menu()
                stdin = get_input()

                if model_menu.list_models.num == stdin:
                    db.list_models()
                if model_menu.list_models_who_modeled_all_photos_for_photographer.num == stdin:
                    pass
                elif model_menu.go_back.num == stdin:
                    break
                elif model_menu.quit_application.num == stdin:
                    quit = True
                else:
                    continue

            
        elif stdin == main_menu.customer_info.num:
            if quit == True:
                break
            print_separator()
            print("*IN CUSTOMER INFO MENU*")

            while quit == False:
                customer_menu.print_menu()
                stdin = get_input()          
                if customer_menu.list_customers.num == stdin:
                    db.list_customers()
                elif customer_menu.list_customers_that_spent_more_than_hundred.num == stdin:
                    pass
                elif customer_menu.list_customers_who_bought_all_portraits_with_model.num == stdin:
                    pass
                elif customer_menu.go_back.num == stdin:
                    break
                elif customer_menu.quit_application.num == stdin:
                    quit = True
                else:
                    continue

        elif stdin == main_menu.compute_sales.num:
            if quit == True:
                break
            print_separator()
            print("*IN COMPUTE SALES MENU*")

            while quit == False:
                compute_sales_menu.print_menu()           
                stdin = get_input()

                if compute_sales_menu.list_total_sales_per_customer.num == stdin:
                    pass
                elif compute_sales_menu.list_total_sales_per_photographer.num == stdin:
                    pass
                elif compute_sales_menu.list_total_sales_by_photo_type.num == stdin:
                    pass
                elif compute_sales_menu.go_back.num == stdin:
                    break
                elif compute_sales_menu.quit_application.num == stdin:
                    quit = True
                else:
                    continue

        elif stdin == main_menu.quit_application.num:
            quit = True
        else:
            continue

    

def main():

    

    menu()
    
    print_separator()
    print("Goodbye")

    db.disconnect()
          
if __name__ == "__main__":
    main()