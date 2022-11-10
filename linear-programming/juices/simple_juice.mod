# Modeling the specific problem
# vscode extension for GNU MathProg: steffenk1337.gmpl

var x1;
var x2;

# objective function1
maximize profit:
    1.25 * x1 + 2.05 * x2;

# constraints
s.t. limited_concentrated:
    0.2 * x1 + 0.5 * x2 <= 2.4;

s.t. limited_juice:
    x1 + x2 <= 6;

end;