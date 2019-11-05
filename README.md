# wasserstein
C++ implementation of the Wasserstein distance (or earth mover's distance) based on scipy

![plt1](https://raw.githubusercontent.com/gnardari/wasserstein/master/aux/plt1.png?token=ABLN6C4AQV2RPJ3I4BOYMX25ZI36K)

`The earth movers distance is: 0`

![plt2](https://raw.githubusercontent.com/gnardari/wasserstein/master/aux/plt2.png?token=ABLN6C4AXSA4SUV2MJXPNAS5ZI4CS)

`The earth movers distance is: 0.582418`

View testdist.cpp to see examples on how to use
```
g++ testdist.cpp -o dist
./dist

The earth movers distance is: 0
The earth movers distance is: 0.582418
The earth movers distance is: 4.07813
The earth movers distance is: 0.25
The earth movers distance is: 5
```

You can run the Python script that calls scipy's implementation for reference:
```
python3.6 dist.py

The earth movers distance is: 0.0
The earth movers distance is: 0.5824175824175825
The earth movers distance is: 4.078133143804786
The earth movers distance is: 0.25
The earth movers distance is: 5.0
```
