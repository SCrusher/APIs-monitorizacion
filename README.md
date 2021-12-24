# APIs-para-monitorizacion-de-servicios-web
API's desarrollados con Python, Flask y PostgreSQL

La finalidad del proyecto es la monitorización y visualización de los servicios entregados por ciertos sistemas y servidores, la idea principal es tener el control del status de las páginas/aplicaciones web y parámetros del PC (disco, ram, cpu, version del SO[Linux]). De ésta manera el usuario podrá ver si todo esta funcionando correctamente mediante las comprobaciones que puede realizar cada cierto tiempo, registros que serán almacenados en la base de datos.

Para ejecutar el proyecto, primero debemos considerar tener instalado Flask, Python3 y crear una cuenta para PostgreSQL.

Una vez instalados los requerimientos, podemos ejecutar app.py que será nuestra API emisora, con ella podemos preguntar por cada prueba que nos interese (disco, ram, version, status, cpu) mediante sus respectivas rutas en nuestro navegador preferido. (localhost:5000)

Luego, podemos ejecutar receptora.py que será nuestra API receptora, es decir, ésta trabajará mediante un CRUD a las app que queramos organizar.

Por último mediante la ruta localhost:4000/mostrar_logs se obtendran todos los registros realizados, incluyendo el nombre de la app que ingresamos a la BD.
