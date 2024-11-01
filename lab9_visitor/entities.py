from typing import  TYPE_CHECKING

if TYPE_CHECKING:
    from visitor import Visitor
class Worker:
    def __init__(self, position:str, salary:float):
        self.position = position
        self.salary = salary

class Department:
    def __init__(self, department_name: str, workers: list[Worker]):
        self.department_name = department_name
        self.workers = workers

    def report_salary(self, visitor):
        return visitor.report_workers(self)

class Company:
    def __init__(self, departments:list[Department]):
        self.departments = departments

    def report_salary(self, visitor):
        return visitor.report_department(self)








