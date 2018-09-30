import dash
import dash_core_components as dcc
import dash_html_components as html

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
    html.H2('Twitter Showcase') 
    ],
    className="container-fluid"
)

# Host the app via Flask
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8051, debug=True)

