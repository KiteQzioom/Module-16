from dash import dcc
from dash import html
import plotly.graph_objects as go

def render_tab(df):

    grouped = df[df['total_amt']>0].groupby('weekday')['total_amt'].sum()
    fig = go.Figure(data=[go.Pie(labels=grouped.index,values=grouped.values)],layout=go.Layout(title='Sprzedaż w danych dniach tygodnia'))

    layout = html.Div([html.H1('Rodzaje sklepów',style={'text-align':'center'}),

                        html.Div([html.Div([dcc.Graph(id='pie-weekdays',figure=fig)],style={'width':'50%'}),
                        html.Div([dcc.Dropdown(id='country_dropdown',
                                    options=[{'label':str(countries),'value':str(countries)} for countries in df['country'].unique()],
                                    value=df['country'].unique()[0]),
                                    dcc.Graph(id='barh-country')],style={'width':'50%'})],style={'display':'flex'}),
                                    html.Div(id='temp-out')
                        ])

    return layout