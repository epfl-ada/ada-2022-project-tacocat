## Repository Structure

```bash
├── data
│   ├── cmu_movie_summary_corpus
│   └── imdb
├── docs
│   └── instr.md
├── generated
│   ├── graphs
│   └── legacy
├── README.md
├── requirements.txt
├── results
│   └── graphs
├── src
│   ├── eda
│   └── utils
│       ├── data_generated.py
│       ├── data_initial.py
│       ├── data_processing.py
│       └── freebase.py
└── temp
```

- [data](../data/) contains the initial datasets used for this project.
- [docs](../docs/) contains various documentation.
- [generated](../generated/) contains the processed data, ready for analysis.
- [generated/legacy](../generated/legacy/) contains generated data, no longer used for the project but still relevant for something (e.g. a milestone submission)
- [requirements.txt](../requirements.txt) contains the required python libraries for this project.
- [results](../results/) contains the results from our analysis.
- [src](../src/) contains the projects code.
- [src/utils](../src/utils/) contains scripts providing functions that may be useful throughout the project.
- temp may be used to store temporary data. It is not tracked by git.

## Repository Usage

- [data_generated.py](../src/utils/data_generated.py) contains the functions used to load the data used in the project. __Only data loaded using these functions should be used for working on the data story.__

- Any code should be placed in the [source folder](../src/)

- Any result should be placed in the [results folder](../results/)

## Reproduce data generation

If you want to generate data for usage in the project, follow the READMEs in [data](../data/) to download the initial datasets. Then use the [data generation notebook](../src/generate_data.ipynb) to generate the data.

## requirements.txt

Use the `pireqsnb` python library to generate it.
