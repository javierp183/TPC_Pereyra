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

{%for i in context.0.patient_data%}
{{ i }}
{%endfor%}


<form>
  <table id="personal">
      
            <tr>
              <th>DNI</th>
              <th>Name</th>
              <th>Lastname</th>
              <th>SecureID</th>
              <th>Email</th>
              <th>Medic</th>
            </tr> 
            
            <tr>
                
              <td>
                  {%for i in context.0.patient_data%}
                <input type="text" name="dni" value={{ i.dni }}>
                {%endfor%}
              </td>
              <td>
                  {%for i in context.0.patient_data%}
                <input type="text" name="name" value={{ i.name }}>
                {%endfor%}
              </td>
              <td>
                  {%for i in context.0.patient_data%}
                <input type="text" name="lastname" value={{ i.lastname }}>
                {%endfor%}
              </td>
              <td>
                  {%for i in context.0.patient_data%}
                  <input type="text" name="secureid" value={{ i. secureid }}>
                  {%endfor%}
                </td>
              <td>
                  {%for i in context.0.patient_data%}
                  <input type="text" name="email" value={{ i.email }}>
                  {%endfor%}
              </td>
              
              <td>
                  {%for i in context.0.patient_data%}
                  <select>
                  
                  
                  
                  {%if i.medic%} <option selected="{{ i.medic }}"> {{ i.medic }} </option>{%endif%}

                  {%for j in context.1.medic_data%}
                  <option>{{ j.name }}</option>
                  {%endfor%}
                  
                 
                  
                  
                  </select>
                {%endfor%}
              </td>
            </tr>
            
      </table>
      <button>Submit changes</button>

     
  
    </form>
    



    


{% include "foot.tpl" %}