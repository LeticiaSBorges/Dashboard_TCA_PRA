import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json

para_reg = json.load(open("Arquivos_geojson/REGIOES_INTEGRACAO.geojson", "r", encoding='utf-8'))
#para_reg.keys()
#type(para_reg["features"][0])
#para_reg["features"][0].keys()
#para_reg["features"][0]['properties']



