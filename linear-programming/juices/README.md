First install Matprog (GLP)
```
sudo apt install glpk-utils
```

In `simple_juice.mod`, you find the definition of the specific problem, you can run it with:
```
glpsol -m simple_juice.mod -o out-simple_juice.txt
```

In `general_juice.mod` we generalized the problem for n types of juices (decision variables).
But we need to define the data for the problem, that is `data.dat`.
```
glpsol -m general_juice.mod -d data.dat -o out-general_juice.txt
```