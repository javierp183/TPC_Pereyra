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

# Database
from pony.orm import db_session, select
from pony.orm import commit,select

# Framework
from bottle import jinja2_view as view
from bottle import request, MultiDict
from bottle import route, run, redirect
from bottle import static_file,response
from bottle import template
import bottle

# Tables / Objects
from database import Medic, Speciality
from database import Agenda, Patient
from database import User
from loader import Loader
from dbapp import Assignation,Usermgmt
from dbapp import DBobjects

# Datetime
import datetime

# Settings and current time
settings = Loader().settings
now = datetime.datetime.now()

# --------------------------------------------------------------------------- #
# Helper - Static - Publish content
# --------------------------------------------------------------------------- #

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

# --------------------------------------------------------------------------- #
# Function - Helpers - Render output
# --------------------------------------------------------------------------- #

@route('/medicassigned')
@view('medic_assigned.tpl', template_lookup=['views'])
def medic_assigned():
    pass


@route('/medicanonssigned')
@view('medic_non_assigned.tpl', template_lookup=['views'])
def medic_non_assigned():
    pass

@route('/wronguserpass')
@view('wronguserpass.tpl', template_lookup=['views'])
def wronguserpass():
    pass

@route('/savemedic')
@view('already_registered.tpl', template_lookup=['views'])
def thanks():
    pass

@route('/savepatient')
@view('complete_fields.tpl', template_lookup=['views'])
def complete():
    pass

# --------------------------------------------------------------------------- #
# Application Main Routes
# --------------------------------------------------------------------------- #

@route('/', method=["GET","POST"])
@db_session
@view('index.tpl', template_lookup=['views'])
def main_index():
    """ Main Index """
    data = dict(request.forms)
    print(data)
    
    access = Usermgmt()
    if request.method == 'POST':

        urol = access.validate(data)
        if urol['role'] == 'admin':
            return redirect('/operator/{}'.format(data['userid']))

        elif urol['role'] == 'medic':
            mid = access.getmedicid(data)
            return redirect('/medic/{}'.format(mid))
        
        elif urol['role'] == 'patient':
            return redirect('/user')

        elif urol['role'] == 'None':
            print("salida")
            #print(urol['role'])
            return redirect('/wronguserpass')
        
    return dict(context={'output': 'none'})
        


@route('/useradd', method=["GET","POST"])
@db_session
@view('useradd.tpl', template_lookup=['views'])
def main_useradd_index():
    """ Main UserAdd Index """
    data = dict(request.forms)
    create = Usermgmt()
    create.adduser(data)

    return dict(context={'output': 'none'})


@route('/userdel', method=["GET","POST"])
@db_session
@view('userdel.tpl', template_lookup=['views'])
def main_useradd_index():
    """ Main UserAdd Index """
    data = dict(request.forms)
    create = Usermgmt()
    create.deleteuser(data)

    return dict(context={'output': 'none'})


@route('/medic/<medicid>', method=["GET","POST"])
@db_session
@view('medic.tpl', template_lookup=['views'])
def main_doctor_index(medicid):
    """ Medic Main Index """
    print("salida")
    dbdata = DBobjects().loadobjects()
    medic = Assignation.medicagenda(medicid,dbdata)
    estado_salida = dict(request.params)

    if request.method == 'POST':
        try:
            if estado_salida['estado'] == 'on':
                print("prendido")
                medic['saludo'] = saludo
                print(medic)
                
        except:
            print("apagado")
            print(medic)
    
    return dict(context=medic)


@route('/operator/<ops>', method=["GET","POST"])
@db_session
@view('operator.tpl', template_lookup=['views'])
def main_operator_index(ops):
    """ operator Main Index """
    admin_user = {
        'operator': {
        'userid': ops,
        'name': '',
        'lastname': ''
        }
    }
    data = DBobjects().loadobjects()
    admin_user['operator']['name'] = User.get(userid=ops).name
    admin_user['operator']['lastname'] = User.get(userid=ops).lastname
    data.append(admin_user)

    if request.method == 'POST':
        Assignation().medicassign(dict(request.forms))
        
    
    return dict(context=data)


@route('/operator/reassignation', method=["GET","POST"])
@db_session
@view('reassignation.tpl', template_lookup=['views'])
def main_operator_reassignation_index():
    """ operator reassign Main Index """
    current = Assignation.currentassign()
    alldata = DBobjects().loadobjects()
    alldata.append(dict(currentdata=current))

    if request.method == 'POST':
        data = dict(request.forms)
        
        Assignation().reassignation(data['current'],data['newtime'])
        pass        
    
    return dict(context=alldata)



@route('/user')
@db_session
@view('user.tpl', template_lookup=['views'])
def main_doctor_index():
    """ User Main Index """
    medics_patients = []
    
    #Get Complete list of Patients
    patients = select(p for p in Patient)[:]
    data_patient = {'patient_data': [p.to_dict() for p in patients]}

    return dict(context=medics_patients)



run(**settings['framework'])



