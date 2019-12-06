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

# Load configurations from YML file.
config = Loader().settings


# --------------------------------------------------------------------------- #
# Populate Database
# --------------------------------------------------------------------------- #

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
        months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto",
                        "Septiembre","Octubre","Noviembre","Diciembre"]
        
        days = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15",
                "16","17","18","19","20","21","22","23","24","25","26","27",
                "28","29","30","31"]

        hours = ["10","11","12"]

        monthday_array = []
        
        #List medics
        mquery = select(m for m in Medic)[:]
        list_medics = {'medic_list': [m.to_dict() for m in mquery]}

        for m in months:
                for d in days:
                        monthday = m + "-" + d
                        monthday_array.append(monthday)

        
        for med in list_medics['medic_list']:
                for md in monthday_array:
                        for hr in hours:
                                
                                Agenda(date=md, state=0, hour=hr,
                                        medico=int(med['id']))
                                commit()

@db_session()
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
#agenda_load()
#set_speciality()
#init_turnos()
