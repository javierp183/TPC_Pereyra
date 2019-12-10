<link href="//cdn.datatables.net/1.10.12/css/jquery.dataTables.min.css" rel="stylesheet"/>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script src="//cdn.datatables.net/1.10.12/js/jquery.dataTables.min.js"></script>

{{ context }}

Ingrese DNI del Paciente:
<form method="POST">
  DNI: <input type="text" name="dni"><br>
  <button type="submit" name="buscar" value="buscar">Buscar turno</button>
  <button type="submit" name="volver" value="volver">Volver a pagina anterior</a></button>
</form>

{%if context is defined%}

<form method="POST">

  <input type="hidden" name="_token" value="23523">
  <input type="hidden" name="show_id" value="533">
  <input type="hidden" name="memberId" value="4567">
  <table id="goatTable" class="display" cellspacing="0" width="100%">
    <thead>
      <tr>
        <th>Nombre</th>
        <th>Apellido</th>
        <th>Fecha</th>
        <th>Hora de Turno (AM)</th>
        <th>Nombre de Medico</th>
        <th>Apellido de Medico</th>
        <th>Especialidad</th>
      </tr>
    </thead>
    <tbody>
    {%for i in context.nombre%}
    {%set nombre_1 = context.nombre[loop.index-1]%}
    {%set apellido_1 = context.apellido[loop.index-1]%}
    {%set fecha_1 = context.fecha[loop.index-1]%}
    {%set hora_1 = context.hora[loop.index-1]%}
    {%set nombre_medico_1 = context.nombremedico[loop.index-1]%}
    {%set apellido_medico_1 = context.apellidomedico[loop.index-1]%}
    {%set especialidad_1 = context.especialidad[loop.index-1]%}

      <tr>
        <td>{{ nombre_1 }}<input type="hidden" name="entry_reg_name" value="{{ nombre_1 }}"></td>
        <td>{{ apellido_1 }}<input type="hidden" name="entry_reg_apellido" value="{{ apellido_1 }}"></td>
        <td>{{ fecha_1 }}<input type="hidden" name="entry_reg_fecha" value="{{ fecha_1 }}"></td>
        <td>{{ hora_1 }}<input type="hidden" name="entry_reg_fecha" value="{{ hora_1 }}"></td>
        <td>{{ nombre_medico_1 }}<input type="hidden" name="entry_reg_nombre_medico" value="{{ nombre_medico_1 }}"></td>
        <td>{{ apellido_medico_1 }}<input type="hidden" name="entry_reg_apellido_medico" value="{{ apellido_medico_1 }}"></td>
        <td>{{ especialidad_1 }}<input type="hidden" name="entry_reg_especialidad" value="{{ especialidad_1 }}"></td>

      </tr>
    </tbody>
    {%endfor%}
  </table>
  
  <button id="anular_turno">Anular turno</button>
  <button id="reasignar_turno">Reasignar turno</button>
</form>

<script>
  $(document).ready(function() {
  var table = $('#goatTable').DataTable();

  $('#goatTable tbody').on( 'click', 'tr', function () {
      $(this).toggleClass('selected');
  } );

  $('#anular_turno').click( function (e) {
    e.preventDefault();
    var selectedRowInputs = JSON.stringify($('.selected input').serializeArray());
    
    //use the serialized version of selectedRowInputs as the data
    //to be sent to the AJAX request

    console.log('serlialized inputs: ',selectedRowInputs);
    
      $.ajax({
        type: "POST",
        url: "/entershowoptions",
        contentType: "application/json",
        dataType: "json",
        data: selectedRowInputs
      });
  });

  $('#reasignar_turno').click( function (e) {
    e.preventDefault();
    var selected = JSON.stringify($('.selected input').serializeArray());
    
    //use the serialized version of selectedRowInputs as the data
    //to be sent to the AJAX request

    console.log('serlialized inputs: ',selected);
    
      $.ajax({
        type: "POST",
        url: "/reasignarturno",
        contentType: "application/json",
        dataType: "json",
        data: selected
      });
      
  });

  
});
</script>

{%endif%}