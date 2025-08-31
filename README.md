# 👥 User-Crud-Cli
<p align="center">
  <img src="assets/title.png" alt="logo" title="img of the logo" height="500px" width="500px" />
</p>

## ⚡ Sobre el proyecto
Es una aplicación de línea de comandos (CLI) creada para practicar y fortalecer mis habilidades como **backend developer**.
El proyecto está desarrollado en **Python** y utiliza librerías como:

- **pymongo**: para conectarse a la base de datos MongoDB.

- **pydantic**: para validar y serializar los datos de entrada.

- **colorama**: para agregar estilo y color a los mensajes en la terminal.
## 💻 Operaciones 
### 📖 Listar usuarios
Muestra a todos los usuarios que se encuentran almacenados en la base de datos.

<img src="assets/lista.gif" alt="logo" title="img of the logo" height="800px" width="800px"/>

### 🔍 Buscar un usuario por 'username'
Te permiten encontrar un usuario especifico usando su **username**.

<img src="assets/buscar.gif" alt="logo" title="img of the logo" height="800px" width="800px"/>

### 📥 Agregar un nuevo usuario
Permite ingresar un nuevo usuario a la base de datos cargando todos los datos personales del mismo.

<img src="assets/ingresar.gif" alt="logo" title="img of the logo" height="800px" width="800px"/>

### 📝 Actualizar un usuario por 'username'
Permite actualizar los datos de un usuario especifico buscandolo por el **username**

<img src="assets/actualizar.gif" alt="logo" title="img of the logo" height="800px" width="800px"/>

### 🗑️ Eliminar un usuario por 'username'
Permite Eliminar todos los datos de un usuario buscandolo por el **username**

<img src="assets/eliminar.gif" alt="logo" title="img of the logo" height="800px" width="800px"/>

## 🛠️ Tecnologias utilizadas
![Python](https://img.shields.io/badge/python-336fa0?style=for-the-badge&logo=python&logoColor=336fa0&labelColor=white)
![MongoDB](https://img.shields.io/badge/mongodb-darkgreen?style=for-the-badge&logo=mongodb&logoColor=darkgreen&labelColor=white)

## 📖 Setup

Este proyecto utiliza variables de entorno para manejar información sensible (como la conexión a la base de datos).

1. Copiá el archivo `.env.sample` y renómbralo a `.env`.
2. Completá las variables con tus valores correspondientes
```bash
MONGO_HOST=your-host
MONGO_PORT=your-port
MONGO_USER=your-username
MONGO_PASS=your-password
MONGO_AUTH_MECHANISM=your-auth-mechanism
```
