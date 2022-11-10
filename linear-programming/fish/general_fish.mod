# fisherman general model

# fisherman can catch different types of fish
set FISH;

# the fisherman can use different baits
set BAIT;

# the family needs diff. types of nutrients
set NUTRIENT;

# each fish has a different amount of each nutrient
param nutrient_per_fish {n in NUTRIENT, f in FISH};  # matrix

# each type of bait catches a diff amount of each type of fish
param fish_per_bait {b in BAIT, f in FISH};

# each type of bait has a different cost
param cost_per_bait {b in BAIT};

# we need a different amount of each nutrient
param nutrient_needed {n in NUTRIENT};

# the dec. vars.: amount of each type of bait to use
var x {b in BAIT};

# obj. function was to minimize the cost of catching the needed amount of fish for nutrients
minimize cost:
    sum {b in BAIT} cost_per_bait[b] * x[b];

# constraints
s.t. minumum_nutrient {n in NUTRIENT}:  # one constraint for each type of nutrients
    sum {b in BAIT, f in FISH} fish_per_bait[b, f] * nutrient_per_fish[n, f] * x[b] >= nutrient_needed[n];

end;