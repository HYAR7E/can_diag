""" Formato de presentación de SINTOMA_X_ENFERMEDAD
# Forma básica
SINTOMA_X_ENFERMEDAD = {
	enfermedad_id: [sintoma_id, sintoma_id],
	enfermedad_id: [sintoma_id, sintoma_id],
}

# Forma con probabilidades
SINTOMA_X_ENFERMEDAD = {
	enfermedad_id: [
		{sintoma_id: probabilidad},
		{sintoma_id: probabilidad},
	],
	enfermedad_id: [
		{sintoma_id: probabilidad},
		{sintoma_id: probabilidad},
	],
}
"""


# Ejemplos de SINTOMA_X_ENFERMEDAD formato básico
SINTOMA_X_ENFERMEDAD_BASICO = {
	1: [1, 2, 3, 4],
	2: [4, 5, 17, 18],
	3: [22, 23, 26],
	4: [2, 4, 5, 6, 8, 19],
	5: [1, 2, 3, 4, 5, 6, 7, 8, 24],
	6: [2, 5, 6, 7, 8],
	7: [11, 13, 15, 20],
	8: [6, 7, 9, 10, 11, 14],
	9: [3, 5, 12],
	10: [21, 24, 25],
}


# Ejemplos de SINTOMA_X_ENFERMEDAD formato con probabilidad
SINTOMA_X_ENFERMEDAD_PROBABILIDAD = {
	1: [
		{1: .25},
		{2: .25},
		{3: .25},
		{4: .25},
	],
	2: [
		{4: .35},
		{5: .35},
		{17: .20},
		{18: .10},
	],
	3: [
		{22: .30},
		{23: .30},
		{26: .40},
	],
	4: [
		{2: .15},
		{4: .20},
		{5: .20},
		{6: .20},
		{8: .15},
		{19: .10},
	],
	5: [
		{1: .14},
		{2: .10},
		{3: .14},
		{4: .09},
		{5: .10},
		{6: .09},
		{7: .10},
		{8: .10},
		{16: .14},
	],
	6: [
		{2: .26},
		{5: .15},
		{6: .22},
		{7: .15},
		{8: .22},
	],
	7: [
		{11: .26},
		{13: .15},
		{15: .22},
		{20: .15},
	],
	8: [
		{6: .10},
		{7: .15},
		{9: .25},
		{10: .15},
		{11: .20},
		{14: .15},
	],
	9: [
		{2: .35},
		{5: .30},
		{12: .35},
	],
	10: [
		{21: .35},
		{24: .25},
		{25: .40},
	],
}


# Configuración del sistema
settings = {
	'umbral_desicion': .7,
}



def diagnosticoBasico(SINTOMA_X_ENFERMEDAD_BASICO, _sintomas):
	""" Comparar arrays estaticos
	* Forma más básica de diagnostico
	* _sintomas = [1, 2, 3, ...]
	"""
	for enfermedad_id, sintomas in SINTOMA_X_ENFERMEDAD_BASICO.items():
		# Comparar la longitud del array
		if len(_sintomas) != len(sintomas):
			# Si los array tienen distintas longitudes
			# Pasar al siguiente array
			continue
		# Comparar los array
		if _sintomas == sintomas:
			# Si los array de sintomas son los mismos
			# Retornar el id de la enfermedad encontrada
			return enfermedad_id
	# Retornar -1 (representa un indice no encontrado)
	return -1


def diagnosticoProbabilidad(SINTOMA_X_ENFERMEDAD_PROBABILIDAD, _sintomas):
	""" Diagnostico basado en probabilidad de suceso
	* Iterar cada posible enfermedad
	* Iterar cada sintoma de la enfermedad
	* Si el sintoma fue enviado entonces se suma la probabilidad
	* Una vez todos los sintomas se han comparado se resuelve si la probabilidad supera el umbral de suceso
	* _sintomas = [1, 2, 3, ...]
	"""
	for enfermedad_id, array_sintomas in SINTOMA_X_ENFERMEDAD_PROBABILIDAD.items():
		# Iniciar en 0 la probabilidad de tener la enfermedad
		probabilidad_desicion = 0
		# Recorrer los sintomas de la enfermedad
		for sintomas in array_sintomas:
			# Separar el objeto en sintoma_id y probabilidad
			for sintoma_id, probabilidad in array_sintomas.items():
				# Verificar si el sintoma de la enfermedad fue enviado
				if sintoma_id in _sintomas:
					# Si el sintoma esta presente se suma la probabilidad
					probabilidad_desicion += probabilidad
		# Si la probabilidad total de la enfermedad supera el umbral
		if probabilidad_desicion > settings.umbral_desicion:
			# Se retorna el id de la enfermedad
			return enfermedad_id
		# Si no se supera el umbral se continua buscando en las siguientes enfermedades
	return -1
