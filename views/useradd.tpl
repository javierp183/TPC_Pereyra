
<form method="POST">
<button type="submit" name="medico" value="medico">Ingreso de medico</button>
<button type="submit" name="operador" value="operador">Ingreso de operador</button>
<button type="submit" name="paciente" value="paciente">Ingreso de paciente</button>
</form>


Ingresar Medico:
<form method="POST">
    Nombre: <input type="text" name="name"><br>
    Apellido: <input type="text" name="lastname"><br>
    Registre Usuario: <input type="text" name="userid"><br>
    Especializacion: <input type="text" name="specialization"><br>
    ID del Medico: <input type="text" name="medicid"><br>
    Clave para el Usuario: <input type="password" name="password"><br>
  Dias de trabajo <br>
<table>
  <tr>
    Lunes
  </tr>
  <tr>
    Martes
  </tr>
  <tr>
    Miercoles
  </tr>
  <tr>
    Jueves
  </tr>
  <tr>
    Viernes
  </tr>
  <tr>
    Sabado
  </tr>
  <tr>
    Domingo
  </tr>
  <tr>
      Es medico?
  </tr>
  <th>
      <input type="checkbox" name="lunes" value="lunes">
  </th>
  <th>
      <input type="checkbox" name="martes" value="martes">
  </th>
  <th>
      <input type="checkbox" name="miercoles" value="miercoles">
  </th>
  <th>
      <input type="checkbox" name="jueves" value="jueves">
  </th>
  <th>
      <input type="checkbox" name="viernes" value="viernes">
  </th>
  <th>
      <input type="checkbox" name="sabado" value="sabado">
  </th>
  <th>
      <input type="checkbox" name="domingo" value="domingo">
  </th>
  <th>
      <input type="checkbox" name="medico" value=1>
  </th>
</table>

Horarios de trabajo: <br>
<table>
  <tr>
    Primer turno
  </tr>
  <tr>
    Segundo turno
  </tr>
  <tr>
    Tercer turno
  </tr>
  <th>
      <input type="checkbox" name="turno1" value=10>  10 AM
  </th>
  <th>
      <input type="checkbox" name="turno2" value=11>  11 AM
  </th>
  <th>
      <input type="checkbox" name="turno3" value=12>  12 AM
  </th>

</table>

<button type="submit">Ingresar medico</button>

</form>