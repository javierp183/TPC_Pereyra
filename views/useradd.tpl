<!DOCTYPE html>
<html>
<body>

<h3>Choose user type:</h3>
<h4>Medic, Patient or User of the App</h4><br>


<form method="POST">

  
  First name:<br>
  <input type="text" name="name">
  <br>
  Last name:<br>
  <input type="text" name="lastname">
  <br>
  Medic ID<br>
  <input type="text" name="medicid">
  <li>Only Medic's</li>
  <br>
  Speciality:<br>
  <input type="text" name="speciality">
  <li>Only Medic's</li>
  <br>
  Userid<br>
  <input type="text" name="userid">
  <br>
  Password
  <input type="password" name="password">
  <br>
  Medic
  <input type="checkbox" name="medic" value=1>
  <br>
  Admin
  <input type="checkbox" name="admin" value=1>
  <br>
  Patient
  <input type="checkbox" name="patient" value=1>
  <br>
  <input type="submit" value="Submit">

</form> 

</body>
</html>
