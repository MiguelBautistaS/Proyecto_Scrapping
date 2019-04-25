import glob
import json
import mysql.connector
import codecs


conexion = mysql.connector.connect(user ='miguel', password='12345', database='materias')

cursor = conexion.cursor()

files = glob.glob('*.json')

days = {'L':1, 'M':2, 'I':3, 'J':4, 'V':5, 'S':6, 'D':7}

def insertarBienRaiz(materia):


    pass

def existe_clave(materia):
    query = 'SELECT * FROM clave where clave = %s'
    cursor.execute(query, (materia['clave'],))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True


def existe_seccion(materia):
    query = 'SELECT * FROM seccion where seccion = %s'
    cursor.execute(query, (materia['seccion'],))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True

def existe_profesor(materia):
    query = 'SELECT * FROM profesor where nombre = %s'
    cursor.execute(query, (materia['Profesor'],))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True

def existe_hora(hora):
    query = 'SELECT * FROM hora where hora = %s'
    cursor.execute(query, (hora,))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True


def existe_hora_inicial(materia):
    hora = materia['Horas'][:4]
    return  existe_hora(hora)


def existe_hora_final(materia):
    hora = materia['Horas'][5:9]
    return  existe_hora(hora)

def existe_edificio(materia):
    query = 'SELECT * FROM edificio where edificio = %s'
    cursor.execute(query, (materia['Edificio'],))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True


def existe_periodo(materia):
    query = 'SELECT * FROM periodo where periodo = %s'
    cursor.execute(query, (materia['Edificio'],))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True


def existe_aula(materia):
    query = 'SELECT * FROM aula where aula = %s'
    cursor.execute(query, (materia['Aula'],))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True


def existe_detalle(materia):
    query = 'SELECT * FROM detalle where nrc = %s'
    cursor.execute(query, (materia['nrc'],))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True

def existe_oferta(materia):
    query = 'SELECT * FROM oferta where nrc = %s'
    cursor.execute(query, (materia['nrc'],))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True

def existe_horario(id_hora_inicial, id_hora_final, id_periodo):
    query = 'SELECT * FROM horario where hora_inicial = %s AND hora_final = %s AND periodo = %s'
    cursor.execute(query, (id_hora_inicial, id_hora_final, id_periodo))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True

def existe_edificios(materia, id_edificio):
    query = 'SELECT * FROM edificios WHERE nrc = %s AND id_edificio = %s'
    cursor.execute(query, (materia['nrc'], id_edificio))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True


def existe_aulas(materia, id_aula):
    query = 'SELECT * FROM aulas WHERE nrc = %s AND id_aula = %s'
    cursor.execute(query, (materia['nrc'], id_aula))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True


def existe_horarios(materia, id_horario):
    query = 'SELECT * FROM horarios WHERE nrc = %s AND id_horario = %s'
    cursor.execute(query, (materia['nrc'], id_horario))
    rows = cursor.fetchall()
    if len(rows) == 0:
        return False
    else:
        return True

# -------------------------------------------------------------------------
def insertar_clave(materia):
    query = 'INSERT INTO clave(clave, materia) VALUES(%s,%s)'
    cursor.execute(query, (materia['clave'],materia['materia']))
    conexion.commit()

def insertar_seccion(materia):
    query = 'INSERT INTO seccion(seccion) VALUES(%s)'
    cursor.execute(query, (materia['seccion'],))
    conexion.commit()


def insertar_profesor(materia):
    query = 'INSERT INTO profesor(nombre) VALUES(%s)'
    cursor.execute(query, (materia['Profesor'],))
    conexion.commit()


def insertar_hora(hora):
        query = 'INSERT INTO hora(hora) VALUES(%s)'
        cursor.execute(query, (hora,))
        conexion.commit()


def insertar_hora_inicial(materia):
    hora = materia['Horas'][:4]
    insertar_hora(hora)


def insertar_hora_final(materia):
    hora = materia['Horas'][5:9]
    insertar_hora(hora)


def insertar_edificio(materia):
    query = 'INSERT INTO edificio(edificio) VALUES(%s)'
    cursor.execute(query, (materia['Edificio'],))
    conexion.commit()


def insertar_periodo(materia):
    query = 'INSERT INTO periodo(periodo) VALUES(%s)'
    cursor.execute(query, (materia['Periodo'],))
    conexion.commit()

def insertar_aula(materia, id_edificio):
    query = 'INSERT INTO aula(aula, edificio) VALUES(%s, %s)'
    cursor.execute(query, (materia['Aula'],id_edificio))
    conexion.commit()


def insertar_detalle(materia):
    query = 'INSERT INTO detalle(nrc, creditos, cupos_totales, cupos_disponibles) VALUES(%s, %s, %s, %s)'
    cursor.execute(query, (materia['nrc'], materia['cr'], materia['cupo'], materia['disponibles']))
    conexion.commit()


def insertar_dia(materia, dia):
    query = 'INSERT INTO dias(nrc, id_dia) VALUES(%s, %s)'
    print(materia['nrc'], days[dia])
    cursor.execute(query, (materia['nrc'], days[dia]))
    conexion.commit()


def insertar_horario(id_hora_inicial, id_hora_final, id_periodo):
    query = 'INSERT INTO horario(hora_inicial, hora_final, periodo) VALUES(%s, %s, %s)'
    cursor.execute(query, (id_hora_inicial, id_hora_final, id_periodo))
    conexion.commit()

def insertar_edificios(materia, id_edificio):
    query = 'INSERT INTO edificios(nrc, id_edificio) VALUES(%s, %s)'
    cursor.execute(query, (materia['nrc'], id_edificio))
    conexion.commit()

def insertar_aulas(materia, id_aula):
    query = 'INSERT INTO aulas(nrc, id_aula) VALUES(%s, %s)'
    cursor.execute(query, (materia['nrc'], id_aula))
    conexion.commit()

def insertar_horarios(materia, id_horario):
    query = 'INSERT INTO horarios(nrc, id_horario) VALUES(%s, %s)'
    cursor.execute(query, (materia['nrc'], id_horario))
    conexion.commit()


def insertar_oferta(materia, id_clave, id_seccion, id_detalle, id_profesor):
    query = 'INSERT INTO oferta(nrc, id_clave, id_seccion, id_detalle, id_profesor) VALUES(%s, %s, %s, %s, %s)'
    cursor.execute(query, (materia['nrc'], id_clave, id_seccion, id_detalle, id_profesor))
    conexion.commit()

# -------------------------------------------------------------------------

def get_Id_Clave(materia):
    query = 'SELECT id FROM clave where clave = %s'
    cursor.execute(query, (materia['clave'],))
    rows = cursor.fetchall()
    return  rows[0][0]

def get_Id_Seccion(materia):
    query = 'SELECT id FROM seccion where seccion = %s'
    cursor.execute(query, (materia['seccion'],))
    rows = cursor.fetchall()
    return rows[0][0]

def get_Id_Profesor(materia):
    query = 'SELECT id FROM profesor where nombre = %s'
    cursor.execute(query, (materia['Profesor'],))
    rows = cursor.fetchall()
    return rows[0][0]

def get_Id_Hora(hora):
    query = 'SELECT id FROM hora where hora = %s'
    cursor.execute(query, (hora,))
    rows = cursor.fetchall()
    return rows[0][0]


def get_Id_Edificio(materia):
    query = 'SELECT id FROM edificio where edificio = %s'
    cursor.execute(query, (materia['Edificio'],))
    rows = cursor.fetchall()
    return rows[0][0]

def get_Id_Periodo(materia):
    query = 'SELECT id FROM periodo where periodo = %s'
    cursor.execute(query, (materia['Periodo'],))
    rows = cursor.fetchall()
    return rows[0][0]


def get_Id_Aula(materia):
    query = 'SELECT id FROM aula where aula = %s'
    cursor.execute(query, (materia['Aula'],))
    rows = cursor.fetchall()
    return rows[0][0]


def get_Id_Detalle(materia):
    query = 'SELECT id FROM detalle where nrc = %s'
    cursor.execute(query, (materia['nrc'],))
    rows = cursor.fetchall()
    return rows[0][0]


def get_Id_Horario(id_hora_inicial, id_hora_final, id_periodo):
    query = 'SELECT id FROM horario where hora_inicial = %s AND hora_final = %s AND periodo = %s'
    cursor.execute(query, (id_hora_inicial, id_hora_final, id_periodo))
    rows = cursor.fetchall()
    return rows[0][0]

# -------------------------------------------------------------------------

#Falta agregar lo de aulas y horarios

for file in files:
    with open(file, encoding = 'utf-8') as f:
        materias = json.load(f)
        for materia in materias:
            id_clave = 0
            id_seccion = 0
            id_detalle = 0
            id_profesor = 0
            id_hora_inicial = 0
            id_hora_final = 0
            id_dia = 0
            id_aula = 0
            id_horario = 0
            id_periodo = 0
            id_detalle = 0
            id_edificio = 0


            if not existe_clave(materia):
                insertar_clave(materia)
            id_clave = get_Id_Clave(materia)

            if not existe_seccion(materia):
                insertar_seccion(materia)
            id_seccion = get_Id_Seccion(materia)

            if not existe_profesor(materia):
                insertar_profesor(materia)
            id_profesor = get_Id_Profesor(materia)

            if not existe_hora_inicial(materia):
                insertar_hora_inicial(materia)
            id_hora_inicial = get_Id_Hora(materia['Horas'][0:4])

            if not existe_hora_final(materia):
                insertar_hora_final(materia)
            id_hora_final = get_Id_Hora(materia['Horas'][5:9])
            
            if not existe_edificio(materia):
                insertar_edificio(materia)
            id_edificio = get_Id_Edificio(materia)
            
            if not existe_periodo(materia):
                insertar_periodo(materia)
            id_periodo = get_Id_Periodo(materia)

            if not existe_horario(id_hora_inicial, id_hora_final, id_periodo):
                insertar_horario(id_hora_inicial, id_hora_final, id_periodo)
            id_horario = get_Id_Horario(id_hora_inicial, id_hora_final, id_periodo)

            if not existe_aula(materia):
                insertar_aula(materia, id_edificio)
            id_aula = get_Id_Aula(materia)

            if not existe_detalle(materia):
                insertar_detalle(materia)
            id_detalle = get_Id_Detalle(materia)

            if not existe_oferta(materia):
                insertar_oferta(materia, id_clave, id_seccion, id_detalle, id_profesor)

            for dia in materia['Dias']:
                insertar_dia(materia, dia)

            if not existe_edificios(materia, id_edificio):
                insertar_edificios(materia, id_edificio)

            if not existe_aulas(materia, id_aula):
                insertar_aulas(materia, id_aula)

            if not existe_horarios(materia, id_horario):
                insertar_horarios(materia, id_horario)











