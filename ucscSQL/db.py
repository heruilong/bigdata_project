import MySQLdb
import time

class WebDB:
        def __init__(self):
                self.connectDB()
        def connectDB(self):
                # Open database connection
                self.db = MySQLdb.connect("genome-mysql.cse.ucsc.edu","genomep","password","ailMel1")

        def disconnDB(self):
                if self.db==None: return
                # disconnect from server
                self.db.close()

        def select(self):
                if self.db==None: return
		# prepare a cursor object using cursor() method
		cursor = db.cursor()

		# execute SQL query using execute() method.
		cursor.execute("SELECT VERSION()")

		# Fetch a single row using fetchone() method.
		data = cursor.fetchone()

		print "Database version : %s " % data

		# disconnect from server
		db.close()
webDB=WebDB()
webDB.select()
