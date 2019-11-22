<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: black;
}

* {
  box-sizing: border-box;
}

/* Add padding to containers */
.container {
  padding: 16px;
  background-color: white;
}

/* Full-width input fields */
input[type=text], input[type=password] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for the submit button */
.registerbtn {
  background-color: #4CAF50;
  color: white;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}

.registerbtn:hover {
  opacity: 1;
}

/* Add a blue text color to links */
a {
  color: dodgerblue;
}

/* Set a grey background color and center the text of the "sign in" section */
.signin {
  background-color: #f1f1f1;
  text-align: center;
}
</style>
</head>
<body>

<form method="POST">
  <div class="container">
    <h1>Use una de las siguientes opciones para borrar un usuario</h1>
    <p>Por favor complete los campos</p>
    <hr>

    <label for="dni"><b>DNI</b></label>
    <input type="text" placeholder="Enter DNI - ONLY FOR PATIENT -" name="dni">

    <label for="medicid"><b>Numero de Medico</b></label>
    <input type="text" placeholder="Enter Medic ID - ONLY FOR MEDIC registration -" name="medicid">

    <label for="userid"><b>USER ID</b></label>
    <input type="text" placeholder="Ingrese USERID ( SOLO PARA OPERADORES )" name="userid">

    <p>Seleccione el tipo de cuenta que desea eliminar: </p>
    <label for="medic"><b>Medico?</b></label>
    <input type="checkbox" placeholder="Medic" name="medic" value=1>
    <br>
    <label for="admin"><b>Admin Operador?</b></label>
    <input type="checkbox" placeholder="Operator" name="admin" value=1>
    <br>
    <label for="patient"><b>Ingreso de Paciente?</b></label>
    <input type="checkbox" placeholder="Patient" name="patient" value=1>
    <br>

    <button type="submit" class="registerbtn">Registrar</button>
  </div>

</form>

</body>
</html>
