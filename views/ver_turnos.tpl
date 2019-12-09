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


    Ingrese DNI del Paciente:
    <form method="POST">
      DNI: <input type="text" name="dni"><br>
      <button type="submit" name="buscar" value="buscar">Buscar turno</button>
      <button type="submit" name="volver" value="volver">Volver a pagina anterior</a></button>
    </form>


    <div class="container mt-3">
        <table>
            <tr>

            </tr>
        </table>
      <h3>Turnos</h3>
      <p>Ingrese dni, comentario o fechas para filtrar:</p>  
      <input class="form-control" id="myInput" type="text" placeholder="Search..">
      <br>

      <form method="POST">
      <table class="table table-bordered">
        <thead>
          <tr>
            <th>Nombre y Apellido</th>
            <th>Horario AM</th>
            <th>DNI</th>
            <th>Mes y Dia</th>
            <th>Comentarias</th>
            <th>Motivo/Especialidad</th>
            <th>opcion</th>
          </tr>
        </thead>
        <tbody id="myTable">

        {%for i in context.nombre%}
        {%set nombre_1 = context.nombre[loop.index-1]%}
        {%set apellido_1 = context.apellido[loop.index-1]%}
        {%set fecha_1 = context.fecha[loop.index-1]%}
        {%set hora_1 = context.hora[loop.index-1]%}
        {%set nombremedico_1 = context.nombremedico[loop.index-1]%}
        {%set apellidomedico_1 = context.apellidomedico[loop.index-1]%}
        
        <td>
            {{ nombre_1 }}
          </td>
          <td>
            {{ apellido_1 }}
          </td>
          <td>
            {{ fecha_1 }}
          </td>
          <td>
            {{ hora_1 }}
          </td>
          <td>
            {{ nombremedico_1 }}
          </td>
          <td>
            {{ apellidomedico_1 }}
          </td>
          <td>
            <input type="checkbox"> Opcion
          </td>
       
          </tr>
          {%endfor%}
      
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




</body>
</html>