from pymongo import MongoClient


class AttendanceManager:

    def __init__(self, connection_string, database_name):

        self.client = MongoClient(connection_string)

        self.database = self.client[database_name]

        self.students = self.database["students"]

        self.attendance = self.database["attendance"]

    def add_student(self, name, roll_no, email, course):

      existing_student = self.students.find_one({
        "roll_no": roll_no
      })

      if existing_student:
        return "Student with this roll number already exists"

      student = {
          "name": name,
          "roll_no": roll_no,
          "email": email,
          "course": course
      }

      result = self.students.insert_one(student)

      return result.inserted_id

    def add_attendance(self, roll_no, date, status):

      student = self.students.find_one({
          "roll_no": roll_no
      })

      if not student:
          return "Student does not exist"

      if status not in ["Present", "Absent"]:
          return "Status must be Present or Absent"

      attendance_record = {
          "roll_no": roll_no,
          "date": date,
          "status": status
      }

      result = self.attendance.insert_one(attendance_record)

      return result.inserted_id

    def get_all_attendance(self):

      records = self.attendance.find()

      return list(records)

    def delete_student(self, roll_no):

      student = self.students.find_one({
          "roll_no": roll_no
      })

      if not student:
          return "Student does not exist"

      result = self.students.delete_one({
          "roll_no": roll_no
      })

      if result.deleted_count == 1:
          return "Student deleted successfully"

      return "Student could not be deleted"