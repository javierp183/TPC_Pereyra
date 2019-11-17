{% include "head.tpl" %}

<header>
<input type="checkbox" id="btn-menu">
<label for="btn-menu"><img src="static/img/button_menu.jpg" height="30" width="30" alt=""></label>

<nav class="menu">
  <ul>
    <li><a href="https://www.infobae.com">Help</a></li>
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
      <td>{{ context.medic.speciality }}</td
    </tr>
  </table>


  
  <table id="personal">
    <tr>
      <th>Patient</th>
      <th>time</th>
      <th>day and month date</th>
      <th>Disable assignation</th>
      <th>Message ( select one )</th>
      <th>Assign new Day and Month</th>
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
      <td><input type="checkbox" name="estado"><h6>Disable assignation</h6><input type="submit"></td>
      <td><input type="text" name="message">Message<input type="radio"><input type="submit"></td>
      <td>

        <select>
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

        <select>
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

        <input type="submit">
      </td>
      
    </tr>
    {%endfor%}
  </form>
</table>

<h5>Total Hours assigned for you today: 200hssss</h5>
<h6>Remember: Select one of this user and send message</h6>


{% include "foot.tpl" %}