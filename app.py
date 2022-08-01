# -*- coding: utf-8 -*-
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import dash_table
import pandas as pd
import lorem
import pathlib
import openpyxl

##################################################### Mapa #############################################################
with open("C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Arquivos_geojson\\REGIOES_INTEGRACAO.geojson",
          encoding='utf-8') as regiao_integracao:dados_geo = json.load(regiao_integracao)

dados_df = pd.read_excel('C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Arquivos_geojson\\'
                         'REGIOES_INTEGRACAO.xlsx')

## Color map
regInt_Color = ['#008080', '#008B8B', '#20B2AA', '#48D1CC', '#40E0D0', '#00CED1',
               '#00FFFF','#5F9EA0','#66CDAA', '#7FFFD4', '#87CEFA', '#ADD8E6']
fig_map = px.choropleth(dados_df, geojson=dados_geo, color="Regiões de Integração",
                    locations="Regiões de Integração", featureidkey="properties.Regiões_d",
                    projection="mercator", hover_data=["Regiões de Integração"],
                    color_discrete_sequence = regInt_Color,
                    #color_discrete_sequence=px.colors.qualitative.Alphabet,
                    #title='Figura 1 - Regiões de Integração no Estado do Pará',
                    height=400, width=700
                   )
fig_map.update_layout(title_text='Figura 1 - Regiões de Integração no Estado do Pará, Brasil.', title_x=0.5, title_y=0.01)
fig_map.update_geos(fitbounds="locations", visible=False)
fig_map.update_layout(margin={"r":0,"t":15,"l":0,"b":0})

################################################### Tabela #############################################################
name_col = ["Região de Integração", 'n° de Imovéis com Licencimento','TCA','Área do Imóvel',
            'Área a Recompor em RL', 'Área a Recompor em APP']
table_df = pd.read_excel("C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Resultados\\"
                         "Geral\\tab_dinamica_TCA.xlsx")
table_fig = go.Figure(data=[go.Table(
    header=dict(values=list(name_col),
                fill_color='#003399',
                align=['left', 'center'],
                font=dict(color='white', size=12),
                height=40),
    cells=dict(values=[table_df.RegInt, table_df.n_de_Imoveis_com_Licencimento, table_df.TCA,table_df.AreaImovel,
                       table_df.AR_RL, table_df.AR_APP],
               fill_color='lavender',
               align=['left', 'center'], font=dict(color='black', size=11))
)])
table_fig.update_layout(title_text='Tabela 1 - Áreas dos imóveis rurais.', title_x=0.15,
                        width=620, height=400,
                        margin={"r":0,"l":117,"b":0, "t":30})

################################################# Graficos #############################################################
## Criação do Gráfico 1
# Grafico Número de imóveis rurais com TCAs em execução e com licenciamento por região de integração
data_tab_din = pd.read_excel('C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Resultados\\Geral\\'
                             'tab_dinamica_TCA-2.xlsx')

regInt = data_tab_din['Região de Integração']
nTCA = data_tab_din['TCA']
nLic = data_tab_din['n° de Imovéis com Licencimento']

graf_1 = go.Figure()
graf_1.add_trace(go.Bar(
    x=regInt,
    y=nTCA,
    name='TCA',
    marker_color='#191970'
))
graf_1.add_trace(go.Bar(
    x=regInt,
    y=nLic,
    name='Nº de imóveis com licenciamento',
    marker_color='#363636'
))

graf_1.update_layout(barmode='group', xaxis_tickangle=-35,
                    width=725, height=400,
                    title = "Figura 2 - Número de imóveis rurais com TCAs em execução e com licenciamento.",
                    font = {'family': 'Arial','size': 11,'color': 'black'},
                    title_x=0.5, title_y=0.01,
                    #legend_orientation = "h",
                    legend=dict(
                            x=0,
                            y=1.0,
                            #bgcolor='rgba(255, 255, 255, 0)',
                            #bordercolor='rgba(255, 255, 255, 0)'
                        ),
                    margin={"r":50,"l":100,"b":100, "t":30})

## Criação do Gráfico 2
# Exercução dos TCAs por ano.
data_ano = pd.read_excel("C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Resultados\\Geral\\"
                         "Ano_Termo_Comp_TCA.xlsx")
data_ano.rename(columns={'Ano_Termo_Compromisso': 'Ano do Termo de Compromisso'}, inplace = True)
data_ano.rename(columns={0: 'Quantidade'}, inplace = True)
graf_2 = px.bar(data_ano, x='Ano do Termo de Compromisso', y='Quantidade', text_auto=True,
                title = "Figura 3 - Imóveis rurais com TCAs em execução.",
                width=725, height=300)
graf_2.update_layout(title_text= "Figura 3 - Imóveis rurais com TCAs em execução.",
                title_x=0.5, title_y=0.02, margin={"r":50,"l":100,"b":100, "t":20})

## Criação do Gráfico 3
#TCAs nas Regiões de Integração no Pará, Brasil
data_graf_3 = pd.read_excel('C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Resultados\\Geral\\'
                            'tab_dinamica_TCA-2.xlsx')
regInt = data_graf_3['Região de Integração']
nTCA = data_graf_3['TCA']

graf_3 = px.pie(names = regInt, values = nTCA)
graf_3.update_layout(#title_text= "Figura 4 - TCAs nas Regiões de Integração no Estado do Pará no Brasil.",
                    font = {'family': 'Arial','size': 9,'color': 'black'},
                    title_x=0.5, title_y=0.01, height = 250,
                     margin={"r":0,"l":0,"b":50 , "t":30})

## Criação do Gráfico 4
#
data_graf_4 = pd.read_excel('C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Resultados\\Geral\\'
                            'tab_dinamica_TCA-2.xlsx')

regInt = data_graf_4['Região de Integração']
nTCA = data_graf_4['TCA']
nLic = data_graf_4['n° de Imovéis com Licencimento']

graf_4 = go.Figure()
graf_4.add_trace(go.Bar(
    x=regInt,
    y=nTCA,
    name='TCA',
    marker_color='#191970'
))
graf_4.add_trace(go.Bar(
    x=regInt,
    y=nLic,
    name='Nº de imóveis com licenciamento',
    marker_color='#363636'
))

graf_4.update_layout(barmode='group', xaxis_tickangle=90,
                    #title = "Figura 5 - Imóveis rurais com TCAs em execução por Região de Integração.",
                    font={'family': 'Arial', 'size': 10, 'color': 'black'},
                    title_x=0.5, title_y=0.01, height=250,
                    margin={"r": 0, "l": 0, "b": 50, "t": 30},
                    legend=dict(x=0, y=1.0)
                     )
graf_4.update_traces(textfont_size=8, textangle=1, textposition="outside", cliponaxis=False)

#############################
## Graficos Baixo Amazonas

data_graf_5 = pd.read_excel('C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Resultados\\Baixo_Amazonas\\'
                     'tab_dinamica_BAmaz.xlsx')

regInt = data_graf_5['MUNICIPIO']
nTCA = data_graf_5['TCA']
nLic = data_graf_5['n° de Imovéis com Licencimento']

graf_5 = go.Figure()
graf_5.add_trace(go.Bar(
    x=regInt,
    y=nTCA,
    name='TCA',
    marker_color='#191970'
))
graf_5.add_trace(go.Bar(
    x=regInt,
    y=nLic,
    name='Nº de imóveis com licenciamento',
    marker_color='#363636'
))
graf_5.update_layout(barmode='group', xaxis_tickangle=-35,
                    #title = "Figura 6 - Número de imóveis rurais com TCAs em execução e com licenciamento por município no Baixo Amazonas.",
                    font={'family': 'Arial', 'size': 10, 'color': 'black'},
                    title_x=0.5, title_y=0.01, height=230,
                    margin={"r": 0, "l": 0, "b": 0, "t": 20},
                    legend=dict(x=0, y=1.0)
                  )

data_graf_6 = pd.read_excel('C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Resultados\\Baixo_Amazonas\\'
                            'Ano_Termo_Comp_BAmaz.xlsx', engine='openpyxl')
data_graf_6.set_axis(['Ano do Termo Compromisso', 'Quantitativo de TCA'],
              axis='columns', inplace=True)
# Convertendo dtype para string
data_graf_6["Ano do Termo Compromisso"] = data_graf_6["Ano do Termo Compromisso"].astype(str)

graf_6 = px.bar(data_graf_6 , x='Ano do Termo Compromisso', y='Quantitativo de TCA',  text_auto=True,
                #title = "Imóveis rurais com TCAs em execução na Região de Integração Baixo Amazonas."
                )
graf_6.update_layout(title_text= "Figura 7 - Imóveis rurais com TCAs em execução na Região de Integração Baixo Amazonas.",
                    font = {'family': 'Arial','size': 9,'color': 'black'},
                    title_x=0.5, title_y=0.01, height = 230,
                     margin={"r":0,"l":0,"b":52 ,"t":20})
graf_6.update_yaxes(title = "TCAs")
graf_6.update_xaxes(title = "Ano")

#############################
## Graficos Rio Capim
data_graf_7 = pd.read_excel('C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Resultados\\RIO_CAPIM\\tab_dinamica_RCapim.xlsx')
regInt = data_graf_7['MUNICIPIO']
nTCA = data_graf_7['TCA']
nLic = data_graf_7['n° de Imovéis com Licencimento']

graf_7 = go.Figure()
graf_7.add_trace(go.Bar(
    x=regInt,
    y=nTCA,
    name='TCA',
    marker_color='#191970'
))
graf_7.add_trace(go.Bar(
    x=regInt,
    y=nLic,
    name='Nº de imóveis com licenciamento',
    marker_color='#363636'
))
graf_7.update_layout(barmode='group', xaxis_tickangle=-35,
                  #title = "Figura 8 - Número de imóveis rurais com TCAs em execução e com licenciamento por município no Rio Capim.",
                font = {'family': 'Arial', 'size': 10, 'color': 'black'},
                title_x = 0.5, title_y = 0.01, height = 230,
                margin = {"r": 0, "l": 0, "b": 0, "t": 20},
                legend = dict(x=0, y=1.0))

data_graf_8 = pd.read_excel('C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Resultados\\RIO_CAPIM\\'
                            'Ano_Termo_Comp_RCapim.xlsx', engine='openpyxl')
data_graf_8.set_axis(['Ano do Termo Compromisso', 'Quantitativo de TCA'],
              axis='columns', inplace=True)

data_graf_8["Ano do Termo Compromisso"] = data_graf_8["Ano do Termo Compromisso"].astype(str)

graf_8 = px.bar(data_graf_8, x='Ano do Termo Compromisso', y='Quantitativo de TCA', text_auto=True)
graf_8.update_layout(title_text= "Figura 9 - Imóveis rurais com TCAs em execução na região de integração Rio Capim.",
                    font = {'family': 'Arial','size': 9,'color': 'black'},
                    title_x=0.5, title_y=0.01, height = 230,
                     margin={"r":0,"l":0,"b":52 ,"t":20})
graf_8.update_yaxes(title = "TCAs")
graf_8.update_xaxes(title = "Ano")

#############################
## Graficos Tapajós
data_graf_9 = pd.read_excel('C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Resultados\\TAPAJÓS\\tab_dinamica_tapajos.xlsx')
regInt = data_graf_9['MUNICIPIO']
nTCA = data_graf_9['TCA']
nLic = data_graf_9['n° de Imovéis com Licencimento']

graf_9 = go.Figure()
graf_9.add_trace(go.Bar(
    x=regInt,
    y=nTCA,
    name='TCA',
    marker_color='#191970'
))
graf_9.add_trace(go.Bar(
    x=regInt,
    y=nLic,
    name='Nº de imóveis com licenciamento',
    marker_color='#363636'
))
graf_9.update_layout(barmode='group', xaxis_tickangle=0,
                  #title = "Figura 10 - Número de imóveis rurais com TCAs em execução e com licenciamento por município no Tapajós.",
                font = {'family': 'Arial', 'size': 10, 'color': 'black'},
                title_x = 0.5, title_y = 0.01, height = 230,
                margin = {"r": 0, "l": 0, "b": 0, "t": 20},
                legend = dict(x=0, y=1.0))


data_graf_10 = pd.read_excel('C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Resultados\\TAPAJÓS\\'
                            'Ano_Termo_Comp_tapajos.xlsx', engine='openpyxl')
data_graf_10.set_axis(['Ano do Termo Compromisso', 'Quantitativo de TCA'],
              axis='columns', inplace=True)
data_graf_10["Ano do Termo Compromisso"] = data_graf_10["Ano do Termo Compromisso"].astype(str)
graf_10 = px.bar(data_graf_10, x='Ano do Termo Compromisso', y='Quantitativo de TCA', text_auto=True)
graf_10.update_layout(title_text= "Figura 11 - Imóveis rurais com TCAs em execução na Regiões de Integração do Tapajós.",
                    font = {'family': 'Arial','size': 9,'color': 'black'},
                    title_x=0.5, title_y=0.01, height = 230,
                     margin={"r":0,"l":0,"b":52 ,"t":20})
graf_10.update_yaxes(title = "TCAs")
graf_10.update_xaxes(title = "Ano")


#############################
## Graficos Xingu
data_graf_11 = pd.read_excel('C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Resultados\\XINGU\\tab_dinamica_xingu.xlsx')
regInt = data_graf_11['MUNICIPIO']
nTCA = data_graf_11['TCA']
nLic = data_graf_11['n° de Imovéis com Licencimento']

graf_11 = go.Figure()
graf_11.add_trace(go.Bar(
    x=regInt,
    y=nTCA,
    name='TCA',
    marker_color='#191970'
))
graf_11.add_trace(go.Bar(
    x=regInt,
    y=nLic,
    name='Nº de imóveis com licenciamento',
    marker_color='#363636'
))
graf_11.update_layout(barmode='group', xaxis_tickangle=-35,
                  #title = "Figura 12. Número de imóveis rurais com TCAs em execução e com licenciamento do Xingu.",
                font = {'family': 'Arial', 'size': 10, 'color': 'black'},
                title_x = 0.5, title_y = 0.01, height = 230,
                margin = {"r": 0, "l": 0, "b": 0, "t": 20},
                legend = dict(x=0, y=1.0))


data_graf_12 = pd.read_excel('C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\Dados\\Resultados\\XINGU\\'
                            'Ano_Termo_Comp_xingu.xlsx', engine='openpyxl')
data_graf_12.set_axis(['Ano do Termo Compromisso', 'Quantitativo de TCA'],
              axis='columns', inplace=True)
data_graf_12["Ano do Termo Compromisso"] = data_graf_12["Ano do Termo Compromisso"].astype(str)
graf_12 = px.bar(data_graf_12, x='Ano do Termo Compromisso', y='Quantitativo de TCA', text_auto=True)
graf_12.update_layout(title_text= "Figura 13 - Imóveis rurais com TCAs em execução na Regiões de Integração do Xingu.",
                    font = {'family': 'Arial','size': 9,'color': 'black'},
                    title_x=0.5, title_y=0.01, height = 230,
                     margin={"r":0,"l":0,"b":52 ,"t":20})
graf_12.update_yaxes(title = "TCAs")
graf_12.update_xaxes(title = "Ano")

##################################################### Dash #############################################################
# Colours
color_1 = "#003399" ##Azul escuro
color_2 = "#00ffff" ##Azul claro
color_3 = "#002277" ##Azul escuro parecido com o primeiro
color_b = "#F8F8FF" ##Branco

app = dash.Dash(__name__)
app.title = "Relatório TCA's Pará"

server = app.server

app.layout = html.Div(
    children=[
        # Pagina 1
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Div(
                                                    html.Img(
                                                        src=app.get_asset_url(
                                                            "brasao_para.png"
                                                        ),
                                                        className="page-1a",
                                                    )
                                                ),
                                                html.Div(
                                                    [
                                                        html.H6("Secretaria de Estado de Meio Ambiente e "
                                                                "Sustentabilidade"),
                                                        html.H5("Relatório dos Termos de Compromissos Executados no "
                                                                "Âmbito do PRA"),
                                                    ],
                                                    className="page-1b",
                                                ),
                                            ],
                                            className="page-1c",
                                        )
                                    ],
                                    className="page-1d",
                                ),
                                html.Div(
                                    [
                                        html.H4(
                                            [
                                                html.Span("20.", className="page-1e"),
                                                html.Span("07.", className="page-1e"),
                                                html.Span("2022"),
                                            ]
                                        ),
                                        html.H6("Edição"),
                                    ],
                                    className="page-1f",
                                ),
                            ],
                            className="page-1g",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6("Autores:"),
                                        html.H6("Rodolpho Zahluth Bastos", className="page-1h"),
                                        html.P("Secretário Adjunto de Gestão e Regularidade Ambiental"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6("Selma Solange Monteiro Santos", className="page-1h"),
                                        html.P("Assessora Técnica da Secretaria Adjunta de Gestão e Reguaridade "
                                               "Ambiental"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6(
                                            "Luiz Edinelson Cardoso e Cardoso", className="page-1h"
                                        ),
                                        html.P("Assessor Técnico da Secretaria Adjunta de Gestão e Reguaridade "
                                               "Ambiental"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6("Bruna Coelho da Conceição Pôjo", className="page-1h"),
                                        html.P("Assessora Técnica da Secretaria Adjunta de Gestão e Reguaridade "
                                               "Ambiental"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6("Maíra Moeira do Canto Lopes", className="page-1h"),
                                        html.P("Assessora Técnica da Secretaria Adjunta de Gestão e Reguaridade "
                                               "Ambiental"),
                                    ],
                                    className="page-1i",
                                ),

                                html.Div(
                                    [
                                        html.H6("Autora do Dashboard:"),
                                        html.H6("Letícia de Sousa Borges", className="page-1h"),
                                        html.P("Técnica em Gestão de Meio Ambiente"),
                                    ],
                                    className="page-1i",
                                ),
                            ],

                            className="page-1j",
                        ),   ##Div dos autores
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.H6(
                                                    "Regiões de Integração no Pará",
                                                    className="page-1h",
                                                ),
                                                html.P(lorem.paragraph() * 2),
                                            ],
                                            className="page-1k",
                                        ),
                                        html.Div(
                                            [
                                                html.H6(
                                                    "Região de Integração Baixo Amazonas",
                                                    className="page-1h",
                                                ),
                                                html.P(lorem.paragraph() ),
                                            ],
                                            className="page-1l",
                                        ),
                                        html.Div(
                                            [
                                                html.H6(
                                                    "Região de Integração Rio Capim",
                                                    className="page-1h",
                                                ),
                                                html.P(lorem.paragraph()),
                                            ],
                                            className="page-1m",
                                        ),
                                        html.Div(
                                            [
                                                html.H6(
                                                    "Região de Integração Tapajós",
                                                    className="page-1h",
                                                ),
                                                html.P(lorem.paragraph() ),
                                            ],
                                            className="page-1l",
                                        ),
                                        html.Div(
                                            [
                                                html.H6(
                                                    "Região de Integração Xingu",
                                                    className="page-1h",
                                                ),
                                                html.P(lorem.paragraph()),
                                            ],
                                            className="page-1m",
                                        ),
                                    ],
                                    className="page-1n",
                                ), #Div dos assuntos tratados
                            ],
                            className="resumo",
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ), #Fim pagina 1
        # Pagina 2
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a" ), #page-2a
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H4("Introdução", className="page-2b"),
                                            html.P(
                                                "Diante dos desafios globais para garantir o combate das mudanças do clima e "
                                                "monitoramento quanto ao uso e ocupação do solo, o Programa de Regularização "
                                                "Ambiental (PRA) se apresenta como instrumento de gestão ambiental, que "
                                                "compreende o conjunto de ações ou iniciativas a serem desenvolvidas por "
                                                "proprietários rurais com o objetivo de adequar e promover a regularização "
                                                "ambiental com vistas ao cumprimento do disposto no art. 59 da Lei Federal nº "
                                                "12.651/2012.", className="page-2b"),
                                            html.P(
                                                "No Pará, o Governo do Estado instituiu o Programa de Regularização Ambiental dos "
                                                "Imóveis Rurais, por meio de Decreto Estadual nº 1.379/2015, com o objetivo de promover a "
                                                "regularização ambiental das posses e propriedades rurais do Estado, em que tenha sido "
                                                "verificada a existência de passivos ambientais, relativos às áreas de preservação permanente "
                                                "(APPs), de reserva legal (RL) e de uso restrito (AUR), detectados na análise do Cadastro "
                                                "Ambiental Rural – CAR.", className="page-2c"),
                                            html.P(
                                                "No âmbito do PRA, a Instrução Normativa SEMAS/PA nº 1/2020, estabelece "
                                                "procedimentos e critérios para adesão ao programa, de modo que esta adesão deve ser "
                                                "realizada pelo proprietário/possuidor do imóvel rural perante a SEMAS/PA, sendo exigido "
                                                "documentos pessoais e do imóvel, o Cadastro Ambiental Rural (CAR), o Projeto de "
                                                "Recomposição de Áreas Degradadas e Alteradas (PRADA), juntamente a assinatura ao Termo "
                                                "de Compromisso Ambiental (TCA).", className="page-2c"),
                                        ],
                                        className="page-3",
                                    ),
                                    html.Div(
                                        [
                                            html.P("O art. 12 do Decreto Estadual nº 1.379/2015, instituiu que o TCA será firmado no ato de "
                                                    "adesão ao PRA e terá eficácia de titulo executivo extrajudicial. Esta assinatura do TCA, "
                                                    "consiste no documento formal de adesão ao Programa de Regularização Ambiental, que "
                                                    "estabelece os compromissos de manter, recuperar ou recompor a APP, RL e AUR do imóvel "
                                                    "rural.", className="page-2b"),
                                            html.P("Neste sentido, a fim de acompanhar a situação atual do PRA junto a SEMAS/PA, este "
                                                    "relatório tem como objetivo quantificar as áreas a recompor de RL, de APP, as AUR e "
                                                    "área total dos imóveis rurais que estão com os Termos de Compromisso Ambiental em "
                                                    "execução, visando reconhecer a situação de adesão ao PRA a partir da assinatura dos "
                                                    "TCA’s dos imóveis rurais nas regiões de integração do Estado do Pará para conservação "
                                                    "dos recursos naturais consistindo em uma agenda desafiadora que traz enormes oportunidades "
                                                    "para gestão ambiental do território.", className="page-2c"),
                                        ],
                                        className="page-3",
                                    ),
                                ],
                                className="fonte",
                            ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ), #Fim Pagina 2
        # Pagina 3
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a" ), #page-2a
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H4("Metodologia", className="page-2b"),
                                        html.P("Para realização deste relatório, foram obtidas informações através do banco "
                                               "de dados da 'Entrada única' inseridas no 'Módulo Relatório', pertencentes no "
                                               "sistema da SEMAS/PA, este banco de dados contém todos os recibos eletrónicos "
                                               "dos imóveis rurais com Cadastros Ambientais Rurais - CAR aprovados e Termos de "
                                               "Compromissos - TCAs Executados no Pará. A planilha com os dados dos TCAs "
                                               "eletrônicos foram obtidas através do CATIS n° 2022033062, já a dos TCAs "
                                               "manuais foram obtidas através do PAE n° 264720/2022 juntamente a Gerência de "
                                               "Adequação Ambiental Rural (GEAR) da SEMAS/PA. Para análise dos dados obtidos "
                                               "até 31 de março de 2022, foi utilizado o Excel como ferramenta de filtro para "
                                               "extrair as informações necessárias por regiões de integração do Estado do Pará "
                                               "em cada recibo de CAR (Figura 1).", className="page-2b"),
                                    ],
                                    className="page-3",
                                ),
                            ], className="fonte",
                        ),
                        html.Div(
                            [
                                dcc.Graph(figure=fig_map)
                            ],
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ), #Fim pagina 3
        #Pagina 4
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a"),  # page-2a
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.P(
                                            "Após a filtragem dos dados dos imóveis rurais, foi realizado o levantamento "
                                            "de imóveis com licenciamento a partir do CPF/CNPJ do proprietário do "
                                            "imóvel no SIMLAM/PA, e por fim foi possível elaborar gráficos a partir: "
                                            "dos TCAs executados, das áreas de RL a recompor, de APP a recompor dos "
                                            "imóveis rurais por Região de Integração e dos imóveis com licenciamento no "
                                            "âmbito do Programa de Regularização Ambiental - PRA.", className="page-2b"),
                                        html.H4("Resultados", className="page-2b"),
                                        html.P(
                                            "A partir dos dados obtidos, identificou-se que 364 imóveis rurais possuem "
                                            "Termos de Compromisso Ambiental- TCAs em execução, correspondendo a uma "
                                            "área total de 744.111,2829 ha, nos quais 10.787,3665 ha estão em processo "
                                            "de recomposição, conforme metodologia e cronograma descritos nos projetos "
                                            "de recomposição de área degradadas e alteradas. Do total de áreas a "
                                            "recompor 8.086,7996 ha são de área de Reserva Legal (RL) a recompor, e "
                                            "2.700,5669 ha são de Área de Preservação Permanente (APP) a recompor. "
                                            "Identificou-se ainda que dos 364 imóveis com TCAs assinados, 280 (77%) "
                                            "possuem processos de licenciamento ambiental formalizados na SEMAS (Tabela 1).",
                                            className="page-2b"),
                                    ],
                                    className="page-3",
                                ),
                                html.Div(
                                    [
                                        dcc.Graph(figure=table_fig)
                                    ], className="marge-table-1"
                                ),
                            ], className="fonte",
                        ),

                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),#Fim pagina 4
        #Pagina 5
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a" ), #page-2a
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.P("Em relação a estes 364 imóveis rurais que estão com TCA em execução, "
                                               "280 requisitaram o licenciamento de suas atividades, sendo a região do "
                                               "Xingu correspondendo a 34,6% do total, com 97 dos 115 imóveis.",
                                               className="page-2b"),
                                    ],
                                    className="page-3",
                                ),
                            ], className="fonte",
                        ),
                        html.Div(
                            [
                                dcc.Graph(figure=graf_1)
                            ],
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.P("A região do Xingu registrou, nos anos de 2018, 2019, 2021 e 2022, o maior "
                                               "número de imóveis com TCA em execução sendo 5, 26, 53 e 14 imóveis, "
                                               "respectivamente. Já em 2020, a região com maior número de imóveis com TCA em "
                                               "execução foi a de Rio Capim, com 21 imóveis. No decorrer dos anos houve um "
                                               "aumento de imóveis rurais com TCAs em execução, crescendo de 5 imóveis em 2018 "
                                               "para 168 em 2021, ressalta-se que no ano de 2022, até o mês de março, houve "
                                               "registro de 54 imóveis (Figura 3).",
                                               className="page-2b"),
                                    ],
                                    className="page-3",
                                ),
                            ], className="fonte",
                        ),
                    ],  className="subpage",
                )
            ],
            className="page",
        ), #Fim pagina 5
        #Pagina 6
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a" ),
                        html.Div(
                            [
                                dcc.Graph(figure=graf_2)
                            ],
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.P("Neste âmbito, observou-se que as Regiões de Integração que possuem a "
                                               "maior quantidade de TCAs executados são: Xingu, Rio Capim, Baixo "
                                               "Amazonas e Tapajós, com 115, 74, 42 e 42 TCAs, respectivamente. As "
                                               "Regiões com menor quantidade de TCAs executados são: Lago do Tucuruí, "
                                               "Cuamá e Marajó, com 12, 4 e 1 TCAs (Figura 4 e 5).",
                                               className="page-2b"),
                                    ],
                                    className="page-3",
                                ),
                            ], className="fonte",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        dcc.Graph(figure=graf_3)
                                                    ]
                                                ),
                                                html.Div(
                                                    [
                                                    html.P("Figura 4 - TCAs nas Regiões de Integração no Estado do "
                                                           "Pará no Brasil.", className="page-2d")
                                                    ], className="fonte",
                                                ),
                                            ],
                                            className="six columns",
                                        ),
                                        html.Div(
                                            [
                                                html.Div(
                                                    [
                                                        dcc.Graph(figure=graf_4),
                                                    ],
                                                ),
                                                html.Div(
                                                    [
                                                    html.P("Figura 5 - Imóveis rurais com TCAs em execução "
                                                            "por Região de Integração.", className="page-2b")
                                                    ], className="fonte",
                                                ),
                                            ],
                                            className="six columns",
                                        ),
                                    ],
                                    className="thirdPage first row",
                                )
                            ],
                            className="page-2c",
                        ),
                    ], className="subpage",
                )
            ],
            className="page",
        ), #Fim pagina 6
        #Pagina 7
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a" ), #page-2a
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6("REGIÃO DE INTEGRAÇÃO BAIXO AMAZONAS", className="page-2b"),
                                        html.P("Na região do Baixo Amazonas, existem 42 imóveis rurais com TCAs em "
                                               "execução, representando 11,5% do total de imóveis no Estado do Pará, "
                                               "sendo a terceira região de integração com maior número de imóveis com "
                                               "TCAs em execução juntamente a região do Tapajós, destes 37 tem "
                                               "licenciamento, com destaque para Mojuí dos Campos (Figura 6). O ano de "
                                               "2021 demonstrou um aumento exponencial no número de imóveis com TCAs "
                                               "em execução, sendo um aumento de 22 imóveis comparado ao ano de "
                                               "2020 (Figura 7).", className="page-2b"),
                                    ],
                                    className="page-3",
                                ),
                            ], className="fonte",
                        ),
                        html.Div(
                            [
                                dcc.Graph(figure=graf_5)
                            ],
                        ),
                        html.Div(
                            [
                                html.P("Figura 6 - Número de imóveis rurais com TCAs em execução e com licenciamento "
                                       "por município no Baixo Amazonas.", className="page-2d")
                            ], className="fonte",
                        ),
                        html.Div(
                            [
                                dcc.Graph(figure=graf_6)
                            ],
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ), #Fim pagina 7
        #Pagina 8
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a" ), #page-2a
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6("REGIÃO DE INTEGRAÇÃO RIO CAPIM", className="page-2b"),
                                        html.P("Encontra-se na região do Rio Capim, 20,3% dos imóveis rurais com TCA em "
                                               "execução, correspondendo os 74 imóveis rurais, destes 53 com "
                                               "licenciamento, sendo que a maior quantidade de imóveis rurais "
                                               "encontra-se no município de Paragominas, com 23 imóveis (Figura 8). "
                                               "O ano de 2021 registrou um grande aumento no número de imóveis com TCAs "
                                               "executados, e no ano de 2022, até março/2022, já registra-se 12 imóveis "
                                               "(Figura 9).", className="page-2b"),
                                    ],
                                    className="page-3",
                                ),
                            ], className="fonte",
                        ),
                        html.Div(
                            [
                                dcc.Graph(figure=graf_7)
                            ],
                        ),
                        html.Div(
                            [
                                html.P("Figura 8 - Número de imóveis rurais com TCAs em execução e com licenciamento "
                                       "por município no Rio Capim.", className="page-2d")
                            ], className="fonte",
                        ),
                        html.Div(
                            [
                                dcc.Graph(figure=graf_8)
                            ],
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ), #Fim pagina 8
        #Pagina 9
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a" ), #page-2a
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6("REGIÃO DE INTEGRAÇÃO TAPAJÓS", className="page-2b"),
                                        html.P("Na região do Tapajós, existem também 42 imóveis rurais com TCAs em "
                                               "execução, representando 11,5% sendo a terceira região de integração com "
                                               "maior número de imóveis com TCAs em execução juntamente a Região do "
                                               "Baixo Amazonas, destes 34 tem licenciamento, com destaque para Novo "
                                               "Progresso, com 25 TCAs executados sendo mais da metade do total na "
                                               "região (Figura 10). O ano de 2020 e 2021 registraram a mesma "
                                               "quantidade de TCAs executados no ano (Figura 11).", className="page-2b"),
                                    ],
                                    className="page-3",
                                ),
                            ], className="fonte",
                        ),
                        html.Div(
                            [
                                dcc.Graph(figure=graf_9)
                            ],
                        ),
                        html.Div(
                            [
                                html.P("Figura 10 - Número de imóveis rurais com TCAs em execução e com licenciamento "
                                       "do Tapajós.", className="page-2d")
                            ], className="fonte",
                        ),
                        html.Div(
                            [
                                dcc.Graph(figure=graf_10)
                            ],
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ), #Fim pagina 9
        # Pagina 10
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a"),  # page-2a
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H6("REGIÃO DE INTEGRAÇÃO XINGU", className="page-2b"),
                                        html.P("A região do Xingu apresenta o maior número de imóveis com TCAs "
                                               "executados, registrando 31,6% do total dos imóveis sendo 115 imóveis "
                                               "rurais os quais 96 com licenciamento, com o munícípio de Uruará "
                                               "registrando o maior número de imóveis - 29 imóveis (Figura 12). "
                                               "No decorrer dos anos, a região também apresentou o maior aumento de "
                                               "imóveis com TCA executados no ano de 2021 (Figura 13).",
                                               className="page-2b"),
                                    ],
                                    className="page-3",
                                ),
                            ], className="fonte",
                        ),
                        html.Div(
                            [
                                dcc.Graph(figure=graf_11)
                            ],
                        ),
                        html.Div(
                            [
                                html.P("Figura 12 - Número de imóveis rurais com TCAs em execução e com licenciamento "
                                       "do Xingu.", className="page-2d")
                            ], className="fonte",
                        ),
                        html.Div(
                            [
                                dcc.Graph(figure=graf_12)
                            ],
                        ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ),  # Fim pagina 10
        #Página 11
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a" ), #page-2a
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H6("REGIÃO DE INTEGRAÇÃO XINGU", className="page-2b"),
                                            html.P("O Programa de Regularização da SEMAS/PA é ferramenta de adequação "
                                                   "de passivos ambientais dos imóveis rurais no Pará, ao aderir ao "
                                                   "PRA os proprietários ou possuidores de imóveis rurais deverão "
                                                   "indicar no CAR seus passivos relativos à manutenção obrigatória de "
                                                   " APP, AUR ou áreas de RL e então assinar o TCA se comprometendo "
                                                   "a cumprir os termos de recomposição ou recuperação destas áreas "
                                                   "definidas no PRADA. Neste sentido, o PRA se define como instrumento "
                                                   "de enfrentamento das irregularidades de imóveis rurais "
                                                   "viabilizando segurança jurídica e ambiental aos produtores rurais, "
                                                   "podendo garantir também, a partir da assinatura do TCA, incentivos "
                                                   "à regularidade de seus imóveis e atividades em que os proprietários "
                                                   "ou possuidores de imóveis rurais poderão até receber pagamentos "
                                                   "pelos serviços ambientais prestados.", className="page-2b"),
                                            html.H6("LEI Nº 12.651, DE 25 DE MAIO DE 2012", className="page-2b"),
                                            html.Ul(
                                                [
                                                    html.Li("Art. 32. São isentos de PMFS:"),
                                                    html.Ol(
                                                        [
                                                        html.Li("O a supressão de florestas e formações sucessoras "
                                                                "para uso alternativo do solo;"),
                                                        html.Li("O manejo e a exploração de florestas plantadas "
                                                                "localizadas fora das Áreas de Preservação Permanente "
                                                                "e de Reserva Legal;"),
                                                        html.Li("A exploração florestal não comercial realizada nas "
                                                                "propriedades rurais a que se refere o inciso V do art."
                                                                " 3º ou por populações tradicionais."),
                                                        ]
                                                    ),
                                                html.Li("Art. 41 - § 4o As atividades de manutenção das Áreas de "
                                                        "Preservação Permanente, de Reserva Legal e de uso restrito "
                                                        "são elegíveis para quaisquer pagamentos ou incentivos por "
                                                        "serviços ambientais, configurando adicionalidade para fins "
                                                        "de mercados nacionais e internacionais de reduções de emissões "
                                                        "certificadas de gases de efeito estufa."),
                                                html.Li("Art. 41 - § 7o O pagamento ou incentivo a serviços ambientais "
                                                        "a que se refere deste artigo serão prioritariamente destinados "
                                                        "aos agricultores familiares como definidos no inciso V do "
                                                        "art. 3º (pequena prórpiedade ou posse rural) desta Lei."),
                                                html.Li(" Art. 52. A intervenção e a supressão de vegetação em Áreas "
                                                        "de Preservação de Reserva Legal para as atividades eventuais "
                                                        "ou de baixo impacto ambiental, previstas no inciso X do art. "
                                                        "3º , excetuadas as alíneas b e g, quando desenvolvidas nos "
                                                        "imóveis a que se refere o inciso V do art. 3º , dependerão de "
                                                        "simples declaração ao órgão ambiental competente, desde que "
                                                        "esteja o imóvel devidamente inscrito no CAR.")
                                                ]
                                            , className="page-2b"
                                            )

                                        ],
                                        className="page-3",
                                    ),
                                ],
                                className="fonte",
                            ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ), #Fim Pagina 11
        #Página 12
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a" ), #page-2a
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Ul(
                                                [
                                                    html.Li("Art. 56. O licenciamento ambiental de PMFS comercial nos "
                                                            "imóveis a que se refere o inciso V do art. 3º se "
                                                            "beneficiará de procedimento simplificado de licenciamento "
                                                            "ambiental."),
                                                    html.Li("Art. 58. Assegurado o controle e a fiscalização dos "
                                                            "órgãos ambientais competentes dos respectivos planos ou "
                                                            "projetos, assim como as obrigações do detentor do imóvel, "
                                                            "o poder público poderá instituir programa de apoio técnico "
                                                            "e incentivos financeiros, podendo incluir medidas "
                                                            "indutoras e linhas de financiamento para atender, "
                                                            "prioritariamente, os imóveis a que se refere o inciso V "
                                                            "do caput do art. 3º."),
                                                    html.Li("Art. 59 - § 4º No período entre a publicação desta Lei e "
                                                            "a implantação do PRA em cada Estado e no Distrito Federal, "
                                                            "bem como após a adesão do interessado ao PRA e enquanto "
                                                            "estiver sendo cumprido o termo de compromisso, o "
                                                            "proprietário ou possuidor não poderá ser autuado por "
                                                            "infrações cometidas antes de 22 de julho de 2008, "
                                                            "relativas à supressão irregular de vegetação em Áreas de "
                                                            "Preservação Permanente, de Reserva Legal e de uso restrito."),
                                                    html.Li("Art. 59 - § 5º A partir da assinatura do termo de "
                                                            "compromisso, serão suspensas as sanções decorrentes das "
                                                            "infrações mencionadas no § 4º deste artigo e, cumpridas as "
                                                            "obrigações estabelecidas no PRA ou no termo de compromisso "
                                                            "para a regularização ambiental das exigências desta Lei, "
                                                            "nos prazos e condições neles estabelecidos, as multas "
                                                            "referidas neste artigo serão consideradas como convertidas "
                                                            "em serviços de preservação, melhoria e recuperação da "
                                                            "qualidade do meio ambiente, regularizando o uso de áreas "
                                                            "rurais consolidadas conforme definido no PRA."),
                                                    html.Li("Art. 60. A assinatura de termo de compromisso para "
                                                            "regularização de imóvel ou posse rural perante o órgão "
                                                            "ambiental competente, mencionado no art. 59, suspenderá a "
                                                            "punibilidade dos crimes previstos nos arts. 38, 39 e 48 da "
                                                            "Lei nº 9.605, de 12 de fevereiro de 1998,  enquanto o "
                                                            "termo estiver sendo cumprido."),
                                                    html.Li("Art. 78-A. Após 31 de dezembro de 2017, as instituições "
                                                            "financeiras só concederão crédito agrícola, em qualquer "
                                                            "de suas modalidades, para proprietários de imóveis rurais "
                                                            "que estejam  inscritos no CAR.")
                                                ]
                                                , className="page-2b"
                                            ),
                                            html.H6("DECRETO Nº 1.379, DE 3 SETEMBRO DE 2015", className="page-2b"),
                                            html.Ul(
                                                [
                                                    html.Li("Art. 5. Os imóveis rurais com área de até 4 (quatro) "
                                                            "módulos fiscais, cuja utilização se enquadre no conceito "
                                                            "de agricultura familiar estabelecido na Lei Federal nº "
                                                            "12.651, de 2012, serão apoiados na elaboração do CAR e, "
                                                            "quando for o caso, nos procedimentos de adesão e "
                                                            "cumprimento do PRA, pelo Governo do Estado do Pará"),

                                                ]
                                                , className="page-2b"
                                            )
                                        ],
                                        className="page-3",
                                    ),
                                ],
                                className="fonte",
                            ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ), #Fim Pagina 12
        #Página 13
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a" ), #page-2a
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Ul(
                                                [
                                                    html.Li("Art. 7. É requisito para adesão ao PRA a inscrição "
                                                            "prévia do imóvel rural no CAR, conforme regulamentação "
                                                            "própria, com a identificação dos remanescentes de "
                                                            "vegetação e passivos ambientais nas APP, áreas de RL ou "
                                                            "de uso restrito, cuja regularização se fará no âmbito "
                                                            "do PRA."),
                                                    html.Li("Art. 8. Identificada a existência de passivos "
                                                            "ambientais, anteriores a 22 de julho de 2008, poderá o "
                                                            "proprietário ou possuidor do imóvel rural requerer a "
                                                            "adesão ao PRA, conforme o art. 4o desta norma, mediante a "
                                                            "declaração das ações que adotará para regularização dessas "
                                                            "áreas, de acordo com as normas técnicas definidas pelo "
                                                            "órgão ambiental competente, bem como as disposições "
                                                            "previstas neste Decreto."),
                                                    html.Li("Art. 9. Na hipótese do proprietário ou possuidor do "
                                                            "imóvel rural não declarar voluntariamente a existência de "
                                                            "todos os passivos ambientais no CAR, será o mesmo "
                                                            "notificado pelo órgão ambiental competente quando de sua "
                                                            "análise para que proceda a retificação das informações "
                                                            "podendo aderir ao PRA, sem prejuízo das penalidades "
                                                            "cabíveis pela omissão das mesmas."),
                                                    html.Li("Art. 22. Protocolado em meio físico ou digital o "
                                                            "pedido de adesão ao PRA/PA, instruído conforme previsto "
                                                            "nesta norma e enquanto estiver sendo cumprido o termo de "
                                                            "compromisso ambiental, o proprietário ou possuidor não "
                                                            "poderá ser autuado por infrações cometidas antes de 22 "
                                                            "de julho de 2008, relativas à supressão irregular de "
                                                            "vegetação em APP, áreas de RL e de uso restrito."),
                                                    html.Li("Art. 24. A assinatura de termo de compromisso para "
                                                            "regularização de imóvel ou posse rural perante o órgão "
                                                            "ambiental competente suspenderá a punibilidade dos crimes "
                                                            "previstos nos arts. 38, 39 e 48 da Lei nº 9.605, de 12 "
                                                            "de fevereiro de 1998, enquanto o termo estiver sendo "
                                                            "cumprido."),
                                                    html.Li("Art. 68. A recomposição das áreas de preservação "
                                                            "permanente sofrerão procedimento especial simplificado "
                                                            "para os imóveis rurais com área de até 4 (quatro) módulos "
                                                            "fiscais, cuja utilização se enquadre no conceito de "
                                                            "agricultura familiar, definida no inciso X do art. 3º da "
                                                            "Lei Federal nº 12.651, de 2012 e conforme disposto no "
                                                            "art. 3º da Lei Federal nº 11.326, de 24 de julho de 2006."),
                                                ]
                                                , className="page-2b"
                                            ),
                                            html.H6("INSTRUÇÃO NORMATIVA Nº 01, DE 08 DE OUTUBRO DE 2020", className="page-2b"),
                                            html.Ul(
                                                [
                                                    html.Li("Art. 24. Os proprietários e possuidores de imóveis "
                                                            "rurais com área até 4 (quatro) módulos fiscais, cuja "
                                                            "utilização se enquadre no conceito de pequena propriedade "
                                                            "ou posse rural familiar estabelecido na Lei Federal nº "
                                                            "12.651, de 2012, poderão obter apoio técnico do Poder "
                                                            "Público Estadual para a recomposição da vegetação "
                                                            "conforme disposto no parágrafo único do art. 54 da Lei "
                                                            "nº 12.651, 2012, bem como todos os procedimentos "
                                                            "aplicáveis ao PRA, incluindo a não obrigatoriedade de "
                                                            "apresentação de ART."),
                                                ]
                                                , className="page-2b"
                                            ),
                                        ],
                                        className="page-3",
                                    ),
                                ],
                                className="fonte",
                            ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ), #Fim Pagina 13
        #Página 14
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a"),  # page-2a
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.P(
                                                    "Parágrafo único. Aplica-se o tratamento disposto no caput deste "
                                                    "artigo, aos proprietários e possuidores de imóveis rurais com "
                                                    "área até 4 (quatro) módulos fiscais que desenvolvam atividades "
                                                    "agrossilvipastoris, bem como aos povos e comunidades tradicionais "
                                                    "que façam uso coletivo do seu território.", className="page-2b"),
                                                html.Ul(
                                                    html.Li("Art. 25. Os proprietários e possuidores rurais "
                                                            "interessados na adesão ao PRA, e que estejam inscritos "
                                                            "em programas e/ou políticas públicas do governo estadual, "
                                                            "relacionadas às ações de preservação, conservação e "
                                                            "regularização ambiental, bem como ao fomento às atividades "
                                                            "sustentáveis, terão prioridade no processo de regularização"
                                                            " ambiental, no âmbito do PRA.")
                                                ),
                                                html.H4("Conclusão", className="page-2b"),
                                                html.P(
                                                    "O presente Relatório objetivou apresentar uma síntese dos "
                                                    "resultados do Programa de Regularização Ambiental (PRA) "
                                                    "efetivados com a assinatura do Termo de Compromisso Ambiental "
                                                    "(TCA) por parte do proprietário ou possuidor do imóvel rural se "
                                                    "comprometendo com o Projeto de Recomposição de Áreas Degradadas e "
                                                    "Alteradas (PRADA), visando regularizar seu passivos ambiental nas "
                                                    "Áreas de Reserva Legal, Áreas de Preservação Permanente e Áreas de "
                                                    "Uso Restrito identificadas por meio da Cadastro Ambiental Rural "
                                                    "(CAR), neste âmbito, da área total dos imóveis rurais com TCAs "
                                                    "firmados, 1,4% corresponde a área de passivo ambiental."
                                                    , className="page-2b"),
                                                html.P(
                                                    "O fortalecimento da gestão ambiental no Pará com o Programa "
                                                    "Regulariza Pará a partir da análise da inscrição dos imóveis "
                                                    "rurais no CAR, na situação cadastral "
                                                    "'analisado, aguardando regularização ambiental (Lei nº 12.651/2012)' do Sistema de "
                                                    "Cadastro Ambiental Rural do Pará - SICAR/PA, foram fatores que "
                                                    "contribuíram o crescimento do número de TCAs firmados no âmbito "
                                                    "do PRA, entre os anos de 2018 a 2021.", className="page-2b"),
                                            ],
                                            className="page-3",
                                        ),
                                    ],
                                    className="fonte",
                                ),
                            ],
                        )
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ), #Fim Pagina 14
        #Página 15
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a"),  # page-2a
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                html.P(
                                                    "O aumento no número de utilizações do instrumento no decorrer dos "
                                                    "anos, que saltou do total de 5 no ano de 2018 para 168 no ano de "
                                                    "2021, fazendo o recorte para os meses de janeiro a março de 2018 "
                                                    "a 2022, registrou-se de 0 em 2018 a 54 em 2022, para os primeiros "
                                                    "meses do ano. Atualmente, 77% dos imóveis rurais com TCA "
                                                    "executado são imóveis que passaram pelo licenciamento, do total "
                                                    "de TCA executados, 21 são atribuídos aos Núcleos Regionais de "
                                                    "Regularidade Ambiental (NUREs).", className="page-2b"),
                                                html.P(
                                                    "Ressalta-se que a municipalização da análise e validação do CAR, "
                                                    "descentralizou esta política através de capacitação dos municípios "
                                                    "para habilita-lo a exercer esta função. O estimulo a adesão ao "
                                                    "PRA seguindo o fluxo do processo de regularização é efetivada a "
                                                    "partir do pagamento e incentivo pelos serviços ambientais "
                                                    "realizados, como: oportunidade de suspensão de multas ambientais "
                                                    "através do compromisso de regularizar as áreas desmatadas, "
                                                    "promover o acesso a crédito rural e demais programas oficiais de "
                                                    "incentivo à produção, comprovação de que está cumprindo com a "
                                                    "regularização ambiental, e segurança jurídica para a atividade "
                                                    "produtiva.", className="page-2b")
                                            ],
                                            className="page-3",
                                        ),
                                    ],
                                    className="fonte",
                                ),
                            ],
                        )
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ), #Fim Pagina 15
        # Pagina 16
        html.Div(
            [
                html.Div(
                    [
                        html.Div([html.H5("Relatório dos TCA's Âmbito PRA")], className="page-2a" ), #page-2a
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H4("Referências", className="page-2b"),
                                            html.P(
                                                "BRASIL. Lei nº 12.651, de 25 de maio de 2012. Dispõe sobre a proteção "
                                                "da vegetação nativa; altera as Leis nºs 6.938, de 31 de agosto de "
                                                "1981, 9.393, de 19 de dezembro de 1996, e 11.428, de 22 de dezembro de "
                                                "2006; revoga as Leis nºs 4.771, de 15 de setembro de 1965, e 7.754, "
                                                "de 14 de abril de 1989, e a Medida Provisória nº 2.166-67, de 24 de "
                                                "agosto de 2001; e dá outras providências. DOU de 28/05/2012. "
                                                "Disponível em: <http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12651.htm> "
                                                "Acesso em 04/04/2022.", className="page-2b"),
                                            html.P(
                                                "SEMAS. Secretaria de Estado de Meio Ambiente e Sustentabilidade. "
                                                "Decreto nº 1.379, de 3 setembro de 2015. Cria o Programa de "
                                                "Regularização Ambiental dos Imóveis Rurais do Estado do Pará – PRA/PA "
                                                "e dá outras providências. DOE de 20/03/2015. Disponível em: "
                                                "<https://www.semas.pa.gov.br/legislacao/normas/view/6673> " 
                                                "Acesso em 04/04/2022.", className="page-2c"),
                                            html.P(
                                                "SEMAS. Secretaria de Estado de Meio Ambiente e Sustentabilidade. "
                                                "Instrução normativa nº 01, de 08 de outubro de 2020. Estabelece os "
                                                "procedimentos e critérios para adesão ao Programa de Regularização "
                                                "Ambiental do Pará – PRA no âmbito da Secretaria de Estado de Meio "
                                                "Ambiente e Sustentabilidade - SEMAS e dá outras providências. "
                                                "DOE 09/10/2020. Disponível em: "
                                                "<https://www.semas.pa.gov.br/legislacao/publico/view/12702> "
                                                "Acesso em 04/04/2022.", className="page-2c"),
                                        ],
                                        className="page-3",
                                    ),
                                ],
                                className="fonte",
                            ),
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ), #Fim Pagina 16
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
