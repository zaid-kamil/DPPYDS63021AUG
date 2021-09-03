# required parameter : base salary
def salary_calc(base_salary):
    if base_salary < 5000:
        return base_salary * 1.05
    elif base_salary > 5000 and base_salary < 10000:
        return base_salary * 2.05
    elif base_salary > 10000 and base_salary < 15000:
        return base_salary * 3.05
    else:
        return base_salary * 4.05

print(salary_calc(3000))
print(salary_calc(5000))
print(salary_calc(12310))
# print(salary_calc())
# print(salary_calc(1,2,3))
