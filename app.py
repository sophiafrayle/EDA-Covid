import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
file_path = '/Users/sofia.fraile/Documents/Portfolio/COVID Project/owid-covid-data.csv'
df = pd.read_csv(file_path)

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Streamlit app layout
st.title('COVID-19 Deaths, Vaccinations, Simulation')

st.sidebar.title('Filter Options')

# Select locations to display
locations = st.sidebar.multiselect(
    'Select Locations',
    options=df['location'].unique(),
    default=['Mexico', 'Netherlands']  # Default to first 5 locations
)

# Filter dataframe based on selected locations
filtered_df = df[df['location'].isin(locations)]

# Plot total confirmed cases over time
fig_total_cases = px.line(
    filtered_df,
    x='date',
    y='total_cases',
    color='location',
    title='Total Confirmed Cases Over Time',
    labels={'total_cases': 'Total Cases', 'date': 'Date'}
)
st.plotly_chart(fig_total_cases, use_container_width=True)

# Plot new confirmed cases over time
fig_new_cases = px.line(
    filtered_df,
    x='date',
    y='new_cases',
    color='location',
    title='New Confirmed Cases Over Time',
    labels={'new_cases': 'New Cases', 'date': 'Date'}
)
st.plotly_chart(fig_new_cases, use_container_width=True)

# Plot total deaths over time
fig_total_deaths = px.line(
    filtered_df,
    x='date',
    y='total_deaths',
    color='location',
    title='Total Deaths Over Time',
    labels={'total_deaths': 'Total Deaths', 'date': 'Date'}
)
st.plotly_chart(fig_total_deaths, use_container_width=True)

# Plot new deaths over time
fig_new_deaths = px.line(
    filtered_df,
    x='date',
    y='new_deaths',
    color='location',
    title='New Deaths Over Time',
    labels={'new_deaths': 'New Deaths', 'date': 'Date'}
)
st.plotly_chart(fig_new_deaths, use_container_width=True)

# Plot total vaccinations over time
fig_total_vaccinations = px.line(
    filtered_df,
    x='date',
    y='total_vaccinations',
    color='location',
    title='Total Vaccinations Over Time',
    labels={'total_vaccinations': 'Total Vaccinations', 'date': 'Date'}
)
st.plotly_chart(fig_total_vaccinations, use_container_width=True)

# Display summary statistics
st.header('Summary Statistics')
st.write(filtered_df.describe())

# Display correlation matrix heatmap
numeric_df = filtered_df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_df.corr()
fig_corr = px.imshow(
    correlation_matrix,
    title='Correlation Matrix',
    labels={'color': 'Correlation Coefficient'}
)
st.plotly_chart(fig_corr, use_container_width=True)


# Interactive case scenario simulator
st.header('Case Scenario Simulator')

# Adjust reproduction rate
reproduction_rate = st.slider('Reproduction Rate (R)', 0.5, 3.5, 1.2, 0.1)

# Adjust vaccination rate
vaccination_rate = st.slider('Vaccination Rate (% of population per day)', 0.0, 1.0, 0.1, 0.01)

# Adjust stringency index
stringency_index = st.slider('Policy Stringency Index (0-100)', 0, 100, 50, 5)

# Simulate new cases based on reproduction rate
days_to_simulate = 30
last_day_data = filtered_df.groupby('location').last().reset_index()
simulated_data = []

for _, row in last_day_data.iterrows():
    cases = row['new_cases']
    population = row['population']
    vaccinated = row['people_vaccinated'] if 'people_vaccinated' in row else 0
    
    for day in range(days_to_simulate):
        susceptible = population - cases - vaccinated
        new_cases = reproduction_rate * (cases / population) * susceptible
        vaccinated += vaccination_rate * population / 100
        
        cases += new_cases
        simulated_data.append([row['location'], row['date'] + pd.Timedelta(days=day+1), cases])

simulated_df = pd.DataFrame(simulated_data, columns=['location', 'date', 'simulated_cases'])

# Plot simulated new cases
fig_simulated_cases = px.line(
    simulated_df,
    x='date',
    y='simulated_cases',
    color='location',
    title='Simulated New Cases Over Time',
    labels={'simulated_cases': 'Simulated Cases', 'date': 'Date'}
)
st.plotly_chart(fig_simulated_cases, use_container_width=True)

# # Save the cleaned and processed data
# cleaned_file_path = 'path/to/save/cleaned_covid_data.csv'
# filtered_df.to_csv(cleaned_file_path, index=False)
# st.write(f"\nCleaned data saved to {cleaned_file_path}")

# # Check for missing values
# st.header('Missing Values')
# missing_values = filtered_df.isnull().sum()
# st.write(missing_values)