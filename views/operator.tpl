<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>

      <link rel="stylesheet" href="/static/css/style.css">
      <link rel="stylesheet" href="/static/css/prism.css">
      <link rel="stylesheet" href="/static/css/chosen.css">
      
      <h1>Nombre de Operador: {{ context.6.operator.name }} </h1>
      <h1>Apellido: {{ context.6.operator.lastname }} </h1>
      <p>Usuario:  {{ context.6.operator.userid }} </p>


      <p>Presione el boton para asignar turnos:</p>
      <button type="button"><a href="/operator/assignation/{{ context.6.operator.userid }}">asignar turno</a></button>

      <p>Presione el boton para reasignar turnos:</p>
      <button type="button"><a href="/operator/reassignation/{{ context.6.operator.userid }}">reasignacion de turnos</a></button>
      
      <p>Presione el boton para añadir usuarios:</p>
      <button type="button"><a href="/useradd/{{ context.6.operator.userid }}">Añadir usuarios</a></button>
      
      <p>Presione el boton para borrar usuarios:</p>
      <button type="button"><a href="/userdel/{{ context.6.operator.userid }}">Borrar usuarios</a></button>

      <p>Presione el boton para añadir especialidad:</p>
      <button type="button"><a href="/agregar_especialidad/{{ context.6.operator.userid }}">Añadir especialidad</a></button>

      <p>Presione el boton para ver los turnos actualmente asignados:</p>
      <button type="button"><a href="/ver_turnos/{{ context.6.operator.userid }}">Ver Turnos</a></button>