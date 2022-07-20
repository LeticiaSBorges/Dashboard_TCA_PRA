# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pandas as pd
import lorem
import pathlib

# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("Data").resolve()

## Read in data
#supplyDemand = pd.read_csv(DATA_PATH.joinpath("supplyDemand.csv"))
#actualSeasonal = pd.read_csv(DATA_PATH.joinpath("actualSeasonal.csv"))
#industrailProd = pd.read_csv(DATA_PATH.joinpath("industrailProd.csv"))
#globalMarket = pd.read_csv(DATA_PATH.joinpath("globalMarket.csv"))
#oecdCommersial = pd.read_csv(DATA_PATH.joinpath("oecdCommersial.csv"))
#wtiPrices = pd.read_csv(DATA_PATH.joinpath("wtiPrices.csv"))
#epxEquity = pd.read_csv(DATA_PATH.joinpath("epxEquity.csv"))
#chinaSpr = pd.read_csv(DATA_PATH.joinpath("chinaSpr.csv"))
#oecdIndustry = pd.read_csv(DATA_PATH.joinpath("oecdIndustry.csv"))
#wtiOilprices = pd.read_csv(DATA_PATH.joinpath("wtiOilprices.csv"))
#productionCost = pd.read_csv(DATA_PATH.joinpath("productionCost.csv"))
#production2015 = pd.read_csv(DATA_PATH.joinpath("production2015.csv"))
#energyShare = pd.read_csv(DATA_PATH.joinpath("energyShare.csv"))
#adjustedSales = pd.read_csv(DATA_PATH.joinpath("adjustedSales.csv"))
#growthGdp = pd.read_csv(DATA_PATH.joinpath("growthGdp.csv"))

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
                        html.Div([html.H4("Relatório dos TCA's Âmbito PRA")], className="page-2a" ), #page-2a
                        html.Div(
                            [
                                html.H3("Introdução", className="page-2b"),
                                html.P("Diante dos desafios globais para garantir o combate das mudanças do clima e "
                                        "monitoramento quanto ao uso e ocupação do solo, o Programa de Regularização "
                                        "Ambiental (PRA) se apresenta como instrumento de gestão ambiental, que "
                                        "compreende o conjunto de ações ou iniciativas a serem desenvolvidas por "
                                        "proprietários rurais com o objetivo de adequar e promover a regularização "
                                        "ambiental com vistas ao cumprimento do disposto no art. 59 da Lei Federal nº "
                                        "12.651/2012.", className="page-2b"),
                                html.P("No Pará, o Governo do Estado instituiu o Programa de Regularização Ambiental dos "
                                        "Imóveis Rurais, por meio de Decreto Estadual nº 1.379/2015, com o objetivo de promover a "
                                        "regularização ambiental das posses e propriedades rurais do Estado, em que tenha sido "
                                        "verificada a existência de passivos ambientais, relativos às áreas de preservação permanente "
                                        "(APPs), de reserva legal (RL) e de uso restrito (AUR), detectados na análise do Cadastro "
                                        "Ambiental Rural – CAR.", className="page-2c"),
                                html.P("No âmbito do PRA, a Instrução Normativa SEMAS/PA nº 1/2020, estabelece "
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
                        html.Div([html.H4("Relatório dos TCA's Âmbito PRA")], className="page-2a" ), #page-2a
                        html.Div(
                            [
                                html.H3("Metodologia", className="page-2b"),
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
                    ],
                    className="subpage",
                )
            ],
            className="page",
        ), #Fim pagina 3
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
