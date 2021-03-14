import os
import sqlite3

class bodDB():
    def __init__(self):
        self.createDB
        self.deleteDB
        self.add2DB
    
    def createDB(self):
        try:
            # Create file
            if not os.path.exists('../data/bods.db'):
                os.mknod('../data/bods.db')
            
            # Connect to 'file'
            con = sqlite3.connect('../data/bods.db')
            cur = con.cursor()

            # Create table
            cur.execute('''CREATE TABLE bods (id, qty, exc, typ, mat, name) ''')
            return('Database created')
        except:
            return('Database already exists')
    
    def deleteDB(self):
        try:
            os.remove('../data/bods.db')
            return('Database deleted')
        except:
            return('No database found')
    
    def add2DB(self):
        print ("Add to DB")
