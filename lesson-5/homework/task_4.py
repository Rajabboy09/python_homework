universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(list_of_unv):
    a,b = 0,0
    for i in list_of_unv:
        a = a + i[1]
        b = b + i[2]
    return f"Total students: {a} \nTotal tuition: ${b}"


print(enrollment_stats(universities))
