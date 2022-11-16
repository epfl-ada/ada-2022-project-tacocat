# 2022 ADA Project by team TACOCAT

For information on repository organisation, see the [instructions](docs/instr.md).

The entry point for evaluating our milestone 2 submission is the [milestone 2 notebook](milestone_2.ipynb).

## Abstract

It's no secret that knowing the right people in the film industry is very important to have a successful film career. But who are these people? In this project we will be analysing the acquitances of each actor, actress, director and writer to further investigate the existence of clusters of people who know each other, why these clusters exist and who are the key people that bridge different clusters. Our main goal is to create a social map of the film industry. To do so, we will build a graph of relationships with clusters. Then, we will dive into interesting clusters to understand their demographic (age, ethnicity, genre etc.) and the key people who connect clusters. What happens *behind the scenes* in the film industry is usually a mystery, so we want to *reveal the curtain* to understand the dynamics of the industry.

## Research Questions

- Are there clustering between the people in the film industry?
    - What are common attributes of people in the same cluster? And do we see clusters within clusters? If so, do sensitive attributes such as age, gender and ethnicity have anything to do with it?
    - Which people are connecting clusters? What makes them special?
- As representation and diversity have more space in conversations, do we see this in the film industry?

## Additional Datasets Used

In addition to the [CMU movie dataset](http://www.cs.cmu.edu/~ark/personas/), we use the [IMDb datasets](https://www.imdb.com/interfaces/). Using this additionnal dataset will allow us to have data on more people for each movie. This does not only include actors, but also producers, writers and so on. It will also allow us to have movie rating data, which could prove useful for our cluster analysis.

We merge the two datasets on movie title. The exact procedure is done and described in our data [generation notebook](src/generate_data.ipynb) for both movie metadata (Combine CMU with IMDB) and people (Process the other datasets/People).

The resulting dataset is presented in our descriptive analysis in the [submission notebook](milestone_2.ipynb)

## Methods

We used three main methods for our analysis: one for drawing graphs, one for cluster coefficient computation, and one for the clustering.

### Drawing graphs

Having the concern of a nice and pleasing-way to draw graphs for our data story, we turned our attention to the Fruchterman-Reingold [force-directed algorithm](https://en.wikipedia.org/wiki/Force-directed_graph_drawing#Methods). Those graphs emphasis the position of the nodes, assuring as few edge crossings and distance disparities as possible. The main concept relies on physics, more precisely on attractive and repelling forces, and aim to reach an equilibrium between those forces. The attractive forces are model as spring-like forces, and repelling forces as anti-gravity forces. The edges between nodes are the springs, and the nodes themselves are the object exercing anti-gravity forces. 

Even if those algorithm have undeniable advantages such as flexibilty and simplcity, it is worth noting that the algorithm iterates until it reaches an equilibrium, so it can take a long time to finish. In worst cases, it can take up to O(N<sup>3</sup>), although optimization can improve the running time to be O(N<sup>2</sup> log(N)), where N is the number of nodes. It is for this reason that we decided to save a serialized version of the result using `Pickle`. 

We used the package `NetworkX` which provides useful tools and functions for complex networks.

### Clustering Coefficient

To compute the [clustering coefficient](https://en.wikipedia.org/wiki/Clustering_coefficient), which indicates the degree nodes in a graph tend to cluster together, we also used the package `NetworkX`. Those coefficients would allow use to efficiently compute the clusters and visually seperate the different nodes within the graph (by colors, sizes, and so forth).


### Clustering

Last be not least, we would like to compute the clusters. When doing our graph, we ultimately already compute some kind of visual clusters, but we need to eplicitly construct them (since the only information we can retrieve are the positions). In order to have clusters that matches our graph, we will then use the positions from the graph, instead of the usual edges and nodes used for graph clustering. Adding to those positions, we might want to be able to clusters according to potential structure we could come up with during the process. We haven't commited to a specific method yet, but we lean towards unsupervised methods, since our nodes are not labelled. We have selected three methods that seem promising to achieve what we desire. 

The first one would be [spectral clustering](https://en.wikipedia.org/wiki/Spectral_clustering). Three main steps can be identified for this technic: construct a similarity graph, project data onto a lower-dimensional space, and cluster the data. Using the positions from our graph, we could create a distance matrix, which would allow use to compute eigenvalues of similarity matrix (derived from distance matrix and degree matrix). One drawback of this method is that it requires the number of clusters, but we could estimate this using k-means with silhouette width as seen in the lectures. Another trick would be projecting the points into a non-linear embedding and analyze the eigenvalues of the Laplacian matrix. This would allow us to deduce the number of clusters present in the data. This would require our similarity graph to be not fully connected. Another drawback is the runtime, which is O(N<sup>3</sup>) without optimization (such as [Fast kernel spectral clustering](https://www.sciencedirect.com/science/article/abs/pii/S0925231217307488))

The second option would be [DBSCAN](https://en.wikipedia.org/wiki/DBSCAN). Since we already have the positions, we could derive the maximum distance between nodes we would set for the algorithm. An advantage is that we don't need to know the number of clusters beforehand. However, we need to be careful when selecting the distance and minimum neighbour required. Also, DBSCAN could detect anomalies in the graph, nodes that are either noise or outliers. We need to be very careful in the interpretation of those nodes should we have any. As seen in class, runtime is O(N log(N)).

Finally, we have [hierarchical clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering). As stated before, we would like to not have the find the number of clusters beforehand. Even if spectral clustering would not allow that, DBSCAN solved this problem. However, DBSCAN is also based on density, and we need to find a good distance parameter to get good results. This option would allow us to solved those two problems. Indeed, hierchical clustering do not require the number of clusters, and we don't have the trouble of setting minimal distance. However, this technic might struggle when facing cluster sizes of vastly different sizes (which seems to be our case by looking at our graph). Moreover, as seen in class, the run time is O(N<sup>3</sup>) without priority queue.

All those options are featured in the `Scikit-learn` library, should we want to use them as such.

## Proposed Timeline

### Week 47

- Focusing on homework 2 and ideally finishing it
- Implement changes on project according to feedback from Milestone 2 (if available)

### week 48

- If not finished, complete homework 2. 
- Generate graph with preprocessed data from Milestone 2. It is  important to have a complete graph on all the data. We should be able to visually identify clusters and possible outliers. 
- Compute clusters.
- Start data story.

### week 49

- Analyze/compare clusters. Understand what are the key features of those clusters.
- Compute outliers and analyze them. Understand what traits makes an outlier and verify if they act as bridges between different clusters. Verify if multiple outliers have shared traits.
- Update data story accordingly.

### week 50

- Start data story.
- Choose a cluster for in-depth anaylsis. Check if there exist clusters within clusters. Do the same with outliers. 
- Update data story accordingly.

### week 51

- Finish data story
- complete and update files for submission.

## Team-internal Organization

## Questions for TAs
