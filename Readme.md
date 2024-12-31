# Descripción del proyecto
El objetivo de este proyecto es desarrollar una página web que muestre la varianza de cada mes de un año en especifico de la UF. Una vez obtenida esta información, el software debe ser capaz de aplicar tres filtros principales:

1. Mostrar los meses en los que la varianza aumentó, ordenados de menor a mayor.
2. Mostrar los meses en los que la varianza disminuyó, ordenados de mayor a menor.
3. Mostrar los meses en los que la varianza no cambió, ordenados alfabéticamente.

Las técnologias utilizadas fueron python con Flask para la parte del backend y javascript con react, ademas el uso de pandas para el manejo de información, requests para hacer la petición de la api de donde se obtenia la información, y flask cors para poder lograr la comunicación entre el frontend y el backend sin problema de reestricciones, por otra parte, para react no se utilizo ninguna libreria en especifico, solamente lo otorgado de un proyecto inicial junto a un css para que se pueda ver de manera más amigable para el usuario

# Modo de uso
La página cuenta con un campo de entrada (input) donde solo se pueden ingresar números. El número debe estar en el rango de 1977 a 2024 para consultar los datos disponibles en la API. Después de presionar el botón "Enviar", se mostrará toda la información obtenida. Al final de la página hay una sección titulada "Información Adicional", donde se indican el peor día y el mejor día del año según el valor de la UF.

# Requisitos
Para ejecutar este programa correctamente, es necesario utilizar el puerto predeterminado de React (5173), ya que el CORS del backend está configurado específicamente para ese puerto.

<h3>Configuración del Backend</h3>

Instalar las librerias python y poder ejecutar el backend:

```
pip install -r requirements.txt
python index.py
```
<h3>Configuración del Frontend</h3>
Instalar los recursos necesarios para ejecutar el front con react:

```
npm install
npm run dev
```

# Estructura del proyecto
El **backend** está organizado de la siguiente manera:

- **`index.py`**  
  Archivo principal que inicia la aplicación y realiza las llamadas iniciales a las funciones necesarias para configurar el sistema, como la función `init`.  
  - **Función `init`:** Se encarga de registrar todas las rutas creadas.

- **`utils/`**  
  Contiene funciones auxiliares y utilidades, como:
  - Respuestas predeterminadas del programa.
  - Llamadas a la API de UF.

- **`services/`**  
  Contiene la lógica principal del programa, donde se maneja y procesa toda la información necesaria para las funcionalidades.

- **`routes/`**  
  Incluye los archivos que representan las conexiones al backend.  
  - **`ufApiResRoutes`:** Maneja las rutas relacionadas con las llamadas a la API, devolviendo información procesada por los servicios o reordenada según sea necesario.

El **frontend** está organizado de la siguiente manera:

- **`main.jsx`**  
  Archivo principal que carga el componente inicial y pone en marcha la página.

- **`components/`**  
  Contiene los componentes principales de la aplicación.  
  - **`App`:** Componente que representa toda la página. Es responsable de enviar la información necesaria al backend y cuenta con un archivo CSS asociado para definir los estilos.

- **`api/`**  
  Contiene el archivo encargado de realizar las llamadas al backend y recibir la información relacionada con la UF.

Esta estructura permite mantener un orden lógico en el proyecto, facilitando la escalabilidad y el mantenimiento.

# Datos personales
- Vicente Gabriel Córdova Castillo
- vgcordovacastillo@gmail.com
- https://www.linkedin.com/in/vicente-cordova/