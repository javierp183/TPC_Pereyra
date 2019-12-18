<!DOCTYPE html>
<html>
  <head>
      <title>TP3 UTN</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
  </head>
  <body>
      <link rel="stylesheet" href="/static/css/style.css">
      <link rel="stylesheet" href="/static/css/prism.css">
      <link rel="stylesheet" href="/static/css/chosen.css">

      <table class="table table-dark">
          <thead>
            <tr>
              <th>
                Nombre y Apellido del Operador
              </th>
              <th>
                Usuario 
              </th>
              <th>
                Operador
              </th>
            </tr>
            </thead>
            <tbody>
              <tr>
                <td>
                    {{ context.6.operator.name }} {{ context.6.operator.lastname }} 
                </td>
                <td>
                    {{ context.6.operator.userid }} 
                </td>
                <td>
                    <img src="/static/img/{{ context.6.operator.userid }}.jpg"  height="60" width="60">
        
                </td>
              </tr>
            </tbody>
        </table>
        
        <table>
    <form method="POST">  
      <button type="submit" name="volver" value="volver">Volver a pagina anterior</a></button>

      <div class="container">         
          <table class="table table-hover">
            <thead>
              <tr>
                <th>Elegir medico y especialidad</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>
                    <form method="POST">
                    <select class="chosen-select" tabindex="5" name="medic">
                    {%for q, b in context.4.select_data.items()%}
                    {%set names = b['name']%}
                    {%set ids = b['idmedic']%}
                   <optgroup label="{{ q }}">
                      {%for id in ids%}
                      <option value="{{ id }}-{{ q }}" {% if ((context.7.ingreso1 == id | string) and ( q == context.7.ingreso0 )) %} selected="selected" {%endif%}>{{ names[loop.index0] }} : {{ q }}</option>
                        {%endfor%}
                      {%endfor%} 
                  </optgroup>  
                    </select>
                <button type="submit" name="medico">Ver y actualizar Fechas disponibles</button>
                    <form>
                </td>
                <td>

                    <form method="POST">

                        {%if context.8 is defined%}
                  
                            {%for x, z in context.8.items() %}
                            {%set y = x | string%}
                            {%set hr = z['hours']%}
                            {%set dias = z['days']%}
                            {%set dates = z['months']%}
                            {%if context.7.ingreso1%}

                            <table>
                              <thead>
                                <tr>
                                  <th>
                                    Ver mes disponible
                                  </th>
                                  <th>
                                    Dia y Horario disponible
                                  </th>
                                  <th>
                                    Seleccione Paciente
                                  </th>
                                  <th>
                                    Ingrese comentarios
                                  </th>
                                </tr>
                              </thead>
                              <tbody>
                                <tr>
                                  <td>
                                      <select class="chosen-select" tabindex="5" name="mes">
                                          {%for h in hr%}<option value="{{ dates[loop.index0].split('/')[0] }}" {%if context.7.ingreso2 == "Diciembre-12" | string%} selected="selected"{%endif%}>{{ dates[loop.index0] }}</option>{%endfor%}
                                    </select>
                                    <p>   </p>
                                    <p>   </p>
                                    <p>   </p>
                                    Comentarios:
                                    <input  id="Ingresar" type="submit" value="Ingresar" name="turno">
                                    <input type="text" name="comments">
                                  </td>
                                  <td>
                                      <select class="chosen-select" tabindex="5" name="dias">
                                          {%for d in dias[context.7.ingreso2] %}  <option> {{ d }} </option> {%endfor%}
                                        </select>

                                  </td>
                                  <td>
                                      <select class="chosen-select" tabindex="5" name="patient">
                                          {%for i in context.0.patient_data%}
                                        <option>{{ i.name }} {{ i.lastname }} - {{ i.dni }}</option>
                                          {%endfor%}
                                        </select>

                                        

                                            
                                            {%endif%}
                                            {%endfor%}
                                        

                                  </td>


                                </tr>
                              
            </tbody>
          </table>
        </div>


         




                
                  <script src="/static/js/jquery-3.2.1.min.js" type="text/javascript"></script>
                  <script src="/static/js/chosen.jquery.js" type="text/javascript"></script>
                  <script src="/static/js/prism.js" type="text/javascript" charset="utf-8"></script>
                  <script src="/static/js/init.js" type="text/javascript" charset="utf-8"></script>
      {%endif%}