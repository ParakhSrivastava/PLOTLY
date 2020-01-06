# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[html.H1(children='Hello Dash'), 
                                html.Div(children='Dash: A web application framework for Python.'),
                                dcc.Graph(id='example-graph',
                                          figure={'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'}],
                                                  'layout': {'title': 'Dash Data Visualization'}}
                                          )
                                ])

'''
Div has only "children"
children has three elements: "H1", "Div", "Graph"
dcc.Graph has two parameters: "id" and "figure"
figure has two parameters: "data" and "layout"
'''

if __name__ == '__main__':
    app.run_server()
