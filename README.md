# ThermaLogic – Interactive Heat Demand Analysis

[**English**](README.md) | [Deutsch](README.de.md)

## Project Overview

ThermaLogic is a Streamlit application developed as a **group project** for the university module *Projekt Wissenschaftliches Arbeiten* (Scientific Project Work). It allows users to explore combined space-heating demand for different building categories using supplied time-series datasets. Users choose building types and quantities, visualize the aggregated demand over time, and download results as CSV.

The application supports schools, hospitals, single-family houses, and retail buildings.

## Methodology and Features

1. **Load time-series data:** Read semicolon-separated CSV files for the four building categories with Pandas and parse the `Zeit` (time) column
2. **Select a building mix:** Choose up to four building types and enter the quantity for each
3. **Calculate demand:** Multiply each selected category's `Raumwaerme` values by its quantity, merge the resulting time series by timestamp, and calculate the total heating demand (`insgesamt_kWh`)
4. **Visualize results:** Display the aggregated time series as an interactive Plotly line chart
5. **Export and navigate:** Download the calculated data as CSV and use the application's navigation, documentation, history, and team-information tabs

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly Express
- Pillow (PIL)

## My Contribution

This was a collaborative project. **My personal contributions were the following two modules:**

- **`home.py` – Home page:** Implemented the Streamlit landing page, introductory content, two image panels, and the overview of the application's features.
- **`time_series.py` – Heat demand analysis:** Implemented loading and date parsing of the four CSV datasets, building-category and quantity inputs, quantity-weighted calculations, merging time series, the total-demand chart, and CSV download. The module also calls the shared history component.

The other modules and the overall application belong to the **group project** and are not presented as solely my work.

## Interpretation and Limitations

- The application calculates **scenario-based demand from existing time series**; the inspected code does **not** train or evaluate a forecasting or machine-learning model.
- Results depend on the source datasets, their units, and the selected building quantities.
- The project code was inspected, but the full application has not been independently run and verified in a clean environment.

