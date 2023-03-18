Buenas! Es este TXT les voy a enseñar como ejecutar el script.
Utilice Pycharm para el desarrollo del script.
En requirements.txt estan las herramientas necesarias para ejecutar. Primero ingresar a ese txt e instalar cada paquete.
Una vez que este instalado debemos configurar las ejecuciones. Estas serian 3, las negativas, positivas y fail.
Para confuguarlas hacer click en RUN(arriba a la izquiera, al lado de Tools, ahi EDIT Configuration, y le damos a add new configuration.
Negative: El nombre debe ser negative login y en additional arguments poner: -m negative --html=reports/negativeReport.html
Positive: El nombre debe ser positive login y en additional arguments poner: -m positive --html=reports/positiveReport.html
Fail:El nombre debe ser fail login y en additional arguments poner: -m fail --html=reports/failReport.html
Y ahi ya se podria ejecutar cada testeo!
Los reportes se encuentran en la carpeta reports, y el script se ejecuta tanto en Chrome, como en Brave.
No necesitan descargar los drivers de cada browser, lo hace automaticamente el script.



