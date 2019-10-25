{% include "head.tpl" %}

<header>
<input type="checkbox" id="btn-menu">
<label for="btn-menu"><img src="static/img/button_menu.jpg" height="30" width="30" alt=""></label>

<nav class="menu">
  <ul>
    <li><a>Help</a></li>
    <li><a>Search</a></li>
    <li><a>Schedule</a></li>
    <li><a>Patients</a></li>
  </ul>

</nav>
</header>

<p class="center">Patients Registered</p>


{%for i in context.data%}
<table id="personal">
        <tr>
          <th>Name</th>
          <th>Lastname</th>
          <th>SecureID</th>
          <th>Email</th>
          <th>Shift</th>
          <th>Medic</th>
        </tr>
        <tr>
          <td>{{ i.name }}</td>
          <td>{{ i.lastname }}</td>
          <td>{{ i.secureid }}</td>
          <td>{{ i.email }}</td>
          <td>{{ i.turnos }}</td>
          <td>{{ i.medic }}</td>
        </tr>
      </table>
{%endfor%}




{% include "foot.tpl" %}