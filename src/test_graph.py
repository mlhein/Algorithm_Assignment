import plotly
import plotly.graph_objs as go
import plotly.plotly as py
from plotly.graph_objs import *

def Scattergraph(dic):

    trace0 = go.Scatter(
        x=dic.keys(),
        y=dic.values(),
        mode = "lines+markers",
        name = "Word Count"
    )
    data = ([trace0])
    layout = go.Layout(
    title='Word Count')
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename = 'basic-line')


def bar(dic):
    barp(dic["Positive"])
    barn(dic["Negative"])

def barp(dic):
    keys = dic.keys()
    value = dic.values()
    data = [go.Bar(
                x = keys,
                y = value
        )]
    layout = go.Layout(title = 'Positive words count')
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='Positive-bar')

def barn(dic):
    keys = dic.keys()
    value = dic.values()
    data = [go.Bar(
                x = keys,
                y = value
        )]
    layout = go.Layout(title = 'Negative words count')
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='Negative-bar')
