from photoshop_database import *
    
def main():
    db = PhotoShopDatabase()
    print(db)
    db.insert_customer("crozario", "password", "Crossley Rozario", "new", "1 Magnolia Ave, Jersey City, NJ, 07306", "1 Magnolia Ave", "None", "Jersey City", "NJ", "07306" )
    # db.insert_photo("1/60", "35mm", "f2.0", "Color", "3840x2160", "$50.00", "2016-04-02", None, None, None)

    db.disconnect()

if __name__ == "__main__":
    main()