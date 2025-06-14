import dash
from dash import html, dcc
import plotly.graph_objs as go
import random
import datetime

app = dash.Dash(__name__)
server = app.server

# Simuler des données pour 24h
temps = [datetime.datetime.now().replace(hour=h, minute=0) for h in range(24)]
temperature = [25 + random.uniform(-3, 3) for _ in range(24)]
humidite_air = [60 + random.uniform(-5, 5) for _ in range(24)]

# Valeurs par défaut
ph_sol = 6.5
eau_sol = 32
npk = 45

# Layout du dashboard
app.layout = html.Div([
    html.H1("🌾 Dashboard Climatique & Sol", style={"textAlign": "center"}),

    html.Div([
        html.Div([
            html.H3(f"pH du sol : ", style={"display": "inline"}),
            html.Span(f"{ph_sol}", style={"color": "green", "fontWeight": "bold", "fontSize": "20px"}),
            dcc.Graph(figure=go.Indicator(
                mode="gauge+number",
                value=ph_sol,
                gauge={"axis": {"range": [0, 14]}, "bar": {"color": "green"}},
                domain={'x': [0, 1], 'y': [0, 1]}
            ))
        ], style={"width": "30%", "display": "inline-block"}),

        html.Div([
            html.H3(f"Teneur en eau du sol (%) : ", style={"display": "inline"}),
            html.Span(f"{eau_sol}", style={"color": "blue", "fontWeight": "bold", "fontSize": "20px"}),
            dcc.Graph(figure=go.Indicator(
                mode="gauge+number",
                value=eau_sol,
                gauge={"axis": {"range": [0, 100]}, "bar": {"color": "blue"}},
                domain={'x': [0, 1], 'y': [0, 1]}
            ))
        ], style={"width": "30%", "display": "inline-block", "marginLeft": "5%"}),

        html.Div([
            html.H3(f"Teneur en NPK (%) : ", style={"display": "inline"}),
            html.Span(f"{npk}", style={"color": "orange", "fontWeight": "bold", "fontSize": "20px"}),
            dcc.Graph(figure=go.Indicator(
                mode="gauge+number",
                value=npk,
                gauge={"axis": {"range": [0, 100]}, "bar": {"color": "orange"}},
                domain={'x': [0, 1], 'y': [0, 1]}
            ))
        ], style={"width": "30%", "display": "inline-block", "marginLeft": "5%"})
    ]),

    html.Div([
        html.H3("Température de l'air (°C)"),
        dcc.Graph(figure={
            "data": [go.Scatter(x=temps, y=temperature, mode="lines+markers", name="Température")],
            "layout": go.Layout(title="Évolution de la température", xaxis_title="Heure", yaxis_title="°C")
        })
    ]),

    html.Div([
        html.H3("Humidité de l'air (%)"),
        dcc.Graph(figure={
            "data": [go.Scatter(x=temps, y=humidite_air, mode="lines+markers", name="Humidité")],
            "layout": go.Layout(title="Évolution de l'humidité de l'air", xaxis_title="Heure", yaxis_title="%")
        })
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
