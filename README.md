# Implementation of hill climbing algorithm in python

In this implementation the algorithm is searching for the most efficient tour to visit a number of cities.

**Cities:** A, B, C

**Distances between Cities:**

| |A|B|C|
|-|-|-|-|
|**A**|0|3|2|
|**B**|3|0|1|
|**C**|2|1|0|

**Possible Tours:**

 **A** --[3 km]--> **B** --[1 km]--> **C** | **[4 km]**

 **A** --[2 km]--> **C** --[1 km]--> **B** | **[3 km]** (most efficient)

If you change the amount of cities (countCities = x), you have to change the threshold aswell. For 20 cities, a threshold between 15-25 is recommended. For 100 cities, a threshold between 100-175 is recommended. The higher the threshold, the more time the algorithm will need to find an optimum.


