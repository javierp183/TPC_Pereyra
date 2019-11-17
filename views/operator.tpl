{% include "head.tpl" %}




<h1> Medical assignation </h1>



<body>
  <form method="POST">

      <em>Choose Speciality</em>
          <select class="chosen-select" tabindex="5" name="medic">
              {%for i in context.4.select_data.items()%}
            <optgroup label="{{ i.0 }}">
                {%for j in i%} <option  value="{%for id in j.idmedic%}{{ id }}{%endfor%}"> {%for n in j.name%}{{ n }} </option> {%endfor%} {%endfor%}
            </optgroup>
              {%endfor%}
          </select>

      <em>Choose Free time</em>
        <select class="chosen-select" tabindex="5" name="daytimehour">
            {%for k, v in context.5.hourmedic.items()%}
            {%set time = v['hours'] %}
            {%set date = v['dates'] %}

             <optgroup label="{{ k }}">     
                {%for t in time%} <option value"{{ t }}"> Hour: {{ t }} Date: {{ date[loop.index0] }} {%endfor%} </option>  
          </optgroup>
          {%endfor%}
        </select>
        
      <em>Choose Patient</em>
      <select class="chosen-select" tabindex="5" name="patient">
        {%for i in context.0.patient_data%}
        <option>{{ i.name }} {{ i.lastname }} - {{ i.dni }}</option>
        {%endfor%}

        
      </select>

  <input type="submit" value="Submit">

  </form>

  

  <script src="/static/js/jquery-3.2.1.min.js" type="text/javascript"></script>
  <script src="/static/js/chosen.jquery.js" type="text/javascript"></script>
  <script src="/static/js/prism.js" type="text/javascript" charset="utf-8"></script>
  <script src="/static/js/init.js" type="text/javascript" charset="utf-8"></script>


  {% include "foot.tpl" %}