# Magnets in the Movie Industry 🧲

## 🗃️ Repository Organization

For information on repository organisation, see the [instructions](docs/instr.md).

The entry point for evaluating our milestone 2 submission is the [milestone 2 notebook](milestone_2.ipynb).

The entry point for evaluating our milestone 3 submission is the [milestone 3 notebook](milestone_3.ipynb). Note that it is an updated version of the milestone 2 submission.

## 🌐 Data Story

For data story click [here](https://tacocat-ada.github.io/) or go to https://tacocat-ada.github.io/

## 📔 Abstract

It's no secret that being in the right social circle the film industry is very important to have a successful film career. In this project we will be analysing the people in the industry (actors, directors, writers, etc.) to further investigate the existence of clusters of people who know each other. Then zoom into the significant clusters to investigate further why these clusters exist, what makes them unique, who are the key people that bridge different clusters and who are left out. We will look at each cluster’s common attributes and tie them into real movie industries. Our main goal is to create a social map of the film industry.


## ❔ Research Questions

- Are there clusterings between the people in the film industry?
    - What are the common attributes of people in the same cluster?
    - Are there people without a cluster? What makes them unique?
- As representation and diversity have more space in conversations today, do we observe the same awareness in the film industry?
    - Are women employed equally to men?
    - How diverse is each cluster?

## 📽️ Additional Datasets Used

In addition to the [CMU movie dataset](http://www.cs.cmu.edu/~ark/personas/), we use the [IMDb datasets](https://www.imdb.com/interfaces/). Using this additionnal dataset will allow us to have data on more people for each movie. This does not only include actors, but also producers, writers and so on. It will also allow us to have movie rating data, which could prove useful for our cluster analysis.

We merge the two datasets on movie title. The exact procedure is done and described in our data [generation notebook](src/generate_data.ipynb) for both movie metadata (Combine CMU with IMDB) and people (Process the other datasets/People).

The resulting dataset is presented in our descriptive analysis in the [submission notebook](milestone_2.ipynb).

## 🪧 Methods

### Step 1: Drawing the Network Graph

- Using Fruchterman-Reingold [force-directed algorithm](https://en.wikipedia.org/wiki/Force-directed_graph_drawing#Methods) since this algorithm emphasize the position of the nodes, assuring as few edge crossings and distance disparities as possible. The algorithm works similarly to the interaction between attractive and repelling forces. The edges between nodes are the springs that pull closer, and the nodes themselves are the object exerting push.
    - It is worth noting that the algorithm iterates until it reaches an equilibrium, so it can take a long time to finish. In worst cases, it can take up to O(N<sup>3</sup>), although optimization can improve the running time to be O(N<sup>2</sup> log(N)), where N is the number of nodes. It is for this reason that we decided to save a serialized version of the result using `Pickle`. 
- We used the package `NetworkX` which provides useful tools and functions for complex networks.

### Step 2: Selecting Clustering Coefficient

- To compute the [clustering coefficient](https://en.wikipedia.org/wiki/Clustering_coefficient), which indicates the degree nodes in a graph tend to cluster together, we also used the package `NetworkX`. 
- Those coefficients would allow use to efficiently compute the clusters and visually seperate the different nodes within the graph (by colors, sizes, and so forth).

### Step 3: Clustering

- We used unsupervised methods, since our nodes are not labelled. We initially selected three methods that seem promising to achieve what we desire, they were [spectral clustering](https://en.wikipedia.org/wiki/Spectral_clustering), [DBSCAN](https://en.wikipedia.org/wiki/DBSCAN) and [hierarchical clustering](https://en.wikipedia.org/wiki/Hierarchical_clustering).
- But in the end, we decided to use [OPTICS](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.OPTICS.html), a close relative to DBSCAN which performs better on large datasets than the `Scikit-learn` implementation of others.
- We only kept the clusters with size more than 400 to be able to generalize well with our analysis.

### Step 4: Cluster Analysis
- With this step, we created plots to answer our research questions on clusters and their unique features. In this step we used `matplotlib.pyplot` library to visualize our data.We always dropped NaN values in our analysis.

- **Are there clusterings between the people in the film industry?**
    - With the clustered graph, we know that the answer is yes.

- **What are the common attributes of people in the same cluster? As representation and diversity have more space in conversations today, do we observe the same awareness in the film industry? Are women employed equally to men? How diverse is each cluster?**
    - On an initial analysis, we saw that people that could be from the same ethnicity was clustered together. Thus we first plotted ethnicity values for each cluster.
    - We saw that ethnicities differ between each cluster, thus we named the clusters by the highest occuring ethnicity values.
    - Then, we plotted the genre, profession, age and gender distribution of each cluster to understand the attributes of each cluster. We also presented information from news articles to support our results.

### Step 5: Outlier and Key People Analysis
- **Are there people without a cluster? What makes them unique?**
    - We saw that more than half of the people were not placed in a cluster, thus we analyzed them further.
    - We plotted the ECDF analysis from `Seaborn` library to understand the connectivity of outliers to each other and clusters.
    - We kept the top 1% of outliers (in terms of connectivity) to ensure a logical analysis.
    - We plotted their profession and ethnicity information to understand who they are.
    - And finally we selected two of the outliers who were interesting to analyze; A.R. Rahman, the most connected outlier to clusters and Takashi Miike, an outlier mostly connected to other outliers.

### Step 6: Data Story
- We used Github pages and the Cayman( a Jekyll theme) to create the data story.
- Since the network plots are rather large, we created an interactive zoom tool by using CSS styles and JavaScript functions (Code source: [W3Schools](https://www.w3schools.com/howto/howto_js_image_magnifier_glass.asp)).
- In the data story, we discuss our results and the methods mentioned above.

## 📅 Proposed Timeline

| Week         | Tasks |
|--------------|:-----|
| Week 47      |  Implement changes on project according to feedback from Milestone 2. Start Homework 2. |
| Week 48      |  Generate graph with preprocessed data from Milestone 2. Computer clusters, visualize clusters and possible outliers. Finish Homework 2.|
| Week 49      |  Analyze/compare clusters. Understand what are the key features of those clusters. Compute outliers and analyze them. Understand what traits makes an outlier and verify if they act as bridges between different clusters. Verify if multiple outliers have shared traits. |
| Week 50      |  Start data story, in-depth analysis of clusters and outliers. |
| Week 51      |  Finish data story, finalize repository for submission. |

## ⚙️ Team-internal Organization

| Member Name  | Tasks |
|--------------|:-----|
| Edin         |  Defining and writing methods, building network graphs, clustering, and generating graph visualizations. |
| Güneş      |  Writing abstract, organization and data story, building the website, and updating README for M3. |
| Jonas      |  EDA, analysing outliers and visualization, and writing first draft of this part of the data story. |
| Louca      |  Defining and writing methods, creating project timeline, analysing clusters and visualizations. |
