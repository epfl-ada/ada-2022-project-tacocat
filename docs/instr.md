## Repository Structure and Usage

```bash
├── data
│   ├── cmu_movie_summary_corpus
│   └── imdb
├── docs
├── generated
├── README.md
├── requirements.txt
├── results
├── src
│   ├── generate_data.ipynb
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
- [requirements.txt](../requirements.txt) contains the required python libraries for this project.
- [results](../results/) contains the results from our analysis.
- [src](../src/) contains the projects code.
- [src/utils](../src/utils/) contains scripts providing functions that may be useful throughout the project.
- [temp](../temp/) may be used to store temporary data

The essentials to work on the project are:

- [generate_data.ipynb](../src/generate_data.ipynb) contains the pipeline used to generate the data for analysis in the project.
- [data_generated.py](../src/utils/data_generated.py) contains the functions used to load the data used in the project. This data should only be loaded using those functions.

## Get initial datasets

If you want to generate data for usage in the project, follow the READMEs in [data](../data/) to download the initial datasets.

## requirements.txt

Use the `pireqsnb` python library to generate it.
