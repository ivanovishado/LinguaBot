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
    'temas_de_la_segunda_seccion': ["pronombres personales", "números", "formar plurales",
                                    "vocabulario"],
    'tipos_de_pronombres': ["sujeto", "adjetivo", "objeto", "posesivos", "reflexivos"],
    'tipos_de_sustantivos': ["plural", "singular"],
    'tipos_de_singular': ["regulares", "irregulares"],
    'tipos_de_numeros': ["cardinales", "ordinales"]
}


def elimina_tildes(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
