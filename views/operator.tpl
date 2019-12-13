<!DOCTYPE html>
<html>
  <head>
    
      <title>TPC - UTN - Javier Pereyra</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
  <body style="background-image: url('https://st3.depositphotos.com/1008648/17034/i/1600/depositphotos_170343438-stock-photo-healthcare-modern-interface-3d-rendering.jpg');">
    
<table class="table table-dark">
  <thead>
    <tr>
      <th>
        Nombre y Apellido del Operador
      </th>
      <th>
        Usuario
      </th>
    </tr>
    </thead>
    <tbody>
      <tr>
        <td>
            {{ context.6.operator.name }} {{ context.6.operator.lastname }}
        </td>
        <td>
            {{ context.6.operator.userid }}
        </td>
      </tr>
    </tbody>
  </table>

<table>
<tr>

</tr>


</table>

<div class="container">
    <p><font color="red"><b>Menu de opciones</b></font></p>            
    <table class="table table-dark table-hover">
      <thead>
        <tr>
            Menu de opciones
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
              <div class="dropdown">
                  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenu2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Turnos
                  </button>
                  <div class="dropdown-menu" aria-labelledby="dropdownMenu2">
                  <button class="dropdown-item" type="button"><a href="/operator/assignation/{{ context.6.operator.userid }}">asignar turno</a></button>
                  <button class="dropdown-item" type="button"><a href="/ver_turnos/{{ context.6.operator.userid }}">Ver Turnos</a></button>
            
                  </div>
              </div>
          </td>
          <td>
              <div class="dropdown">
                  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenu2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Listar usuarios
                  </button>
                  <div class="dropdown-menu" aria-labelledby="dropdownMenu2">
                    <button  class="dropdown-item" type="button"><a href="/lista_operadores/{{ context.6.operator.userid }}">Listar Operadores</a></button>
                    <button  class="dropdown-item" type="button"><a href="/lista_medicos/{{ context.6.operator.userid }}">Listar Medicos</a></button>
                    <button  class="dropdown-item" type="button"><a href="/lista_pacientes/{{ context.6.operator.userid }}">Listar Pacientes</a></button>


                  </div>
              </div>
          </td>
          <td>
              <div class="dropdown">
                  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenu2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Alta/Baja de usuarios
                  </button>
                  <div class="dropdown-menu" aria-labelledby="dropdownMenu2">
                      <button   class="dropdown-item" type="button"><a href="/useradd/{{ context.6.operator.userid }}">Agregar usuarios</a></button>
                      <button  class="dropdown-item"  type="button"><a href="/userdel/{{ context.6.operator.userid }}">Eliminar usuarios</a></button>
                  </div>
              </div>
            
          </td>
          <td>
              <div class="dropdown">
                  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenu2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Especialidades
                  </button>
                  <div class="dropdown-menu" aria-labelledby="dropdownMenu2">
                      <button class="dropdown-item" type="button"><a href="/agregar_especialidad/{{ context.6.operator.userid }}">Añadir especialidad</a></button>

                  </div>
              </div>
          </td>
      </tbody>
    </table>
  </div>
  </body>
</head>
</html>
