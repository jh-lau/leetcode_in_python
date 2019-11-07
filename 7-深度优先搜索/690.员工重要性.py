"""
  User: Liujianhan
 """
__author__ = 'liujianhan'


class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    importance = 0

    def get_importance(self, employees, id):
        for emp in employees:
            if id == emp.id:
                self.importance += emp.importance
                if emp.subordinates:
                    for sub_id in emp.subordinates:
                        self.get_importance(employees, sub_id)
        return self.importance


if __name__ == '__main__':
    employee = []
    test = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
    for x in test:
        employee.append(Employee(*x))
    id = 1
    print(Solution().get_importance(employee, id))
