import csv
import os

def read_grades(file_name):
    grades = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append({
                'Name': row['Name'],
                'Subject': row['Subject'],
                'Grade': int(row['Grade'])
            })
    return grades

def calculate_average_grades(grades):
    subject_totals = {}
    subject_counts = {}

    for entry in grades:
        subject = entry['Subject']
        grade = entry['Grade']
        
        if subject not in subject_totals:
            subject_totals[subject] = 0
            subject_counts[subject] = 0
        
        subject_totals[subject] += grade
        subject_counts[subject] += 1
    averages = {
        subject:subject_totals[subject] / subject_counts[subject]
        for subject in subject_totals
    }
    return averages

def write_average_grades(file_name, averages):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, avg in averages.items():
            writer.writerow([subject, avg])
            
if __name__ == '__main__':
    file_name = 'grades.csv'
    
    if not os.path.exists(file_name):
        with open(file_name,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Subject', 'Grade'])
            writer.writerows([
                ['Alice', 'Math', 85],
                ['Bob', 'Science', 78],
                ['Carol', 'Math', 92],
                ['Dave', 'History', 74]
            ])
        grades = read_grades(file_name)
        average_grades = calculate_average_grades(grades)
        write_average_grades('average_grades.csv', average_grades)



        

