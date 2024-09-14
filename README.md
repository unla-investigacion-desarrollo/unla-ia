# Configuración del Entorno para el Proyecto
Sigue estos pasos para configurar el entorno y preparar el proyecto:

# 1.Crear un Entorno Virtual
Abre la terminal y navega a la raíz del proyecto. Ejecuta el siguiente comando para crear un entorno virtual:
python -m venv .venv

# 2.Activar el Entorno Virtual
Activa el entorno virtual con el siguiente comando:
En Windows PowerShell:
.\.venv\Scripts\Activate
En Windows Command Prompt:
.venv\Scripts\activate.bat

# 3.Instalar Pandas
Con el entorno virtual activado, instala Pandas usando pip:
pip install pandas

# 4.Crear y Configurar el Archivo .gitignore
Crea un archivo llamado .gitignore en la raíz del proyecto con el siguiente contenido para ignorar la carpeta .venv:
.venv/

# 5.Agregar y Confirmar Cambios en Git
Agrega el archivo .gitignore al repositorio y confirma los cambios:
git add .gitignore
git commit -m "Añadido .gitignore para excluir la carpeta .venv"

# 6.Verificar la Instalación
Verifica que Pandas esté instalado correctamente con:
pip show pandas

Asegúrate de tener Python instalado y, si es necesario, Pandas de forma global para otros proyectos.

Para una guía adicional sobre exploración de datos, consulta este [enlace a Kaggle](https://www.kaggle.com/code/dansbecker/basic-data-exploration).

[Introducción a ML](https://docs.google.com/document/d/1Ie-IRaUuVi8KXPXWfcmDVh1BT5q7Igm2/edit?rtpof=true#heading=h.gjdgxs)

