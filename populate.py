#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the  nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# --------------------------------------------------------------------------- #
# Imports
# --------------------------------------------------------------------------- #

# from uuid import uuid4

from pony.orm import commit
from pony.orm import db_session
from pony.orm import select
from loader import Loader
import yaml

from database import Medic,Patient
from database import Agenda,User
from database import Speciality,Turno
import datetime
import calendar

# Load configurations from YML file.
config = Loader().settings


# --------------------------------------------------------------------------- #
# Populate Database
# --------------------------------------------------------------------------- #

def agenda_cargador(data):
    
    agenda = {}
    meses = ["Enero-1","Febrero-2","Marzo-3","Abril-4","Mayo-5","Junio-6",
                        "Julio-7","Agosto-8",
                        "Septiembre-9","Octubre-10",
                        "Noviembre-11","Diciembre-12"]


    for mes in meses:
        agenda[mes] = {
            'lunes': {
            'dias': [],
            'horario': []
        },
        'martes': {
            'dias': [],
            'horario': []
        },
        'miercoles': {
            'dias': [],
            'horario': []
        },
        'jueves': {
            'dias': [],
            'horario': []
        },
        'viernes': {
            'dias': [],
            'horario': []
        },
        'sabado': {
            'dias': [],
            'horario': []
        },
        'domingo': {
            'dias': [],
            'horario': []
        }
    }

    #Obtiene el mes actual para la carga
    ahora = datetime.datetime.now()
    diadehoy = ahora.day
    
    mes_inicio = ahora.month
    mes_fin = 13
    #Carga de lunes
    for dia_activo in data['semana']:
        if dia_activo == "lunes":
            for mes in range(mes_inicio, mes_fin):
                micalendario = calendar.monthcalendar(2019, mes)
                for i in agenda:
                    if mes == int(i.split("-")[1]):
                        for j in range(0, 5):
                            lunes = micalendario[j]             
                            if lunes[calendar.MONDAY] != 0:
                                dialunes = lunes[calendar.MONDAY]                  
                                agenda[i]['lunes']['dias'].append(dialunes)
                                agenda[i]['lunes']['horario'].append(data['horario'])
    
    
    #Carga de martes
    for dia_activo in data['semana']:
        if dia_activo == "martes":
            for mes in range(mes_inicio, mes_fin):
                micalendario = calendar.monthcalendar(2019, mes)
                for i in agenda:
                    if mes == int(i.split("-")[1]):
                        for j in range(0, 5):
                            martes = micalendario[j]
                            if martes[calendar.TUESDAY] != 0:
                                diamartes = martes[calendar.TUESDAY]
                                agenda[i]['martes']['dias'].append(diamartes)
                                agenda[i]['martes']['horario'].append(data['horario'])

    #Carga de miercoes
    for dia_activo in data['semana']:
        if dia_activo == "miercoles":
            for mes in range(mes_inicio, mes_fin):
                micalendario = calendar.monthcalendar(2019, mes)
                for i in agenda:
                    if mes == int(i.split("-")[1]):
                        for j in range(0, 5):
                            miercoles = micalendario[j]
                            if miercoles[calendar.WEDNESDAY] != 0:
                                diamiercoles = miercoles[calendar.WEDNESDAY]
                                agenda[i]['miercoles']['dias'].append(diamiercoles)
                                agenda[i]['miercoles']['horario'].append(data['horario'])

    #Carga de juebes
    for dia_activo in data['semana']:
        if dia_activo == "jueves":
            for mes in range(mes_inicio, mes_fin):
                micalendario = calendar.monthcalendar(2019, mes)
                for i in agenda:
                    if mes == int(i.split("-")[1]):
                        for j in range(0, 5):
                            jueves = micalendario[j]
                            if jueves[calendar.WEDNESDAY] != 0:
                                diajueves = jueves[calendar.THURSDAY]
                                agenda[i]['jueves']['dias'].append(diajueves)
                                agenda[i]['jueves']['horario'].append(data['horario'])
    
    #Carga de viernes
    for dia_activo in data['semana']:
        if dia_activo == "viernes":
            for mes in range(mes_inicio, mes_fin):
                micalendario = calendar.monthcalendar(2019, mes)
                for i in agenda:
                    if mes == int(i.split("-")[1]):
                        for j in range(0, 5):
                            viernes = micalendario[j]
                            if viernes[calendar.WEDNESDAY] != 0:
                                diaviernes = viernes[calendar.FRIDAY]
                                agenda[i]['viernes']['dias'].append(diaviernes)
                                agenda[i]['viernes']['horario'].append(data['horario'])
    
    #Carga de Sabado
    for dia_activo in data['semana']:
        if dia_activo == "sabado":
            for mes in range(mes_inicio, mes_fin):
                micalendario = calendar.monthcalendar(2019, mes)
                for i in agenda:
                    if mes == int(i.split("-")[1]):
                        for j in range(0, 5):
                            sabado = micalendario[j]
                            if sabado[calendar.WEDNESDAY] != 0:
                                diasabado = sabado[calendar.SATURDAY]
                                agenda[i]['sabado']['dias'].append(diasabado)
                                agenda[i]['sabado']['horario'].append(data['horario'])
    
    #Carga de Domingo
    for dia_activo in data['semana']:
        if dia_activo == "domingo":
            for mes in range(mes_inicio, mes_fin):
                micalendario = calendar.monthcalendar(2019, mes)
                for i in agenda:
                    if mes == int(i.split("-")[1]):
                        for j in range(0, 5):
                            domingo = micalendario[j]
                            if domingo[calendar.WEDNESDAY] != 0:
                                diadomingo = domingo[calendar.SUNDAY]
                                agenda[i]['domingo']['dias'].append(diadomingo)
                                agenda[i]['domingo']['horario'].append(data['horario'])

    return agenda

@db_session()
def speciality_add():
    for i in config['loader']['medics']['speciality']:
        Speciality(name=i)
    commit()


@db_session()
def medic_add():
    for i in range(2):
        Medic(name=config['loader']['medics']['name'][i],
              lastname=config['loader']['medics']['lastname'][i],
              medicid=config['loader']['medics']['medicid'][i])
        commit()


@db_session()
def patient_add():
    for i in range(2):
        Patient(dni=config['loader']['patients']['data']['dni'][i],
                name=config['loader']['patients']['data']['name'][i],
                lastname=config['loader']['patients']['data']['lastname'][i],
                secureid=config['loader']['patients']['data']['secureid'][i],
                email=config['loader']['patients']['data']['email'][i]
                )


@db_session()
def user_add():
    User(name="Maximiliano", lastname="Sar Fernandez", userid="maxi182", password="abc123",
        rol="admin")
    commit()
    for i in range(2):
        User(name=config['loader']['user']['data']['name'][i],
            lastname=config['loader']['user']['data']['lastname'][i],
            userid=config['loader']['user']['data']['userid'][i],
            password=config['loader']['user']['data']['password'][i],
            rol=config['loader']['user']['data']['rol'][i],
            medicid=config['loader']['user']['data']['medicid'][i])
        commit()


@db_session()
def agenda_load():
    data = {'semana': ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo'], 
    'horario': ['10', '11', '12'], 'medicid': '200', 'medico': 1, 'name': 'geremias', 'lastname': 'avogadro',
     'userid': 'gere182', 'password': 'abc123', 'specialization': 'pediatra,cardiologo'}
    print("output 1")
    nonempty_spec_list = []
    nonempty_spec_list_id = []
    magenda = agenda_cargador(data)
    print("salida:")
    print(data)

    #Genera una nueva lista de especialidades si esta no
    #existiere
    for spec in data['specialization'].split(","):
        if not Speciality.get(name=spec):
            Speciality(name=spec)
            commit()
    
    print("output 2")
    
    #Suma al nuevo medico a la lista de especialidades
    for spec in data['specialization'].split(","):
        query = "m for m in Medic if m.speciality.name == '{}' and m.medicid == '{}'".format(spec,data['medicid'])
        cmdquery = select(query)[:]

        if cmdquery:
            nonempty_spec_list.append(False)
        else:
            nonempty_spec_list.append(spec)
    
    print("output 3")


    for i in nonempty_spec_list:
        nonempty_spec_list_id.append(Speciality.get(name=i))
    
    print("output 4")
    
    
    for i in nonempty_spec_list_id:
        if i:
            Medic(name=data['name'], lastname=data['lastname'],
                    medicid=data['medicid'], patient=None, speciality=i)
            commit()

    print("output 5")
    
    #Genera una agenda libre para el medico
    query = "m for m in Medic if m.speciality.name == '{}' and m.medicid == '{}'".format(spec,data['medicid'])
    cmdquery = select(query)[:]
    dbmedicid = cmdquery[0]
    
    months = ["Enero-1","Febrero-2","Marzo-3","Abril-4","Mayo-5","Junio-6",
            "Julio-7","Agosto-8",
            "Septiembre-9","Octubre-10","Noviembre-11","Diciembre-12"]
    
    
    dias = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]


    hours = ["10","11","12"]

    
    monthday_array = []


    for k, v in magenda.items():
        if v['lunes']['dias'] or v['martes']['dias'] or v['miercoles']['dias'] \
            or v['jueves']['dias'] or v['viernes']['dias'] or v['sabado']['dias'] \
                or v['domingo']['dias']:
            

            for d in dias:
                for tdias in v[d]['dias']:
                    for hr in v[d]['horario'][0]:
                        monthday = k + "/" + d + "-" + str(tdias) + "/" + str(hr)
                        monthday_array.append(monthday)
    
    print("output 6")
    

    for md in monthday_array:
        Agenda(date=md, state=0, hour=md.split("/")[2], medico=dbmedicid.id)
        commit()
    

    newuser = User(name=data['name'], lastname=data['lastname'],
                userid=data['userid'], password=data['password'],
                medicid=data['medicid'],rol="medic")
    commit()
    print("comiteo")

    return True

def set_speciality():
        a = Medic[1]
        a.speciality = Speciality[1]
        b = Medic[2]
        b.speciality = Speciality[2]
        commit()


@db_session()
def init_turnos():
        Turno(turno=1)
        commit()

# # --------------------------------------------------------------------------- #
# # Sample Database
# # --------------------------------------------------------------------------- #

speciality_add()
#medic_add()
patient_add()
user_add()
agenda_load()
#set_speciality()
init_turnos()
