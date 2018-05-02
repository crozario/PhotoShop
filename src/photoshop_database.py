from mysql.connector import Error, MySQLConnection
from database_config_parser import read_db_config

class PhotoShopDatabase():
    def __init__(self, user='root', password='Halo2014', host='localhost', database='test'):
        try:
            self.conn = MySQLConnection(user=user, password=password, host=host, database=database)
            if not self.conn.is_connected():
                print("Database connection failed")
            else:
                print("Connected to Database")
        except Error as error:
            print(error)
    
    def disconnect(self):
        self.conn.close()

    def iter_row(self, cursor, size=10):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row
    
    # Customer Menu
    
    def list_customers(self):
        try:
            cursor = self.conn.cursor()
            query = """ SELECT * FROM Customer; """
            cursor.execute(query)
            print("*RESULTS*")
            for row in self.iter_row(cursor, 10):
                print(row)
            print("*RESULTS*")
        except Error as e:
            print("list_customrer failed")
            print(e)
        finally:
            cursor.close()
        
    def list_customers_that_spent_more_than_hundred(self):
        try:
            cursor = self.conn.cursor()
            query = """ SELECT * FROM Photographer; """
            cursor.execute(query)
            print("*RESULTS*")
            for row in self.iter_row(cursor, 10):
                print(row)
            print("*RESULTS*")
        except Error as e:
            print("list_photographers failed")
            print(e)
        finally:
            cursor.close()
        

    # Photographer Menu

    def list_photographers(self):
        try:
            cursor = self.conn.cursor()
            query = """ SELECT * FROM Photographer; """
            cursor.execute(query)
            print("*RESULTS*")
            for row in self.iter_row(cursor, 10):
                print(row)
            print("*RESULTS*")
        except Error as e:
            print("list_photographers failed")
            print(e)
        finally:
            cursor.close()

    # Transaction Menu

    # Model Menu

    def list_models(self):
        try:
            cursor = self.conn.cursor()
            query = """ SELECT * FROM MODEL; """
            cursor.execute(query)
            print("*RESULTS*")
            for row in self.iter_row(cursor, 10):
                print(row)
            print("*RESULTS*")
        except Error as e:
            print("list_models failed")
            print(e)
        finally:
            cursor.close()

    # Compute Sales Menu

    # Photo Menu

    def list_all_photos(self):
        try:
            cursor = self.conn.cursor()
            query = """ SELECT * FROM Photo; """
            cursor.execute(query)
            print("*RESULTS*")
            for row in self.iter_row(cursor, 10):
                print(row)
            print("*RESULTS*")
        except Error as e:
            print("list_all_photos failed")
            print(e)
        finally:
            cursor.close()

    def list_photos_bought(self):
        try:
            cursor = self.conn.cursor()
            query = """ SELECT * FROM Photo WHERE TransID IS NOT NULL;"""
            cursor.execute(query)
            print("*RESULTS*")
            for row in self.iter_row(cursor, 10):
                print(row)
            print("*RESULTS*")
        except Error as e:
            print("list_all_photos failed")
            print(e)
        finally:
            cursor.close()

    def list_photos_not_bought(self):
        try:
            cursor = self.conn.cursor()
            query = """ SELECT * FROM Photo WHERE TransID IS NULL; """
            cursor.execute(query)
            print("*RESULTS*")
            for row in self.iter_row(cursor, 10):
                print(row)
            print("*RESULTS*")
        except Error as e:
            print("list_all_photos failed")
            print(e)
        finally:
            cursor.close()

    def delete_photo(self, photo_id):
        try:
            cursor = self.conn.cursor()
            query = """ DELETE FROM Photo WHERE PhotoID = %s; 
            """
            cursor.execute(query, (photo_id,))
            self.conn.commit()
            print("*RESULTS*")
            print("Photo deleted")
            print("*RESULTS*")
        except Error as e:
            print("delete_photo failed")
            print(e)
        finally:
            cursor.close()


    


    
    


    def execute_query(self, query, args):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, args)
            self.conn.commit()

            print("Added to Database")

        except Error as e:
            self.conn.rollback()      
            print(e)
        finally:
            cursor.close()

    def insert_photo(self, speed, film, f_stop, color_bw, resolution, price, date, trans_id, pname, pbdate):
        
        query = """INSERT INTO `Photo`(Speed, Film, F-Stop, Color/B&W, Resolution, Price, Date, TransID, PName, PBDate) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

        args = (speed, film, f_stop, color_bw, resolution, price, date, trans_id, pname, pbdate)

        self.execute_query(query, args)

    def insert_landscape(self, photo_id, place, country):
        
        query = """INSERT INTO `Landscape`(PhotoID, Place, Country) 
        VALUES(%s, %s, %s);"""

        args = (photo_id, place, country)

        self.execute_query(query, args)

    def insert_location(self, place, country, description):
        
        query = """INSERT INTO `Location`(Place, Country, Description) 
        VALUES(%s, %s, %s)"""

        args = (place, country, description)

        self.execute_query(query, args)
    
    def insert_abstract(self, photo_id, comment):
        
        query = """INSERT INTO `Abstract`(PhotoID, Comment) 
        VALUES(%s, %s)"""

        args = (photo_id, comment)

        self.execute_query(query, args)

    def insert_models(self, photo_id, mname, mbdate, agency):
        
        query = """INSERT INTO `Models`(PhotoID, MName, MBDate, Agency) 
        VALUES(%s, %s, %s, %s);"""

        args = (photo_id, mname, mbdate, agency)

        self.execute_query(query, args)
    
    def insert_model(self, mname, mbdate, mbio, msex):
        
        query = """INSERT INTO `Model`(MName, MBDate, MBio, MSex) 
        VALUES(%s, %s, %s, %s);"""

        args = (mname, mbdate, mbio, msex)

        self.execute_query(query, args)
    
    def insert_photographer(self, pname, pbdate, pbio, paddress, pnationality):
        
        query = """INSERT INTO `Photographer`(PName, PBDate, PBio, PAddress, PNationality)
        VALUES(%s, %s, %s, %s, %s);"""

        args = (pname, pbdate, pbio, paddress, pnationality)

        self.execute_query(query, args)

    def insert_influences(self, epname, epbdate, rpname, rpbdate):
        
        query = """INSERT INTO `Influences`(EPName, EPBDate, RPName, RPBDate)
        VALUES(%s, %s, %s, %s);"""

        args = (epname, epbdate, rpname, rpbdate)

        self.execute_query(query, args)
    
    def insert_transaction(self, trans_id, tdate, card_no, card_type, card_exp_date, total_amount, login_name):
        
        query = """INSERT INTO `Transaction`(TransID, TDate, CardNo, CardType, CardExpDate, TotalAmount, LoginName)
        VALUES(%s, %s, %s, %s, %s, %s, %s)"""

        args = (trans_id, tdate, card_no, card_type, card_exp_date, total_amount, login_name)

        self.execute_query(query, args)
    

    def insert_customer(self, login_name, password, cname, ctype, billing_address, str1, str2, city, state, zip):
        
        query = """INSERT INTO `Customer`(LoginName, Password, CName, CType, BillingAddress, Str1, Str2, City, State, Zip) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

        args = (login_name, password, cname, ctype, billing_address, str1, str2, city, state, zip)

        self.execute_query(query, args)
    

    

    