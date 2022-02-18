


#%%



#%%
import dash

from dash import Dash, html, dcc, Input, Output


app = dash.Dash(
    __name__,
    external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
)

app.layout = html.Div( [ 
    html.H1('cheese'),
    html.H2('potato'),


    html.H2('dropdown'),
        html.Div('Who is responsible for 9/11'),
        html.Br(),
        dcc.Dropdown(
                id='dd1',
        options = [
            {'label': "George W. Bush", 'value': "g_w_bush"},
            {'label': "Osama Bin Ladin", 'value': "o_b_ladin"},
            {'label': "Snake People", 'value': "snake_people"}
                ],
        value='g_w_bush',
                style={
                        'width': '50%'
                    }
            ),
        html.Br(),
        html.Div(id="dd1_output")
         ] )
@app.callback(
    Output('dd1_output', 'children'),
    Input('dd1', 'value')
)
def update_scooby_selection(value):
    return 'Scooby Doo "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
# %%


# Things to put in this
# Data base of different animals
# Sliding bar
# Text entry option
# Dropdown Menu
# 