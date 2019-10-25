<!DOCTYPE html>
<html>
<body>

<h3>Choose user type:</h3>
<h4>Medic, Patient or User of the App</h4><br>

<table>
    <tr>
        <td>Medic: <input type="checkbox" value="medic"></td>
        <td>Patient: <input type="checkbox" value="patient"></td>
        <td>User: <input type="checkbox" value="user"></td>
    </tr>

</table>

<form>
  First name:<br>
  <input type="text" name="name">
  <br>
  Last name:<br>
  <input type="text" name="lastname">
  <br>
  Medic ID<br>
  <input type="number" name="medicid">
  <li>Only Medic's</li>
  <br>
  Speciality:<br>
  <input type="text" name="speciality">
  <li>Only Medic's</li>
  <br>
  Userid<br>
  <input type="text" name="userid">
  <br>
  <input type="submit" value="Submit">
</form> 

</body>
</html>
