<html>
  <head>

      <title>TPC - UTN - Javier Pereyra</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
      <link rel="stylesheet" href="/static/css/style.css">
<link rel="stylesheet" href="/static/css/prism.css">
<link rel="stylesheet" href="/static/css/chosen.css">

  </head>
  <body>



<form method="POST">
    <button type="submit" name="medico" value="medico">Ingreso de medico</button>
    <button type="submit" name="operador" value="operador">Ingreso de operador</button>
    <button type="submit" name="paciente" value="paciente">Ingreso de paciente</button>
    <button type="submit" name="volver" value="volver">Volver atras</a></button>
  </form>
    
    Ingresar Medico:
    <form method="POST">
        Nombre: <input type="text" name="name"><br>
        Apellido: <input type="text" name="lastname"><br>
        Usuario del sistema ( USERID ): <input type="text" name="userid"><br>
        ID del Medico: <input type="text" name="medicid"><br>
        Clave para el Usuario: <input type="password" name="password"><br>
        Subir Foto? <input type="checkbox" name="foto"><br>
      Dias de trabajo <br>
    <table class="table table-dark">
        <thead>
      <th>
        Lunes
      </th>
      <th>
        Martes
      </th>
      <th>
        Miercoles
      </th>
      <th>
        Jueves
      </th>
      <th>
        Viernes
      </th>
      <th>
        Sabado
      </th>
      <th>
        Domingo
      </th>
    </thead>
    <tbody>
      <td>
          <input type="checkbox" name="lunes" value="lunes">
      </td>
      <td>
          <input type="checkbox" name="martes" value="martes">
      </td>
      <td>
          <input type="checkbox" name="miercoles" value="miercoles">
      </td>
      <td>
          <input type="checkbox" name="jueves" value="jueves">
      </td>
      <td>
          <input type="checkbox" name="viernes" value="viernes">
      </td>
      <td>
          <input type="checkbox" name="sabado" value="sabado">
      </td>
      <td>
          <input type="checkbox" name="domingo" value="domingo">
      </td>
    </tbody>
    </table>
    
    Horarios de trabajo: <br>
    <table class="table table-dark">
        <thead>
      <th>
        Primer turno
      </th>
      <th>
        Segundo turno
      </th>
      <th>
        Tercer turno
      </th>
    </thead>

      <td>
          <input type="checkbox" name="turno1" value=10>  10 AM
      </td>
      <td>
          <input type="checkbox" name="turno2" value=11>  11 AM
      </td>
      <td>
          <input type="checkbox" name="turno3" value=12>  12 AM
      </td>
    </table>
    
    Especializades: <br>
    {%for i in context.2.spec_data%}
    <input type="checkbox" name="{{ i.name }}" value="{{ i.name }}">{{ i.name }}
    {%endfor%} 
    <br>
    
    <button type="submit">Ingresar medico</button>
    
    </form>  



  </body>

</html>
