import dash
import dash_table
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

external_stylesheets = [dbc.themes.BOOTSTRAP]

#create app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
#read file Energy Generated
energy=pd.read_csv('https://opendata.maryland.gov/api/views/79zg-5xwz/rows.csv?accessType=DOWNLOAD')
energy=energy.fillna(0)
energy=energy.drop([energy.index[8], energy.index[9]])
energy=energy.sort_values('Year')

#read file Energy Capacity
capacity=pd.read_csv('https://opendata.maryland.gov/api/views/mq84-njxq/rows.csv?accessType=DOWNLOAD')
capacity = capacity.fillna(0)
capacity = capacity.sort_values('Year')
capacity['Year']=capacity['Year'].astype(float)

a=pd.DataFrame()
melt_energy=pd.melt(energy, id_vars=['Year'])
melt_cap=pd.melt(capacity, id_vars=['Year'])
f=melt_energy[melt_energy['variable']=='Electricity Generation from Renewable Sources (MWh)'],
label=['2007','2008','2009','2010','2011', '2012','2013','2014','2015','2016']

fig=go.Figure(data=[
                go.Bar(name='Renewable', x=label, y=melt_energy[melt_energy['variable']=='Electricity Generation from Renewable Sources (MWh)']['value']),
                go.Bar(name='All Sources', x=label, y=melt_energy[melt_energy['variable']=='Electricity Generation from All Sources (MWh)']['value'])  
                ])
fig.update_layout(barmode='group',  title_text='Electricity Generation Comparison')
fig2=px.bar(f,x=label, y=melt_energy[melt_energy['variable']=='Electricity Generation from Renewable Sources (MWh)']['value'], 
color=label, labels={'x':'Years', 'y':'MWh'})
fig2.update_layout(title_text='Electricity Generation from Renewable Sources (MWh)')

#Logo to be added next to title
PLOTLY_LOGO="https://pics.clipartpng.com/midle/Renewable_Energy_PNG_Clipart-2976.png"

####################
#### About page ####
page_1=html.Div([
    
    dcc.Markdown([
        ('''
    ## About


     This app contains two datasets regarding the recorded generated renewable energy 
     and the estimated generating capacity for each renewable source type.
     The first dataset estimates the installed capacity for renewable energy generation in Maryland, in 
     megawatts (MW). Reported data comes from energy generators in Maryland registered to generate 
     renewable energy credits (RECs) through the PJM Environmental Information Services (EIS) 
     Generation Attributes Tracking System (GATS) (available [here](https://gats.pjm-eis.com/gats2/PublicReports/RenewableGeneratorsRegisteredinGATS)).

     Please note, as renewable energy generators are not required to register in GATS, there may be some renewable energy 
    generation capacity installed in Maryland but not generating RECs that is not captured in this estimate. 
    The second data set describes the amount of energy generated annually by renewable sources 
    in Maryland in megawatt hours (MWh). In addition, there is a column which describes 
    the percent of all energy generated in Maryland coming from renewable sources each year.
    Renewable energy generation data comes from PJM's Generation Attribute Tracking System 
    (PJM GATS). Total generation comes from the U.S. Energy Information Administration's State 
    Level Generation report, released in October 2016 with revisions in November 2016. 
    ([Click here to access the U.S. Energy Information Administration page](https://www.eia.gov/electricity/data.php))

     As you navegate through the app, you will have access to the dataset through the *Data* tab. Then, in the
     *Generation Capacity* tab, you will be able to access the dataset for the annual estimated renewable energy 
     generating capacity (2006-2017) and you will be able to create your own plot. Likewise, in the *Energy Generated*
     tab you will access this dataset and generate your own plot.

    ##### Preview

     From the menu below, you may select an analysis. The first plot *Renewable Energy Over the Years* will display the 
     total electricity generated from all renewable sources over the years in MWh. The second option will portray the total
     electricity generated in the State of Maryland from all sources in MWh. Both plots will open in a new window.
     
    ''')],
    style={'marginLeft': 70, 'marginRight': 90, 'marginTop': 10, 'marginBottom': 10,
    'color': '#696969', 'align':'center'}),

    html.Div([
        html.Div(children=[
            html.Br(),
            dcc.Dropdown(id='overyears',
            options=[
            {'label': 'Renewable Energy Over the Years', 'value':'over'},
            {'label': 'Renewable vs. All Sources', 'value':'compare'}
        ], style= dict(width='60%',
                    verticalAlign="middle",
                    marginLeft=60),
            placeholder="Select"),
            html.Br(),
            html.Div(id='over2')
            ],
    )])
])

#Tab styles
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'color': '#696969'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#006400',
    'color': 'white',
    'padding': '6px'
}

#set-up of title, logo, and tabs.
logo = html.Div([
                # Use row and col to control vertical alignment of logo / brand
                dbc.NavbarBrand([
                    dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="60px")),
                        dbc.Col(html.H1("Renewable Energy In Maryland"),
                            style={'color': '#696969'}),
                            ],),
                    ],
                ),
            dcc.Tabs(
                id="tabs-with-classes",
        value='tab-1',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(
                label='About',
                value='tab-1',
                style=tab_style, selected_style=tab_selected_style,
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Data',
                value='tab-2',
                style=tab_style, selected_style=tab_selected_style,
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Generation Capacity',
                value='tab-3', 
                style=tab_style, selected_style=tab_selected_style,
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Energy Generated',
                value='tab-4',
                style=tab_style, selected_style=tab_selected_style,
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
        ]),
    html.Div(id='tabs-content-classes'),
            
])

########################
####### Data Page ######
etab=html.Div([
    #description
    dcc.Markdown([
        ('''
    ## Data

    Did you know that Maryland ranks 28, among the 50 states, in renewable
    energy generation? Its largest renewable energy source is Hydroelectric.
    Maryland's 10-year renewable energy growth is 47.6%, the 16th slowest growth 
    rate after Idaho. Vermont leads all states with an outstanding 99.6% electricity
    generated from renewables. If you want to learn more about each State's ranking,
    and growth, click [here](https://amp.usatoday.com/amp/39801879).

    
    In this page you can access the Maryland's renewable energy capacity and generation datat. 
    Please use the dropdown menu below to make a selection. 


    '''), ],
    style={'marginLeft': 70, 'marginRight': 90, 'marginTop': 10, 'color': '#696969', 
    'align':'center'},),

    html.Div([
        html.Div(children=[
            html.Br(),
            dcc.Dropdown(id='data-select',
            options=[
            {'label': 'Renewable Energy Generated (2007-2017)', 'value':'energytab'},
            {'label': 'Renewable Energy Generation Capacity (2006-2017)', 'value':'captab'}
        ], style= dict(width='60%',
                    verticalAlign="middle"),
            placeholder="Select"),
            html.Br(),
        html.Div(id='data-sel',
        style={'width':'85%',
        'padding':'45px',
        'marginLeft': '180px',
        'marginRight': '140px',
        'textAlign': 'center'
        },
        
        )],
    )]),
])


###########################
#### Generated En Page ####

enpage= html.Div([
    dcc.Markdown([
                        ('''
                    #### Make your own Plot!
                    Use the dropdown menu below to access the data (by year)
                    and make your own plot.


    '''), ],style={'marginLeft': 70, 'marginRight': 90, 'marginTop': 10, 'color': '#696969', 
    'align':'center'},),
    #multi dropdown year selector for table
    html.Div(children=[
        html.Br(),
        dcc.Dropdown( id='energytab2',
        options=[
            {'label':i, 'value':i} for i in energy.Year.unique()
            ], style = dict(
                    width='60%',
                    verticalAlign="middle"),
                    placeholder="Make a Selection",
                    multi=True),
                    html.Div(id='table-container',
                    children='EDetails',
                    style={'width':'80%',
                    'padding':'20px',
                    'marginLeft': '180px',
                'marginRight': '140px',
                'textAlign': 'center'}
                    )]
                    
                    ),

                    html.Div(
                        dcc.Graph(id='graphen'))
])


###########################
#### Capacity En Page ####

gpage= html.Div([
    dcc.Markdown([
                        ('''
                    #### Make your own Plot!
                    On this page, you are in charge. Use the dropdown menu below to access the data (by year)
                    and make your own plot.


    '''), ],style={'marginLeft': 70, 'marginRight': 90, 'marginTop': 10, 'color': '#696969', 
    'align':'center'},),
    #multi dropdown year selector
    html.Div(children=[
        html.Br(),
        dcc.Dropdown( id='captab2',
        options=[
            {'label':i, 'value':i} for i in capacity.Year.unique()
            ], style = dict(
                    width='60%',
                    verticalAlign="middle"),
                    placeholder="Make a Selection",
                    multi=True),
                    html.Div(id='table-container2',
                    children='Details',
                    style={'width':'80%',
                    'padding':'15px',
                    'marginLeft': '180px',
                'marginRight': '140px',
                'textAlign': 'center'})
                    ]),

        dcc.Graph(id='graphcap')
])


#call it into the display of the app
app.layout=html.Div([
    logo
    ])

#Navegation tabs call backs
@app.callback(Output('tabs-content-classes', 'children'),
              [Input('tabs-with-classes', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return page_1
    elif tab == 'tab-2':
        return etab
    elif tab == 'tab-3':
        return gpage
    elif tab == 'tab-4':
        return enpage
@app.callback(Output('over2','children'),
                [Input('overyears', 'value')])
def graph_sel(tabb):
    if tabb=='over':
        fig2.show()
    elif tabb=='compare':
        fig.show()

# Table for Capacity and Energy Gen pages:
def generate_table(dataframe, max_rows=12):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )
# Data Page call back

@app.callback(
    dash.dependencies.Output('data-sel', "children"),
    [dash.dependencies.Input('data-select', "value")])
def update_data(dataset):
    if dataset=='energytab':
        return generate_table(energy)
    elif dataset=='captab':
        return generate_table(capacity)

#Capacity page table call back
@app.callback(
    dash.dependencies.Output('table-container2', "children"),
    [dash.dependencies.Input('captab2',"value")])
def display_table2(dvalue):
    if dvalue is None:
        return generate_table(a)
    dff=capacity[capacity['Year'].isin(dvalue)]
    return generate_table(dff)

@app.callback(
    dash.dependencies.Output('graphcap', 'figure'),
    [dash.dependencies.Input('captab2', "value")])
def update_grapcap(cvalue):
    if cvalue is None:
        dmc=a.copy()
    else:
        dmc=capacity.loc[capacity['Year'].isin(cvalue)]
        dmc=pd.melt(dmc, id_vars=['Year'])
    return {
                'data':[
                    go.Bar(
                        x=dmc[dmc['Year']==i]['variable'],
                        y=dmc[dmc['Year']==i]['value'],
                        name=i
                    ) for i in dmc.Year.unique()
                ],
                'layout':go.Layout(
                barmode='group',
                xaxis={'title': 'Energy Source'},
                yaxis={'title':'Megawatts'})
            
        }


#Generated Energy Table callback
@app.callback(
    dash.dependencies.Output('table-container', "children"),
    [dash.dependencies.Input('energytab2',"value")])
def display_table(ddvalue):
    if ddvalue is None:
        return generate_table(a)
    dff=energy[energy['Year'].isin(ddvalue)]
    return generate_table(dff)


@app.callback(
    dash.dependencies.Output('graphen', 'figure'),
    [dash.dependencies.Input('energytab2', "value")])
def update_graphen(gvalue):
    if gvalue is None:
        dm=a.copy()
    else:
        dm=energy.loc[energy['Year'].isin(gvalue)]
        dm=pd.melt(dm, id_vars=['Year'])
    return {
                'data':[
                    go.Bar(
                        x=dm[dm['Year']==i]['variable'],
                        y=dm[dm['Year']==i]['value'],
                        name=i
                    ) for i in dm.Year.unique()
                ],
                'layout':go.Layout(
                barmode='group',
                xaxis={'title': 'Energy Source'},
                yaxis={'title':'Megawatts Hours'})
            
        }


if __name__ == '__main__':
    app.run_server(debug=True, port=1627)