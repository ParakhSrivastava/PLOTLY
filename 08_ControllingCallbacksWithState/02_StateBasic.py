#######
# A very basic Input/Output callback, with State!
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([dcc.Input(id='number-in',
                                 value=1,
                                 style={'fontSize':28}
                                 ),

                       html.Button(id='submit-button',
                                   n_clicks=0,  # for getting how many number of clicks this button had
                                   children='Submit',
                                   style={'fontSize':28}),
                                   
                       html.H1(id='number-out')])

@app.callback(Output('number-out', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('number-in', 'value')])
def output(input_value, state_value):
    return state_value

if __name__ == '__main__':
    app.run_server()
