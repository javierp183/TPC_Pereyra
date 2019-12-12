{%for q, b in context.4.select_data.items()%}
{%set names = b['name']%}
{%set ids = b['idmedic']%}

{{ ids }}

{%endfor%}


{{ context.4.select_data.items() }}