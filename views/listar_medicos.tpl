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


<form method="POST">
    <button class="btn btn-secondary" type="submit" name="volver" value="volver">Volver a pagina anterior</a></button>
    <button class="btn btn-secondary" type="submit" name="agregar" value="agregar"> Ir a añadir usuario medico</a></button>
    <button class="btn btn-secondary" type="submit" name="eliminar" value="eliminar">Ir a eliminar usuario medico</a></button>
</form>
  <h3>Lista de Medicos registrados en el sistema</h3>
  <p>Ingrese nombre, apellido o UserID para filtrar:</p>  
  <input class="form-control" id="myInput" type="text" placeholder="Search..">
  <br>
  <table class="table table-dark table-bordered">
    <thead>
      <tr>
        <th>Nombre y Apellido</th>

        <th>UserID</th>
        <th>ID Medico</th>
      </tr>
    </thead>
    <tbody id="myTable">
        {%for data in context.medico_data%}
        {%set nombres = data['name']%}
        {%set apellidos = data['lastname']%}
        {%set userid = data['userid']%}
        {%set medicid = data['medicid']%}
        <tr>
        <td>
            {{ nombres }} {{ apellidos }}
        </td>
        <td>
           {{ userid }}
        </td>
        <td>
                {{ medicid }}
        </td>
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
