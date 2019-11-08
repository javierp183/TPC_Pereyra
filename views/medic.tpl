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

<p class="center">Medic Agenda</p>

<table id="personal">
    <tr>
      <th>Medic Name:</th>
      <th>Lastname:</td>
      <th>Medic ID:</th>
      <th>Speciality</th>
    </tr>
    <tr>
      <td>{{ context.medic.name }}</td>
      <td>{{ context.medic.lastname }}</td>
      <td>{{ context.medic.medicid }}</td>
      <td>{{ context.medic.speciality }}</td>
    </tr>
  </table>
  
  <table id="personal">
    <tr>
      <th>Patient</th>
      <th>time</th>
      <th>day and month date</th>
      <th>Disable assignation</th>
    </tr>

    <form method="POST">
    {%for i in context.patients.name%}
    
    <tr>
        {% set item_1 = context.patients.name[loop.index-1] %}
        {% set item_2 = context.patients.lastname[loop.index-1] %}
        {% set item_3 = context.patients.time[loop.index-1] %}
        {% set item_4 = context.patients.daymonth[loop.index-1] %}
      <td>{{ item_1 }} {{ item_2 }}</td>
      <td>{{ item_3 }}</td>
      <td>{{ item_4 }}</td>
      <td><input type="checkbox" name="estado">Use this button to disable patient assignation<input type="submit"></td>
      
    </tr>
    {%endfor%}

    

  </form>

</table>


{% include "foot.tpl" %}