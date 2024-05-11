def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = [line.strip().split(',') for line in file.readlines()]
            total_salary = sum(int(salary) for _, salary in salaries)
            average_salary = total_salary / len(salaries)
            return total_salary, average_salary
    except FileNotFoundError:
        print("File not found.")
        return None, None
    except Exception as error_msg:
        print("An error occurred:", error_msg)
        return None, None


total, average = total_salary("C:/Users/br4vetrave1er/Desktop/projects/goit-algo-hw-04/text1.txt")
if total is not None and average is not None:
    print(f"Total salary: {total}, Average salary: {average}")

