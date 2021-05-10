from datetime import datetime, timedelta

import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.development.base_component import Component


def unix_time_millis(date):
    return int(date.timestamp())


def get_marks_from_start_end(start, end):
    nb_marks = 10
    result = []
    time_delta = int((end - start).total_seconds() / nb_marks)
    current = start
    if time_delta > 0:
        while current <= end:
            result.append(current)
            current += timedelta(seconds=time_delta)
        result[-1] = end
        if time_delta < 3600 * 24:
            if time_delta > 3600:
                date_f = '%x %Hh'
            else:
                date_f = '%x %Hh%M'
        else:
            date_f = '%x'
        marks = {}
        for date in result:
            marks[unix_time_millis(date)] = str(date.strftime(date_f))
        return marks
    return None


def card_value_div(card_id, unit, value="-"):
    return html.Div([html.Div(value, id=card_id, className="mr-2"), html.Div(unit)],
                    className="d-flex flex-row justify-content-center")


def dash_date_to_datetime(st):
    return datetime.strptime(st, "%Y-%m-%dT%H:%M:%S.000Z")


def create_card(card: dict):
    res = []
    for tile, value in card.items():
        rows = value["text"]
        # if isinstance(text, str):
        #     text = html.H3(text)
        html_text = []
        for row in rows:
            html_text.append(html.Div(row, className="d-flex flex-row justify-content-center"))
        res.append(html.Div(
            dbc.Card([
                html.H4(tile, className="card-title text-center"),
                dbc.Row([
                    dbc.Col(dbc.CardBody(html_text, style={"whiteSpace": "nowrap", "fontSize": "160%"}),
                            className="text-center"),
                    dbc.Col(dbc.CardImg(src=value.get("src", Component.UNDEFINED), style={"maxHeight": "7rem"}))
                ],
                    className="align-items-center flex-nowrap")
            ], className="h-100 p-2"),
            className="col-sm-12 col-md-6 col-lg-3 py-2"
        ))
    return res
