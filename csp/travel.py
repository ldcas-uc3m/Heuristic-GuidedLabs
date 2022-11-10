'''
A hotel has to organize trips to cities.
Each guest chooses cities they want to visit.
The hotel wants to know if they can plan the trips in 3 days.
If a guest chooses two cities, the trips cannot be in the same day
Guest1 chooses Salamanca and Patones
Guest2 chooses Segovia and Toledo
Guest3 chooses Salamanca and Toledo
'''

from constraint import *

def main():
    problem = Problem()

    # adding variables with the same domain
    vars = ["Salamanca", "Patones", "Segovia", "Toledo"]
    domain = range(3)
    problem.addVariables(vars, domain)

    # constraints
    def diffDays(cit1, cit2):
        # you have to visit specific cities on diff days
        return cit1 != cit2

    problem.addConstraint(diffDays, ("Salamanca", "Patones"))
    problem.addConstraint(diffDays, ("Segovia", "Toledo"))
    problem.addConstraint(diffDays, ("Salamanca", "Toledo"))

    print("Solutions:")
    for sol in problem.getSolutions():
        print(sol)

    print("The number of solutions is:", len(problem.getSolutions()))


if __name__ == "__main__":
    main()

    