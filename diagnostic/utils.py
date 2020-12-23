""" This file will contain expert system's functions
"""
from experta import KnowledgeEngine, Fact, Field, DefFacts, Rule,\
	MATCH, TEST
from .models import Sickness, DiagnosticXSymphtom


"""
SINTOMA_X_ENFERMEDAD formato con probabilidad
"""
# Configuración del sistema
settings = {
	'umbral': .65,
}
SINTOMA_X_ENFERMEDAD_PROBABILIDAD = {
	'1': [
		{'1': .25},
		{'2': .25},
		{'3': .25},
		{'4': .25},
	],
	'2': [
		{'4': .35},
		{'5': .35},
		{'17': .20},
		{'18': .10},
	],
	'3': [
		{'22': .30},
		{'23': .30},
		{'26': .40},
	],
	'4': [
		{'2': .15},
		{'4': .20},
		{'5': .20},
		{'6': .20},
		{'8': .15},
		{'19': .10},
	],
	'5': [
		{'1': .14},
		{'2': .10},
		{'3': .14},
		{'4': .09},
		{'5': .10},
		{'6': .09},
		{'7': .10},
		{'8': .10},
		{'16': .14},
	],
	'6': [
		{'2': .26},
		{'5': .15},
		{'6': .22},
		{'7': .15},
		{'8': .22},
	],
	'7': [
		{'11': .26},
		{'13': .15},
		{'15': .22},
		{'20': .15},
	],
	'8': [
		{'6': .10},
		{'7': .15},
		{'9': .25},
		{'10': .15},
		{'11': .20},
		{'14': .15},
	],
	'9': [
		{'2': .35},
		{'5': .30},
		{'12': .35},
	],
	'10': [
		{'21': .35},
		{'24': .25},
		{'25': .40},
	],
}

def getProbabilidadDiagnostico(SINTOMA_X_ENFERMEDAD_PROBABILIDAD, _sintomas):
	""" Obtener la probabilidad de diagnostico
	* Iterar cada posible enfermedad
	* Iterar cada sintoma de la enfermedad
	* Si el sintoma fue enviado entonces se suma la probabilidad
	* Una vez todos los sintomas se han comparado retorne la probabilidad total resultante por enfermedad
	* _sintomas = [1, 2, 3, ...]
	* return = [{"1": .84}, {"2": .71}]
	"""
	prob_x_diag = list()
	for enf_key, array_sintomas in SINTOMA_X_ENFERMEDAD_PROBABILIDAD.items():
		# Iniciar en 0 la probabilidad de tener la enfermedad
		prob_decision = 0
		# Recorrer cada sintoma de la enfermedad
		for sintoma in array_sintomas:
			# Separar el objeto en sintoma_key y probabilidad
			for sintoma_key, probabilidad in sintoma.items():
				# Verificar si el sintoma de la enfermedad fue enviado
				if int(sintoma_key) in _sintomas:
					# Si el sintoma esta presente se suma la probabilidad
					prob_decision += float(probabilidad)
		# Agregar al array resultado la probabilidad de la enfermedad
		prob_x_diag.append({enf_key: round(float(prob_decision), 2)})
	return prob_x_diag


class SicknessXProb(Fact):
	key = Field(str, mandatory=True)
	name = Field(str)
	prob = Field(float, mandatory=True)  # Probability

class DiagnosticMachine(KnowledgeEngine):
	@DefFacts()
	def declare_probxdiag(self, prob_x_diag):
		for pxd in prob_x_diag:
			for enf_key, prob in pxd.items():
				yield SicknessXProb(key=enf_key, prob=prob)

	# Diagnostic N°1
	@Rule(
		SicknessXProb(prob=MATCH.p, key=MATCH.k),
		TEST(lambda k: k=="1"),
		TEST(lambda p: p>=settings.get('umbral')))
	def diagnosticate01(self, k, p): set_diagnostique(self.diagnostic, 1)

	# Diagnostic N°2
	@Rule(
		SicknessXProb(prob=MATCH.p, key=MATCH.k),
		TEST(lambda k: k=="2"),
		TEST(lambda p: p>=settings.get('umbral')))
	def diagnosticate02(self, k, p): set_diagnostique(self.diagnostic, 2)

	# Diagnostic N°3
	@Rule(
		SicknessXProb(prob=MATCH.p, key=MATCH.k),
		TEST(lambda k: k=="3"),
		TEST(lambda p: p>=settings.get('umbral')))
	def diagnosticate03(self, k, p): set_diagnostique(self.diagnostic, 3)

	# Diagnostic N°4
	@Rule(
		SicknessXProb(prob=MATCH.p, key=MATCH.k),
		TEST(lambda k: k=="4"),
		TEST(lambda p: p>=settings.get('umbral')))
	def diagnosticate04(self, k, p): set_diagnostique(self.diagnostic, 4)

	# Diagnostic N°5
	@Rule(
		SicknessXProb(prob=MATCH.p, key=MATCH.k),
		TEST(lambda k: k=="5"),
		TEST(lambda p: p>=settings.get('umbral')))
	def diagnosticate05(self, k, p): set_diagnostique(self.diagnostic, 5)

	# Diagnostic N°6
	@Rule(
		SicknessXProb(prob=MATCH.p, key=MATCH.k),
		TEST(lambda k: k=="6"),
		TEST(lambda p: p>=settings.get('umbral')))
	def diagnosticate06(self, k, p): set_diagnostique(self.diagnostic, 6)

	# Diagnostic N°7
	@Rule(
		SicknessXProb(prob=MATCH.p, key=MATCH.k),
		TEST(lambda k: k=="7"),
		TEST(lambda p: p>=settings.get('umbral')))
	def diagnosticate07(self, k, p): set_diagnostique(self.diagnostic, 7)

	# Diagnostic N°8
	@Rule(
		SicknessXProb(prob=MATCH.p, key=MATCH.k),
		TEST(lambda k: k=="8"),
		TEST(lambda p: p>=settings.get('umbral')))
	def diagnosticate08(self, k, p): set_diagnostique(self.diagnostic, 8)

	# Diagnostic N°9
	@Rule(
		SicknessXProb(prob=MATCH.p, key=MATCH.k),
		TEST(lambda k: k=="9"),
		TEST(lambda p: p>=settings.get('umbral')))
	def diagnosticate09(self, k, p): set_diagnostique(self.diagnostic, 9)

	# Diagnostic N°10
	@Rule(
		SicknessXProb(prob=MATCH.p, key=MATCH.k),
		TEST(lambda k: k=="10"),
		TEST(lambda p: p>=settings.get('umbral')))
	def diagnosticate10(self, k, p): set_diagnostique(self.diagnostic, 10)


	# Undefined Diagnostic

def compute_diagnostic(diagnostic):
	print("compute_diagnostic")
	_symphtoms = DiagnosticXSymphtom.objects.filter(diagnostic=diagnostic)
	symphtoms = [int(dxs.symphtom.key) for dxs in _symphtoms]
	print("symphtoms: %s"%symphtoms)
	xsep = getProbabilidadDiagnostico(SINTOMA_X_ENFERMEDAD_PROBABILIDAD, symphtoms)
	print("xsep: %s"%xsep)
	# Delete previous diagnostic's sickness
	diagnostic.sickness = None
	diagnostic.save()
	# Create DiagnosticMachine instance
	dm = DiagnosticMachine()
	# Set initial facts by passing xsep
	dm.reset(prob_x_diag=xsep)
	# Bind diagnostic object to DiagnosticMachine instance
	dm.diagnostic = diagnostic
	# Execute expert system
	dm.run()
	#print("dm.facts")
	#print(dm.facts)
	return True

def set_diagnostique(diagnostic, key):
	diagnostic.sickness = Sickness.objects.get(key=key)
	diagnostic.save()
