# NaPTAN Bus Stop Visual Analytics and Geospatial Preprocessing

**Status: Early geospatial/visual analytics project | Core preprocessing and exploratory analysis complete**

This project explores UK bus stop data from the **NaPTAN (National Public Transport Access Nodes)** dataset through iterative preprocessing, geospatial cleaning, and visual analytics.

The work focused on cleaning a large real-world transport dataset, restoring missing coordinates, filtering to relevant bus stop records, and preparing grouped datasets for analysis of stop density, locality characteristics, and maintenance-related temporal behaviour.


---


## Overview

The original aim of the project was to investigate disparities between bus stops across different types of areas. As the work evolved, the project became more focused on the data engineering and analytical preparation needed to support visual exploration.

The strongest completed parts of the project are:

- large-scale missing data handling
- coordinate restoration using Easting/Northing conversion
- filtering to relevant bus stop categories
- narrowing the dataset from national scope to Greater London
- locality-level grouping
- administrative-area density analysis
- temporal feature extraction from creation and modification timestamps


---


## Dataset

**Source:** UK Government NaPTAN dataset  
**Name:** National Public Transport Access Nodes (NaPTAN)

The raw dataset initially contained:

- **435,046 rows**
- **43 columns**

The dataset includes:

- stop identifiers
- locality information
- Easting / Northing coordinates
- Longitude / Latitude coordinates
- stop type and bus stop type
- administrative area codes
- creation and modification timestamps
- revision and modification metadata


---


## Project goals

Across its iterations, the project focused on the following analytical questions:

- what can be visualised about maintenance activity using modification timestamps, revision counts, and modification status?
- how do bus stop densities vary across administrative areas?
- what patterns emerge when stops are grouped by locality name and locality-centre status?
- how can a large transport dataset be cleaned and reduced into more usable analytical subsets?

An earlier north/south clustering branch was also explored, but this became secondary to the stronger locality, density, and temporal analyses.


---


## Repository structure

```text
visual_analytics_naptan_disparities_project/
├── docs/
│   ├── references.md
│   └── research_plan.md
├── images/
│   ├── preprocessed_data_variables.png
│   ├── visual_analytics_detailed.png
│   └── visual_analytics_simplified.png
├── notebooks/
│   ├── data_preprocessing.ipynb
│   └── visual_analytics.ipynb
├── outputs/
├── .gitignore
├── README.md
└── requirements.txt
```

---


## Repository structure

The project followed an iterative visual analytics approach inspired by Schneiderman's mantra:

- Overview
- Zoom
- Filter
- Details-on-demand
- Relate
- History
- Extract

The main workflow was:

1. Inspect the raw NaPTAN dataset
2. Clean and reduce the missing values
3. Recover missing longitude/latitude values from Easting/Northing
4. Remove low-value or highly incomplete columns
5. Filter to the relevant bus stop categories
6. Reduce the project scope to Greater London
7. Generate processed datasets for separate analytical questions
8. Visualise stop types, densities, locality grouping, and temporal patterns


---


## Key preprocessing steps

A major part of this project was devoted to preparing the data for analysis.

### Cleaning and filering

- Removed rows marked as deleted and inactive
- Standardised the mixed boolean-style values found in the LocalityCentre column
- Dropped the columns with more than 40% missing data
- Removed the rows that were missing critical identifiers such as the NaptanCode column/feature
- Dropped the rows with missing Modification column values after processing other filtering stages
- Filtered transport stop records down to bus-stop related StopType column values only

### Geospatial recovery

The rows with missing Longitude and Latitude column values were restored using existing Easting and Northing column values through pyproj coordinate conversion.

This recovered 52,389 rows that would have been lost otherwise. 

### Imputation and type handling

- Imputed selected categorical fields such as BusStopType and TimingStatus columns
- Filled in the missing RevisionNumber column values with zero
- Converted the datetime fields for temporal analysis
- Converted several text columns to the categorical dtype to reduce memory usage


---


## Final scoped dataset

After the iterative preprocessing process:

- The dataset was reduced from the full national NaPTAN set
- Non-bus stops were removed
- The scope was narrowed down to include Greater London only
- A London-focused subset of 18,999 rows was used for the final scoped analysis


---


## Analytical outputs

This project created processed datasets for different questions, for example:

### Q2: Locality grouping

The stops were grouped by the following columns:

- LocalityName
- LocalityCentre

The derived outputs include the following:

- Stop count
- Most recent modification date
- Total revision count

### Q3: Stop density by administrative area

The stops were grouped by the following column:

- AdministrativeAreaCode

The derived outputs include the following:

- Stop count
- Density proxy for administrative areas

### Q4: Temporal feature extraction

The features derived from creation and modification timestamps included the following columns:

- TimeSinceCreation
- TimeSinceModification


---


## Visual analytics work:

The visual analysis notebook includes work on the following:

- Stop type distributions
- Bus stop type distributions
- Grouped locality trends
- Maintenance-related time trends
- Administrative area density plots
- Temporal distributions of bus stop creation and modification

This project also experimented with interactive mapping and clustering workflows, although these were not the strongest final outcome.


---


## Main outcomes

The strongest technical outcomes of the project include the following:

- A successful preparation of a large messy transport dataset for analysis
- A restoration of missing geospatial coordinates
- A creation of grouped analytical datasets for locality, density, and temporal questions
- Memory-aware datatype optimisation
- An iterative refinement of scope when the original framing became too broad


---


## Limitations

This was an early MSc project and this should be read as an exploratory analytical workflow rather than a polished production repository.

The known limitations include the following:

- The repository is primarily notebook-based
- There is no src directory
- The original rural/urban objective was not finalised successfully
- One exploratory north/south clustering branch was only partially convincing in a methodological sense.
- Some of the notebook cells include package installation commands that should be moved out of the notebooks
- One temporal analysis notebook ends with an incomplete cell/error
- The density metric uses a simplified area approximation rather than a more rigorous geospatial method


---


## How to run

1. Clone the repository

git clone https://github.com/CharlieMaguire1/visual_analytics_naptan_disparities_project

cd visual_analytics_naptan_disparities_project

2. Install dependencies

pip install -r requirements.txt

3. Open the notebooks

The notebooks are:

- notebooks/data_preprocessing.ipynb
- notebooks/visual_analytics.ipynb

These files contain the preprocessing workflow and the visual analytics workflow respectively.


---


## Requirements

This repository currently includes a notebook-focused analysis using Python libraries such as:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- pyproj
- geopy
- folium
- geopandas
- osmnx
- pyarrow


---


## Technical skills demonstrated

- Python
- Pandas data manipulation
- Geospatial preprocessing
- Coordinate conversion
- Missing data analysis
- Imputation
- Datetime feature engineering
- Grouping and aggregation
- Exploratory visual analytics
- Working with large public datasets
- Iterative scoping of the analysis problems


---


## Notes

This project should be seen as an early geospatial and visual analytics project showing how I approached a large real-world public transport dataset, refined the scope according to time constraints, and built a reusable preprocessing and analysis workflow.

The strongest portfolio value comes from the preprocessing decisions, geospatial restoration, and grouped analytical outputs rather than from a single final model or a dashboard. 


---


## Author

Charlie Maguire
