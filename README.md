# wasserstein
C++ implementation of the Wasserstein distance (or earth mover's distance)

### Parameters
```
A: Values observed in the distribution A

AWeights: Weight for each value of A

B: Values observed in the distribution B

BWeights: Weight for each value of B
```
### Usage

```
std::vector<double> av = {3.4, 3.9, 7.5, 7.8};
std::vector<double> aw = {1.4, 0.9, 3.1, 7.2};
std::vector<double> bv = {4.5, 1.4};
std::vector<double> bw = {3.2, 3.5};

dist = wasserstein(av,aw,bv,bw);
```

### Examples

![plt1](https://raw.githubusercontent.com/gnardari/wasserstein/master/aux/plt1.png?token=ABLN6C4AQV2RPJ3I4BOYMX25ZI36K)

`The earth movers distance is: 0`

![plt2](https://raw.githubusercontent.com/gnardari/wasserstein/master/aux/plt2.png?token=ABLN6C4AXSA4SUV2MJXPNAS5ZI4CS)

`The earth movers distance is: 0.582418`

View testdist.cpp to see examples on how to use
```
g++ testdist.cpp -o test -I..
./test

The earth movers distance is: 0
The earth movers distance is: 0.582418
The earth movers distance is: 4.07813
The earth movers distance is: 0.25
The earth movers distance is: 5
```

You can run the Python script that calls scipy's implementation for reference:
```
python dist.py

The earth movers distance is: 0.0
The earth movers distance is: 0.5824175824175825
The earth movers distance is: 4.078133143804786
The earth movers distance is: 0.25
The earth movers distance is: 5.0
```
