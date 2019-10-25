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

<p class="center">Users currently registered</p>


<h3></h3>

{%for i in context.data%}
<table id="personal">
        <tr>
          <th>Name</th>
          <th>Lastname</th>
          <th>UserID</th>
          <th>password</th>
          <th>rol</th>
        </tr>
        <tr>
          <td>{{ i.name }}</td>
          <td>{{ i.lastname }}</td>
          <td>{{ i.userid }}</td>
          <td>{{ i.password }}</td>
          <td>{{ i.rol }}</td>
        </tr>
      </table>
{%endfor%}



{% include "foot.tpl" %}