# 2022 ADA Project by team TACOCAT

Follow the [instructions](docs/instr.md) on how to use this repository. 

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
