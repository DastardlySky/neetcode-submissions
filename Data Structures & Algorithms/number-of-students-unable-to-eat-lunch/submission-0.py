class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for i in range(1000):
            if len(students) > 0 and sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
            elif len(students) > 0:
                front_student = students.pop(0)
                students.append(front_student)

        return len(students)