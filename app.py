# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:36:11 2020

@author: emora
"""
#make sure you install dash from the prompt shell
#conda install -c conda-forge dash
#conda install -c conda-forge dash-bootstrap-components
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd
import dash_table
#read a file
#df = pd.read_csv('https://forge.scilab.org/index.php/p/rdataset/source/file/master/csv/ggplot2/msleep.csv') 
df_url = 'https://forge.scilab.org/index.php/p/rdataset/source/file/master/csv/ggplot2/msleep.csv'
df = pd.read_csv(df_url)
df_vore = df['vore'].dropna().sort_values().unique()
opt_vore = [{'label': x + 'vore', 'value': x} for x in df_vore]

#create app
app=dash.Dash()
app.title="My App"
color={"font-color":"blue"}
#attach an htlm page components
#add 2 spaces after each reference link
markdown_text = '''
#### Some references

[Dash Core Components](https://dash.plot.ly/dash-core-components)  
[Dash HTML Components](https://dash.plot.ly/dash-html-components)  
[Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/l/components)  

''' 
#create a table off the data
#def generate_table(data, max_rows=5):
 #   return html.Table([
  #      html.Thead(
   #             html.Tr(
    #                [html.Th(i) for i in data.columns]
     #               )
      #          ),
       # html.Tbody(
        #    [html.Tr(
         #       [html.Td(col) for col in row.values]
          #      ) for index, row in data.head(max_rows).iterrows()])
        #])
    


#when the app is loaded, the style sheet below will be loaded
#external_stylesheest=['']
app=dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout= html.Div([
    #add page title
    html.H1("My first Dash App!",
            #change page title color
            style={"color": "blue"}),
    #adds the reference links from above
    dcc.Markdown(markdown_text),
    html.Div(id='my-div',
             style={
                 'background' : 'yellow',
                 'color' : 'blue'
             }),
    #adds plotly, note Montreal has a u so that the plot keeps the accent 
    dcc.Graph(id="example-graph",
              figure={"data":[
                              {"x":[1,2,3], "y":[4,2,1], "type": "bar", "name": "DF"},
                              {"x":[1,2,3], "y":[2,4,5], "type": "bar", "name": u'Montréal'}
                              ],
                  "layout":{"font:":{"color": color["font-color"]}
                      }
                      }
            ),
    html.Div([ 

                html.Label('Dropdown'), 
                dcc.Dropdown( 
                     id='my-dropdown',
                        options=opt_vore,
                        value=df_vore[0]
                ), 
                html.Label('Multi-Select Dropdown'), 
                dcc.Dropdown( 
                    options=[ 
                        {'label': 'New York City', 'value': 'NYC'}, 
                        {'label': u'Montréal', 'value': 'MTL'}, 
                        {'label': 'San Francisco', 'value': 'SF'} 

                    ], 
                    value=['MTL', 'SF'], 
                    multi=True 
                ), 
                html.Label('Radio Items'), 
                dcc.RadioItems( 
                    options=[ 
                        {'label': 'New York City', 'value': 'NYC'}, 
                        {'label': u'Montréal', 'value': 'MTL'}, 
                        {'label': 'San Francisco', 'value': 'SF'} 
                    ], 
                    value='MTL' 
                ), 
                html.Label('Checkboxes'), 
                dcc.Checklist( 
                    options=[ 
                        {'label': 'New York City', 'value': 'NYC'}, 
                        {'label': u'Montréal', 'value': 'MTL'}, 
                        {'label': 'San Francisco', 'value': 'SF'} 
                    ], 
                    value=['MTL', 'SF'] 
                ), 

                html.Label('Text Input'), 
                dcc.Input(value='MTL', type='text'), 

                html.Label('Slider'), 
                dcc.Slider( 

                    min=0, 
                    max=9, 
                    marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)}, 
                    value=5, 
                ), 
            ], style={'columnCount': 2}),
        
               # generate_table(df),
                dash_table.DataTable(id='table',
                                     columns=[{"name":i, "id":i} for i in df.columns],
                                     #function must read dataset as a dictionary
                                     data = df.head().to_dict('records')
                                     )
                
    ])
                

#When you run up to the above tab, the output should come out on an html page
#from your console, copy and paste the server http address into your broswer. 
#Mine is: *Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)

#create the module
if __name__=="__main__":
    #launch the app on server, add the debug so you can get any errors and solve them directly
    app.run_server(debug=True)
    print("hello")