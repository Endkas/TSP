# A meta-heuristic way to solve a combinatorial problem

1st Endrit Kastrati
dept. of Finance
HEC, University of Lausanne
Lausanne, Switzerland
endrit.kastrati@unil.ch

2nd Gregory Porchet
dept. of Finance
HEC, University of Lausanne
Lausanne, Switzerland
gregory.porchet@unil.ch

3rd Diego Levy
dept. of Finance
HEC, University of Lausanne
Lausanne, Switzerland
diego.levy@unil.ch


 # Abstract
—”Given a list of cities and the distances between each
pair of cities, what is the shortest possible path that visits each
city exactly once and returns to the starting city?”
The Traveling salesman problem has been one of the most studied
combinatorial problem for the past two decades. This problem
is quite easy to represent, and since it lies in the category of
NP-hard problems, it is a interesting research problem. The goal
of this paper is to look at performance of heuristic algorithms,
which are less time consuming and more computer friendly than
the robust method of testing every single possibility.
In this paper, we will focus on two heuristic algorithms. The
Nearest Neighbor algorithm and the Ant Colony optimization
algorithm.

# I. INTRODUCTION
The traveling salesman problem (TSP) asks the following
question :” What is the shortest path between a fixed number
of cities with distances between each pair of cities, knowing
that you can visit each town exactly once and that you need
to return to your starting city ?”
The TSP is a NP(non-deterministic polynomial time))-hard
problem,indeed as we increase the number of cities, it in-
creases exponentially the amount of possibles paths.
We can use graph theory to represent the TSP. Each voyage can
be represented as a graph G = (V, E) where each destination,
including the starting city, is a vertex, and if there is a direct
route that connects two distinct cities then there is an edge
between those two vertices. The traveling salesman problem
is solved if there exists a shortest route that visits each
destination once and permits the salesman to return to his
starting point.This route is called a Hamiltonian Cycle,a cycle
in a given graph G that contains every vertex of G is called a
Hamiltonian Cycle of G.
There are many ways to represent the TSP conceptually,an
other one would be with a matrix of distances. Indeed, this
matrix with 0 on diagonals, would contain the distances
between each town. The entry (i,j), is the distance from city i
to city j. The 0 on diagonals are necessary as it is the distance
from a city to itself,which is rationally 0.
In this paper, we will focus only on the symmetric TSP,which
states that the distance from 2 cities is the same whatever the
direction.

The problem has been formulated mathematically as follows
by Dantzig–Fulkerson–Johnson :
Label the cities with the numbers 1,... , n and define:

![](https://github.com/Endkas/TSP/blob/main/ab.png)

The equation (1) is the minimization problem subject to
constraints equations (2), (3) and (4). The constraints (2) and
(3) ensure that all cities are visited once and that we go back
to the starting city.The constraint (4) ensures no proper subset
Q can form a sub-tour, so the solution returned is a single
tour and not the union of smaller tours.
After solving this minimization for a fixed number n of
cities,We obtain the minimum length. We can also infer the
smallest path,which is a sequence of the labeled cities.In this
sequence, the starting city appears at the begging and the
end.The length of the sequence is n + 1 and therefore form a
Hamiltonian Cycle.

Let’s look concretely at an example to see properly the
problem. Imagine our starting point is Zurich, and we want to
visit the nine other biggest cities of Switzerland. If you look at
Figure 1, you can see the shortest path if you want to visit these
destinations with your car.Nevertheless, it might be easier to
represent the shortest path as the crow flies, which is what
we did in Figure 2. The second representation highlights the
problem and all his constraints. 
The shortest path for Figure
2 is : \
Zurich→Winterthur→St.Gallen→Lugano
→Geneva→Lausanne→Bern
→Biel→Basel→Lucerne→Zurich

In the first representation, distances are expressed in kilometers
whereas in second it is the euclidean distance between the
coordinates (longitude and latitude) of one city from another.
Indeed,latitudes and longitudes allow to represent a city loca-
tion in the coordinates system. From now on, we will use a
coordinate system to express the location of a city.
For this small example, intuitively we could think that there
is not a lot of possible paths.Nevertheless, there are 184’
possible paths for the symmetric TSP and twice as much
for the asymmetric one. 

![](https://github.com/Endkas/TSP/blob/main/abc.png)
The Table 1 shows the evolution of
number of possible paths. We can clearly see that the traveling
salesman problem belongs to the NP category.

Fig. 1. The shortest path by car between the 10 biggest cities in Switzerland,
coded in python with folium and openrouteservice
![](https://github.com/Endkas/TSP/blob/main/mapcoupe.png)

Fig. 2. The shortest path as the crow flies between the 10 biggest in
Switzerland, coded in python with folium
![](https://github.com/Endkas/TSP/blob/main/mapcoupe2.png)

### II. DESCRIPTION OF THE RESEARCH QUESTION

The fastest known algorithm to find the correct answer of
the TSP for a number n of cities, is the Held-Karp Algorithm
using dynamic programming.This algorithm has a complexity
of O( 2 n).
We could think that with parallel computing and high-
performance computing,we could easily approach the TSP
with the Held-Karp algorithm.The truth is, that for a number
of cities which is extremely big,this algorithm is going to take
too much time to find the correct answer.
The traveling salesman problem highlights the trade-off be-
tween time and precision.Indeed, the answer needs to be
precise,that is the shortest path.But as the fastest known
algorithm to solve the problem has an exponential complexity,
we need to find another approach to potentially deal with large
numbers of cities,which is heuristic algorithms.
Heuristic algorithms are faster and more efficient but they
sacrifice precision for speed.
We developed two main algorithms: the Ant colony optimiza-
tion and our version of the Nearest Neighbours.Through this
paper,we will analyse these algorithms to see their perfor-
mance solving the TSP.
We will look at the execution time and the precision. The
precision will be defined as follows : 1 −mlhml−ml,withmlh
the minimum length found by the different heuristic algorithms
and ml the true minimum length.
### III. METHODOLOGY
A. Brute Force Algorithm

The brute force algorithm is simple, it tries every permu-
tations of paths possible from the starting city. This algo-
rithm will always find the shortest path for a complexity of
O((n−1)!).If we look at the Table 1,we observe the number
of possible paths for 25 cities. If we apply the brute force (BF)
algorithm it will test twice as much paths,i.e 6.2e+23.
We clearly see the inefficiency of this algorithm, even for a
small number of cities, the amount of time needed to solve
the problem is extremely high. We wanted to first use the BF
algorithm to check the precision of the heuristic algorithms.
Unfortunately, the amount of time needed to execute our code
was not decent. We found it very lately, with our project’s
structure already being done.
Therefore, we decided to use a library(python-tsp) with the
Held-Karp algorithm implemented.


B. Nearest Neighbour Algorithm

The nearest neighbour algorithm, or as we called it the
nearest neighbour available (NNV) is a greedy algorithm.
Indeed from a city it chooses the closest not visited city and
does this for every city, in the hope to do the shortest tour of
all cities. We implemented our own version of it, our pseudo
code would be as follows :

1. select a city as current city.
2. find out the shortest distance connecting the current city
and an unvisited city.
3. set the new city as current city.
4. mark the previous current city as visited.
5. if all the cities are visited, then go back to starting city,
else go back to step 2.

Let’s dig into an simple example. Let A be the matrix
of distances withf < e < d < c < b < a, P the matrix of
paths and the cities are labeled form 1 to 4. The algorithm
starts at line 1 of the matrix A and chooses the smallest
distance which in this example is c and corresponds to the
entry of the matrix (1,4). Therefore, we go from city 1 to
city 4. We are now at city 4, thus we have to look at line
4 of the matrix now. From there, the shortest distance is
f, i.e the entry (4,3). We are now in city 3, there we have
only one remaining choice: city 2. Indeed, city 4 has already
been visited and we can only come back to city 1 when we
have visited all the cities. From city 2,which is the last city
being visited,we must come back to city 1. The matrix of
paths P, has a 1 on same entries as distances chosen. In this
example,(1,4),(4,3),(3,2) and (2,1).

![](https://github.com/Endkas/TSP/blob/main/abcde.png)

The matrix multiplication  <img src="https://latex.codecogs.com/gif.latex?AP^T" title="AP^T" />
gives us the length of the min-path if we start from the first
line of the matrix A, which is the first city. The min-path value
is therefore c + f + d + a. We can infer the path sequence from
the matrix P as we explained before.The min-path sequence
for this example is : 1 → 4 → 3 → 2 → 1

From this small example, we can see the weakness of the NNV,
when we visit the last city we have to go back to our starting
city. This last length can be very costly. Indeed, it costs us a,
which is the biggest distance in this example. In Figure 3, we
can see this graphically,indeed the TSP was solved with 200
cities. The line in light-blue is the last length, i.e the distance
to go back to the starting city from last city visited. We also
see in this figure, that the last distance with NNV can be very
costly.

Fig. 3. NNV shortest path found with 200 cities GraphNNV-200citiesGOOD
![](https://github.com/Endkas/TSP/blob/main/GraphNNV-200citiesGOOD.png)

To potentially deal with this problem, we thought we could try
to begin the algorithm at different starting cities. We applied
the algorithm to each city being the starting city and then
compared the minimum value of the path. To understand the
utility of testing each city as a starting city, we need to
highlight the advantage of being the starting city. Indeed when
we are the first city, all others cities are still not visited. Thus,
we have n-1 choices. When a city is not the starting the city
it has necessarily less than n-1 choices. Therefore by doing
this, we test all possible chaining and find the smallest path
possible to be found by the Nearest Neighbour algorithm.
Let’s be clear about how the algorithm works. We assume
that we have n cities labeled from 1 to n. We apply the NNV
algorithm with city 1 as starting city and get a sequence of
path and the length of it. Then we apply algorithm with city
2 as starting city,then city 3 and so on...
Therefore, we will have n sequences of paths with their
respective length. From these n lengths, we sort them and
choose the smallest one to be the smallest path possible to be
found by NNV.
We observe the sorted length of paths on Figure 4. We clearly
see now the utility to start the algorithm at each city. We notice
that the range of the value is quite big and that we can gain a
lot of precision by simply starting the algorithm at each city.
The algorithm complexity is quite easy to show. As mentioned
before, when we are the first city, we have n-1 choices with n
being the number of cities. Then, when we are the second city
we have n-2 choices etc... Therefore, in every case we must
check for each city the n-i choices, with i being the position
of the city. This can be represented mathematically :
![](https://github.com/Endkas/TSP/blob/main/proof.png)
By using big O notation, we can therefore conclude that that
the algorithm complexity is O(n^2). As every city will be tested
as the first one, we will apply the algorithm n times. This
implies that the final complexity of our algorithm is O(n^3).

Fig. 4. NNV shortest path found with 200 cities
![](https://github.com/Endkas/TSP/blob/main/nnv-2000.png)

C. Ant Colony Optimization

Insect societies have developed a highly well-structured
organization, despite the simplicity of their individuals. This
phenomenon was first noticed in 1988 by Frank Moyson and
Bernard Manderick, who published an article about the self-
organization among ants. In 1990, this research was taken a
step further by the researcher Marco Dorigo, who tried to solve
a combinatorial optimization problem based on ant’s behavior
when seeking food.
These insects’ behavior has not only inspired the Ant colony
optimization but many other algorithms. The division of labor
and foraging are two of the multiple behaviors of ants that
have been researched. Foraging is defined as the act of an
ant depositing a chemical while going through a path, which
increases the probability that another ant chooses the same
path.

D. Ants Behaviour

Most ants are blind, and as stated above, they communicate
with each other and locate themselves in their environment
with these chemicals they leave on the floor. These chemicals,
called pheromones, are a vast part of the ant colony optimiza-
tion algorithm.
As we can see in Figure 5, the upper path is twice as long
as the lower path. At first, there is the same probability of
going through each path, as the ants look for food randomly.
However, the ant that chooses the lower path has time to get
to the food and come back, while the other ant only has time
to get to the food. Thus, the lower path has twice as much
pheromones as the one above. When the second batch of ants
chooses a path, there is a higher probability that they will
choose the one below. Also, after a certain number of batches,
the upper path will not be chosen anymore. This number of
batches will depend on the evaporation rate: if the pheromones
evaporate quickly, the number of batches needed for the upper
path to no longer be chosen will be higher.

Fig. 5. An illustration of two ants, which go from their nests to the food and
come back
![](https://github.com/Endkas/TSP/blob/main/pheromone.png)

E. ACO for traveling salesman problem
As stated above, the main goal of the traveling salesman
problem is to find the shortest path going through a specified
number of cities, only once per city, and come back to the
starting point. Therefore, the only way to find the optimal
solution for each specific path would be to try every single
possibility. However, when the path carries more than a dozen
cities, the program takes a considerable amount of time to
carry out the calculations.
The goal of the ACO was to get a solution similar to the
minimal length of the Hamiltonian circuit, in a much shorter
lapse of time. In order to achieve this, we developed the
algorithm in the following manner: we positioned several ants
through the different cities, and the starting point of each ant
was assigned randomly. Then for each ant, we created the
memory vector. The memory of each ant contains the cities
that the ant has already visited. Memory has two main goals.
First, to make the ant remember the cities it has visited and
therefore not returning to a city it has already visited, to meet
the algorithm’s requirements.
Secondly, memory allows the algorithm to compute the length
of the tour achieved by each ant. Without it, we would not
be able to compare the ants, and the algorithm would in turn
not achieve the optimal solution.
```
```
Every time an ant lies in specific city, it has to decide which
city to visit next. For this decision to be as close to reality as
possible, every ant is assigned a transition probability to each
city it has not visited yet.
Based on the probabilities, the ant decides to which city it
travels next and the memory vector is updated. Also, the ants,
leaving a pheromone trail, will influence future ants in their
decision.
The pheromone lying on a specific path is highly important
for this algorithm. It allows the next ants to learn how
essential it is to go to a city j when lying on a city i. This
pheromone trail is constantly updated after each ant has
finished its tour. When an ant has achieved a good path, the
pheromone trail will be higher. However, when a path is not
```

as successful, the pheromone trail will be smaller, and this
will allow future ants to differentiate a potential good path
from one they should not take.

If the entire decision was based on pheromones, every ant
would take the same path as the ant that carried out the first
tour. Therefore, the probability assigned to each city cannot
only depend on the amount of pheromone lied on a path.
We also had to take into account another factor, which is
desirability.
It can be seen as the distance between a city i and a city j and is
calculated as follows:ηij= 1/Lijbecause when the distance
between two cities is higher, the desirability decreases.
The reason we use desirability is explained by the fact that
when an ant goes and gets food, it is more likely that it will
try to find the resources in a place that is close to its position.
The same applies to the traveling salesman’s path. It is more
likely that he will visit the cities that are closer to his current
location to find the optimal path.
Now that we have all the parameters, we are going to look
at the entire probability formula:

```
pij=
```
```
(τijα)(ηβij)
∑
(τijα)(ηβij)
```
Both the desirability and the pheromone trail have an
exponent, respectively alpha and beta. Those exponents will
allow us to give a higher weight to either the pheromone or
the desirability when an ant makes a decision.
As an example, if alpha = 0, the closest cities are more likely to
be selected, and the model will turn into a stochastic algorithm.
On the other hand, if beta = 0, the decision will mainly be
made on the pheromone trail, and the model will rapidly reach
its peak as every new batch will take the same path as the first
batch.
The last parameter we used in our algorithm is the
evaporation rate. In order to make it as realistic as possible,
we made the pheromone evaporate after a while. Therefore,
we incorporated its rate in our model. When the evaporation
rate is high, the optimal path will take slightly longer to
get found since there are more negligible pheromone traces.
When this rate is low, the path will be found faster on average.

Regarding the complexity of the Ant colony algorithm, it
was developped by N.Attiratanasunthron and J. Fakcharoen-
phol(2007). They were able to approximate the complexity to

O(

### 1

```![Capture d’écran (169)](https://user-images.githubusercontent.com/81076141/132995387-081be765-4c0d-461c-a689-f12b624480a8.png)

ρ
```
```
n^3 logn), where n is the number of cities, and rho the
```
evaporation rate.
Finally, Figure 6 presents a summary of the different steps
of the ant’s colony algorithm.
We can observe the evolution of the ACO algorithm on the
Figure 7, both the path and the pheromones when the number
of cities is of fifty. We notice that after five iterations, the
result is already satisfactory, and the key axes start to gain
some noticeable pheromone traces.

```
Fig. 6. Summary of the steps of the ACO
```
```
Moreover, the optimal path is almost found after fifteen
iterations, as seen in Figure 7. Hence, the ant colony algorithm
does not require many iterations or ants to find an adequate
path, even if it is not the most optimal one. In this algorithm,
the pheromone traces quickly converge, and we observe that
there is only a small difference between fifteen and fifty
iterations.
This result is surprising as we set a relatively high evaporation
value of about fifty percent. However, it shows the quickness
and efficiency of the ACO.
IV. CODEIMPLEMENTATION
We implemented the different codes in Python, we created
a Class for each algorithm.
In order to solve the traveling salesman problem, we needed
to provide distance matrices. We created a class named Cities.
This class generates random latitudes and longitudes and
compute from it a matrix of distances. As represented on our
different figures, the x axis which is the latitude and the y axis
the longitude. We all know that latitude and longitude do not
go from 0 to 18 and 0 to 36 but ours are only positive.
The class Cities, takes as argument n, which is the number of
cities we want to generate. Also there is a seed per default
for the random data generation, which can be changed. The
use of the seed offers a lot of flexibility, indeed with it, we
can generate different cities location for the same number of
cities. This flexibility will be crucial to compute the precision
of heuristic algorithms.
To make it even more convenient, the class Cities will be
the super class of the different algorithms, which implies that
the class for the Brute Force algorithm (BF), the class for the
Ant Colony Optimization algorithm (Ant) and the class for the
Nearest Neighbour algorithm (NNV) will inherit the matrix of
distances and the hypothetical coordinates values of the cities
from Cities.
```

```
Fig. 7. An illustration of ACO for 50 cities
```
This allows us to easily compare algorithms for a fixed number
of cities. Indeed, if we create an instance Ant and an instance
NNV with a the same number of cities, the matrix of distances
and coordinates values will be exactly the same for the two
instances. This will allows us to look at the performance of
the algorithms for exactly the same TSP.
As we mentioned earlier, our first idea was to use the Brute
Force algorithm to check the precision of the heuristic algo-
rithms. Regrettably, we only found lately that the Brute Force
algorithm, even for a small number of cities, was taking too
much time. We therefore decided to use a library with the
Held-Karp algorithm to solve the traveling salesman problem.
As we did not code this algorithm ourselves, we could not
make it a subclass of the class Cities as we did for the others
algorithms. But it is not an issue at all, as we could create
instances of the class Cities. From it, we recovered the matrix
of distances. We gave this matrix of distances as input to the

```
library using the Held-Karp algorithm that solved the TSP in
question and returned the minimum distance of the path and
the path itself.
At this point, we have now all the necessary tools to aboard
our research question.
```
```
A. Nearest Neighbour Parallelization
As we coded this algorithm using principally lists, loops
and Numpy arrays ,we had the idea to use Numba to
parallelize our code.
Numba translates Python functions to optimized machine
code at runtime using the industry-standard LLVM compiler
library.
Numba is built for scientific computing and is designed to be
used with NumPy arrays and functions, which is perfectly in
harmony with how we implemented the NNV algorithm.
With numba, the compilation of a python function is activated
by a decorator. Decorators allow us to wrap another function
in order to extend the behavior of the wrapped function,
without permanently modifying it.
As shown below on the piece of code example, which shows
how the decorators works. You may have noticed, the piece
of code is not in classes.As we faced some issues trying
to implement Numba with classes,we therefore coded the
algorithm in classic way.
The code below is used to create the matrices of distances to
solve the TSP.
In order to to make it work, we need to put a @jit decorator
in front of every function used or the process will fail.
We used the mode ”nopython” as instruction to Numba.
This mode is the one recommended as it gives the best
performance. The mode ”nopython” compiles the decorated
function so that it runs entirely without the participation of
the Python interpreter.
We were extremely surprised by the performance of our
algorithm with Numba. We will share it in the results sections.
```
```
import numpy a s np
from numba import j i t
import r a n d o m
```
```
@ j i t ( n o p y t h o n = T r u e )
def latlongNUMBA ( n ) :
x = [ ]
y= [ ]
r a n d o m. s e e d ( n )
for i in range( n ) :
a = r a n d o m. u n i f o r m ( 0 , 1 8 )
b = r a n d o m. u n i f o r m ( 0 , 3 6 )
x. a p p e n d ( a )
y. a p p e n d ( b )
return x , y
```
```
@ j i t ( n o p y t h o n = T r u e )
def matdistNUMBA ( n ) :
```

```
a = latlongNUMBA ( n )
x= a [ 0 ]
y = a [ 1 ]
c o o r d = [ ]
m a t = np. z e r o s ( ( n , n ) )
for i in range( n ) :
c o o r d. a p p e n d ( ( x [ i ] , y [ i ] ) )
for j in range( i + 1 , n ) :
l a = ( x [ i ] − x [ j ] )* * 2
l o n = ( y [ i ] − y [ j ] )* * 2
m a t [ i , j ] = ( l a + l o n )* *0. 5
m a t [ j , i ] = m a t [ i , j ]
return mat , c o o r d
```
B. ACO

In the ant colony optimization algorithm we had to make a
certain amount of assumptions.
1) First, regarding the number of ants, when we incorporate
a lot of ants to our system, the best answer will be more
likely to be found. However we will get a model which
is slower. The goal of our model is to find the best
algorithm in the shortest lapse of time. This trade-off
was discussed in a research paper by Christoffer Lundell
Johansson and Lars Petersson.

```
Fig. 8. Trade-off between number of ants, and time
```
```
According to their study, the optimal number of ants
with approximately one hundred cities, lies between 20
and 30 percent of the amount of cities. Therefore, we
decided to keep the amount of ants to 30 percent of the
amount of cities in our algorithm.
```
```
2) For the evaporation rate, it determines at which fre-
quency the pheromones on the path will evaporate.
When this rate lies closer to 1, the pheromones will
immediately evaporate and will not have an impact on
future ants. On the other hand, when it is lower, the ants
will quickly find the best path. Therefore, as we did not
want to make it too simple for the ants, nor too hard,
we decided to keep this rate at 0.
```
3) Alpha and Beta decide the importance respectively of
the pheromone trail and of the desirability. We wanted
our model to take both of these factors equivalently,
therefore we set them both at 1.
Here is a summary of the Ant colony algorithm that we
built:

```
1) We created an algorithm on python based on different
classes. We created a class ant, which allowed us to
create our ants and to make them have a memory vector.
Based on this memory, we were able to make the ants
do a tour where they visit each cities, and retrieve this
tour to calculate the length.
```
```
2) The most important part of the algorithm lies in the
colony method. This method allowed us to make the
ants take into account the probability equation, and make
them choose their future destination based on it. In order
to do so, we created a cumulative sum with all the
probabilities, and then the ant picked a random number
between 0 and 1. Based on this number, the decision is
made.
```
```
3) Now that each ant made its tour, we created a method
update pheromone, which updates the pheromones that
lie on the path based on the performance of the tour of
the different ants. This allows future ants to learn from
their ancestors.
```
```
4) We wanted the output to be as visual as possible,
therefore the method Draw graph was created. It takes
into account every path of the different ants within a
batch. From these different ants, it highlights the best
one and prints out its tour. At the end of the algorithm,
it prints out the optimal path based on our algorithm.
```
```
V. RESULTS
Here are the results of our research question. Our research
question was to look at the performance of heuristic
algorithms.
```
```
It is important to remember that heuristic algorithms do not
solve the TSP for sure, we will never know if the distance
found by the NNV or ACO is indeed the smallest one.
We will first discuss about the precision of heuristic
algorithms. As we defined earlier, precision is :
1 −mlhml−ml,with mlh the minimum length found by the
different heuristic algorithms and ml the true minimum
length.
To find the true minimum length, we used the Held-Karp
algorithm. To compute precision, we solved 100 different
TSP for each number of cities :n∈[5,20]. Therefore, we
looked at precision over 1500 different traveling salesman
problems. We only took into account TSP with small number
of cities because the Held-Karp algorithm was taking too
much time for n larger than 20.
The results are visible on Table II. It took us more than 10
hours of execution time to obtain those results. We can see
that on average the NNV algorithm has a precision of 96.19%
compared to an average precision in a range of 84.13-96.89%
for the ACO algorithm. The precision of the Ant Colony
depends on the number of ants. When the amount of ants is
equal to the number of cities, the precision is better than the
```

one from the Nearest Neighbor. However when the amount
of ants is equal to 30% of the number of cities, the precision
is much smaller than the one of the NNV algorithm and is
only equal to 84.13%.
To go further, we wanted to analyse how the heuristic
algorithms perform against each other. we solved 100
different TSP for each number of citiesn ∈ [21,40]and
discerned which one of them found the shortest distance
on average. We surprisingly found that the NNV algorithm
was slightly doing best on average. We needed 11 hours of
execution time to obtain this result.

```
TABLE II
ALGORITHMS COMPLEXITY AND PRECISION
Algorithm Complexity Precision
Brute Force O((n−1)!) 100%
Held-Karp O( 2 n) 100%
Nearest Neighbour O(n^3 ) 96.19%
Ant Colony Optimization O( 2 n^3 log(n)) 84.13-96.89%
```
We will now discuss the execution time. If we look at
Figure 9, we can see the execution time needed by each
algorithm for different number of cities. We can clearly see
that the NNV algorithm dominates the ACO algorithm. For
the ACO algorithm, we notice that the execution time, as the
precision, also depend on the number of ants. By generating
more ants, we certainly gain in precision but we also need
more time. This gain of precision costs us a certain amount
of execution time.

The Nearest Neighbour algorithm is already pretty fast.
Nevertheless, we wanted to push it further by parallelizing
the algorithm with Numba.
If we look at Figure 10 ,we can see the execution time of
the algorithm with and without Nubma. We can observe that
up to 100 cities, the implementation with Numba takes more
time. This might be caused by the compilation step of the
decorated function. For more than 100 cities, the algorithm
with Numba takes less time than the algorithm without it.
To show what our algorithm with Numba is capable of, we
applied the algorithm with 5000 cities. After more than 1
hour of execution time, we get the result that is shown on
Figure 11.
We clearly see that the shortest path found might not
be the optimal one and that therefore the TSP is not
solved. Nevertheless, it seems visually to be a really good
approximation.

To conclude, based on our results, we can say that the
Nearest Neighbor algorithm might be better than the Ant
Colony Optimization algorithm in most cases. Indeed, the
NNV algorithm is much more faster for a precision nearly
equal to the ACO algorithm.

### VI. CONCLUSION

```
Through this paper we approached a combinatorial problem
with two heuristic algorithms and were able to quantify the
average precision of them for a specific range of cities.
We found that heuristic algorithms provide a relatively good
approximation of the true answer for TSP with n cities, with
n∈[5,20].
These results are specific to our approach and are valid only
for the range used to compute the average precision. We
surely can say that these average precision would be reduced
as we increase the number of cities.
```
```
As we showed through this paper, the travelling salesman
problem is a combinatorial problem which is categorized as
a NP(Non-deterministic polynomial time)-problem.
For large numbers of cities, algorithms that found the correct
answer in a deterministic way take an execution time which
is not decent.
As time is one of the most important thing for humans, we
need heuristic algorithms to have an approximate solution of
the problem.
```
```
Fig. 9. Execution time comparison between heuristic algorithms
```

Fig. 10. Performance comparison of our NNV algorithm implemented with
and without Numba

```
Fig. 11. NNV(With Numba) shortest path found for 5000 cities
```
```
REFERENCES
[1] C.L. Johansson, L.PettersonAnt Colony Optimization - Optimal Num-
ber of Ants, STOCKHOLM, SWEDEN 2018.
[2] M. Dorigo, G. Di Caro, L. M. Gambardella.Ant Algorithms for
Discrete Optimization, UniversitC Libre de Bruxelles, Belgium 1998.
[3] T. Stutzle, Holger Hoos.Artificial Neural Networks and Genetic
Algorithms, pringer Verlag, Wien New York, 1998
[4] G. Reinelt.The Traveling Salesman Problem: Computational solution
for TSP applications, Berlin: Springer-Verlag, 1994.
[5] Corinne BrucatoThe Traveling Salesman Problem, University of Pitts-
burgh, 2013.
[6] Simon ScheideggerProgramming course, University of Lausanne,
2021.
[7] M. Dorigo , T. St ̈utzle,Ant colony optimization: overview and recent
advances. In Handbook of metaheuristics (pp. 227-263). Springer US,
2010.
[8] M. Pedemonte, S. Nesmachnow H. Cancela.A survey on parallel ant
colony optimization. Applied Soft Computing, 11(8), 5181-5197, 2011.
[9] N. Attiratanasunthron , J. Fakcharoenphol.A running time analysis of
an Ant Colony Optimization algorithm for shortest paths in directed
acyclic graphs,Kasetsart University, Bangkok ,2007.
```

