import os
from dotenv import load_dotenv

from attendance_manager import AttendanceManager


load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")


manager = AttendanceManager(
    MONGO_URI,
    "college_attendance"
)


# result = manager.add_student(
#     "Rahul Sharma",
#     "CS101",
#     "rahul@example.com",
#     "B.Tech CSE"
# )
# result = manager.add_attendance(
#     "CS101",
#     "2026-09-21",
#     "Present"
# )
manager.delete_student("CS101")



# print("Attendance:", result)
# print(result)