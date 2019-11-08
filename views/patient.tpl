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




<form method="POST"> 
  <table id="personal">
      
            <tr>
              <th>DNI ( Name and Lastname ) </th>
              <th>Speciality</th>
              <th>Shift/Time</th>
              <th>Day</th>
              <th>Month</th>
              <th>Overwrite ( yes or no )</th>
            </tr> 
            
            <tr>
                
              <td>
                
                <select name="userdbid">
                {%for i in context.0.patient_data%}
                <option value="{{i.id}}">{{ i.dni }} - {{ i.name }} {{ i.lastname }}</option>
                {%endfor%}
            
              </select>       
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
                  <option value="1">January</option>
                  <option value="2">February</option>
                  <option value="3">March</option>
                  <option value="4">April</option>
                  <option value="5">May</option>
                  <option value="6">June</option>
                  <option value="7">July</option>
                  <option value="8">August</option>
                  <option value="9">September</option>
                  <option value="10">October</option>
                  <option value="11">November</option>
                  <option value="12">December</option>
                </select>
              </td>

              <td>
                  <input type="checkbox" value=1>Use checkbox
              </td>
            </tr>

            
      </table>
      <button>Submit changes</button>

     
  
    </form>


{% include "foot.tpl" %}