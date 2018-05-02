import photoshop_database as pd
    
def main():
    db = pd.PhotoShopDatabase()
    print(db)
    # db.insert_photo("1/60", "35mm", "f2.0", "Color", "3840x2160", 50.00, "2016-04-02", None, "Jake", "1990-02-01") #NOT WORKING
    # db.insert_photographer("John", "1990-08-01", "hello my name is john", "1 washington street", "American")
    # db.insert_photographer("Jake", "1991-02-04", "hello my name is jake", "1 jefferson street", "American")
    # db.insert_influences("John", "1990-08-01", "Jake", "1991-02-04")
    db.insert_models(1, "Jane", "1980-10-02", "VS")
    db.insert_model("Jane", "1980-10-02", "Hello my name is jane", "F")
    db.insert_model("Mary", "1988-11-04", "Hi, im Mary", "F")
    # db.insert_landscape(1, "New Jersey", "USA")
    # db.insert_location("New Jersey", "USA", "Location is NJ")
    # db.insert_abstract(1, "This is an abstract")
    # db.insert_transaction(1, "2015-10-04", 123456 , "Discover", "2019-10-03", 132.00, "crozario")


     # Customers
    # db.insert_customer("crozario", "password", "Crossley Rozario", "new", "1 Magnolia Ave, Jersey City, NJ, 07306", "1 Magnolia Ave", "None", "Jersey City", "NJ", "07306" )
    # db.insert_customer("jj", "password", "John J", "new", "1 Magnolia Ave, Jersey City, NJ, 07306", "1 Magnolia Ave", "None", "Jersey City", "NJ", "07306" )
    # db.insert_customer("ll", "password", "Linda L", "new", "1 Magnolia Ave, Jersey City, NJ, 07306", "1 Magnolia Ave", "None", "Jersey City", "NJ", "07306" )
    
    # Transactions
    # db.insert_transaction(12, "2015-10-04", 123456 , "Discover", "2019-10-03", 132.00, "crozario")
    # db.insert_transaction(2, "2015-11-04", 123456 , "Discover", "2019-10-03", 52.00, "jj")
    # db.insert_transaction(3, "2015-01-04", 123456 , "Discover", "2019-10-03", 51.00, "ll")
    # db.insert_transaction(4, "2015-02-04", 123456 , "Discover", "2019-10-03", 56.00, "ll")




    db.disconnect()

if __name__ == "__main__":
    main()