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




  <h3>Lista de Operadores</h3>
  <p>Ingrese nombre, apellido o UserID para filtrar:</p>  
  <input class="form-control" id="myInput" type="text" placeholder="Search..">
  <br>
  <table class="table table-bordered">
    <thead>
      <tr>
        <th>Nombre y Apellido</th>
        <th>UserID</th>
      </tr>
    </thead>
    <tbody id="myTable">
        {%for data in context.op_data%}
        {%set nombres = data['name']%}
        {%set apellidos = data['lastname']%}
        {%set usuarios = data['userid']%}
        <tr>
        <td>
            {{ nombres }} {{ apellidos }}
        </td>
        <td>
            {{ usuarios }}
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
