synthetic_time_series
==============================

This project repo contains experiments with synthetic price/return series generation. 

Currently the project is investigating methods of block bootstrapping for generating realistic looking price series, but as time permits other models and methodologies will be explored.

Some ideas for future experiments:
- stationary bootstrap
- cut and paste blocks from correlated assets
- cut and paste blocks from different assets
- mixture models for generating paths
- "traditional" model based generation

Project Organization
--------------------

    .
    ├── AUTHORS.md
    ├── LICENSE
    ├── README.md
    ├── bin
    ├── config
    ├── data
    │   ├── external
    │   ├── interim
    │   ├── processed
    │   └── raw
    ├── docs
    ├── notebooks
    ├── reports
    │   └── figures
    └── src
        ├── data
        ├── external
        ├── models
        ├── tools
        └── visualization
