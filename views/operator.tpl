{% include "head.tpl" %}

<link rel="stylesheet" href="/static/css/style.css">
<link rel="stylesheet" href="/static/css/prism.css">
<link rel="stylesheet" href="/static/css/chosen.css">

<h1>Nombre de Operador: {{ context.6.operator.name }} </h1>
<h1>Apellido: {{ context.6.operator.lastname }} </h1>
<p>Usuario:  {{ context.6.operator.userid }} </p>

<h1> Asignacion de turnos medicos: </h1>

<body>
  <form method="POST">

      <em>Elegir medico y especialidad</em>
          <select class="chosen-select" tabindex="5" name="medic">
              {%for q, b in context.4.select_data.items()%}
              {%set names = b['name'] %}
              {%set ids = b['idmedic']%}
            <optgroup label="{{ q }}">
              {%for n in names%} <option value="{{ ids[loop.index0] }}">{{ n }}</option> {%endfor%}
            </optgroup>
            {%endfor%}
          </select>

      <em>Elegir tiempo libre</em>
        <select class="chosen-select" tabindex="5" name="daytimehour">
            {%for k, v in context.5.hourmedic.items()%}
            {%set time = v['hours'] %}
            {%set date = v['dates'] %}

             <optgroup label="{{ k }}">     
                {%for t in time%} <option value"{{ t }}"> Hour: {{ t }} Date: {{ date[loop.index0] }} {%endfor%} </option>  
          </optgroup>
          {%endfor%}
        </select>
        
      <em>Elegir paciente</em>
      <select class="chosen-select" tabindex="5" name="patient">
        {%for i in context.0.patient_data%}
        <option>{{ i.name }} {{ i.lastname }} - {{ i.dni }}</option>
        {%endfor%}
      </select>
      <br>
  <input type="text" name="comments">
  <input type="submit" onclick="alert('Turno Asignado!!!')" value="Ingresar">

</form>

<p>Presione el boton para reasignar turnos:</p>
<button type="button"><a href="/operator/reassignation/{{ context.6.operator.userid }}">reasignacion de turnos</a></button>

<p>Presione el boton para añadir usuarios:</p>
<button type="button"><a href="/useradd/{{ context.6.operator.userid }}">Añadir usuarios</a></button>

<p>Presione el boton para borrar usuarios:</p>
<button type="button"><a href="/userdel/{{ context.6.operator.userid }}">Borrar usuarios</a></button>

  <script src="/static/js/jquery-3.2.1.min.js" type="text/javascript"></script>
  <script src="/static/js/chosen.jquery.js" type="text/javascript"></script>
  <script src="/static/js/prism.js" type="text/javascript" charset="utf-8"></script>
  <script src="/static/js/init.js" type="text/javascript" charset="utf-8"></script>

  {% include "foot.tpl" %}