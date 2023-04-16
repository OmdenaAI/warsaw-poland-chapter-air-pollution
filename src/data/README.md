# Data

This folder contains all the data relevant to this project.

* `data_raw`: contains the original, unprocessed data from the data sources as provided at the beginning of the project
* `data_translated`: contains the dataset `daily_air_quality_data_2015-2021` translated to English and truncated to 2017-2021
* `data_auxiliary`: contains auxiliary files used at different stages of the project
* `data_processed`: contains the processed data from the data sources
* `data_imputed`: contains the imputed data sets for weather and pollutants
* `data_merged`: contains the datasets merged from weather, pollutant, and static annual data
* `final_data`: contains the final dataset with CAQI values

After additional feature engineering was performed on the final dataset, the datasets in `data_for_modelling` were used to train the air-quality prediction models:
* temporal: with lag and window features (used for forecasting)
* non-temporal: without lag and window features

The data in `data_for_forecasting` was used to make forecasts beyond the considered period 2015-2021.





