![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
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
El siguiente comando descarga todos los capítulos del manga especificado  
``` python3 scraper.py -n 'boruto' -i 1 -f last ```


### 2. Descargar una serie de capítulos de un manga entre x e y  
El siguiente comando descargará solo los capítulos que se encuentren entre los valores especificados (incluyéndolos), en el ejemplo descargara desde el capítulo 4 hasta el capítulo 21
``` python3 scraper.py -n 'blue lock' -i 4 -f 21 ```  
> En este comando es necesario que el valor que se especifica en el valor de la bandera -i sea menor al valor de la bandera -f, en caso contrario arrojara una excepción
> En el caso de que el capítulo especificado en la bandera -f sea mayor al último capítulo existente del manga especificado, el script descargara hasta el último capítulo existente y luego arrojara una excepción


### 3. Descargar solo un capítulo de un manga
El siguiente comando descargará solo un capítulo del manga especificado, en el ejemplo sería el capítulo número 3  
``` python3 scraper.py -n 'one piece' -s 3 ```


### 4. Descargar desde un capítulo x hasta el último
El siguiente comando descargará una serie de capítulos iniciando e incluyendo al especificado en la bandera -i hasta el último  
``` python3 scraper.py -n 'Trigun' -i 4 -f last ```


### 5. Descargar solo el último capítulo de un manga
El siguiente comando solo descargará el último capítulo existente del manga   
``` python3 scraper.py -n 'Vinland Saga' -l true ```


## Significado de banderitas
* *-n* : Nombre del manga, es obligatorio en todos los comandos, el nombre de los mangas debe ir **SIEMPRE** entre comillas
* *-i* : Initial chapter, capítulo inicial del manga, indica desde que capitulo se comenzara a descargar, es de caracter opcional, pero si se usa se debe usar la banderita -f
* *-f* : Final chapter, capítulo final del manga, indica hasta que capitulo incluyéndolo
* *-s* : single chapter, descargará solo el capítulo indicado
* *-l* : Last chapter, se utiliza para descargar solo el último capítulo, debe ir acompañado de la palabra true




Los mangas quedarán guardados en la raíz del proyecto en una carpeta llamada Mangas  
![image](https://user-images.githubusercontent.com/27713965/234107481-e124da06-b7a9-4bed-ac45-f5f7a10ca25a.png)




Cada capítulo queda guardado en una carpeta independiente con el número correspondiente  
![image](https://user-images.githubusercontent.com/27713965/234107570-7b08fc14-fe74-4293-b981-c255a87dfff6.png)




Las carpetas quedan listas para ser importadas directamente en el software de [KindleComicConverter](https://kcc.iosphe.re/) a formato MOBI o EPUB y luego subidas a la Kindle ya sea por correo o usando [Calibre](https://calibre-ebook.com/)




***
## Construido con 🛠️
* [Python 3.8](https://www.python.org) - Lenguaje de programación


***




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
- [ ] Opcion para descargar solo imagenes o transformarlas ya a MOBI
