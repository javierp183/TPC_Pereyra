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
import bottle

# Tables / Objects
from database import Medic, Speciality
from database import Agenda, Patient
from database import User
from loader import Loader
from dbapp import Assignation

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

@route('/validate')
@view('validate.tpl', template_lookup=['views'])
def error():
    pass

@route('/saveuser')
@view('thanks.tpl', template_lookup=['views'])
def thanks():
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

@route('/')
@db_session
@view('index.tpl', template_lookup=['views'])
def main_doctor_index():
    """ Main Index """
    pass

@route('/useradd')
@db_session
@view('useradd.tpl', template_lookup=['views'])
def main_doctor_index():
    """ Main Index """
    pass


@route('/agenda')
@db_session
@view('index.tpl', template_lookup=['views'])
def main_doctor_index():
    """ Main Index """
    pass


@route('/medic')
@db_session
@view('medic.tpl', template_lookup=['views'])
def main_doctor_index():
    """ Medic Main Index """

    #Get Complete list of Medics
    medics = select(m for m in Medic)[:]
    result = {'data': [m.to_dict() for m in medics]}

    return dict(context=result)


@route('/patient', method=["GET","POST"])
@db_session
@view('patient.tpl', template_lookup=['views'])
def main_doctor_index():
    """ Patient Main Index """
    medics_patients = []
    html_table_data = {
        'dni':[], 'name':[], 'lastname': [], 'spec_selected': [],
        'time': []
    }
    
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


    medics_patients.append(data_patient)
    medics_patients.append(data_medic)
    medics_patients.append(data_speciality)
    medics_patients.append(data_agenda)


    for i in html_table_data.keys():
        html_table_data[i] = request.GET.getall(i)

    p = Assignation()

    p.medicassign(html_table_data,medics_patients)


    return dict(context=medics_patients)


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
