import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv("country_wise_latest.csv")

Europa = df[
	(df['WHO Region'] == "Europe") &
	(df['Confirmed last week'] > 2000) &
	(df['Deaths'] > 1500) &
	(df['Confirmed'] > 15000)
]


Africa = df[
	(df['WHO Region'] == "Africa") &
	(df['Confirmed last week'] > 2000) &
	(df['New deaths'] < 7) &
	(df['Deaths'] > 70) &
	(df['Confirmed'] >15000)
]

Eastern_Mediterranean = df[
	(df['WHO Region'] == "Eastern Mediterranean") &
	(df['Confirmed last week'] > 2000) & 
	(df['Deaths'] > 70) &
	(df['Confirmed'] >15000)
]


Americas = df[
	(df['WHO Region'] == "Americas") &
	(df['Confirmed last week'] > 2000) &
	(df['Deaths'] > 70) &
	(df['Confirmed'] > 15000)
]

South_East_Asia= df[
	(df['WHO Region'] == "South-East Asia") &
	(df['Confirmed last week'] > 2000) &
	(df['Deaths'] > 0) &
	(df['Confirmed'] > 15000)
]

Western_pacific = df[
	(df['WHO Region'] == "Western Pacific") &
	(df['Confirmed last week'] > 2000) &
	(df['Deaths'] > 0) &
	(df['Confirmed'] > 15000)
]	


Ind_alto = df[
	(df["Confirmed"] > 30000) &
	(df["Deaths"] > 5000) &
	(df["Recovered"] > 5000)
]

Ind_rec = df[
	(df["Confirmed"] < 10000) &
	(df["Deaths"] < 5000) &
	(df["Recovered"] > 3000)
]

	
app = dash.Dash(__name__)
app.layout = html.Div([
	html.H1(["Indíce de Contaminação da Covid19 no Mundo."]),
	html.Br([]),
	html.H4([" Países da Europa com maior taxa de contaminação "]),	
	html.Br([]),
		html.Div([
			dash_table.DataTable(
		    id='table',
		    columns=[{"name": i, "id": i} for i in df.columns],
		    data= Europa.to_dict('records'))]),
		    html.Br([]),
		    html.P(["""• Países que lideram o ranking de contaminação na Europa: """]),
		    html.Br([]),
		    html.Ul([
		    	html.Li(["1° Russia "]),
		    	html.Li(["2° United Kingdom"]),
		    	html.Li(["3° Spain"])
		    ]),
		    html.H3(["Visualização do crescimento de contágio na Europa"]),
		    html.Br([]),
		    dcc.Graph(
	figure = {
		'data' : [
	{'x': 7,
	 'y': Europa['1 week % increase'],'type':"bar", 'name':"Europe",
	}]}),
	
	
	
	html.Hr([]),
	html.Br([]),
	html.Br([]),
	html.H4([" Países da África com maior taxa de contaminação "]),	
		html.Div([
			dash_table.DataTable(
		    id='table2',
		    columns=[{"name": i, "id": i} for i in df.columns],
		    data= Africa.to_dict('records'))]),
		    html.Br([]),
		    html.P(["""• Países que lideram o ranking de contaminação na África: """]),
		    html.Br([]),
		    html.Ul([
		    	html.Li(["1° Nigeria"]),
		    	html.Li(["2° Ghana"]),
		    	html.Li(["3° Kenya"])
		    ]),
		    html.Br([]),
		    html.H3(["Visualização do crescimento de contágio na África"]),
		    dcc.Graph(
	figure = {
		'data' : [
	{'x': 7,
	 'y': Africa['1 week % increase'],'type':"bar", 'name':"Africa"
	}]}),
	
html.Hr([]),	
html.Br([]),
html.Br([]),
	html.H4([" Países do Oriente com maior taxa de contaminação "]),	
		html.Div([
			dash_table.DataTable(
		    id='table3',
		    columns=[{"name": i, "id": i} for i in df.columns],
		    data= Eastern_Mediterranean.to_dict('records'))]),
		    html.Br([]),
		    html.P(["""• Países que lideram o ranking de contaminação na Oriente: """]),
		    html.Br([]),
		    html.Ul([
		    	html.Li(["1° Iran"]),
		    	html.Li(["2° Pakistan"]),
		    	html.Li(["3° Saudi Arabia"])
		    ]),
		    html.Br([]),
		    html.H3(["Visualização do crescimento de contágio na Eastern Mediterranea"]),
		    html.Br([]),
		    dcc.Graph(
	figure = {
		'data' : [
	{'x': 7,
	 'y': Eastern_Mediterranean['1 week % increase'],'type':"bar", 'name':"Eastern Mediterranea"
	}]}),
	
	
html.Hr([]),	
html.Br([]),
html.Br([]),	
	html.H4([" Países da Ámerica com maior taxa de contaminação "]),
	html.Br([]),	
		html.Div([
			dash_table.DataTable(
		    id='table4',
		    columns=[{"name": i, "id": i} for i in df.columns],
		    data= Americas.to_dict('records'))]),
		    html.Br([]),
		   html.P(["""• Países que lideram o ranking de contaminação na Ámerica: """]),
		    html.Br([]),
		    html.Ul([
		    	html.Li(["1° Venezuela"]),
		    	html.Li(["2° Costa Rica"]),
		    	html.Li(["3° El Salvador"])
		    ]),
		    html.Br([]),
		    html.H3(["Visualização do crescimento de contágio na América"]),
		    dcc.Graph(
	figure = {
		'data' : [
	{'x': 7,
	 'y': Americas['1 week % increase'],'type':"bar", 'name':"Americas"
	}]}),
	
		
		
		
html.Hr([]),		
html.Br([]),
html.Br([]),		
	html.H4([" Países da Ásia com maior taxa de contaminação "]),
	html.Br([]),
		html.Div([
			dash_table.DataTable(
		    id='table5',
		    columns=[{"name": i, "id": i} for i in df.columns],
		    data= South_East_Asia.to_dict('records'))]),
		    html.Br([]),
		    html.P(["""• Países que lideram o ranking de contaminação na Ásia:"""]),
		    html.Br([]),
		    html.Ul([
		    	html.Li(["1° Bangladesh"]),
		    	html.Li(["2° Índia"]),
		    	html.Li(["3° Indonésia"])
		    ]),
		    html.Br([]),
		    html.H3(["Visualização do crescimento de contágio na Ásia"]),
		    dcc.Graph(
	figure = {
		'data' : [
	{'x': 7,
	 'y': South_East_Asia['1 week % increase'],'type':"bar", 'name':"South_East_Asia"
	}]}),
	

html.Hr([]),
html.Br([]),
html.Br([]),
	html.H4([" Países do Ocidente com maior taxa de contaminação "]),	
		html.Div([
			dash_table.DataTable(
		    id='table6',
		    columns=[{"name": i, "id": i} for i in df.columns],
		    data= Western_pacific.to_dict('records'))]),
		    html.Br([]),
		    html.P(["""• Países que lideram o ranking de contaminação na Ocidente:"""]),
html.Br([]),
		    html.Ul([
		    	html.Li(["1° China"]),
		    	html.Li(["2° Philippines"]),
		    	html.Li(["3° Singapore"])
		    ]),
		    html.H3(["Visualização do crescimento de contágio no Ocidente"]),
		    dcc.Graph(
	figure = {
		'data' : [
	{'x': 7,
	 'y': Western_pacific['1 week % increase'],'type':"bar", 'name':"Africa"
	}]}),

			html.Hr([]),
			html.H3([" Picos da doença no Mundo "]),
		    html.Div([
			dash_table.DataTable(
		    id='table7',
		    columns=[{"name": i, "id": i} for i in df.columns],
		    data= Ind_alto.to_dict('records'))]),
		    
		    html.Br([]),
		    html.H3([" Países com índice de contágio baixo no Mundo "]),
		    html.Div([
			dash_table.DataTable(
		    id='tabl8',
		    columns=[{"name": i, "id": i} for i in df.columns],
		    data= Ind_rec.to_dict('records'))]),
html.Br([]),
html.Br([]),		    		    
#html.P(["""Atualmente sabemos que a pandemia mundial se alastrou de forma muito rápida, e está muito forte ainda, por conta das novas variantes que surgiram nos últimos dias. Torna-se necessário medidas críticas de combate ao vírus, e o isolamneto social é uma das armas mais fortes que temos no agora, sendo que a vacina é priordade para profissionais da saúde e para idosos maiores de 83 anos, sendo assim fique em casa, use a máscara e alcoól em gel,para vencermos essa pandemia."""]),
html.Br([]),
html.Br([]),


])		    
if __name__ == '__main__':
    app.run_server(debug=True)



