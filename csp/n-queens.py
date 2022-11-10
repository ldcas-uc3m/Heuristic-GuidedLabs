'''
We have N queens on an NxN chessboard
We need N variables: each one represents the position of a queen
in its respective column
Place each queen in a way that they are all safe
'''

from constraint import *


def printQueens(assignment):
    # show grafically the solution
    N = len(assignment)
    for i in range(N):
        print(f"{'# ' * assignment[i]}{assignment[i]} {'# ' * (N - 1 - assignment[i])}")


def main(N = 4):
    problem = Problem()

    # N vars, domain: {0, 1, ..., N-1}

    vars = range(N)
    domain = range(N)

    # add all variables
    problem.addVariables(vars, domain)

    # constraints

    problem.addConstraint(AllDifferentConstraint())  # each queen is in a different row
    
    # can't be in same diagonal
    for q1 in vars:
        for q2 in vars:
            if q1 != q2:
                problem.addConstraint(\
                    lambda queen1, queen2, c1 = q1, c2 = q2:\
                        abs(c1 - c2) != abs(queen1 - queen2), (q1, q2))

    print("One solution:")
    printQueens(problem.getSolution())

    print("The total number of solutions is:", len(problem.getSolutions()))


if __name__ == "__main__":
    main()

    