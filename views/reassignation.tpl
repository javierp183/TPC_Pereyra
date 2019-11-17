{% include "head.tpl" %}

<link rel="stylesheet" href="/static/css/style.css">
<link rel="stylesheet" href="/static/css/prism.css">
<link rel="stylesheet" href="/static/css/chosen.css">






<h1> Medical RE-assignation </h1>

<body>
  <form method="POST">

      <em>Choose Speciality</em>
          <select class="chosen-select" tabindex="5" name="medic">
              {%for q, b in context.4.select_data.items()%}
              {%set names = b['name'] %}
              {%set ids = b['idmedic']%}
            <optgroup label="{{ q }}">
              {%for n in names%} <option value="{{ ids[loop.index0] }}">{{ n }}</option> {%endfor%}
            </optgroup>
            {%endfor%}
          </select>

      <em>Current Assigned Schedule:</em>
        <select class="chosen-select" tabindex="5" name="daytimehour">
            {%for k, v in context.5.hourmedic.items()%}
            {%set time = v['hours'] %}
            {%set date = v['dates'] %}

          <optgroup label="{{ k }}">     
                {%for t in time%} <option value"{{ t }}"> Hour: {{ t }} Date: {{ date[loop.index0] }} {%endfor%} </option>  
          </optgroup>
          {%endfor%}
        </select>
      
      <em>Choose free time to re-assign:</em>
      <select class="chosen-select" tabindex="5" name="daytimehour">
            {%for k, v in context.5.hourmedic.items()%}
            {%set time = v['hours'] %}
            {%set date = v['dates'] %}

      <optgroup label="{{ k }}">     
                {%for t in time%} <option value"{{ t }}"> Hour: {{ t }} Date: {{ date[loop.index0] }} {%endfor%} </option>  
      </optgroup>
          {%endfor%}
      </select><br>
  Write comments:
  <input type="text" name="comments">
  <input type="submit" value="Submit">

</form>



  

  <script src="/static/js/jquery-3.2.1.min.js" type="text/javascript"></script>
  <script src="/static/js/chosen.jquery.js" type="text/javascript"></script>
  <script src="/static/js/prism.js" type="text/javascript" charset="utf-8"></script>
  <script src="/static/js/init.js" type="text/javascript" charset="utf-8"></script>


  {% include "foot.tpl" %}