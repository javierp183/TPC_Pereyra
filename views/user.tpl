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
    <li></li>
  </ul>

</nav>
</header>



{%for i in context.0.patient_data%}

<table id="personal">
        <tr>
          <th>Name</th>
          <th>Lastname</th>
          <th>Secure ID</th>
          <th>In Agenda</th>
          <th>Patients</th>
          <th>Speciality</th>
        </tr>
        <tr>
          <td>{{ i.name }}</td>
          <td>{{ i.lastname }}</td>
          <td>{{ i.secureid }} </td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </table>
{%endfor%}





{% include "foot.tpl" %}