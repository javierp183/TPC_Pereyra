<!DOCTYPE html>
<html lang="en">
<head>
  <title>TP3 UTN</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</head>
<body>



<div class="container mt-3">
    <table>
        <tr>
          <th>Nombre del medico:</th>
          <th>ID del medico:</th>
        </tr>
        <tr>
          <td>{{ context.medic.name }} {{ context.medic.lastname }}</td>
          <td>{{ context.medic.medicid }}</td>
          <td>{{ context.medic.speciality }}</td
        </tr>
    </table>
  <h3>Pacientes</h3>
  <p>Ingrese dni, comentario o fechas para filtrar:</p>  
  <input class="form-control" id="myInput" type="text" placeholder="Search..">
  <br>
  <table class="table table-bordered">
    <thead>
      <tr>
        <th>Nombre y Apellido</th>
        <th>Horario</th>
        <th>DNI</th>
        <th>Mes y Dia</th>
        <th>Comentarias</th>
        <th>Motivo/Especialidad</th>
      </tr>
    </thead>
    <tbody id="myTable">
        {%for i in context.patients.name%}
        {% set item_1 = context.patients.name[loop.index-1] %}
        {% set item_2 = context.patients.lastname[loop.index-1] %}
        {% set item_3 = context.patients.time[loop.index-1] %}
        {% set item_4 = context.patients.daymonth[loop.index-1] %}
        {% set item_5 = context.patients.dni[loop.index-1] %}
        {% set item_6 = context.patients.comments[loop.index-1]%}
        {% set item_7 = context.patients.speciality[loop.index-1]%}
        <tr>
        <td>{{ item_1 }} {{ item_2 }}</td>
        <td>{{ item_3 }}</td>
        <td>{{ item_5 }}</td>
        <td>{{ item_4  }}</td>
        <td>{{ item_6 }}</td>
        <td>{{ item_7 }}</td>
        <td>
        </tr>
        {%endfor%}
    </tbody>
  </table>
  
</div>

<script>
$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#myTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
</script>

</body>
</html>
