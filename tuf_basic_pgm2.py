
"""
Given marks of a student, print on the screen:

Grade A if marks >= 90
Grade B if marks >= 70
Grade C if marks >= 50
Grade D if marks >= 35
Fail, otherwise.
"""
class Solution:
    def studentGrade(self, marks):
        if marks>=90:
            print('GRADE A')
        elif marks>=70:
            print('GRADE B')
        elif marks>=50:
            print('GRADE C')
        elif marks>=35:
            print('GRADE D')
        else:
            print('FAIL')
student_instance=Solution()                            
student_instance.studentGrade(95)                            