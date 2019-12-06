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

Ingrese el ID del medico:
<form method="POST">
  MEDICID: <input type="text" name="medicid"><br>
  <button type="submit" name="buscar" value="buscar">Buscar medico</button>
  <button type="submit" name="volver" value="volver">Volver atras</a></button>
</form>



{%if context.patients is defined%}
<table>
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
        <td>{{ item_4.split("/")[0].split("-")[0] }} - {{ item_4.split("/")[1].split("-")[1] }} </td>
        <td>{{ item_6 }}</td>
        <td>{{ item_7 }}</td>
        <td>
        </tr>
        {%endfor%}
    </tbody>
  </table>
{%endif%}


</body>
</html>