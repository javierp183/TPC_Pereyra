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

from database import Patient,Medic,Agenda
from database import Speciality
from database import User
from pony.orm import commit
from pony.orm import select


class DBobjects:
    def loadobjects(self):
        #Declare the array
        medics_patients = []

        #Get Complete list of Patients
        patients = select(p for p in Patient)[:]
        data_patient = {'patient_data': [p.to_dict() for p in patients]}

        #Get Complete list of Medics
        medics = select(m for m in Medic)[:]
        data_medic = {'medic_data': [m.to_dict() for m in medics]}

        #Get Complete list of specialities
        speciality = select(s for s in Speciality)[:]
        data_speciality = {'spec_data': [s.to_dict() for s in speciality]}

        #Get Complete list of the Agenda
        agenda = select(a for a in Agenda)[:]
        data_agenda = {'agenda_data': [a.to_dict() for a in agenda]}

        #Append data to array
        medics_patients.append(data_patient)
        medics_patients.append(data_medic)
        medics_patients.append(data_speciality)
        medics_patients.append(data_agenda)

        return medics_patients


class Assignation:
    def medicassign(self,table_data,db_data):
        """ Medic Assignation by Specialization """
        patients = []
        dayandmonth = []

        d = 0
        for i in table_data['day']:
            dayandmonth.append(i + "-" + table_data['month'][d])
        
        table_data['daymonth'] = dayandmonth
        
        
        for i in table_data['spec_selected']:
            if i != 'None':
                medic_state = True
        
        
        if not db_data[3]['agenda_data']:
            agenda_state = False

        
        for i in table_data['dni']:
            patients.append(Patient.get(dni=i))

        p = 0
        for i in table_data['spec_selected']:
            patients[p].medic = i

            if Agenda.get(hour=table_data['time'][p]) == None:
                Agenda(state=1, hour=table_data['time'][p],
                medico=i,patient=patients[p].id)
            else:
                print("actualizando base de datos")
                a = Agenda.get(hour=table_data['time'][p])
                a.state = 1
                a.hour = table_data['time'][p]
                a.medico = i
                a.patient = patients[p].id
                a.date = table_data['daymonth'][p]
            
            p = p + 1
            commit()


class Usermgmt:
    def adduser(self,data):
        try:
            if data['medic']:
                User(name=data['name'], lastname=data['lastname'],
                    userid=data['userid'], password=data['password'],
                    rol="medic")
                commit()
        except:
            pass

        try:
            if data['admin']:
                User(name=data['name'], lastname=data['lastname'],
                    userid=data['userid'], password=data['password'],
                    rol="admin")
                commit()
        except:
            pass
            
        try:
            if data['patient']:
                User(name=data['name'], lastname=data['lastname'],
                    userid=data['userid'], password=data['password'],
                    rol="admin")
                commit()
        except:
            pass

    def modifyuser(self,data):
        pass

    def deleteuser(self,data):
        pass

    def validate(self, data):
        try:
            if User.exists(userid=data['userid']):
                role = User.get(userid=data['userid']).rol
                password = User.get(userid=data['userid']).password
                if data['password'] == password:
                    return dict({'state': True, 'rol': role})
        except:
            return dict({'state': False, 'rol': 'None'})
            
        

        
