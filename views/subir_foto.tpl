Subir foto: <br>
<form action="/upload/{{ context.ops }}/{{ context.newops}}" method="post" enctype="multipart/form-data">
  Categoria:     <input type="text" name="category" />
  Seleccionar foto: <input type="file" name="upload"/>
  <input type="submit" value="Subir Archivo" />
</form>