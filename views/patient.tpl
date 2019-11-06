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
              <th>Day</th>
              <th>Month</th>
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

              <td>
                <select name="day">
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                  <option>6</option>
                  <option>7</option>
                  <option>8</option>
                  <option>9</option>
                  <option>10</option>
                  <option>11</option>
                  <option>12</option>
                  <option>13</option>
                  <option>14</option>
                  <option>15</option>
                  <option>16</option>
                  <option>17</option>
                  <option>18</option>
                  <option>19</option>
                  <option>20</option>
                  <option>21</option>
                  <option>22</option>
                  <option>23</option>
                  <option>24</option>
                  <option>25</option>
                  <option>26</option>
                  <option>27</option>
                  <option>28</option>
                  <option>29</option>
                  <option>30</option>
                  <option>31</option>
                </select>
              </td>

              <td>
                <select name="month">
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                  <option>6</option>
                  <option>7</option>
                  <option>8</option>
                  <option>9</option>
                  <option>10</option>
                  <option>11</option>
                  <option>12</option>
                </select>
              
            </tr>
            {%endfor%}
      </table>
      <button>Submit changes</button>

     
  
    </form>
    



    


{% include "foot.tpl" %}