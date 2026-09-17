# 9. Implement a class incorrectly first:
# • Attendance stored in a list
# • Exposed directly so any outside code can modify it
# Then redesign properly:
# • Make attendance private
# • Provide controlled methods for marking attendance only
# Explain the difference

class AttendanceBad:
    def __init__(self):
        self.attendance=[]
class AttendanceGood:
    def __init__(self):
        self.__attendance=[]
    def mark_present(self,student):
        self.__attendance.append(student)
    def get_attendance(self):
        return list(self.__attendance)
bad=AttendanceBad()
bad.attendance.append("Nikhil")
print(bad.attendance)
good=AttendanceGood()
good.mark_present("Nikhil")
print(good.get_attendance())