import query_database as qd


logged_in = False
login_name = ""
quit = False

def print_menu():
    if logged_in:
        print("1 - sign out")
    else:
        print("1 - login")
    
    print("2 - List Photos not bought")

def check_input(stdin):
    global quit
    
    if stdin == "quit" or stdin == "exit" or stdin == "q":
        quit = True

def main_menu():
    global logged_in, login_name

    if logged_in:
        print("Logged in as", login_name)
    else:
        print("Not logged in")


    print_menu()

    stdin = input()

    check_input(stdin)

    

def main():

    # conn = qd.connect_to_database()

    while not quit:
        main_menu()

    # qd.disconnect_from_database(conn)
          
if __name__ == "__main__":
    main()