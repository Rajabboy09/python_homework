
def convert_far_to_cel(f):
    c = (f - 32) * 5/9
    return f"{f} degrees F = {c:.2f} degrees C \n"


def convert_cel_to_far(c):
    F = c * 9/5 + 32
    return f"{c} degrees C = {F:.2f} degrees F \n "

F = float(input("Enter a temperature in degrees F: "))
print(convert_far_to_cel(F))

C = float(input("Enter a temperature in degrees C: "))
print(convert_cel_to_far(C))