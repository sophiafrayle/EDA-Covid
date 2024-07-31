![Project Banner](https://github.com/sophiafrayle/EDACovid/blob/main/images/Screenshot%202024-07-30%20at%2021.37.45.png)

# COVID-19 Data Exploration and Scenario Simulator


## Introduction

Welcome to the COVID-19 Data Exploration and Scenario Simulator. This interactive Streamlit app allows users to explore and analyze COVID-19 data from around the world. The app provides detailed visualizations of various COVID-19 metrics, and includes an interactive simulator to model the potential impacts of different scenarios on case numbers.

## Features

- **Data Visualization**: Interactive line charts for total cases, new cases, total deaths, new deaths, and total vaccinations.
- **Summary Statistics**: Display of basic summary statistics and missing values.
- **Correlation Matrix**: Heatmap of the correlation matrix for numerical variables.
- **Case Scenario Simulator**: Allows users to adjust reproduction rate, vaccination rate, and policy stringency to simulate new cases over the next 30 days.
- **Comparative Analysis**: Enables users to filter and compare data across different countries or regions.

## Installation

To run this project locally, you'll need to have Python installed. Follow these steps to set up the project:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/covid-data-exploration.git
    cd covid-data-exploration
    ```

2. **Install the required packages**:
    ```bash
    pip install streamlit plotly pandas
    ```

3. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

## Usage

Once the app is running, you can access it in your web browser. The sidebar contains filters and sliders for customizing the data view and simulation parameters.

### Filter Options

- **Select Locations**: Choose the countries or regions you want to explore.
- **Adjust Simulation Parameters**: Modify the reproduction rate, vaccination rate, and policy stringency to see how they impact new cases over time.

### Data Visualizations

The app provides various interactive charts:
- **Total Confirmed Cases Over Time**
- **New Confirmed Cases Over Time**
- **Total Deaths Over Time**
- **New Deaths Over Time**
- **Total Vaccinations Over Time**

### Case Scenario Simulator

Adjust the reproduction rate, vaccination rate, and policy stringency to simulate new cases for the next 30 days. This helps to visualize potential future trends based on different scenarios.

## Screenshots

### Total Confirmed Cases Over Time
![Total Confirmed Cases](https://github.com/sophiafrayle/EDACovid/blob/main/images/Screenshot%202024-07-30%20at%2021.17.58.png)

### New Confirmed Cases Over Time
![New Confirmed Cases](https://github.com/sophiafrayle/EDACovid/blob/main/images/Screenshot%202024-07-30%20at%2021.18.08.png)

### Total Deaths Over Time
![Total Deaths](https://github.com/sophiafrayle/EDACovid/blob/main/images/Screenshot%202024-07-30%20at%2021.18.13.png)

### Case Scenario Simulator
![Case Scenario Simulator](https://github.com/sophiafrayle/EDACovid/blob/main/images/Screenshot%202024-07-30%20at%2021.18.43.png)

## Data Source

The data used in this project is sourced from the [Our World in Data COVID-19 dataset](https://github.com/owid/covid-19-data/tree/master/public/data). This dataset includes comprehensive information on confirmed cases, deaths, hospitalizations, testing, and vaccinations.


## Acknowledgements

I would like to thank the contributors of the [Our World in Data](https://github.com/owid/covid-19-data) project for providing comprehensive and accessible COVID-19 data.

---

*This project is a work in progress and we welcome any suggestions or improvements. Please feel free to open issues or pull requests.*

![Footer Image](images/Sophia Frayle.png)
