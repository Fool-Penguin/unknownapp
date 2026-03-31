"""
Task 5: Equivalent Python Implementation of a Single Use Case.
Use Case Selected: Register for a Course (with pre-requisites and capacity checks).
"""
# This is a python implementation of the register course use case which
# is originated from the forked repository of the original java code.

class TimeSlot:
    def __init__(self, days, start, end):
        self.days = days
        self.start = start
        self.end = end

    def overlaps(self, other):
        if not self._share_days(self.days, other.days):
            return False
        
        start1 = self._to_minutes(self.start)
        end1 = self._to_minutes(self.end)
        start2 = self._to_minutes(other.start)
        end2 = self._to_minutes(other.end)

        return start1 < end2 and start2 < end1

    def _share_days(self, d1, d2):
        # A simpler/corrected day intersection check than the Java version
        valid_days = ["M", "T", "W", "Th", "F"]
        # Very simple check for demo purposes
        return any(day in d1 and day in d2 for day in valid_days)

    def _to_minutes(self, time_str):
        h, m = map(int, time_str.split(':'))
        return h * 60 + m

    def __str__(self):
        return f"{self.days} {self.start}-{self.end}"

class Course:
    def __init__(self, code, title, capacity, time_slot, prereqs=None):
        self.code = code
        self.title = title
        self.capacity = capacity
        self.time_slot = time_slot
        self.prerequisites = prereqs or []
        self.enrolled_students = []

    def is_full(self):
        return len(self.enrolled_students) >= self.capacity

    def __str__(self):
        return f"{self.code} - {self.title} (Seats: {self.capacity - len(self.enrolled_students)}/{self.capacity}) [{self.time_slot}]"

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled = []
        self.completed = []

# Mock Data Storage
courses = {
    "CS101": Course("CS101", "Intro to Programming", 30, TimeSlot("MWF", "09:00", "10:00")),
    "CS201": Course("CS201", "Data Structures", 2, TimeSlot("MWF", "10:00", "11:00"), prereqs=["CS101"]),
    "CS301": Course("CS301", "Algorithms", 25, TimeSlot("MWF", "09:00", "10:30"), prereqs=["CS201"]) # Overlaps CS101 deliberately
}

students = {
    "STU001": Student("STU001", "Alice"),
    "STU002": Student("STU002", "Bob (Needs CS101)")
}

# Pre-populate some states
students["STU001"].completed.append("CS101")
students["STU001"].enrolled.append("CS101")
courses["CS101"].enrolled_students.append("STU001")


def register_course(student_id, course_code):
    student = students.get(student_id)
    if not student:
        return False, "Student not found."

    course = courses.get(course_code)
    if not course:
        return False, "Course not found."
        
    if course_code in student.enrolled:
        return False, f"You are already enrolled in {course_code}."

    if course.is_full():
        return False, f"Course {course_code} is full."

    for prereq in course.prerequisites:
        if prereq not in student.completed:
            return False, f"Prerequisite not met: {prereq} required."

    for enrolled_code in student.enrolled:
        enrolled_course = courses.get(enrolled_code)
        if enrolled_course and course.time_slot.overlaps(enrolled_course.time_slot):
            return False, f"Time conflict with {enrolled_code}."

    student.enrolled.append(course_code)
    course.enrolled_students.append(student_id)
    return True, f"Successfully enrolled in {course_code}."

def main():
    print("=== Welcome to the Simplied Course Registration ===")
    
    student_id = input("Enter Student ID (STU001 or STU002): ").strip()
    if student_id not in students:
        print("Invalid student. Exiting.")
        return
        
    student = students[student_id]
    print(f"\nWelcome, {student.name}!")
    
    while True:
        print("\n--- Course Catalog ---")
        for c in courses.values():
            print(c)
            
        code = input("\nEnter course code to register (or 'exit' to quit): ").strip().upper()
        if code == 'EXIT' or code == '':
            break
            
        success, message = register_course(student_id, code)
        if success:
            print(f"[✓] {message}")
        else:
            print(f"[✗] {message}")

if __name__ == "__main__":
    main()
