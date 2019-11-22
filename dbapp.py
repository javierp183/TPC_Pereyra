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
from database import Turno
from pony.orm import commit
from pony.orm import select,delete
from loader import Loader
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load configurations from YML file.
config = Loader().settings

class Email:
    def __init__(self):
        self.account = config['email']['account']
        self.password = config['email']['password']
        self.smtp = config['email']['smtp']
        self.port = config['email']['port']
    
    def send(self, receiver, name, date, hour, turno):
        message = MIMEMultipart()
        message['From'] = self.account
        message['To'] = receiver
        message['Subject'] = 'Hospital - TSP - Javier Pereyra'
        mail_content = "Usted tiene un turno con el medico {} en la fecha {} a las {} horas - Turno numero: {}".format(name,date,hour,turno)
        message.attach(MIMEText(mail_content, 'plain'))

        session = smtplib.SMTP(self.smtp, self.port)
        session.starttls()
        session.login(self.account, self.password)
        text = message.as_string()
        session.sendmail(self.account, receiver, text)
        session.quit()
        pass


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
                    'dates': [],
                    'agenda_id': []
                }
        
        #Append Free date and time
        for i in data_agenda['agenda_data']:
            if bool(i['state']) == False:
                hourbymedic[i['name']]['hours'].append(i['hour'])
                hourbymedic[i['name']]['dates'].append(i['date'])
        

        #Get Agenda ID from database
        query = "a for a in Agenda if a.state == False"
        cmdquery = select(query)[:]
        for i in cmdquery:
            hourbymedic[i.medico.name]['agenda_id'].append(i.id)


        allobjects.append(dict(hourmedic=hourbymedic))
  
        return allobjects
        


class Assignation:
    def medicassign(self,data):
        hour = data['daytimehour'].split(":")[1].split(" ")[1]
        date = data['daytimehour'].split(":")[2].split(" ")[1]
        patientdni = data['patient'].split("-")[1]
        idmedic = data['medic']
        comment = data['comments']
        medictype = False
        inc = 0


        query = "a for a in Agenda if a.date == '{}' and a.medico.id == '{}' and a.hour == '{}'".format(date, idmedic, hour)
        cmdquery = select(query)
        if not cmdquery:
            medictype = True
            idmedic = int(idmedic)
            idmedic = idmedic + 1
            query = "a for a in Agenda if a.date == '{}' and a.medico.id == '{}' and a.hour == '{}'".format(date, idmedic, hour)
            cmdquery = select(query)
        obj = cmdquery.get()

        # Valida si el estado del medico se encuentra disponible.
        if obj.state == False:
            p = Patient.get(dni=patientdni).id
            pemail = Patient.get(dni=patientdni).email

            obj.date = date
            obj.hour = hour

            if medictype == True:
                idmedic = idmedic - 1
                obj.medico = idmedic
            else:
                obj.medico = idmedic
            
            obj.patient = p
            obj.comments = comment
            obj.state = 1

            #Obtengo nombre del medico
            nombre_medico = Medic.get(id=idmedic).name

            #Genera un turno.
            a = Turno[1]
            a.turno = a.turno + 1
            commit()

            #Sent email
            EnviarEmail = Email()
            EnviarEmail.send(pemail,nombre_medico,date,hour,a.turno)

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
                'daymonth':[],
                'comments':[],
                'speciality':[]
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

        query = "a for a in Agenda if a.medico.medicid == '{}' and a.state == True".format(medicid)
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
            data['patients']['comments'].append(i.comments)
            data['patients']['speciality'].append(i.medico.speciality.name)

        print(data)

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
        
        
        for i in dbdata[2]['spec_data']:
            medicgroups[i['name']]['spec_id'].append(i['id'])


        for i in dbdata[2]['spec_data']:
            for j in medicgroups[i['name']]['spec_id']:
                for z in dbdata[1]['medic_data']:
                    if z['speciality'] == j:
                        medicgroups[i['name']]['name'].append(z['name'])
                        medicgroups[i['name']]['lastname'].append(z['lastname'])
                        medicgroups[i['name']]['idmedic'].append(z['id'])


        return medicgroups
    
    def currentassign():
        data = {}
        mydata = []

        # Get Complete list of the Agenda
        agenda = select(a for a in Agenda)[:]
        data_agenda = {'agenda_data': [a.to_dict() for a in agenda]}

        #Get Names for the Agenda list
        query = select(n for n in Agenda)[:]

        #Insert name of medic
        for k, v in enumerate(query):
            data_agenda['agenda_data'][k].update(name=v.medico.name)
            data_agenda['agenda_data'][k].update(medicid=v.medico.medicid)
            data_agenda['agenda_data'][k].update(hours=v.hour)
            data_agenda['agenda_data'][k].update(dates=v.date)
            data_agenda['agenda_data'][k].update(medicn=v.medico.name)

        #Assign names as key value for dict
        for i in data_agenda['agenda_data']:
            if bool(i['state']) == True:
                data[i['name']] = {
                    'medicid': [],
                    'medic_name': [],
                    'patientsid':[],
                    'patient_name':[],
                    'patient_lastname':[],
                    'patient_email':[],
                    'patient_dni':[],
                    'hours': [],
                    'dates': [],
                    'speciality_name': [],
                    'agenda_id': []
                }


        for i in data_agenda['agenda_data']:
            if bool(i['state']) == True:
                data[i['name']]['medicid'].append(i['medicid'])
                data[i['name']]['medic_name'].append(i['name'])
                data[i['name']]['hours'].append(i['hour'])
                data[i['name']]['dates'].append(i['date'])

        
        query2 = "a for a in Agenda if a.state == True"
        cmdquery = select(query2)[:]

        for i in cmdquery:
            data[i.medico.name]['patientsid'].append(i.patient.id)
            data[i.medico.name]['patient_name'].append(i.patient.name)
            data[i.medico.name]['patient_name'].append(i.patient.lastname)
            data[i.medico.name]['patient_lastname'].append(i.patient.lastname)
            data[i.medico.name]['patient_email'].append(i.patient.email)
            data[i.medico.name]['patient_dni'].append(i.patient.dni)
            data[i.medico.name]['speciality_name'].append(i.medico.speciality.name)
            data[i.medico.name]['agenda_id'].append(i.id)

        
        return data

    def reassignation(self,datacurrent,datanew):
        current = Agenda.get(id=datacurrent)
        newsched = Agenda.get(id=datanew)
        current.state = False
        newsched.state = True
        newsched.comments = current.comments
        newsched.medico = current.medico
        newsched.patient = current.patient
        commit()
        print("creo que cambio!")
        pass


class Usermgmt:
    def adduser(self,data):
        try:
            if data['medic']:
                nonempty_spec_list = []
                nonempty_spec_list_id = []

                # Genera una nueva lista de especialidades si esta no
                # existiere
                for spec in data['specialization'].split(","):
                    if not Speciality.get(name=spec):
                        Speciality(name=spec)
                        commit()
                
                # Suma al nuevo medico a la lista de especialidades
                for spec in data['specialization'].split(","):
                    query = "m for m in Medic if m.speciality.name == '{}' and m.medicid == '{}'".format(spec,data['medicid'])
                    cmdquery = select(query)[:]

                    if cmdquery:
                        nonempty_spec_list.append(False)
                    else:
                        nonempty_spec_list.append(spec)


                for i in nonempty_spec_list:
                    nonempty_spec_list_id.append(Speciality.get(name=i))
                
                
                for i in nonempty_spec_list_id:
                    if i:
                        Medic(name=data['name'], lastname=data['lastname'],
                                medicid=data['medicid'], patient=None, speciality=i)
                        commit()
                
                # Genera una agenda libre para el medico
                query = "m for m in Medic if m.speciality.name == '{}' and m.medicid == '{}'".format(spec,data['medicid'])
                cmdquery = select(query)[:]
                dbmedicid = cmdquery[0]
                
                months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
                        "Julio","Agosto",
                        "Septiembre","Octubre","Noviembre","Diciembre"]
                
                days = ["1","2","3","4","5","6","7","8","9","10","11","12",
                "13","14","15",
                "16","17","18","19","20","21","22","23","24","25","26","27",
                "28","29","30","31"]

                hours = ["10","11","12"]

                
                monthday_array = []

                for m in months:
                    for d in days:
                        monthday = m + "-" + d
                        monthday_array.append(monthday)
                


                for md in monthday_array:
                    for hr in hours:
                        Agenda(date=md, state=0, hour=hr, medico=dbmedicid.id)
                        commit()
                

                newuser = User(name=data['name'], lastname=data['lastname'],
                            userid=data['userid'], password=data['password'],
                            medicid=data['medicid'],rol="medic")
                commit()
                print("comiteo")
        except:
            pass

        try:
            if data['admin']:
                newuser = User(name=data['name'], lastname=data['lastname'],
                            userid=data['userid'], password=data['password'],
                            rol="admin")
                commit()
                print("comiteo")
        except:
            pass

        try:
            if data['patient']:
                if not Patient.get(dni=data['dni']):
                    newuser = Patient(name=data['name'], lastname=data['lastname'],
                    dni=data['dni'], email=data['email'])
                    commit()
                    print("comiteo")
        except:
            pass

    def modifyuser(self,data):
        pass

    def deleteuser(self,data):
        try:
            if data['admin']:
                deleteuser = User.get(userid=data['userid'])
                deleteuser.delete()
                commit()
        except:
            pass

        try:
            if data['medic']:
                print("salida 1")
                deleteuser = User.get(userid=data['userid'])
                print("salida 2")
                deleteuser.delete()
                print("salida 3")
                delete(m for m in Agenda if m.medico.medicid == data['medicid'])
                commit()
        except:
            pass

    def validate(self, data):
        try:
            if User.exists(userid=data['userid']):
                role = User.get(userid=data['userid']).rol
                password = User.get(userid=data['userid']).password
                if data['password'] == password:
                    return dict({'state': True, 'role': role})
                else:
                    return dict({'state': False, 'role': 'None'})
            else:
                return dict({'state': False, 'role': 'None'})
        except:
            pass


    def getmedicid(self, data):
        """ Obtain medic id number """
        medicid = User.get(userid=data['userid']).medicid
        return medicid


