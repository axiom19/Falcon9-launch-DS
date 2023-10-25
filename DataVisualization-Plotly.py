# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',options=[
                                    {'label' : 'All Sites', 'value': 'ALL'},
                                    {'label' : 'CCAFS LC-40', 'value' : 'CCAFS LC-40'},
                                    {'label' : 'KSC LC-39A', 'value' : 'KSC LC-39A'},
                                    {'label' : 'VAFB SLC-4E', 'value' : 'VAFB SLC-4E'},
                                    {'label' : 'CCAFS SLC-40', 'value' : 'CCAFS SLC-40'}
                                ],
                                value='ALL',
                                placeholder='Search a Launch Site',
                                searchable=True
                                ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(figure={}, id='success-pie-chart')),
                                html.Br(),
                                html.P("Payload range (Kg):"),

                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(
                                    id='payload-slider',
                                    min= 0, max=10000, step=1000,
                                    marks={
                                        0:"0",
                                        100:"100"
                                    },
                                    value=[min_payload, max_payload]
                                    ),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(figure={}, id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    # First, group the data by 'class' column (success/failure) 
    # to get counts of each class for the entire dataset or for a specific site
    if entered_site == 'ALL':
        data_grouped = spacex_df.groupby('class').size().reset_index(name='counts')
        title = 'Total Launches for all sites'
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        data_grouped = filtered_df.groupby('class').size().reset_index(name='counts')
        title = f'Total Launches for site {entered_site}'

    # Create the pie chart
    fig = px.pie(
        names=data_grouped['class'].tolist(),
        values=data_grouped['counts'].tolist(),
        title=title,
        color=data_grouped['class'].tolist(),
        color_discrete_map={0: 'red', 1: 'green'}
    )
    
    return fig


# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value'),
    Input(component_id='payload-slider', component_property='value')
)
def get_scatterplot(entered_site, payload_range):
    # Filter the DataFrame based on the selected payload range
    low, high = payload_range
    mask = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered_df = spacex_df[mask]
    
    # Check if a specific site is selected or if 'ALL' is selected
    if entered_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
    
    # Render the scatter plot
    fig = px.scatter(
        filtered_df, 
        x='Payload Mass (kg)', 
        y='class',  # Assuming 'class' column contains launch outcomes
        color="Booster Version Category",
        title=f"Payload vs. Outcome for {entered_site}" if entered_site != 'ALL' else "Payload vs. Outcome for ALL Sites"
    )

    return fig



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=7000)
