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

<p class="center">Assign patient to medic</p>




<form>
  <table id="personal">
      
            <tr>
              <th>DNI</th>
              <th>Name</th>
              <th>Lastname</th>
              <th>Speciality</th>
              <th>Shift/Time</th>
            </tr> 
            
            <tr>
                {%for i in context.0.patient_data%}
              <td>
                  
                <input type="text" name="dni" value={{ i.dni }}>
                 
              </td>

              <td>
                  
                <input type="text" name="name" value={{ i.name }}>
                  
              </td>

              <td>
                  
                <input type="text" name="lastname" value={{ i.lastname }}>
                  
              </td>
              
              
              <td>
                <select name="spec_selected">
                    {%for i in context.2.spec_data%}
                    <option value="{{ i.medic }}">{{ i. name }}</option>
                    {%endfor%}
                </select>
                </td>

              <td>
                <select name="time">
                  <option>10</option>
                  <option>11</option>
                  <option>12</option>
                </select>
              </td>
              
            </tr>
            {%endfor%}
      </table>
      <button>Submit changes</button>

     
  
    </form>
    



    


{% include "foot.tpl" %}