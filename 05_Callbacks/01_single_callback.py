import dash
import dash_core_components as dcc
import dash_html_components as html

# for Callbacks
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([dcc.Input(id='my-id',
                                 value='initial value',
                                 type='text'),
                       html.Div(id='my-div',
                                style={'border':'2px blue solid'})
                       ])


'''
Callback decorator is directly connected to the Function, and Output of callback decorator 
is going as Input of the function.
'''

# connects core to html components
@app.callback(Output(component_id='my-div',            # we want to display input at inner DIV
                     component_property='children'),   # Inner div has children, which will show the output
              [Input(component_id='my-id',             # Id of Input is 'my-id' that is of outer DIV
                     component_property='value')])     # that input value is stored as 'initial value' in value
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


if __name__ == '__main__':
    app.run_server()
