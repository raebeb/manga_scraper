![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  
[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/raebeb)
# MANGA DOWNLOADER 🚣📄🗺
Quería leer vinland saga en mi Kindle, pero no encontraba donde descargarlo así que me vi en la obligación de hacer un script que descargue las imágenes para luego pasarlas a formato MOBI  
Luego de descargar los capítulos que quería leer me di cuenta que podría hacer que el script funcionara para cualquier manga, así fue que nació esto ฅ^•ﻌ•^ฅ  
Las imágenes son descargadas de https://www.mangatigre.net/



## Comenzando 🚀
_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

-   Python 3.x

---

## Instalación 🔧

### 1. Clonar el repositorio
```
git clone git@github.com:raebeb/manga_scraper.git
```
ó
```
git clone https://github.com/raebeb/manga_scraper.git
```
>En caso de no tener git instalado (y no tener la intención ni la necesidad de hacerlo) se puede descargar el repositorio como ZIP  
![image](https://user-images.githubusercontent.com/27713965/233815307-a77df529-2633-4791-8229-b30ca9db8b7b.png)


### 2. Descarga e instala Python 

Sigue las instrucciones de https://www.python.org/downloads/

### 3. Instalar PIP

En este sitio están detalladas las instrucciones para descargar e instalar pip según tu sistema operativo https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/


---

### 2. Ejecucion
## Instalar librerias necesarias

Para esto es necesario en la raíz del proyecto ejecutar el siguiente comando  
```pip install -r requirements.txt```
> en caso de que el comando anterior falle probar con ```pip3 install -r requirements.txt```

Una vez que se hayan instalado todas las dependencias podemos seguir con el siguiente paso  

## Descargar los mangas
A continuación se detallarán ejemplos de los distintos modos para descargar mangas

### 1. Conoce los argumetos que puedes utilizar
Ejecuta este comando para ver las diferentes opciones para descargar mangas

```bash 
$ python3 scraper.py --help
```
output: 
```bash 
    
usage: scraper.py [-h] [-i INITIAL_CHAPTER] [-f FINAL_CHAPTER] [-l] [-s SINGLE_CHAPTER] manga_title

  Download manga from Manga Tigre.

  positional arguments:
    manga_title           Title of the manga

  options:
    -h, --help            show this help message and exit
    -i INITIAL_CHAPTER, --initial_chapter INITIAL_CHAPTER
                          Initial chapter to download
    -f FINAL_CHAPTER, --final_chapter FINAL_CHAPTER
                          Final chapter to download
    -l, --download_last_chapter
                          Download the last chapter
    -s SINGLE_CHAPTER, --single_chapter SINGLE_CHAPTER
                          Download a single chapter
```

### 2 Ejemplos de uso
```bash
# Por defecto sin bandera, te intentará descargar todos los capítulos
python3 scraper.py 'blue lock' # es similar a  --initial_chapter 1 --final_chapter last

# Descargar solo los capítulos que se encuentren entre los valores especificados (incluyéndolos)
python3 scraper.py 'blue lock' --initial_chapter 4 --final_chapter 21
python3 scraper.py 'blue lock' -i 4 -f 21

# Descargar solo un capítulo del manga especificado, en el ejemplo sería el capítulo número 3
python3 scraper.py 'one piece' --single_chapter 3
python3 scraper.py 'one piece' -s 3

# Descargar desde un capítulo x hasta el último
python3 scraper.py 'Trigun' --initial_chapter 4 --final_chapter last
python3 scraper.py 'Trigun' -i 4 -f last

# Descargar solo el último capítulo de un manga
python3 scraper.py 'Vinland Saga' --download_last_chapter
python3 scraper.py 'Vinland Saga' -l 

```


## Significado de las opciones
* `manga_title`: Nombre del manga, es obligatorio en todos los comandos, el nombre de los mangas debe ir **SIEMPRE** con comillas.
* `-i`, `--initial_chapter`: Capítulo inicial del manga, indica desde que capitulo se comenzara a descargar, es de caracter opcional, pero si se usa se debe usar la opción `--final_chapter`.
* `-f`, `--final_chapter`: Capítulo final del manga, indica hasta que capitulo incluyéndolo se descargará.
* `-s`, `--single_chapter`: Descargará solo el capítulo indicado.
* `-l`, `--download_last_chapter`: Se utiliza para descargar solo el último capítulo.


# Después qué?


Los mangas quedarán guardados en la raíz del proyecto en una carpeta llamada Mangas  
![image](https://user-images.githubusercontent.com/27713965/234107481-e124da06-b7a9-4bed-ac45-f5f7a10ca25a.png)




Cada capítulo queda guardado en una carpeta independiente con el número correspondiente  
![image](https://user-images.githubusercontent.com/27713965/234107570-7b08fc14-fe74-4293-b981-c255a87dfff6.png)


# Pasar imagenes a EPUB
## Opcion 1
Para pasar los mangas recien descargados o que ya tengamos dentro de la carpeta ```/Mangas``` debemos ejecutar lo siguiente en la terminal:  
```python3 epub.py```  
  
Esto nos desplegara una lista con los mangas que ya tenemos descargados  
![image](https://github.com/raebeb/manga_scraper/assets/27713965/1fe7bba4-5fba-4af8-8d12-9c47ea21e77b)  
  
Seguido del siguiente mensaje:  
![image](https://github.com/raebeb/manga_scraper/assets/27713965/b29e7b26-e8fe-4f01-aa2a-fba19d828c72)  
aqui tenemos que ingresar cualquier de los numeros que se muestran junto al nombre del manga  
  
Una vez ingresado el numero correspondiente al manga que queremos transformar y comenzara a transformar todas las carpetas con capitulos a **un archivo epub**  
![image](https://github.com/raebeb/manga_scraper/assets/27713965/b2dd6952-4eeb-4a53-89bd-0e7f8dbb4d33)
> si, esta mal calculado el porcentaje, lo arreglare

Una vez finalizado el proceso en la raiz de nuestro proyecto nos encontraremos con una carpeta llamada ```/Epubs```, dentro de esta habran carpetas con los nobres de los managas y dentro de estas los archivos epub
```
/Epubs
    |-- /Trigun
        |-- trigun.epub
```

## Opción 2

Las carpetas quedan listas para ser importadas directamente en el software de [KindleComicConverter](https://kcc.iosphe.re/) a formato MOBI o EPUB y luego subidas a la Kindle ya sea por correo o usando [Calibre](https://calibre-ebook.com/)




***
## Construido con 🛠️
* [Python 3.8](https://www.python.org) - Lenguaje de programación


***
## Como contribuir? 📝
Este proyecto está abierto a contribuciones. Aquí hay algunas formas en las que puedes contribuir:

1. Fork del repositorio a tu cuenta de GitHub.  
2. Clona el repositorio a tu máquina local.

```bash
git clone git@github.com:tuNombreDeUsuario/manga_scraper.git
```
3. Crea una nueva rama para trabajar en la característica o corrección que desees hacer.  
```bash
git checkout -b nombre-de-tu-rama
```
4. Realiza tus cambios y haz un commit con una descripción concisa y clara de tus cambios.
5. Haz push de tu rama a tu fork en GitHub.
```
git push origin nombre-de-tu-rama
```




## Contributors ✒️
* [Francisca Osores](https://www.linkedin.com/in/francisca-osores-ortiz-152347149/) - Trabajo inicial
* [Daniel Mansilla](https://github.com/Mansilla1)  
* Ante cualquier duda o comentario escribir a fmosoresortiz@gmail.com






## Agradecimientos
* Este proyecto ha sido fuertemente inspirado por el trabajo de [Carleslc](https://github.com/Carleslc) y su repositorio https://github.com/Carleslc/InMangaKindle 
> en caso de que al usar mi script no puedas descargar algún manga te recomiendo revisar el trabajo de Carleslc, ya que la obtención de los mangas la hacemos a distintas páginas

## ⌨️ con ❤️ por [Francisca Osores](https://www.linkedin.com/in/francisca-osores-ortiz-152347149/) 👩‍💻

```
          ／＞　 フ
         | 　_　_| 
       ／` ミ＿xノ 
      /　　　　 |
     /　 ヽ　　 ﾉ
    │　　|　|　|
／￣|　　 |　|　|
(￣ヽ＿_  ヽ_)__)
＼二)
```

## Trabajos futuros:
- [ ] Elejir la ruta donde almacenar los mangas descargados
- [ ] Agregar tests
- [x] Optimizar la busqueda del ultimo capitulo
- [x] Opcion para descargar solo imagenes o transformarlas ya a MOBI
    - [ ] Opcion para seleccionar solo algunas carpetas de capitulos
