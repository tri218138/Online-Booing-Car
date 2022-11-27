import pymysql.cursors

Database = pymysql.connect(
    host="localhost",
    user="root",
    password="280818",
    database="onlinebookingcar",
    cursorclass=pymysql.cursors.DictCursor
)
Cursor = Database.cursor()

# note to use 
# Database.commit()