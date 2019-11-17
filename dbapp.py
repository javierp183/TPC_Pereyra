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
        allobjects = []
        assign = {}
        hourbymedic = {}
       
        

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

        #Get Names for the Agenda list
        query = select(n for n in Agenda)[:]

        #Insert name of medic
        for k, v in enumerate(query):
            data_agenda['agenda_data'][k].update(name=v.medico.name)

        #Append data to array
        allobjects.append(data_patient)
        allobjects.append(data_medic)
        allobjects.append(data_speciality)
        allobjects.append(data_agenda)

        assign['select_data'] = Assignation().medicbytypes(allobjects)
        allobjects.append(assign)

        #Get Free time by medic
        freemedic = select(f for f in Agenda if f.state == False)[:]
        free_time = {'time_free': [f.to_dict() for f in freemedic]}

        #Get Busy time by medic
        busymedic = select(f for f in Agenda if f.state == True)[:]
        busy_time = {'time_busy': [f.to_dict() for f in freemedic]}

        #Assign names as key value of dict
        for i in data_agenda['agenda_data']:
            if bool(i['state']) == False:
                hourbymedic[i['name']] = {
                    'hours': [],
                    'dates': []
                }
        
        #Append Free date and time
        for i in data_agenda['agenda_data']:
            if bool(i['state']) == False:
                hourbymedic[i['name']]['hours'].append(i['hour'])
                hourbymedic[i['name']]['dates'].append(i['date'])

        allobjects.append(dict(hourmedic=hourbymedic))


                
        return allobjects
        


class Assignation:
    def medicassign(self,data):
        hour = data['daytimehour'].split(":")[1].split(" ")[1]
        date = data['daytimehour'].split(":")[2].split(" ")[1]
        patientdni = data['patient'].split("-")[1]
        idmedic = data['medic']
        comment = data['comments']

        
        query = "a for a in Agenda if a.date == '{}' and a.medico.id == '{}' and a.hour == '{}'".format(date, idmedic, hour)
        cmdquery = select(query)
        obj = cmdquery.get()
        print(obj)
        if obj.state == False:
            print("medico disponible en ese horario, con ese id y a esa fecha")
            p = Patient.get(dni=patientdni).id
            obj.date = date
            obj.hour = hour
            obj.medico = idmedic
            obj.patient = p
            obj.comments = comment
            obj.state = 1
            commit()
        else:
            print("el medico se encuentra ocupado")

    
    def medicagenda(medicid,dbdata):
        """ Obtain medic agenda information """
        data = {
            'patients' : {
                'name':[],
                'lastname':[],
                'time':[],
                'dni':[],
                'email':[],
                'daymonth':[]
            },
            'medic':{
                'id': '',
                'name': '',
                'lastname': '',
                'patientsid': [],
                'spec_number': [],
                'speciality': [],
                'medicid': ''
            }
        }

        query = "a for a in Agenda if a.medico.medicid == '999999' and a.state == True"
        cmdquery = select(query)[:]

        for i in dbdata[1]['medic_data']:
            if i['medicid'] == int(medicid):
                data['medic']['id'] = i['id']
                data['medic']['name'] = i['name']
                data['medic']['lastname'] = i['lastname']
                data['medic']['medicid'] = int(medicid)
                data['medic']['spec_number'] = i['speciality']        
        
        for i in cmdquery:
            data['patients']['name'].append(i.patient.name)
            data['patients']['lastname'].append(i.patient.lastname)
            data['patients']['dni'].append(i.patient.dni)
            data['patients']['email'].append(i.patient.email)
            data['patients']['daymonth'].append(i.date)
            data['patients']['time'].append(i.hour)




        # for i in patients['as_assigned']:
        #     data['patients']['name']
        #     data['patients']['daymonth'].append(i['date'])

        

        print(data)



        # for i in dbdata[1]['medic_data']:
        #     if i['medicid'] == int(medicid):
        #         data['medic']['id'] = i['id']
        #         data['medic']['name'] = i['name']
        #         data['medic']['lastname'] = i['lastname']
        #         data['medic']['medicid'] = int(medicid)
        #         data['medic']['spec_number'] = i['speciality']

        # for i in dbdata[2]['spec_data']:
        #     if i['id'] == data['medic']['spec_number']:
        #         data['medic']['speciality'] = i['name']

        # for i in dbdata[3]['agenda_data']:
        #     if i['medico'] == data['medic']['id']:
        #         data['medic']['patientsid'].append(i['patient'])
        #         data['patients']['time'].append(i['hour'])
        #         data['patients']['daymonth'].append(i['date'])

        
        # print(dbdata[3]['agenda_data'])
        #print(data['patients'])


        # for i in data['medic']['patientsid']:
        #     for j in dbdata[0]['patient_data']:
        #         if i == j['id']:
        #             data['patients']['name'].append(j['name'])
        #             data['patients']['lastname'].append(j['lastname'])
        #             data['patients']['dni'].append(j['dni'])

        # print("patient ID:")
        # print(dbdata[3]['agenda_data'][1]['medico'])

        return data

    def medicbytypes(self,dbdata):
        medicgroups = {}
        for i in dbdata[2]['spec_data']:
            medicgroups[i['name']] = {
                'idmedic':[],
                'spec_id': [],
                'name': [],
                'lastname': []

            }
        
        #
        for i in dbdata[2]['spec_data']:
            medicgroups[i['name']]['spec_id'].append(i['id'])


        for i in dbdata[2]['spec_data']:
            for j in medicgroups[i['name']]['spec_id']:
                for z in dbdata[1]['medic_data']:
                    if z['speciality'] == j:
                        medicgroups[i['name']]['name'].append(z['name'])
                        medicgroups[i['name']]['lastname'].append(z['lastname'])
                        medicgroups[i['name']]['idmedic'].append(z['id'])
        
        # for i in dbdata[2]['spec_data']:
        #     for j in medicgroups:
        #         if i['name'] == j:
        #             medicgroups[i['name']]['idmedic'].append(i['medic'])
        #             medicgroups[i['name']]['spec_id'].append(i['id'])

        
        # for i in medicgroups:
        #     for j in medicgroups[i]['idmedic']:
        #         for z in dbdata[1]['medic_data']:
        #             if z['id'] == j:
        #                 medicgroups[i]['name'].append(z['name'])
        #                 medicgroups[i]['lastname'].append(z['lastname'])
            
        return medicgroups


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
                    return dict({'state': True, 'role': role})
        except:
            return dict({'state': False, 'rol': 'None'})
    

    def getmedicid(self, data):
        """ Obtain medic id number """
        medicid = User.get(userid=data['userid']).medicid
        return medicid


