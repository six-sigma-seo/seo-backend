""" Some utilities that are used in the application"""

#Python
import requests
import json
import os


class Utils:

    def test(web_site):
        r = requests.get('https://app.scrapinghub.com/api/v2/datasets/UhNGprd2Cts/download?format=json') 
        if r.status_code == 200:
            data = r.text
        else:
            data = 0
        return data

    def get_data_scrapy(web_site):
        os.chdir('search/search')
        os.system(f"scrapy crawl seo -a domain={web_site}")
        os.chdir('../')
        os.chdir('../')
        with open('search/search/seo.json', "r") as file:
            data = file.read()
            data = data[1:]
            data = data[:-1]
            data = json.loads(data)
        general_data = {
                            "date": data['date'],
                            "titilepage": data['titlepage'],
                            "metadescription": data['metadescription'],
                            "features" : [
                                {
                                "title": "Alternativas Textuales",
                                "description": "Todos los elementos no visuales de la pagina deben incluir la etiqueta alt para facilitar la lectrura por el robot de Google.",
                                "boolean": data['booleanAT'],
                                "endpoint": "/textualalternatives"
                                },
                                {
                                "title": "Titulo de pagina",
                                "description": "Unicamente debe exister una etiqueta title dentro de la estructura de la pagina y el contendio de esta debe ser descriptivo en relación al contenido de la pagina.",
                                "boolean": data['booleanTP'],
                                "endpoint": "/titlepage"
                                },
                                {
                                "title": "Deaclaración de idioma",
                                "description": "Se debe especificar el idioma de la pagina con la etiqueta: <html lang=eng>.",
                                "boolean": data['booleanDI'],
                                "endpoint": "/languagedeclaration"
                                },
                                {
                                "title": "Estructura Semantica",
                                "description": "La pagina deberia utilizar un mínimo de etiquetas semánticas las cuales son: header, section, footer, main.",
                                "boolean": data['booleanES'],
                                "endpoint": "/semanticstructure"
                                },
                                {
                                "title": "Etiqueta Arial",
                                "description": "Las etiquetas de button e input deberian tener el atributo aria-label y el contenido de este debe ser superior a 6 caracteres.",
                                "boolean": data['booleanEA'],
                                "endpoint": "/ariallabel"
                                },
                                {
                                "title": "Jerarquias Textuales",
                                "description": "La etiquetas de titulos deben seguir un jerarquia de acuerdo a su orden, solo deberia usarse una vez la etiqueta <h1> por ejemplo.",
                                "boolean": data['booleanJT'],
                                "endpoint": "/textualhierarchies"
                                },
                                {
                                "title": "Etiquetas en desuso",
                                "description": "Con el paso de las versiones de html se han dejado de usar ciertas etiquetas, se recomienda su sustitución.",
                                "boolean": data['booleanED'],
                                "endpoint": "/disusedlabels"
                                },
                                {
                                "title": "Meta información",
                                "description": "Se recomienda el uso de las etiquetas de meta información para asegurar que el robot de google entienda nuestra pagina. Así como para la correcta representación en redes sociales.",
                                "boolean": data['booleanMI'],
                                "endpoint": "/metadescription"
                                }
                            ]
                        }
        os.system("rm search/search/seo.json")
        return data, general_data

    def get_textual_alternatives(data):
        """ something """
        textual_data = {
                            "imgwithoutalt": data['imgwithoutalt'],
                            "qtyimgwithoutalt": data['qtyimgwithoutalt'],
                            "imgwithaltempty": data['imgwithaltempty'],
                            "qtyimgwithaltempty": data['qtyimgwithaltempty'],
                            "totalimg": data['totalimg'],
                            "percentajeemptyaltinimg": data['percentajeemptyaltinimg']
                        }
        return textual_data
    
    def get_meta_data(data):
        """ something """
        meta_data = {
                        "metadescription": data['metadescription'],
                        "lenthmetadescription": data['lenthmetadescription'],
                        "rigthdimensionmetadescription": data['rigthdimensionmetadescription'],
                        "qtymetadescription": data['qtymetadescription'],
                        "google": data['google'],
                        "facebook": data['facebook'],
                        "twitter": data['twitter']
                    }
        return meta_data


    def get_titlepage_data(data):
        """something"""
        titlepage_data = {
                            "titlepage": data['titlepage'], 
                            "qtytitlepage": data['qtytitlepage'],
                            "lenthtitlepage": data['lenthtitlepage'],
                            "rigthdimensiontitlepage": data['rigthdimensiontitlepage'],
                        }
        return titlepage_data
    

    def get_languagedeclaration_data(data):
        """something"""
        languagedeclaration_data = {
                                    "language_tag":data['language_tag']
                                }
        return languagedeclaration_data
    

    def get_semanticstructure_data(data):
        """something"""
        semanticstructure_data = {
                            "title_duplicated":data['title_duplicated'],
                            "old_tags":data['old_tags'],
                            "number_tags_h1":data['number_tags_h1'],
                            "number_tags_h2":data['number_tags_h2'],
                            "header":data['header'],
                            "footer":data['footer']
                        }
        return semanticstructure_data

    def get_ariallabel_data(data):
        """something"""
        semanticstructure_data = {
                            "buttons_without_arial_tags":data['buttons_without_arial_tags'],
                        }
        return semanticstructure_data


    def get_textualhierarchies_data(data):
        """something"""
        textualhierarchies_data = {
                                    "h1title": data['h1title'],
                                    "qtyh1title": data['qtyh1title']
                                }
        return textualhierarchies_data

    def get_disusedlabels_data(data):
        """something"""
        disusedlabels_data = {
                                "keywords": data['keywords'],
                                "qtymeta_keywords": data['qtymeta_keywords'],
                            }
        return disusedlabels_data