import db_manager


class StudentAccount:
    # class variable
    _last_assigned_number = 90188000

    # The constructor that initializes the instance variables such as photo, id, names, email, etc.
    def __init__(self, first_name, last_name, admittance_year):
        self._first_name = first_name
        self._last_name = last_name
        self._admittance_year = admittance_year
        self._email = first_name[0].lower() + last_name.lower() + str(admittance_year) + "@my.fit.edu"
        StudentAccount._last_assigned_number = StudentAccount._last_assigned_number + 1
        self._id = StudentAccount._last_assigned_number
        self._data = []
        self.set_photo(self._first_name+" "+self._last_name)
        self.populate_record(self._id, self._first_name, self._last_name, self._email, self._admittance_year, self._photo)

    # initializes the instance variables (example, from DB data fetched using the DBManager)
    def populate_record(self, sid, first_name, last_name, email, admittance_year, photo):
        self._data.append(sid)
        self._data.append(first_name)
        self._data.append(last_name)
        self._data.append(email)
        self._data.append(admittance_year)
        self._data.append(photo)
        db = db_manager.DBManager()
        db.open_connection()
        db.add_record(self._data)
        db.close_connection()

    # Returns a student record (example, as a tuple)
    def get_record(self):
        return self._first_name, self._last_name, self._admittance_year, self._email, self._photo

    # checks if a photo exists for person and assigns them their photo, otherwise assigns male_silhouette.png
    def set_photo(self, photo):
        names = ["Willena Shupe", "Jolanda Agin", "Leta Stacker", "Leonora Oliverio", "Birgit Stoudt", "Aron Valtierra",
                 "Vi Buschman", "Janee Barnwell", "Agnus Flower", "Byron Mccartney", "Victoria Crabill", "Amy Swinton",
                 "Arla Mohamed", "Bryon Vester", "Lue Benway", "Mozelle Macauley", "Suzann Galindo", "Delicia Barriere",
                 "Marcella Uyehara", "Jane Curley"]
        if photo in names:
            self._photo = self._first_name+"_"+self._last_name+"_"+str(self._id)+".png"
        else:
            self._photo = "male_silhouette.png"

