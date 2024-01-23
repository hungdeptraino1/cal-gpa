name = str(input('Enter your name: '))
def calculate_gpa(component_scores):
    total_credits = 0
    weighted_sum = 0
    
    for i in component_scores:
        grade = i[0]
        credits = i[1]
        
        if not isinstance(grade, (int, float)) or not isinstance(credits, (int, float)):
            raise ValueError("The number of subjects and credits must be natural numbers and your score must be a number!")
        
        total_credits += credits
        weighted_sum += grade * credits
    
    if total_credits == 0:
        raise ZeroDivisionError("Total credits cannot be zero.")
    
    gpa = weighted_sum / total_credits
    return gpa


def print_gpa(gpa):
    print(f"Your GPA is: {gpa:.2f}")


def main():
    try:
        component_scores = []
        
        num_subject = int(input("Enter the number of subjects: "))
        
        for i in range(num_subject):
            grade = float(input(f'Enter the grade of the subject {i+1}: '))
            credits = float(input(f'Enter the number of credits of the {i+1} subject: '))
            component_scores.append((grade, credits))
        
        gpa = calculate_gpa(component_scores)
        print_gpa(gpa)
        result=[f'Name: {name}',f'grade and credits: {component_scores}',f'Gpa: {gpa}']
        with open("F:/bai tap/asmpython/asmpython.txt",'w') as f:
            f.write(f'{result}')
    except ValueError:
        print(f"Error")
    
    except ZeroDivisionError :
        print(f"Error")
main()





