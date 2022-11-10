# General model for the juices problem

set JUICES;  # types of juices we want to sell

# each juice has a profit and specific amount of concentrated associated to it
param profit {j in JUICES};  # parameter profits for each j in set JUICES
param concentrated {j in JUICES};

# now we define the decision variables
var x {j in JUICES};  # amount of juice to create for each type of juice

# x = [Type A: X, Type B: Y, ...]


# define the obj. function
maximize benefit:
    sum {j in JUICES} profit[j] * x[j];  # sum of profits times amounts

# now the constraints
s.t. limited_concentrated:
    sum {j in JUICES} concentrated[j] * x[j] <= 2.4;  # resources tend to be hard-coded, but can be defined w/ a parameter

s.t. limited_juice:
    sum {j in JUICES} x[j] <= 6;

end;