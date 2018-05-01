from mysql.connector import Error, MySQLConnection
from database_config_parser import read_db_config

class Database():
    def __init__(self, user='root', password='Halo2014', host='localhost', database='test'):
        try:
            self.conn = MySQLConnection(user=user, password=password, host=host, database=database)
            if not self.conn.is_connected():
                print("Database connection failed")
            else:
                print("Connected to Database")
        except Error as error:
            print(error)
        
    
    def execute_query(self, query, args):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, args)
            self.conn.commit()

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')

        except Error as e:
            self.conn.rollback()      
            print(e)
        finally:
            cursor.close()

    def insert_photo(self, speed, film, f_stop, color_bw, resolution, price, date, trans_id, pname, pbdate):
        
        query = """INSERT INTO Photo(Speed, Film, F-Stop, ColorB&W, Resolution, Price, Date, TransID, PName, PBDate) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        args = (speed, film, f_stop, color_bw, resolution, price, date, trans_id, pname, pbdate)

        self.execute_query(query, args)

    def insert_landscape(self, photo_id, place, country):
        
        query = """INSERT INTO Landscape(PhotoID, Place, Country) 
        VALUES(%s, %s, %s)"""

        args = (photo_id, place, country)

        self.execute_query(query, args)

    def insert_location(self, place, country, description):
        
        query = """INSERT INTO Location(Place, Country, Description) 
        VALUES(%s, %s, %s)"""

        args = (place, country, description)

        self.execute_query(query, args)
    
    def insert_abstract(self, photo_id, comment):
        
        query = """INSERT INTO Abstract(PhotoID, Comment) 
        VALUES(%s, %s)"""

        args = (photo_id, comment)

        self.execute_query(query, args)

    def insert_models(self, photo_id, mname, mbdate, agency):
        
        query = """INSERT INTO Models(PhotoID, MName, MBDate, Agency) 
        VALUES(%s, %s, %s, %s)"""

        args = (photo_id, mname, mbdate, agency)

        self.execute_query(query, args)
    
    def insert_model(self, mname, mbdate, mbio, msex):
        
        query = """INSERT INTO Model(MName, MBDate, MBio, MSex) 
        VALUES(%s, %s, %s, %s)"""

        args = (mname, mbdate, mbio, msex)

        self.execute_query(query, args)
    
    def insert_photographer(self, pname, pbdate, pbio, paddress, color_bw, pnationality):
        
        query = """INSERT INTO Photographer(PName, PBDate, PBio, PAddress, Color/B&W, PNationality)
        VALUES(%s, %s, %s, %s, %s, %s)"""

        args = (pname, pbdate, pbio, paddress, color_bw, pnationality)

        self.execute_query(query, args)

    def insert_influences(self, epname, epbdate, rpname, rpbdate):
        
        query = """INSERT INTO Influences(EPName, EPBDate, RPName, RPBDate)
        VALUES(%s, %s, %s, %s)"""

        args = (epname, epbdate, rpname, rpbdate)

        self.execute_query(query, args)
    
    def insert_transaction(self, tdate, card_no, card_type, card_exp_date, total_amount, login_name):
        
        query = """INSERT INTO Transaction(TDate, CardNo, CardType, CardExpDate, TotalAmount, LoginName)
        VALUES(%s, %s, %s, %s, %s, %s)"""

        args = (tdate, card_no, card_type, card_exp_date, total_amount, login_name)

        self.execute_query(query, args)
    

    def insert_customer(self, login_name, password, cname, ctype, billing_address, str1, str2, city, state, zip):
        
        query = """INSERT INTO Customer(LoginName, Password, CName, CType, BillingAddress, Str1, Str2, City, State, Zip) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        args = (login_name, password, cname, ctype, billing_address, str1, str2, city, state, zip)

        self.execute_query(query, args)
    


    # def iter_row(self, cursor, size=10):
    #     while True:
    #         rows = cursor.fetchmany(size)
    #         if not rows:
    #             break
    #         for row in rows:
    #             yield row

    def disconnect(self):
        self.conn.close()



def main():
    db = Database()
    print(db)
    db.insert_customer("crozario", "password", "Crossley Rozario", "new", "1 Magnolia Ave, Jersey City, NJ, 07306", "1 Magnolia Ave", "None", "Jersey City", "NJ", "07306" )
    # db.insert_photo("1/60", "35mm", "f2.0", "Color", "3840x2160", "$50.00", "2016-04-02", None, None, None)

if __name__ == "__main__":
    main()