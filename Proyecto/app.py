# coding=utf-8
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/')
def index1():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	cur.close()
	conn.close()

	return render_template('index.html')

@app.route('/cant-antenas-hospicio')
def index2():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'Alto Hospicio';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-hospicio.html', antenasENcomuna = antenasENcomuna)

@app.route('/cant-antenas-valparaiso')
def index3():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'Valparaiso';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-valparaiso.html', antenasENcomuna = antenasENcomuna)

@app.route('/cant-antenas-pintana')
def index4():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'La Pintana';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-pintana.html', antenasENcomuna = antenasENcomuna)

@app.route('/cant-antenas-niebla')
def index5():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'Niebla';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-niebla.html', antenasENcomuna = antenasENcomuna)

@app.route('/cant-antenas-rosendo')
def index6():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'San Rosendo';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-rosendo.html', antenasENcomuna = antenasENcomuna)

@app.route('/cant-antenas-curacavi')
def index7():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'Curacavi';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-curacavi.html', antenasENcomuna = antenasENcomuna)

@app.route('/cant-antenas-linares')
def index8():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'Linares';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-linares.html', antenasENcomuna = antenasENcomuna)

@app.route('/cant-antenas-central')
def index9():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'Estacion Central';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-central.html', antenasENcomuna = antenasENcomuna)

@app.route('/cant-antenas-angeles')
def index10():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'Los Angeles';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-angeles.html', antenasENcomuna = antenasENcomuna)

@app.route('/cant-antenas-frutillar')
def index11():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'Frutillar';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-frutillar.html', antenasENcomuna = antenasENcomuna)

@app.route('/cant-antenas-santiago')
def index12():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'Santiago';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-santiago.html', antenasENcomuna = antenasENcomuna)

@app.route('/cant-antenas-niunioa')
def index13():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'Niunioa';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-niunioa.html', antenasENcomuna = antenasENcomuna)

@app.route('/cant-antenas-montt')
def index14():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'Puerto Montt';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-montt.html', antenasENcomuna = antenasENcomuna)

@app.route('/cant-antenas-valdivia')
def index15():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'Valdivia';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-valdivia.html', antenasENcomuna = antenasENcomuna)

@app.route('/cant-antenas-coyhaique')
def index16():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una comuna particular #UNA CONSULTA POR COMUNA, MISMA LOGICA
		cur.execute ("Select count(*) From antenas Where antenas.comuna = 'Coyhaique';")
		conn.commit()
		antenasENcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-coyhaique.html', antenasENcomuna = antenasENcomuna)


@app.route('/antenas-en-cada-comuna')
def index17():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en cada comuna
		cur.execute ("Select count(*), antenas.comuna From antenas Group by antenas.comuna;")
		conn.commit()
		antenasXcomuna = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas-en-cada-comuna.html', antenasXcomuna = antenasXcomuna)


@app.route('/censo')
def index18():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de habitantes por región
		cur.execute ("Select sum(zonas.cant_habitantes), zonas.region From zonas Group by zonas.region;")
		conn.commit()
		tot_habit = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('censo.html', tot_habit = tot_habit)


@app.route('/senal-arica')
def index19():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Arica y Parinacota';")
		conn.commit()
		frecuencia_arica = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_arica.html', frecuencia_arica = frecuencia_arica)

@app.route('/senal-tarapaca')
def index20():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Tarapaca';")
		conn.commit()
		frecuencia_tarapaca = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_tarapaca.html', frecuencia_tarapaca = frecuencia_tarapaca)

@app.route('/senal-antofagasta')
def index21():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Antofagasta';")
		conn.commit()
		frecuencia_antofagasta = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_antofagasta.html', frecuencia_antofagasta = frecuencia_antofagasta)

@app.route('/senal-atacama')
def index22():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Atacama';")
		conn.commit()
		frecuencia_atacama = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_atacama.html', frecuencia_atacama = frecuencia_atacama)

@app.route('/senal-coquimbo')
def index23():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Coquimbo';")
		conn.commit()
		frecuencia_coquimbo = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_coquimbo.html', frecuencia_coquimbo = frecuencia_coquimbo)

@app.route('/senal-valparaiso')
def index24():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Valparaiso';")
		conn.commit()
		frecuencia_valparaiso = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_valparaiso.html', frecuencia_valparaiso = frecuencia_valparaiso)

@app.route('/senal-santiago')
def index25():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Metropolitana de Santiago';")
		conn.commit()
		frecuencia_santiago = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_santiago.html', frecuencia_santiago = frecuencia_santiago)

@app.route('/senal-lbo')
def index26():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Libertador General Bernardo O_Higgins';")
		conn.commit()
		frecuencia_lbo = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_lbo.html', frecuencia_lbo = frecuencia_lbo)

@app.route('/senal-maule')
def index27():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Maule';")
		conn.commit()
		frecuencia_maule = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_maule.html', frecuencia_maule = frecuencia_maule)

@app.route('/senal-nuble')
def index28():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Niuble';")
		conn.commit()
		frecuencia_nuble = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_nuble.html', frecuencia_nuble = frecuencia_nuble)

@app.route('/senal-biobio')
def index29():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Biobio';")
		conn.commit()
		frecuencia_biobio = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_biobio.html', frecuencia_biobio = frecuencia_biobio)

@app.route('/senal-araucania')
def index30():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'La Araucania';")
		conn.commit()
		frecuencia_araucania = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_araucania.html', frecuencia_araucania = frecuencia_araucania)

@app.route('/senal-rios')
def index31():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Los Rios';")
		conn.commit()
		frecuencia_los_rios = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_los_rios.html', frecuencia_los_rios = frecuencia_los_rios)

@app.route('/senal-lagos')
def index32():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Los Lagos';")
		conn.commit()
		frecuencia_los_lagos = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_los_lagos.html', frecuencia_los_lagos = frecuencia_los_lagos)

@app.route('/senal-aysen')
def index33():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Aysen';")
		conn.commit()
		frecuencia_aysen = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_aysen.html', frecuencia_aysen = frecuencia_aysen)

@app.route('/senal-magallanes')
def index34():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Frecuencia promedio de señal en una región especifica
		cur.execute ("Select avg(antenas.frecuencia) From antenas, zonas Where antenas.comuna = zonas.comuna And zonas.region = 'Magallanes y Antartica Chilena';")
		conn.commit()
		frecuencia_magallanes = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_magallanes.html', frecuencia_magallanes = frecuencia_magallanes)


@app.route('/antenas-will')
def index35():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una empresa particular
		cur.execute ("Select count(*) From antenas, empresas, concesionan Where empresas.rut = concesionan.rut_empresa And concesionan.id_antena = antenas.id And Empresas.nombre = 'Will';")
		conn.commit()
		antenasXempresa_will = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenasXempresa_will.html', antenasXempresa_will = antenasXempresa_will)

@app.route('/antenas-virgin')
def index36():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una empresa particular
		cur.execute ("Select count(*) From antenas, empresas, concesionan Where empresas.rut = concesionan.rut_empresa And concesionan.id_antena = antenas.id And Empresas.nombre = 'Virgin Mobile';")
		conn.commit()
		antenasXempresa_virgin = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenasXempresa_virgin.html', antenasXempresa_virgin = antenasXempresa_virgin)

@app.route('/antenas-wom')
def index37():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una empresa particular
		cur.execute ("Select count(*) From antenas, empresas, concesionan Where empresas.rut = concesionan.rut_empresa And concesionan.id_antena = antenas.id And Empresas.nombre = 'WOM';")
		conn.commit()
		antenasXempresa_wom = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenasXempresa_wom.html', antenasXempresa_wom = antenasXempresa_wom)

@app.route('/antenas-claro')
def index38():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una empresa particular
		cur.execute ("Select count(*) From antenas, empresas, concesionan Where empresas.rut = concesionan.rut_empresa And concesionan.id_antena = antenas.id And Empresas.nombre = 'Claro';")
		conn.commit()
		antenasXempresa_claro = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenasXempresa_claro.html', antenasXempresa_claro = antenasXempresa_claro)

@app.route('/antenas-movistar')
def index39():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una empresa particular
		cur.execute ("Select count(*) From antenas, empresas, concesionan Where empresas.rut = concesionan.rut_empresa And concesionan.id_antena = antenas.id And Empresas.nombre = 'Movistar';")
		conn.commit()
		antenasXempresa_movistar = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenasXempresa_movistar.html', antenasXempresa_movistar = antenasXempresa_movistar)

@app.route('/antenas-entel')
def index40():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en una empresa particular
		cur.execute ("Select count(*) From antenas, empresas, concesionan Where empresas.rut = concesionan.rut_empresa And concesionan.id_antena = antenas.id And Empresas.nombre = 'Entel';")
		conn.commit()
		antenasXempresa_entel = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenasXempresa_entel.html', antenasXempresa_entel = antenasXempresa_entel)


@app.route('/antenas-totales-de-cada-empresa')
def index41():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas en cada empresa
		cur.execute ("Select count(*), empresas.nombre  From antenas, empresas, concesionan Where empresas.rut = concesionan.rut_empresa And concesionan.id_antena = antenas.id  Group by empresas.nombre;")
		conn.commit()
		antenas_empresas = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas_empresas.html', antenas_empresas = antenas_empresas)


@app.route('/operativas')
def index42():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Estado de las antenas (mantención (0) o habilitada (1))
		cur.execute ("Select antenas.id, antenas.comuna, zonas.region From antenas, zonas Where antenas.comuna = zonas.comuna And antenas.estado = 1;")
		conn.commit() #si es insert, update o create
		antenas_operativas = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas_operativas.html', antenas_operativas = antenas_operativas)

@app.route('/no-operativas')
def index43():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Estado de las antenas (mantención (0) o habilitada (1))
		cur.execute ("Select antenas.id, antenas.comuna, zonas.region From antenas, zonas Where antenas.comuna = zonas.comuna And antenas.estado = 0;")
		conn.commit() #si es insert, update o create
		antenas_no_operativas = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('antenas_no_operativas.html', antenas_no_operativas = antenas_no_operativas)


@app.route('/inversion-anual')
def index44():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Inversiones a la red móvil según el año
		cur.execute ("Select sum(invierten.monto), invierten.anio_inversion From invierten Group by invierten.anio_inversion; ")
		conn.commit()
		inversion_anual = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('inversion_anual.html', inversion_anual = inversion_anual)




@app.route('/empresa-antenoide')
def index45():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Rut de la empresa con más antenas a nivel nacional
		cur.execute ("Select max(concesionan.rut_empresa) From empresas, concesionan Where empresas.rut = concesionan.rut_empresa And empresas.rut = (select max(concesionan.rut_empresa) from concesionan); ")
		conn.commit()
		empresa_mayor_antenas = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('empresa_mayor_antenas.html', empresa_mayor_antenas = empresa_mayor_antenas)

@app.route('/frecuencia-mas-comun')
def index46():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Tipo de frecuencia más común en cada región
		cur.execute ("Select max(antenas.tipo_frecuencia), zonas.region From antenas, zonas Where antenas.comuna = zonas.comuna Group by zonas.region;" )
		conn.commit()
		frecuencia_region = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('frecuencia_region.html', frecuencia_region = frecuencia_region)

@app.route('/cobertura-total')
def index47():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cobertura total en metros de cada empresa
		cur.execute ("Select empresas.nombre , sum(antenas.radio_cobertura) From empresas, antenas, concesionan Where empresas.rut = concesionan.rut_empresa And concesionan.id_antena = antenas.id Group by empresas.nombre;")
		conn.commit()
		cobertura_total = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('cobertura_total.html', cobertura_total = cobertura_total )



@app.route('/a-1999')
def index48():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 1999;")
		conn.commit() #si es insert, update o create
		region_top_antenas_1999 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_1999.html', region_top_antenas_1999 = region_top_antenas_1999 )

@app.route('/a-2000')
def index49():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2000;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2000 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2000.html', region_top_antenas_2000 = region_top_antenas_2000)

@app.route('/a-2002')
def index50():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2002;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2002 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2002.html', region_top_antenas_2002 = region_top_antenas_2002)

@app.route('/a-2003')
def index51():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2003;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2003 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2003.html', region_top_antenas_2003 = region_top_antenas_2003)

@app.route('/a-2004')
def index52():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2004;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2004 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2004.html', region_top_antenas_2004 = region_top_antenas_2004)

@app.route('/a-2005')
def index53():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2005;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2005 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2005.html', region_top_antenas_2005 = region_top_antenas_2005)

@app.route('/a-2006')
def index54():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2006;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2006 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2006.html', region_top_antenas_2006 = region_top_antenas_2006)

@app.route('/a-2007')
def index55():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2007;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2007 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2007.html', region_top_antenas_2007 = region_top_antenas_2007)

@app.route('/a-2011')
def index56():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2011;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2011 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2011.html', region_top_antenas_2011 = region_top_antenas_2011)

@app.route('/a-2012')
def index57():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2012;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2012 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2012.html', region_top_antenas_2012 = region_top_antenas_2012)

@app.route('/a-2015')
def index58():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2015;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2015 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2015.html', region_top_antenas_2015 = region_top_antenas_2015)

@app.route('/a-2016')
def index59():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2016;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2016 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2016.html', region_top_antenas_2016 = region_top_antenas_2016)

@app.route('/a-2017')
def index60():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2017;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2017 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2017.html', region_top_antenas_2017 = region_top_antenas_2017)

@app.route('/a-2018')
def index61():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2018;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2018 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2018.html', region_top_antenas_2018 = region_top_antenas_2018)

@app.route('/a-2019')
def index62():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2019;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2019 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2019.html', region_top_antenas_2019 = region_top_antenas_2019)

@app.route('/a-2020')
def index63():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2020;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2020 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2020.html', region_top_antenas_2020 = region_top_antenas_2020)

@app.route('/a-2021')
def index64():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Región con mayor cantidad de antenas instaladas en cierto año
		cur.execute ("Select max(zonas.region) From zonas, antenas Where antenas.comuna = zonas.comuna And antenas.anio_instalacion = 2021;")
		conn.commit() #si es insert, update o create
		region_top_antenas_2021 = cur.fetchall() #si es un select
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('region_top_antenas_2021.html', region_top_antenas_2021 = region_top_antenas_2021)


@app.route('/antenas-op')
def index65():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Cantidad de antenas operativas a nivel nacional
		cur.execute ("Select count(*) From antenas Where antenas.estado = 1;")
		conn.commit()
		cantidad_antenas_operativas = cur.fetchall()
	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('cantidad_antenas_operativas.html', cantidad_antenas_operativas = cantidad_antenas_operativas)


@app.route('/empresa-menor-cobertura')
def index66():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Empresa que realizo la mayor inversión a la red
		cur.execute ("Select t1.nombre From (Select empresas.nombre , sum(antenas.radio_cobertura)as suma From empresas, antenas, concesionan Where empresas.rut = concesionan.rut_empresa And concesionan.id_antena = antenas.id Group by empresas.nombre) as t1 Where t1.suma = (select min(t2.suma) from (Select empresas.nombre , sum(antenas.radio_cobertura)as suma From empresas, antenas, concesionan Where empresas.rut = concesionan.rut_empresa And concesionan.id_antena = antenas.id Group by empresas.nombre) as t2);")
		conn.commit()
		empresa_menos_favorable = cur.fetchall()

	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('empresa_menos_favorable.html', empresa_menos_favorable = empresa_menos_favorable)


@app.route('/inversion-empresarial')
def index67():

	conn = psycopg2.connect(
		host = "localhost",
		database = "proyecto",
		user = "postgres",
		port = 5433,
		password = "postpass")

	cur = conn.cursor()

	try:
		#Empresa que realizo la mayor inversión a la red
		cur.execute ("Select Empresas.nombre From Empresas, Invierten Where Empresas.rut = (Select t1.rut_empresa From (Select sum(Invierten.monto) as inversion, Invierten.rut_empresa From Invierten Group by Invierten.rut_empresa)as t1 Where t1.inversion = (Select max(t2.inversion) From (Select sum(Invierten.monto)as inversion From Invierten Group by Invierten.rut_empresa)as t2));")
		conn.commit()
		max_inversion = cur.fetchall()

	except:
		print ("no puedo ejecutar esto")

	cur.close()
	conn.close()
	return render_template('inversion-empresarial.html', max_inversion = max_inversion)

if __name__ == '__main__':
	app.run()
