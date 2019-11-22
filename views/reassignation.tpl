{% include "head.tpl" %}

<link rel="stylesheet" href="/static/css/style.css">
<link rel="stylesheet" href="/static/css/prism.css">
<link rel="stylesheet" href="/static/css/chosen.css">

<h1> Re-asignacion de turnos: </h1>


<body>
  <form method="POST">

      <em>Asignaciones actuales:</em>
        <select class="chosen-select" tabindex="5" name="current">
            {%for k, v in context.6.currentdata.items()%}
            {%set time = v['hours'] %}
            {%set date = v['dates'] %}
            {%set medic_name = v['medic_name']%}
            {%set patient_name = v['patient_name']%}
            {%set patient_lastname = v['patient_lastname']%}
            {%set patient_dni = v['patient_dni']%}
            {%set speciality_name = v['speciality_name']%}
            {%set agenda_id = v['agenda_id']%}

          <optgroup label="{{ k }}">     
                {%for t in time%} <option value="{{ agenda_id[loop.index0] }}"> Hour: {{ t }} Date: {{ date[loop.index0] }} Patient: 
                  {{ patient_lastname[loop.index0] }} DNI: {{ patient_dni[loop.index0] }}
                   Spec: {{ speciality_name[loop.index0] }}
                  {%endfor%} </option>  
          </optgroup>
          {%endfor%}
        </select>
      
      <em>Seleccione un turno libre:</em>
      <select class="chosen-select" tabindex="5" name="newtime">
            {%for k, v in context.5.hourmedic.items()%}
            {%set time = v['hours'] %}
            {%set date = v['dates'] %}
            {%set agenda_id = v['agenda_id']%}

      <optgroup label="{{ k }}">     
                {%for t in time%} <option value="{{ agenda_id[loop.index0] }}"> Hour: {{ t }} Date: {{ date[loop.index0] }} {%endfor%} </option>  
      </optgroup>
          {%endfor%}
      </select><br>
  <input type="submit" onclick="alert('Turno Re-Asignado!!!')" value="Asignar">

</form>



  

  <script src="/static/js/jquery-3.2.1.min.js" type="text/javascript"></script>
  <script src="/static/js/chosen.jquery.js" type="text/javascript"></script>
  <script src="/static/js/prism.js" type="text/javascript" charset="utf-8"></script>
  <script src="/static/js/init.js" type="text/javascript" charset="utf-8"></script>


  {% include "foot.tpl" %}