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
from pony.orm import commit


class Assignation:
    def medicassign(self,table_data,db_data):
        """ Medic Assignation by Specialization """
        patients = []
        #print(table_data)
        
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
            
            #Agenda(state=1, timestart=table_data['time'][p],
            #        medico=i,patient=patients[p].id)
            p = p + 1
            commit()


class Usercreate:
    def adduser(self,data):
        pass

    def modifyuser(self,data):
        pass

    def deleteuser(self,data):
        pass
            
        

        
