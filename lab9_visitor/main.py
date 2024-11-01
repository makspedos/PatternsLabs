from entities import Company, Department, Worker
from visitor import ReportVisitor


if __name__ == '__main__':
    visitor = ReportVisitor()

    worker_1 = Worker(position='UX/UI designer', salary=30000)
    worker_2 = Worker(position='Frontend developer', salary=40000)
    department_1 = Department(department_name='Website department', workers=[worker_1, worker_2])
    print(department_1.report_salary(visitor))

    worker_3 = Worker(position='Data scientist', salary=40000)
    worker_4 = Worker(position='Machine learning engineer', salary=60000)
    department_2 = Department(department_name='AI department', workers=[worker_3, worker_4])

    company = Company(departments=[department_1, department_2])
    print(company.report_salary(visitor))

