# universities = [
#     ['California Institute of Technology', 2175, 37704],
#     ['Harvard', 19627, 39849],
#     ['Massachusetts Institute of Technology', 10566, 40732],
#     ['Princeton', 7802, 37000],
#     ['Rice', 5879, 35551],
#     ['Stanford', 19535, 40569],
#     ['Yale', 11701, 40500]
# ]
N = int(input("Nechta qator kiritasiz: "))
universities = []

for _ in range(N):
    user_input = input("Enter: ")
    words = [word.strip() for word in user_input.split(',')]
    for i in range(1,3):
        words[i] = int(words[i])
    universities.append(words)

def enrollment_stats(list_of_unv):
    T_s = []
    T_t = []
    for i in list_of_unv:
        T_s.append(i[1])
        T_t.append(i[2])
    return T_s, T_t
def mean(val):
    return sum(val) / len(val)

def median(val):
    sorted_val = sorted(val)
    n = len(sorted_val)
    mid = n//2
    if n%2 == 0:
        return (sorted_val[mid-1]+sorted_val[mid])/2
    else:
        return sorted_val[mid]
    
student_enrollments,tuition_fees = enrollment_stats(universities)

total_students = sum(student_enrollments)
total_tuition = sum(tuition_fees)

student_mean = mean(student_enrollments)
student_median = median(student_enrollments)

tuition_mean = mean(tuition_fees)
tuition_median = median(tuition_fees)

print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")

print(f"\nStudent mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,.2f}")

print(f"\nTuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,.2f}")