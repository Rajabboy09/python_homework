import json
import csv
def load_tasks(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_name} not found")
        return
def save_tasks(file_name, tasks):
    with open(file_name, 'w') as f:
        json.dump(tasks, f, indent=4)

def display_tasks(tasks):
    print("\nTasks:")
    print(f"{'ID':<5}{'Task Name':<20}{'Completed':<12}{'Priority':<8}")
    print("-" * 50)
    for task in tasks:
        print(f"{task['id']:<5}{task['task']:<20}{task['completed']:<12}{task['priority']:<8}")

def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(task['completed'] for task in tasks)
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\nTask Completion Stats:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")

def convert_to_csv(tasks, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Task', 'Completed', 'Priority']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'ID': task['id'],
                'Task': task['task'],
                'Completed': task['completed'],
                'Priority': task['priority']
            })

    print(f"\nTasks have been successfully exported to {csv_filename}.")


if __name__ == "__main__":
    json_filename = 'tasks.json'
    csv_filename = 'tasks.csv'

    tasks = load_tasks(json_filename)


    display_tasks(tasks)


    calculate_stats(tasks)

   
    convert_to_csv(tasks, csv_filename)
