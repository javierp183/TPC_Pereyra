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

@route('/agregar_especialidad/<ops>', method=["GET","POST"])
@view('agregar_especialidades.tpl', template_lookup=['views'])
def agregar_especialidad(ops):
    if request.forms.get('volver') == "volver":
        return redirect('/operator/{}'.format(ops))
    pass


@route('/turnoasignado')
@view('turno_asignado.tpl', template_lookup=['views'])
def turno_asignado():
    pass


@route('/medicanonssigned')
@view('medic_non_assigned.tpl', template_lookup=['views'])
def medic_non_assigned():
    pass

@route('/wronguserpass')
@view('wronguserpass.tpl', template_lookup=['views'])
def wronguserpass():
    pass

@route('/wrongops')
@view('wrongops.tpl', template_lookup=['views'])
def wronguserpass():
    pass

@route('/wrongmedic')
@view('wrongmedic.tpl', template_lookup=['views'])
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

@route('/addmedic/<ops>', method=["GET","POST"])
@db_session
@view('useradd_medic.tpl', template_lookup=['views'])
def addmedic(ops):
    form_data = {
        'semana': [],
        'horario': [],
        'medicid': '',
        'specialization': '',
        'medico': '',
        'password': ''
    }
    obj = DBobjects().loadobjects()
    especialidades = []
    string = ""

    try:
        if not User.get(userid=ops).rol == 'admin':
            return redirect('/wrongops')
    except AttributeError:
        return 'Ingreso no valido, vuelva a la pagina anterior'

    try:
        if request.method == 'POST':
            if request.forms.get('operador') == "operador":
                return redirect('/addoperator/{}'.format(ops))
            elif request.forms.get('paciente') == "paciente":
                return redirect('/addpaciente/{}'.format(ops))
            elif request.forms.get('medico') == "medico":
                return redirect('/addmedic/{}'.format(ops))
            elif request.forms.get('volver') == "volver":
                return redirect('/operator/{}'.format(ops))
    except AttributeError:
        return redirect('/addmedic/{}'.format(ops))
    
    if request.method == 'POST':
        form_data['name'] = request.forms.get('name').lower()
        form_data['lastname'] = request.forms.get('lastname').lower()
        form_data['userid'] = request.forms.get('userid').lower()
        form_data['semana'].append(request.forms.get('lunes'))
        form_data['semana'].append(request.forms.get('martes'))
        form_data['semana'].append(request.forms.get('miercoles'))
        form_data['semana'].append(request.forms.get('jueves'))
        form_data['semana'].append(request.forms.get('viernes'))
        form_data['semana'].append(request.forms.get('sabado'))
        form_data['semana'].append(request.forms.get('domingo'))
        form_data['horario'].append(request.forms.get('turno1'))
        form_data['horario'].append(request.forms.get('turno2'))
        form_data['horario'].append(request.forms.get('turno3'))
        form_data['medicid'] = request.forms.get('medicid')
        form_data['specialization'] = request.forms.get('specialization').lower()
        form_data['medico'] = 1
        form_data['password'] = request.forms.get('password')

        for i in obj[2]['spec_data']:
            if request.forms.get(i['name']) != None:
                especialidades.append(i['name'])
        
        for palabra in especialidades:
            string = string + palabra + ","
        
        form_data['specialization'] = string[:-1]

    
        if not form_data['name']:
            return "Complete todos los campos!, volver atras"

        if not form_data['lastname']:
            return "Complete todos los campos!, volver atras"

        if not form_data['userid']:
            return "Complete todos los campos!, volver atras"

        if not form_data['specialization']:
            return "Complete todos los campos!, volver atras"
        
        if not form_data['specialization']:
            return "Complete todos los campos!, volver atras"
        
        if User.exists(medicid=int(request.forms.get('medicid'))):
            return "El usuario ya existe!!!, volver atras"


    create = Usermgmt()
    if create.adduser(form_data):
        return "Usuario creado"
    

    
    return dict(context=obj)



@route('/addoperator/<ops>', method=["GET","POST"])
@db_session
@view('useradd_operador.tpl', template_lookup=['views'])
def addoperator(ops):
    form_data = {
        'name': '',
        'lastname': '',
        'userid': '',
        'password': '',
        'admin': ''
    }

    try:
        if not User.get(userid=ops).rol == 'admin':
            return redirect('/wrongops')
    except AttributeError:
        return 'Ingreso no valido, vuelva a la pagina anterior'
    

    if request.method == 'POST':
        if request.forms.get('medico') == "medico":
            return redirect('/addmedic/{}'.format(ops))
        elif request.forms.get('paciente') == "paciente":
            return redirect('/addpaciente/{}'.format(ops))
        elif request.forms.get('operador') == "operador":
            return redirect('/addoperator/{}'.format(ops))
        elif request.forms.get('volver') == "volver":
            return redirect('/operator/{}'.format(ops))
    
    if request.method == 'POST':
        form_data['name'] = request.forms.get('name')
        form_data['lastname'] = request.forms.get('lastname')
        form_data['userid'] = request.forms.get('userid')
        form_data['password'] = request.forms.get('password')
        form_data['admin'] = 1

        if not form_data['name']:
            return "Complete todos los campos!"

        if not form_data['lastname']:
            return "Complete todos los campos!"

        if not form_data['userid']:
            return "Complete todos los campos!"

        if not form_data['password']:
            return "Complete todos los campos!"

    create = Usermgmt()
    if create.adduser(form_data):
        return "Usuario operador creado"
    
    print(form_data)


@route('/addpaciente/<ops>', method=["GET","POST"])
@db_session
@view('useradd_paciente.tpl', template_lookup=['views'])
def addpaciente(ops):
    form_data = {
        'name': '',
        'lastname': '',
        'dni': '',
        'email': '',
        'admin': ''
    }

    try:
        if not User.get(userid=ops).rol == 'admin':
            return redirect('/wrongops')
    except AttributeError:
        return 'Ingreso no valido, vuelva a la pagina anterior'


    if request.method == 'POST':
        if request.forms.get('medico') == "medico":
            return redirect('/addmedic/{}'.format(ops))
        elif request.forms.get('operador') == "operador":
            return redirect('/addoperator/{}'.format(ops))
        elif request.forms.get('paciente') == "paciente":
            return redirect('/addpaciente/{}'.format(ops))
        elif request.forms.get('volver') == "volver":
            return redirect('/operator/{}'.format(ops))
    
    if request.method == 'POST':
        form_data['name'] = request.forms.get('name')
        form_data['lastname'] = request.forms.get('lastname')
        form_data['dni'] = request.forms.get('dni')
        form_data['email'] = request.forms.get('email')
        form_data['patient'] = 1

        if not form_data['name']:
            return "Complete todos los campos!"

        if not form_data['lastname']:
            return "Complete todos los campos!"

        if not form_data['dni']:
            return "Complete todos los campos!"

        if not form_data['email']:
            return "Complete todos los campos!"
        
        if Patient.exists(dni=int(request.forms.get('dni'))):
            return "El DNI ya esta registrado, registre otro!"
        elif Patient.exists(email=str(request.forms.get('email'))):
            return "El Email ya esta registrado, use otro!"

    create = Usermgmt()
    if create.adduser(form_data):
        return "Paciente creado"
    
    print(form_data)

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
            return redirect('/wronguserpass')
        
    return dict(context={'output': 'none'})
        


@route('/useradd/<ops>', method=["GET","POST"])
@db_session
@view('useradd.tpl', template_lookup=['views'])
def main_useradd_index(ops):
    """ Main UserAdd Index """
    data = dict(request.forms)
    ingresos = {
        'ingreso1': '',
        'ingreso2': '',
        'ingreso3': ''
    }
    form_data = {
        'semana': [],
        'horario': [],
        'medicid': '',
        'medico': ''

    }

    try:
        if not User.get(userid=ops).rol == 'admin':
            return redirect('/wrongops')
    except AttributeError:
        return 'Ingreso no valido, vuelva a la pagina anterior'

    try:
        if User.get(userid=ops).rol == 'admin':
            if request.method == 'POST':
                if request.forms.get('medico') == "medico":
                    return redirect('/addmedic/{}'.format(ops))
                elif request.forms.get('operador') == "operador":
                    return redirect('/addoperator/{}'.format(ops))
                elif request.forms.get('paciente') == "paciente":
                    return redirect('/addpaciente/{}'.format(ops))
                elif request.forms.get('volver') == "volver":
                    return redirect('/operator/{}'.format(ops))
            else:
                pass
        else:
            return redirect('/wrongops')
    except AttributeError:
        return redirect('/wrongops')


    if request.method == 'POST':
        form_data['name'] = request.forms.get('name').lower()
        form_data['lastname'] = request.forms.get('lastname').lower()
        form_data['userid'] = request.forms.get('userid').lower()
        form_data['semana'].append(request.forms.get('lunes'))
        form_data['semana'].append(request.forms.get('martes'))
        form_data['semana'].append(request.forms.get('miercoles'))
        form_data['semana'].append(request.forms.get('jueves'))
        form_data['semana'].append(request.forms.get('viernes'))
        form_data['semana'].append(request.forms.get('sabado'))
        form_data['semana'].append(request.forms.get('domingo'))
        form_data['horario'].append(request.forms.get('turno1'))
        form_data['horario'].append(request.forms.get('turno2'))
        form_data['horario'].append(request.forms.get('turno3'))
        form_data['medicid'] = request.forms.get('medicid')
        form_data['specialization'] = request.forms.get('specialization').lower()
        form_data['medico'] = 1
        form_data['password'] = request.forms.get('password')
        
        if not form_data['name']:
            return "Complete todos los campos!"

        if not form_data['lastname']:
            return "Complete todos los campos!"

        if not form_data['userid']:
            return "Complete todos los campos!"

        if not form_data['specialization']:
            return "Complete todos los campos!"

        if not form_data['specialization']:
            return "Complete todos los campos!"

        if User.exists(userid=str(request.forms.get('userid'))):
            return "El userid ya se esta usando!!!"

        if User.exists(medicid=int(request.forms.get('medicid'))):
            return "El usuario ya existe!!!"
    
    create = Usermgmt()
    if create.adduser(form_data):
        return "Usuario creado"

    
    obj = DBobjects().loadobjects()
    print(obj)

    return dict(context=obj)



@route('/userdel/<ops>', method=["GET","POST"])
@db_session
@view('userdel.tpl', template_lookup=['views'])
def main_userdel_index(ops):
    """ Main UserAdd Index """
    data = dict(request.forms)

    if User.get(userid=ops).rol == 'admin':
        print("este es un usuario admin")
    else:
        return redirect('/wrongops')
    

    create = Usermgmt()
    create.deleteuser(data)

    return dict(context={'output': 'none'})


@route('/medic/<medicid>', method=["GET","POST"])
@db_session
@view('medic.tpl', template_lookup=['views'])
def main_doctor_index(medicid):
    """ Medic Main Index """
    try:
        if User.get(medicid=medicid).rol == 'medic':
            print("este es un usuario medico")
        else:
            return redirect('/wrongmedic')
    except AttributeError:
        return redirect('/wrongmedic')

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
    ingresos = {
        'ingreso1': '',
        'ingreso2': '',
        'ingreso3': '',
        'patient': '',
        'comments': '',
        'turno': ''
    }
    freetime = {
        'hours': [],
        'dates': []
    }

    data = DBobjects().loadobjects()

    try:
        admin_user['operator']['name'] = User.get(userid=ops).name
        admin_user['operator']['lastname'] = User.get(userid=ops).lastname
    except AttributeError:
        return "Ingreso no valido!!!, vuelva atras desde el explorador"

    if not User.get(userid=ops).rol == 'admin':
        return redirect('/wrongops')

    data.append(admin_user)
    ingresos['ingreso1'] = 0
    print("primer ingreso:")
    print(ingresos['ingreso1'])
    data.append(ingresos)

    if request.method == 'POST':
        print("segundo ingreso:")
        ingresos['ingreso1'] = request.forms.get('medic')
        print(ingresos['ingreso1'])
        ingresos['ingreso2'] = request.forms.get('mes')
        ingresos['ingreso3'] = request.forms.get('dias')
        ingresos['patient'] = request.forms.get('patient')
        ingresos['comments'] = request.forms.get('comments')
        ingresos['turno'] = request.forms.get('turno')
        query = request.forms.get('medic')
        buscar = DBobjects()
        salida = buscar.get_free_time_by_medic_id(query)
        salida2 = buscar.get_free_days(query)
        data.append(salida)
        data.append(salida2)
        if ingresos['turno'] == "Ingresar":
            doassign = Assignation()
            out = doassign.medicassign(ingresos)
            if out == "ok":
                return template('turno_asignado.tpl', context=ops)
        else:
            print("nada que asignar")

    return dict(context=data)



@route('/operator/reassignation/<ops>', method=["GET","POST"])
@db_session
@view('reassignation.tpl', template_lookup=['views'])
def main_operator_reassignation_index(ops):
    """ operator reassign Main Index """

    try:
        if User.get(userid=ops).rol == 'admin':
            print("este es un usuario medico")
        else:
            return redirect('/wrongops')
    except AttributeError:
        return redirect('/wrongops')

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



