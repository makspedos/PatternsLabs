from entities import Company, Department
class Visitor:
    def report_workers(self, department:Department)->str:
        pass
    def report_department(self, company:Company)->str:
        pass

class ReportVisitor(Visitor):
    def report_workers(self, department:Department)->str:
        workers_salary = f'Report {department.department_name}\n'
        for worker in department.workers:
            workers_salary+= f'Position: {worker.position}, salary: {worker.salary}\n'
        return workers_salary

    def report_department(self, company:Company)->str:
        department_salary = 'Company report\n'
        i = 1
        for department in company.departments:
            workers_salary = ''
            for worker in department.workers:
                workers_salary += f'Position: {worker.position}, salary: {worker.salary}\n'
            department_salary+=f'{i} Report {department.department_name}:\n{workers_salary}\n'
            i+=1
        return department_salary



