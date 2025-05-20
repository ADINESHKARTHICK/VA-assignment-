import numpy as np
years = list(range(2010, 2021))
data = []
     

for year in years:
    temp = df.copy()
    temp['Year'] = year
    # Simulate change in renewable energy usage
    temp['Renewable_Energy'] = temp['Renewable_Energy'] * (1 + 0.03 * (year - 2010)) + np.random.rand(len(temp)) * 50
    temp['Total_Energy'] = temp['Renewable_Energy'] * np.random.uniform(2, 5, len(temp))
    data.append(temp)
     

df_all = pd.concat(data)
     

fig_choropleth = px.choropleth(df_all,
                                locations="Code",
                                color="Renewable_Energy",
                                hover_name="Country",
                                animation_frame="Year",
                                color_continuous_scale="Greens",
                                title="Global Renewable Energy Usage (%) Over Time")
     

fig_choropleth.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
fig_choropleth.show()
     

fig_bubble = px.scatter_geo(df_all,
                            locations="Code",
                            color="Renewable_Energy",
                            hover_name="Country",
                            size="Total_Energy",
                            animation_frame="Year",
                            projection="natural earth",
                            title="Total Energy Usage and Renewable Energy (%) Over Time",
                            color_continuous_scale="Viridis")
     

fig_bubble.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
fig_bubble.show()
