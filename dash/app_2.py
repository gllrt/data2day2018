import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime as dt, timedelta

# Define object for external CSS stylesheet
external_stylesheets = [
    'https://getbootstrap.com/docs/3.3/getting-started/',
    {
        'href': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u',
        'crossorigin': 'anonymous'
    }
]

# Initialize app object and add external stylesheet
app = dash.Dash(__name__, 
    external_stylesheets=external_stylesheets)

# Define the layout
app.layout = html.Div(children=[
    html.H2('Twitter Showcase'), 

    # Create a new Row in the UI for Inputs
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.P('Datumsbereich:')
                    ],
                    className="control-label"
                ),
                dcc.DatePickerRange(
                    id='my-date-picker-range',
                    min_date_allowed=(dt.now() - timedelta(weeks=52)).date(),
                    max_date_allowed=dt.today(),
                    initial_visible_month=dt.today(),
                    start_date=(dt.now() - timedelta(days=7)).date(),
                    end_date=dt.now().date(),
                    display_format='DD.MM.YYYY',
                 )
                 ]
            )
            ],
            className="col-sm-4"
        ),
        html.Div([
            html.Div([
                html.P('Hash-Tag oder Benutzer:')
                ],
                className="control-label"
            ),
            dcc.Input(
                id='hashtag-input',
                type='text',
                value='@data2day'
            )
            ],
            className="col-sm-4"
        ),
        html.Div([
            html.Div([
                html.P('Anzahl von Tweets:')
                ],
                className="control-label"
            ),
            dcc.Slider(
                id='number-tweets-slider',
                min=100,
                max=2000,
                value=500,
                step=100,
                marks={i: '{}'.format(i) for i in list(filter(lambda x: '{}'.format(x) if (x/100)%2 == 1 else '', [(100*(i+1)) for i in range(20)]))}
            )
            ],
            className="col-sm-4"
        )

        ],
        className="row"
    ),

    # Create a new row for exemplary output
    html.Div([
        html.Div([
            html.Div(id='output-container-date-picker-range')
            ],
            className="col-sm-4"
        ),
        html.Div([
            html.Div(id='output-hashtag-input')
            ],
            className="col-sm-4"
        ),
        html.Div([
            html.Div(id='ouput-number-tweets-slider')
            ],
            className="col-sm-4"
        )
        ],
        className="row"
    )
    ],
    className="container-fluid"
)

# Create function based on input of date range slider
@app.callback(
    Output('output-container-date-picker-range', 'children'),
    [Input('my-date-picker-range', 'start_date'),
     Input('my-date-picker-range', 'end_date')]
)
def update_output(start_date, end_date):
    string_prefix = 'Aktuelle Auswahl: '
    if start_date is not None:
        start_date = dt.strptime(start_date, '%Y-%m-%d')
        start_date_string = start_date.strftime('%d. %B %Y')
        string_prefix = string_prefix + start_date_string + ' bis '
    if end_date is not None:
        end_date = dt.strptime(end_date, '%Y-%m-%d')
        end_date_string = end_date.strftime('%d. %B %Y')
        string_prefix = string_prefix + end_date_string
    if len(string_prefix) == len('You have selected: '):
        return 'Select a date to see it displayed here'
    else:
        return string_prefix

# Create function based on input of text input
@app.callback(
    Output('output-hashtag-input', 'children'),
    [Input('hashtag-input', 'value')]
)
def update_output_hashtag(input_hashtag):
    return '{}'.format(input_hashtag)

# Create function based on input of integer slider
@app.callback(
    dash.dependencies.Output('ouput-number-tweets-slider', 'children'),
    [dash.dependencies.Input('number-tweets-slider', 'value')])
def update_output_number_tweets(input_number_tweets):
    return 'Anzahl an abzurufenden Tweets: {}'.format(input_number_tweets)

# Host the app via Flask
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8052, debug=True)

