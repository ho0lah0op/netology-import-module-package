from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employee


if __name__ == '__main__':
    print(datetime.now())
    get_employee()
    calculate_salary()
