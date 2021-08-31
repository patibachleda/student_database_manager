import sqlite3


class DBManager:
    def __init__(self, db_path=""):
        # set up any necessary instance variables
        self._connection = sqlite3.connect("cse2050_students_db.db")
        self._cursor = self._connection.cursor()

    # Note that it is good practice to open and close connections every time you complete a transaction on a DB
    def open_connection(self):
        # create table
        self._cursor.execute('''CREATE TABLE IF NOT EXISTS Students
                     (student_id VARCHAR(50), first_name VARCHAR(50), last_name VARCHAR(50), 
                     email_address VARCHAR(50), admittance_year INTEGER, photo VARCHAR(200))''')
        self._connection.commit()

    def close_connection(self):
        self._connection.close()

    # This method is expected to create the table and load the initial data into the database
    def init_tables(self):
        # Remove old tables each time your app loads
        # (just for demonstration purposes and for this assignment; not applicable in the real world)
        sql_command = """
        DROP TABLE IF EXISTS Students
        """
        self._cursor.execute(sql_command)

    # adds the list provided into the six fields of database
    def add_record(self, record):
        # prepare the record for insertion into the DB
        try:
            self._cursor.execute(''' INSERT INTO Students VALUES(?,?,?,?,?,?)''', record)
            self._connection.commit()

        except Exception:
            raise Exception

    # using SELECT * FROM to find fields of student with specified student_id
    def search_by_id(self, student_id):
        # return a single record based on the given student id
        query = f"SELECT * FROM Students WHERE student_id LIKE '%{student_id}%'"
        self._cursor.execute(query)
        rows = self._cursor.fetchall()
        return rows

    # using SELECT * FROM to find fields of student with specified student_name
    def search_by_name(self, student_name):
        query = f"SELECT * FROM Students WHERE last_name LIKE '%{student_name}%' OR first_name LIKE '%{student_name}%'"
        self._cursor.execute(query)
        rows = self._cursor.fetchall()
        return rows

