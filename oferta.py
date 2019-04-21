import  requests
import json
from bs4 import BeautifulSoup
import datetime

class Oferta:
    def __init__(self):
        self.lista = []
        pass

    def to_json(self, nombre):
        with open(nombre, 'w') as archivo:
            json.dump(self.lista, archivo, sort_keys=False, indent=4)

    def scrapping(self, url):
        r = requests.get(url)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')
        items = soup.find_all('tr')

        self.scrapping_oferta(items)


    def scrapping_oferta(self, oferta):
        nrc = ""
        clave = ""
        materia = ""
        seccion = ""
        creditos = ""
        cupo = ""
        disponible = ""
        sesion = ""
        hora = ""
        dias = ""
        edificio = ""
        aula =""
        periodo =""
        profesor = ""
        nroFila = 0
        nroCelda = 0
        tam = 2

        for fila in oferta:
            if nroFila == len(oferta) - 2:
                break
            if nroFila == tam:
                tam = nroFila + int((len(fila.find_all('td')) / 6) + 1)
                nroCelda = 0
                for celda in fila.find_all('td'):
                    if nroCelda == 0:
                        nrc = celda.text
                        print("NRC:", nrc)
                    if nroCelda == 1:
                        clave = celda.text
                        print("Clave:", clave)
                    if nroCelda == 2:
                        materia = celda.text
                        print("Materia:", materia)
                    if nroCelda == 3:
                        seccion = celda.text
                        print("Seccion:", seccion)
                    if nroCelda == 4:
                        creditos = celda.text
                        print("Creditos:", creditos)
                    if nroCelda == 5:
                        cupo = celda.text
                        print("Cupo:", cupo)
                    if nroCelda == 6:
                        disponible= celda.text
                        print("Disponibles:", disponible)
                    if nroCelda == 7:
                    #     sesion = celda.text
                    #     print("Sesion:", sesion)
                    # if nroCelda == 9:
                    #     hora = celda.text
                    #     print("Hora:", hora)
                    # if nroCelda == 10:
                    #     dias = celda.text
                    #     print("Dias:", dias)
                    # if nroCelda == 11:
                    #     edificio = celda.text
                    #     print("Edificio:", edificio)
                    # if nroCelda == 12:
                    #     aula = celda.text
                    #     print("Aula:", aula)
                    # if nroCelda == 13:
                    #     periodo = celda.text
                    #     print("Periodo:", periodo)
                    # if nroCelda == 16:
                    #     profesor = celda.text
                    #     print("Profesor:", profesor)
                        for i in fila.find_all('tr'):
                            nroCelda2 = 0
                            for a in i.find_all('td'):
                                if len(i.find_all('td')) == 6:
                                    break
                                if nroCelda2 == 0:
                                    sesion = a.text
                                    print("Sesion:", sesion)
                                if nroCelda2 == 1:
                                    profesor = a.text
                                    print("Profesor:", profesor)
                                nroCelda2 = nroCelda2 + 1

                        for i in fila.find_all('tr'):
                            nroCelda2 = 0
                            for a in i.find_all('td'):
                                if len(i.find_all('td')) == 2:
                                    break
                                if nroCelda2 == 0:
                                    sesion = a.text
                                    print("Sesion:", sesion)
                                if nroCelda2 == 1:
                                    hora = a.text
                                    print("Hora:", hora)
                                if nroCelda2 == 2:
                                    # dias = a.text
                                    dias = ""
                                    for c in a.text:
                                        if c is not "." and c is not ' ':
                                            dias += c
                                    print("Dias:", dias)
                                if nroCelda2 == 3:
                                    edificio = a.text
                                    print("Edificio:", edificio)
                                if nroCelda2 == 4:
                                    aula = a.text
                                    print("Aula:", aula)
                                if nroCelda2 == 5:
                                    periodo = a.text
                                    print("Periodo:", periodo)
                                    ofertas = {
                                        "nrc": nrc,
                                        "clave": clave,
                                        "materia": materia,
                                        "seccion": seccion,
                                        "cr": creditos,
                                        "cupo": cupo,
                                        "disponibles": disponible,
                                        "Sesion": sesion,
                                        "Horas": hora,
                                        "Dias": dias,
                                        "Edificio": edificio,
                                        "Aula": aula,
                                        "Periodo": periodo,
                                        "Ses": sesion,
                                        "Profesor": profesor
                                    }
                                    self.lista.append(ofertas)
                                nroCelda2 = nroCelda2 + 1


                    # if nroCelda == 16:
                    #     profesor = celda.text
                    #     print("Profesor:", profesor)

                    nroCelda = nroCelda + 1
                # ofertas = {
                #         "nrc": nrc,
                #         "clave": clave,
                #         "materia":materia,
                #         "seccion": seccion,
                #         "cr": creditos,
                #         "cupo": cupo,
                #         "disponibles": disponible,
                #         "Sesion": sesion,
                #         "Horas": hora,
                #         "Dias":dias,
                #         "Edificio":edificio,
                #         "Aula":aula,
                #         "Periodo":periodo,
                #         "Ses": sesion,
                #         "Profesor": profesor
                #     }
                # self.lista.append(ofertas)
            nroFila = nroFila + 1

