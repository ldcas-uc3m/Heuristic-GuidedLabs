'''
There are 3 friends that want to order takeout
Juan is willing to eat Pizza or Chicken
Marta Pasta or Chicken
Roberto Hamburger, Pasta, Pizza or Chicken
'''

from constraint import *

problem = Problem()

# -----------------------------
# simple & dirty way to model

# variables
problem.addVariable("Juan", ["Pizza", "Chicken"])
problem.addVariable("Marta", ["Pasta", "Chicken"])
problem.addVariable("Roberto", ["Pasta", "Chicken", "Pizza", "Hamburger"])

# constraints
problem.addConstraint(lambda f1, f2: f1 == f2, ("Juan", "Marta"))  # Juan and Marta orders the same food
problem.addConstraint(lambda f1, f2: f1 == f2, ("Juan", "Roberto"))  # Juan and Roberto orders the same food
problem.addConstraint(lambda f1, f2: f1 == f2, ("Marta", "Roberto"))  # Marta and Roberto orders the same food

# solver
solution = problem.getSolution()  # gives one solution
solutions = problem.getSolutions()  # gives all posible solutions

print(solutions)

problem.reset()  # reset problem

# -----------------------------

# cleaner way to model

# define variables
vars = {
    "Juan": ["Pizza", "Chicken"],
    "Marta": ["Pasta", "Chicken"],
    "Roberto": ["Pasta", "Chicken", "Pizza", "Hamburger"]
}

# add variables
for var, domain in vars.items():
    problem.addVariable(var, domain)


# define constraints
def isEqual(f1, f2):
    return f1 == f2

# add constraints
for var1 in vars:
    for var2 in vars:
        if var1 != var2:
            problem.addConstraint(isEqual, (var1, var2))


solutions = problem.getSolutions()

print(solutions)

problem.reset()

# ------------------------------
# even prettier

# add variables
for var, domain in vars.items():
    problem.addVariable(var, domain)

problem.addConstraint(AllEqualConstrint())  # predefined constraint

solutions = problem.getSolutions()

print(solutions)
