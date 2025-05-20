import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("Significant Earthquake Dataset 1900-2023.csv")

# Convert 'Time' to datetime and extract year
df['Time'] = pd.to_datetime(df['Time'], errors='coerce')
df['Year'] = df['Time'].dt.year

# Clean data: drop missing lat/lon/magnitude
df_clean = df.dropna(subset=['Latitude', 'Longitude', 'Mag'])

# ----------------------
# Bubble Map (Individual Earthquakes)
# ----------------------
bubble_map = px.scatter_geo(
    df_clean,
    lat='Latitude',
    lon='Longitude',
    color='Mag',
    size='Mag',
    hover_name='Place',
    animation_frame='Year',
    projection='natural earth',
    title='Global Significant Earthquakes (1900–2023)',
    color_continuous_scale='Turbo'
)
bubble_map.update_layout(geo=dict(showland=True, landcolor='rgb(217, 217, 217)'))

# Save as HTML
bubble_map.write_html("earthquake_bubble_map.html")

# ----------------------
# Choropleth Map (Avg. Magnitude per Country by Year)
# ----------------------
# Extract country names from 'Place' (last part after comma)
df_clean['Country'] = df_clean['Place'].apply(lambda x: x.split(',')[-1].strip() if pd.notnull(x) and ',' in x else None)
df_country = df_clean.dropna(subset=['Country'])

# Aggregate average magnitude by country and year
choropleth_data = df_country.groupby(['Year', 'Country'])['Mag'].mean().reset_index()

choropleth_map = px.choropleth(
    choropleth_data,
    locations='Country',
    locationmode='country names',
    color='Mag',
    animation_frame='Year',
    color_continuous_scale='Plasma',
    title='Average Earthquake Magnitude by Country Over Time'
)
choropleth_map.update_layout(geo=dict(showframe=False, showcoastlines=True))

# Save as HTML
choropleth_map.write_html("earthquake_choropleth_map.html")
