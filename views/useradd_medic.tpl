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
    Usuario del sistema ( USERID ):: <input type="text" name="userid"><br>
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

Especializades: <br>
{%for i in context.2.spec_data%}
<input type="checkbox" name="{{ i.name }}" value="{{ i.name }}">{{ i.name }}
{%endfor%} 
<br>

<button type="submit">Ingresar medico</button>

</form>

