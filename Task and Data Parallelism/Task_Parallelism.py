from concurrent.futures import ThreadPoolExecutor

employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

def compute_sss(salary):
    return salary * 0.045

def compute_philhealth(salary):
    return salary * 0.025

def compute_pagibig(salary):
    return salary * 0.02

def compute_tax(salary):
    return salary * 0.10


def compute_deductions(name, salary):
    with ThreadPoolExecutor() as executor:
        future_sss = executor.submit(compute_sss, salary)
        future_philhealth = executor.submit(compute_philhealth, salary)
        future_pagibig = executor.submit(compute_pagibig, salary)
        future_tax = executor.submit(compute_tax, salary)

        sss = future_sss.result()
        philhealth = future_philhealth.result()
        pagibig = future_pagibig.result()
        tax = future_tax.result()

    total_deductions = sss + philhealth + pagibig + tax
    net_salary = salary - total_deductions

    return {
        "Name": name,
        "Gross Salary": salary,
        "SSS": sss,
        "PhilHealth": philhealth,
        "Pag-IBIG": pagibig,
        "Tax": tax,
        "Net Salary": net_salary
    }

for name, salary in employees:
    result = compute_deductions(name, salary)
    print(result)
