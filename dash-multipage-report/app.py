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
with open("C:\\Users\\letic\\Documents\GitHub\\Dashboard_TCA_PRA\\assets\\Arquivos_geojson\\REGIOES_INTEGRACAO.geojson",
          encoding='utf-8') as regiao_integracao:dados_geo = json.load(regiao_integracao)

dados_df = pd.read_excel('C:\\Users\\letic\\Documents\GitHub\\Dashboard_TCA_PRA\\assets\\Arquivos_geojson\\'
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
name_col = ["Região de Integração", 'Área do Imóvel', 'Área a Recompor em RL', 'Área a Recompor em APP']
table_df = pd.read_excel("C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\assets\Dados\\Dados_TCA.xlsx")
table_fig = go.Figure(data=[go.Table(
    header=dict(values=list(name_col),
                fill_color='#003399',
                align=['left', 'center'],
                font=dict(color='white', size=12),
                height=40),
    cells=dict(values=[table_df.RegInt, table_df.AreaImovel, table_df.AR_RL, table_df.AR_APP],
               fill_color='lavender',
               align=['left', 'center'], font=dict(color='black', size=11))
)])
table_fig.update_layout(title_text='Tabela 1 - Áreas dos imóveis rurais.', title_x=0.15,
                        width=620, height=400,
                        margin={"r":0,"l":117,"b":0, "t":30})

################################################# Graficos #############################################################
## Criação do Gráfico 1
# Grafico Número de imóveis rurais com TCAs em execução e com licenciamento por região de integração
data_tab_din = pd.read_excel('C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\assets\\Resultados\\Geral\\'
                             'tab_dinamica_TCA.xlsx')

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
data_ano = pd.read_excel("C:\\Users\\letic\\Documents\\GitHub\\Dashboard_TCA_PRA\\assets\\Resultados\Geral\\"
                         "Ano_Termo_Comp_TCA.xlsx")
data_ano.rename(columns={'Ano_Termo_Compromisso': 'Ano do Termo de Compromisso'}, inplace = True)
data_ano.rename(columns={0: 'Quantidade'}, inplace = True)
graf_2 = px.bar(data_ano, x='Ano do Termo de Compromisso', y='Quantidade', text_auto=True)

## Criação do Gráfico 3
#

## Criação do Gráfico 4
#

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
                                                        html.H6("Secretaria de Estado de Meio Ambiente e Sustentabilidade"),
                                                        html.H5("Relatório dos Termos de Compromissos Executados no Âmbito do PRA"),
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
                                        html.P("Assessora Técnica da Secretaria Adjunta de Gestão e Reguaridade Ambiental"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6(
                                            "Luiz Edinelson Cardoso e Cardoso", className="page-1h"
                                        ),
                                        html.P("Assessor Técnico da Secretaria Adjunta de Gestão e Reguaridade Ambiental"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6("Bruna Coelho da Conceição Pôjo", className="page-1h"),
                                        html.P("Assessora Técnica da Secretaria Adjunta de Gestão e Reguaridade Ambiental"),
                                    ],
                                    className="page-1i",
                                ),
                                html.Div(
                                    [
                                        html.H6("Maíra Moeira do Canto Lopes", className="page-1h"),
                                        html.P("Assessora Técnica da Secretaria Adjunta de Gestão e Reguaridade Ambiental"),
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
                                        html.P("A região do Xingu registrou, nos anos de 2018, 2019, 2021 e 2022, o maior "
                                               "número de imóveis com TCA em execução sendo 5, 26, 53 e 14 imóveis, "
                                               "respectivamente. Já em 2020, a região com maior número de imóveis com TCA em "
                                               "execução foi a de Rio Capim, com 21 imóveis. No decorrer dos anos houve um "
                                               "aumento de imóveis rurais com TCAs em execução, crescendo de 5 imóveis em 2018 "
                                               "para 168 em 2021, ressalta-se que no ano de 2022, até o mês de março, houve "
                                               "registro de 54 imóveis.",
                                               className="page-2b"),
                                    ],
                                    className="page-3",
                                ),
                            ], className="fonte",
                        ),
                    ], className="subpage",
                )
            ],
            className="page",
        ), #Fim pagina 6
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
