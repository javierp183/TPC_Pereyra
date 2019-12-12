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
import json

# Tables / Objects
from database import Medic, Speciality
from database import Agenda, Patient
from database import User
from loader import Loader
from dbapp import Assignation,Usermgmt
from dbapp import DBobjects

# Datetime
import datetime

# HTML Parser
from html.parser import HTMLParser

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


@route('/lista_medicos/<ops>', method=["GET","POST"])
@view('listar_medicos.tpl', template_lookup=['views'])
def lista_medicos(ops):
    obj = DBobjects().loadobjects()
    pass


@route('/lista_operadores/<ops>', method=["GET","POST"])
@db_session
@view('listar_operadores.tpl', template_lookup=['views'])
def lista_operadores(ops):
    try:
        if not User.get(userid=ops).rol == 'admin':
            return redirect('/wrongops')
    except AttributeError:
        return 'Ingreso no valido, vuelva a la pagina anterior'
    #Obtener lista completa de operadores
    operadores = select(o for o in User if o.rol == 'admin')[:]
    datos_operadores = {'op_data': [o.to_dict() for o in operadores]}

    if request.forms.get('volver') == "volver":
        return redirect('/operator/{}'.format(ops))

    if request.forms.get('agregar') == "agregar":
        return redirect('/addoperator/{}'.format(ops))
    
    if request.forms.get('eliminar') == "eliminar":
        return redirect('/userdel_operador/{}'.format(ops))


    return dict(context=datos_operadores)


@route('/anular_turno', method=["GET","POST"])
@db_session
def anular_turno():
    postdata = request.body.read()
    dni = json.loads(postdata)[2]
    fecha = json.loads(postdata)[3]
    valor_dni = int(dni['value'])
    query = "a for a in Agenda if a.dni == '{}' and a.date == '{}'".format(valor_dni,fecha['value'])
    cmdquery = select(query)[:]
    paciente_a_anular_turno = cmdquery[0]
    paciente_a_anular_turno.state = False
    commit()
    pass


@route('/reasignar_turno', method=["GET","POST"])
@db_session
def reasignar_turno():
    postdata = request.body.read()
    dni = json.loads(postdata)[2]
    fecha = json.loads(postdata)[3]
    valor_dni = int(dni['value'])
    query = "a for a in Agenda if a.dni == '{}' and a.date == '{}'".format(valor_dni,fecha['value'])
    cmdquery = select(query)[:]
    paciente_a_anular_turno = cmdquery[0]
    paciente_a_anular_turno.state = False
    commit()
    pass


@route('/agregar_especialidad/<ops>', method=["GET","POST"])
@db_session
@view('agregar_especialidades.tpl', template_lookup=['views'])
def agregar_especialidad(ops):
    try:
        if not User.get(userid=ops).rol == 'admin':
            return redirect('/wrongops')
    except AttributeError:
        return 'Ingreso no valido, vuelva a la pagina anterior'

    if request.forms.get('volver') == "volver":
        return redirect('/operator/{}'.format(ops))
    
    if request.forms.get("name") != None:
        Speciality(name=request.forms.get("name"))
        commit()
        return "Se agrego la nueva especialidad: {}, <a href='/agregar_especialidad/{}'>volver a pagina anterior</a>".format(str(request.forms.get("name")),ops)
    pass


@route('/turnoasignado')
@view('turno_asignado.tpl', template_lookup=['views'])
def turno_asignado():
    pass


@route('/ver_turnos/<ops>', method=["GET","POST"])
@db_session
@view('ver_turnos.tpl', template_lookup=['views'])
def ver_turnos(ops):
    """ Medic Main Index """
    try:
        if not User.get(userid=ops).rol == 'admin':
            return redirect('/wrongops')
    except AttributeError:
        return 'Ingreso no valido, vuelva a la pagina anterior'

    medic = 0
    print(request.forms.get('nombre'))
    try:
        if request.method == 'POST':
            if request.forms.get('buscar') == "buscar":
                turno = request.forms.get("dni")
                turno = int(turno)
                print(turno)
                return dict(context=Assignation().buscarpacienteporturno(turno))
    except:
        return "Ingrese un Turno valido!!!, <a href='/ver_turnos/{}'>volver atras</a>".format(ops)
    
    if request.method == 'POST':
        if request.forms.get('volver') == "volver":
            return redirect('/operator/{}'.format(ops))

    return dict(context=medic)



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
        form_data['medico'] = 1
        form_data['password'] = request.forms.get('password')

        for i in obj[2]['spec_data']:
            if request.forms.get(i['name']) != None:
                especialidades.append(i['name'])
        
        for palabra in especialidades:
            string = string + palabra + ","
        
        form_data['specialization'] = string[:-1]

    
        if not form_data['name']:
            return "Complete todos los campos!, volver atras, <a href='/useradd/{}'>volver atras</a>".format(ops)

        if not form_data['lastname']:
            return "Complete todos los campos!, volver atras, <a href='/useradd/{}'>volver atras</a>".format(ops)

        if not form_data['userid']:
            return "Complete todos los campos!, volver atras, <a href='/useradd/{}'>volver atras</a>".format(ops)

        if not form_data['specialization']:
            return "Complete todos los campos!, volver atras, <a href='/useradd/{}'>volver atras</a>".format(ops)
        
        if not form_data['specialization']:
            return "Complete todos los campos!, volver atras, <a href='/useradd/{}'>volver atras</a>".format(ops)
        
        if User.exists(medicid=int(request.forms.get('medicid'))):
            return "El usuario ya existe!!!, <a href='/useradd/{}'>volver atras</a>".format(ops)


    create = Usermgmt()
    if create.adduser(form_data):
        return "Usuario creado!!!, <a href='/useradd/{}'>volver atras</a>".format(ops)
    
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
            return "Complete todos los campos!, <a href='/addoperator/{}'>volver atras</a>".format(ops)

        if not form_data['lastname']:
            return "Complete todos los campos!, <a href='/addoperator/{}'>volver atras</a>".format(ops)

        if not form_data['userid']:
            return "Complete todos los campos!, <a href='/addoperator/{}'>volver atras</a>".format(ops)

        if not form_data['password']:
            return "Complete todos los campos!, <a href='/addoperator/{}'>volver atras</a>".format(ops)

    create = Usermgmt()
    if create.adduser(form_data):
        return "Usuario operador creado, <a href='/addoperator/{}'>volver atras</a>".format(ops)
    
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
            return "Complete todos los campos!, <a href='/addpaciente/{}'>volver atras</a>".format(ops)

        if not form_data['lastname']:
            return "Complete todos los campos!, <a href='/addpaciente/{}'>volver atras</a>".format(ops)

        if not form_data['dni']:
            return "Complete todos los campos!, <a href='/addpaciente/{}'>volver atras</a>".format(ops)

        if not form_data['email']:
            return "Complete todos los campos!, <a href='/addpaciente/{}'>volver atras</a>".format(ops)
        
        if Patient.exists(dni=int(request.forms.get('dni'))):
            return "El DNI ya esta registrado, registre otro!, <a href='/useradd/{}'>volver atras</a>".format(ops)
        elif Patient.exists(email=str(request.forms.get('email'))):
            return "El Email ya esta registrado, use otro!, <a href='/useradd/{}'>volver atras</a>".format(ops)

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
    obj = DBobjects().loadobjects()
    especialidades = []
    string = ""

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
        form_data['medico'] = 1
        form_data['password'] = request.forms.get('password')

        for i in obj[2]['spec_data']:
            if request.forms.get(i['name']) != None:
                especialidades.append(i['name'])
        
        for palabra in especialidades:
            string = string + palabra + ","
        
        form_data['specialization'] = string[:-1]
        
        if not form_data['name']:
            return "Complete todos los campos!, <a href='/useradd/{}'>volver atras</a>".format(ops)

        if not form_data['lastname']:
            return "Complete todos los campos!, <a href='/useradd/{}'>volver atras</a>".format(ops)

        if not form_data['userid']:
            return "Complete todos los campos!, <a href='/useradd/{}'>volver atras</a>".format(ops)

        if not form_data['specialization']:
            return "Complete todos los campos!, <a href='/useradd/{}'>volver atras</a>".format(ops)

        if not form_data['specialization']:
            return "Complete todos los campos!, <a href='/useradd/{}'>volver atras</a>".format(ops)

        if User.exists(userid=str(request.forms.get('userid'))):
            return "El userid ya se esta usando!!!"

        if User.exists(medicid=int(request.forms.get('medicid'))):
            return "El usuario ya existe!!!, <a href='/useradd/{}'>volver atras</a>".format(ops)
    
    create = Usermgmt()
    if create.adduser(form_data):
        return "Usuario creado, <a href='/useradd/{}'>volver atras</a>".format(ops)


    return dict(context=obj)


@route('/userdel_paciente/<ops>', method=["GET","POST"])
@db_session
@view('userdel_paciente.tpl', template_lookup=['views'])
def main_userdel_paciente_index(ops):
    if User.get(userid=ops).rol == 'admin':
        print("este es un usuario admin")
    else:
        return redirect('/wrongops')

    try:
        if request.forms.get('volver') == "volver":
            return redirect('/operator/{}'.format(ops))
        elif request.forms.get('operador') == "operador":
            return redirect('/userdel_operador/{}'.format(ops))
        elif request.forms.get('paciente') == "paciente":
            return redirect('/userdel_paciente/{}'.format(ops))
        elif request.forms.get('medico') == "medico":
            return redirect('/userdel/{}'.format(ops))
        
        if request.method == 'POST':
            print("test")
            dni = request.forms.get('dni')
            if Patient.exists(dni=dni):
                obj = User.get(dni=dni)
                nombre = obj.name
                apellido = obj.lastname
                obj.delete()
                commit()
                return "Paciente {} {} borrado del sistema, <a href='/userdel/{}'>volver atras</a>".format(nombre,apellido,ops)
            else:
                return "El DNI no existe!, <a href='/userdel_operador/{}'>volver atras</a>".format(ops)
    except ValueError:
        return "Ingrese un DNI valido, <a href='/userdel_operador/{}'>volver atras</a>".format(ops)



@route('/userdel_operador/<ops>', method=["GET","POST"])
@db_session
@view('userdel_operador.tpl', template_lookup=['views'])
def main_userdel_operador_index(ops):
    if User.get(userid=ops).rol == 'admin':
        print("este es un usuario admin")
    else:
        return redirect('/wrongops')

    try:
        if request.forms.get('volver') == "volver":
            return redirect('/operator/{}'.format(ops))
        elif request.forms.get('operador') == "operador":
            return redirect('/userdel_operador/{}'.format(ops))
        elif request.forms.get('paciente') == "paciente":
            return redirect('/userdel_paciente/{}'.format(ops))
        elif request.forms.get('medico') == "medico":
            return redirect('/userdel/{}'.format(ops))
        
        if request.method == 'POST':
            print("test")
            userid = request.forms.get('userid')
            userid = str(userid)
            if User.exists(userid=userid):
                obj = User.get(userid=userid)
                nombre = obj.name
                apellido = obj.lastname
                obj.delete()
                commit()
                return "Operador {} {} borrado del sistema, <a href='/userdel/{}'>volver atras</a>".format(nombre,apellido,ops)
            else:
                return "El USERID no existe!, <a href='/userdel_operador/{}'>volver atras</a>".format(ops)
    except ValueError:
        return "Ingrese un userid valido, <a href='/userdel_operador/{}'>volver atras</a>".format(ops)
    


@route('/userdel/<ops>', method=["GET","POST"])
@db_session
@view('userdel.tpl', template_lookup=['views'])
def main_userdel_index(ops):
    """ Main UserAdd Index """

    if User.get(userid=ops).rol == 'admin':
        print("este es un usuario admin")
    else:
        return redirect('/wrongops')

    try:
        if request.forms.get('volver') == "volver":
            return redirect('/operator/{}'.format(ops))
        elif request.forms.get('operador') == "operador":
            return redirect('/userdel_operador/{}'.format(ops))
        elif request.forms.get('paciente') == "paciente":
            return redirect('/userdel_paciente/{}'.format(ops))
        elif request.forms.get('medico') == "medico":
            return redirect('/userdel/{}'.format(ops))
        
        if request.method == 'POST':
            medicid = int(request.forms.get('medicid'))
            if User.exists(medicid=medicid):
                obj = User.get(medicid=medicid)
                nombre = obj.name
                apellido = obj.lastname
                obj.delete()
                commit()
                return "Medico {} {} borrado del sistema, <a href='/userdel/{}'>volver atras</a>".format(nombre,apellido,ops)
            else:
                return "El MEDICID no existe!, <a href='/userdel/{}'>volver atras</a>".format(ops)
    except ValueError:
        return "Ingrese un medicid valido, <a href='/userdel/{}'>volver atras</a>".format(ops)
    

    

    # create = Usermgmt()
    # create.deleteuser(data)

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
                medic['saludo'] = saludo
                print(medic)
                
        except:
            pass
    
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
    data.append(ingresos)


    try:
        if request.method == 'POST':
            query = request.forms.get('medic')
            query2 = query.split("-")[1]
            query = query.split("-")[0] 
            ingresos['ingreso0'] = query2
            ingresos['ingreso1'] = query
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
                    print("test 2")
                    return template('turno_asignado.tpl', context=ops)
                elif out == "error":
                    return "Horario o entrada no valido, vuelva atras, actualize e ingrese un horario valido, <a href='/operator/{}'>volver atras</a>".format(ops)
        else:
            print(" test re loco ")
    except AttributeError:
        pass
            

    return dict(context=data)



@route('/operator/assignation/<ops>', method=["GET","POST"])
@db_session
@view('assignation.tpl', template_lookup=['views'])
def assignation(ops):
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
    data.append(ingresos)


    try:
        if request.method == 'POST':
            query = request.forms.get('medic')
            query2 = query.split("-")[1]
            query = query.split("-")[0] 
            ingresos['ingreso0'] = query2
            ingresos['ingreso1'] = query
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
                    print("test 2")
                    return template('turno_asignado.tpl', context=ops)
                elif out == "error":
                    return "Horario o entrada no valido, vuelva atras, actualize e ingrese un horario valido, <a href='/operator/{}'>volver atras</a>".format(ops)
        else:
            print(" test re loco ")
    except AttributeError:
        pass

    if request.method == 'POST':
        if request.forms.get('volver') == "volver":
            return redirect('/operator/{}'.format(ops))
            

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


    if request.forms.get('volver') == "volver":
        return  redirect('/operator/{}'.format(ops))


    if request.method == 'POST':
        data = dict(request.forms)
        Assignation().reassignation(data['current'],data['newtime'])
        return "Turno reasignado!!!, <a href='/operator/reassignation/{}'>volver atras</a>".format(ops)
    
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



