# Pasos para Crear y Sincronizar un Proyecto con GitHub

## 1. Crear una cuenta en GitHub
1. Ve a [GitHub](https://github.com/).
2. Haz clic en "Sign up" (Registrarse).
3. Sigue las instrucciones para crear tu cuenta.

## 2. Crear el Repositorio en GitHub
1. Inicia sesión en tu cuenta de GitHub.
2. Haz clic en el ícono de "+" en la esquina superior derecha y selecciona "New repository" (Nuevo repositorio).
3. Dale un nombre a tu repositorio y completa los demás detalles como descripción, visibilidad, etc.
4. Haz clic en "Create repository" (Crear repositorio).

## 3. Crear el directorio usando VSCode
1. Abre Visual Studio Code.
2. Selecciona "File" (Archivo) > "Open Folder" (Abrir carpeta) y crea una nueva carpeta para tu proyecto o abre una existente.

## 4. Ejecutar los comandos de GitHub en el Directorio de Visual Studio Code
1. Abre la terminal integrada en Visual Studio Code (View > Terminal o `Ctrl+` `).
2. Navega hasta el directorio de tu proyecto usando `cd ruta/del/directorio`.
3. Inicializa un repositorio de Git local con el comando:
   ```bash
   git init
   ```
Conecta tu repositorio local con el de GitHub:
bash
Copiar código
git remote add origin https://github.com/tu-usuario/tu-repositorio.git
5. Crear un archivo clase.py en Visual Studio Code
En el directorio de tu proyecto, haz clic derecho y selecciona "New File" (Nuevo archivo).
Nombra el archivo como clase.py.
Escribe el contenido que desees en clase.py y guarda el archivo.
6. Sincronizar el contenido del punto 5 a GitHub
Agrega los archivos a tu repositorio local:
```bash
  git add .
```

Haz un commit de tus cambios:
```bash
  git commit -m "Añadir archivo clase.py"
```
Sube tus cambios al repositorio de GitHub:
```bash
  git push -u origin master
```