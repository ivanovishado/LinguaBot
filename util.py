import unicodedata

topicos = {
    'pronombre': ["i", "you", "he", "she", "it", "we", "they"],
    'pronombre_de_adjetivo': ["my", "your", "his", "her", "its", "our", "you", "their"],
    'pronombre_de_objeto': ["me", "you", "him", "her", "it", "us", "you", "them"],
    'pronombre_posesivo': ["mine", "yours", "his", "hers", "its", "ours", "theirs"],
    'pronombre_reflexivo': ["myself", "yourself", "himself", "herself", "itself", "ourselves",
                            "yourselves", "themselves", "each other"],
    'plurales': ["s", "es", "ies", "ves"],
    'presentaciones': ["saludos", "despedidas", "nuevas presentaciones"],
    'temas_de_la_segunda_seccion': ["pronombres personales", "números ordinales",
                                    "números cardinales", "formar plurales", "vocabulario"],
    'tipos_de_pronombres': ["sujeto", "adjetivo", "objeto", "posesivos", "reflexivos"],
    'tipos_de_sustantivos': ["plural", "singular"],
    'tipos_de_singular': ["regulares", "irregulares"],
    'tipos_de_numeros': ["cardinales", "ordinales"],
    'numeros_cardinales': ["1 al 12", "13 al 19", "20 al 90", "formar decenas", "formar centenas",
                        "centenas con docenas", "millares", "millones"],
    'numeros_ordinales': ["primero al tercero", "cuarto al decimoavo", "docenas millares millon",
                       "formar decenas"]
}


def elimina_tildes(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
