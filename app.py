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