# Graph-Coloring-Program-Using-Genetic-Algorithms

A project that was developed as a university assignment for the subject "Artificial Intelligence and Experiential Systems". 

The program was implemented in python and as a development tool Visual Studio Code was chosen. The code implements a genetic algorithm with single-point crossover. An adjacency matrix was used to record the elements that are adjacent to each other. The suitability function used calculates the percentage of adjacent elements that have a different color compared to all adjacent elements. A noteworthy benchmark is that the higher the percentage the greater the similarity.The crossover is performed using the simple roulette technique, which assigns percentages to regions of the form (a,b] with α<β and by generating a number between the interval [0,1] we get the member of the population to be crossed. For the crossover, the higher the percentage obtained by that member, the higher the probability of being selected for the generation process. The algorithm terminates after the predefined number of epochs(epochs) or if a member with similarity greater than the predefined fitness threshold is generated. The example shows the operation of the algorithm called in the following way.  </br> </br>

<b>Ιnstallation Ιnstructions:</b> </br> </br>

1. Download the project. </br>
2. Open the project with Visual Studio Code. </br>
3. Run it and explore its functions. </br> </br>

<b>Here are typical screenshots of the functionality: </b>

• <b>10 washing samples,10 seasons suitability threshold equal to 90% similarity to the optimal solution.</b>

![image](https://github.com/user-attachments/assets/3e9bbd46-e8d0-4425-ba90-6c2e06d8656a) </br> </br>

![image](https://github.com/user-attachments/assets/5f5b9aef-ea80-48a4-9ae8-518b4ec502e9) 

