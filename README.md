# Entrega1-ContinoEmiliano

# SUPERUSUARIO ADMIN: emi
# Contraseña: emi12345

*Pasos para bajar y correr el proyecto:

- Bajar el proyecto desde un link de Git Hub.
- Clonar el repositorio con : git clone ("link").
- Una vez abierto verificamos con que paquetes trabaja, dentro de "requeriments.txt ". 
  Abrir una terminal y los instalamos con: pip install -r requirements.txt 
- Ejecutar python manage.py migrate, para que se cree la basse de datos.
- Ejecutar python manage.py runserver para correr el proyecto.
- Ingresar a la ruta que nos brinda la terminal.

*Proyecto pagina

- La pagina principal nos muestra:
  Un panel de navegacion que contiene Inicio, Ver Chefs, Crear Chef, iniciar sesion, registrarse, algunas imagenes, texto y un Acerca de mi.
  
- Inicio: se muestra la pagina principal, en esta vista encontraras:
  Imagen de bienvenida y un texto haciendo referencia un poco de que va la pagina.
  Imagenes de platos gourmet, en donde al hacer click se agrandan y se mustra su receta.

- Registrarse: Nos pedira cierta informacion para que podamos loguearnos luego.

- Iniciar Sesion: Una vez registrados procedemos a loguearnos.

- Crear Chef : Redirecciona a la vista donde podremos crear un usuario chef.
  Nos va a solicitar lo siguiente, siempre y cuando estemos registrados:
  
  Nombre: "Guarda el nombre en la base de datos"
  Apellido: "Guarda el apellido en la base de datos"
  edad:"Guarda la edad en la base de datos"
  Receta preferida: "Guarda el  nombre de la receta en la base de datos"
  Descripcion de la Receta: "guarda los detalles de como es el procedimiento de la receta en la base de datos "
  Imagen receta : "Guarda la imagen de esa receta "

  Boton de crear, para efectivamente guardar toda la informacion.

- Ver Chef : Redirecciona a la vista donde podremos ver el listado de los usuarios chef, si es que los      hay.

   Si los hubiese nos va a mostrar el listado de cada usuario, en donde podremos editar o eliminar el registro.


  En "Editar", realiza modificaciones a los datos del registro de ese usuario.
  En "Eliminar", en donde podras eliminar ese usuario. 

  Tambien nos permitira en ese listado buscar el nombre de quien creo esa receta.

- Perfil del usuario:
  Nos muestra toda la informacion del usuario.
  El Nombre y apellido, su Email con su Link de Pagina.
  Detalle de que "Contanos tu experiencia", para que se explaye en escribir lo que desee el usuario.
  Y poder cargar la foto de un avatar.

  Se podrian editar todos estos datos, como asi tambien cambiar Contraseña.
 
- Acerca de mi:
  Cuento brevemente porque se realizo este proyecto y algun detalle personal.

    
- Contino Emiliano - 



