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
      
    <form method="POST">      
      
      <form method="POST">

          <em>Elegir medico y especialidad</em>
              <select class="chosen-select" tabindex="5" name="medic">

                  {%for q, b in context.4.select_data.items()%}
                  {%set names = b['name']%}
                  {%set ids = b['idmedic']%}

                <optgroup label="{{ q }}">
                    {%for id in ids%}
                    <option value="{{ id }}" {%if context.7.ingreso1 == id | string%} selected="selected"{%endif%}>{{ names[loop.index0] }}</option>
                      {%endfor%}
                    {%endfor%} 
                </optgroup>
                
              </select>
          <button type="submit" name="medico">Ver y actualizar Fechas disponibles</button>
      <form>



      <form method="POST">

      {%if context.8 is defined%}

          {%for x, z in context.8.items() %}
          {%set y = x | string%}
          {%set hr = z['hours']%}
          {%set dias = z['days']%}
          {%set dates = z['months']%}
          {%if context.7.ingreso1%}
          

          
          
          <select class="chosen-select" tabindex="5" name="mes">
                {%for h in hr%}<option value="{{ dates[loop.index0].split('/')[0] }}" {%if context.7.ingreso2 == "Diciembre-12" | string%} selected="selected"{%endif%}>{{ dates[loop.index0] }}</option>{%endfor%}
          </select>
          
          <em>Seleccione dia y horario</em>
          <select class="chosen-select" tabindex="5" name="dias">
          {%for d in dias[context.7.ingreso2] %}  <option> {{ d }} </option> {%endfor%}
          </select>

          <em>Elegir paciente</em>
          <select class="chosen-select" tabindex="5" name="patient">
            {%for i in context.0.patient_data%}
          <option>{{ i.name }} {{ i.lastname }} - {{ i.dni }}</option>
            {%endfor%}
          </select>
          <br>
          Comentarios:
          <input type="text" name="comments">
          <input  id="Ingresar" type="submit" value="Ingresar" name="turno" onclick="recargar_pagina("test")">
          {%endif%}
          {%endfor%}
      
          </form>
   </form>
                
                  <script src="/static/js/jquery-3.2.1.min.js" type="text/javascript"></script>
                  <script src="/static/js/chosen.jquery.js" type="text/javascript"></script>
                  <script src="/static/js/prism.js" type="text/javascript" charset="utf-8"></script>
                  <script src="/static/js/init.js" type="text/javascript" charset="utf-8"></script>
      {%endif%}

      <p>Presione el boton para reasignar turnos:</p>
      <button type="button"><a href="/operator/reassignation/{{ context.6.operator.userid }}">reasignacion de turnos</a></button>
      
      <p>Presione el boton para añadir usuarios:</p>
      <button type="button"><a href="/useradd/{{ context.6.operator.userid }}">Añadir usuarios</a></button>
      
      <p>Presione el boton para borrar usuarios:</p>
      <button type="button"><a href="/userdel/{{ context.6.operator.userid }}">Borrar usuarios</a></button>

      <p>Presione el boton para añadir especialidad:</p>
      <button type="button"><a href="/agregar_especialidad/{{ context.6.operator.userid }}">Añadir especialidad</a></button>