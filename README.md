![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
# MANGA DOWNLOADER 🚣📄🗺
Queria leer vinland saga en mi kindle, pero no encontraba donde descargarlo asi que me vi en la obligacion de hacer un script que descargue las imagenes para luego pasarlas a formato MOBI  
Luego de descargar los capitulos que queria leer me di cuenta que podria hacer que el script funcionara para cualquier manga, asi fue que nacio esto ฅ^•ﻌ•^ฅ  
Las imagenes son descargadas de https://www.mangatigre.net/



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
> En caso de no tener git instalado (y no tener la intencion ni la necesida de hacerlo) se puede descargar el repositorio como zip 
![image](https://user-images.githubusercontent.com/27713965/233815307-a77df529-2633-4791-8229-b30ca9db8b7b.png)


### 2. Descarga e instala Python 

Sigue las instrucciones de https://www.python.org/downloads/

### 3. Instalar PIP

En este sitio estan detalladas la instrucciones para descargar e instalar pip segun tu sistema operativo https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/


---

### 2. Ejecucion
## Instalar librerias necesarias

Para esto es necesario en la raiz del proyecto ejecutar el siguiente comando  
```pip install -r requirements.txt```
> en caso de que el comando anterior falle probar con ```pip3 install -r requirements.txt```

una vez que se hayan instalado todas las dependencias podemos seguir con el siguiente paso

## Descargar los mangas
A continuacion se detallaran ejemplos de los distintos modos para descargar mangas
### 1.- Descargar todos los capitulos de un manga  
El siguiente comando descarga todos los capitulos del manga especificado  
``` python3 scraper.py -n 'boruto' -i 1 -f last ```

### 2. Descargar una serie de capitulos de un manga entre x e y  
El siguiente comando descargara solo los capitulos que se encuentren entre los valores espeficiados (incluyendolos), en el ejemplo descargara desde el capitulo 4 hasta el capitulo 21
``` python3 scraper.py -n 'blue lock' -i 4 -f 21 ```  
> En este comando es necesario que el valor que se especifica en el valor de la bandera -i sea menor al valor de la bandera -f, en caso contrario arrojara una exepcion
> En el caso de que el capitulo especificado en la bandera -f sea mayor al ultimo capitulo existente del manga especificado el script descargara hasta el ultimo capitulo existente y luego arrojara una excepcion

### 3. Descargar solo un capitulo de un manga
El siguiente comando descargara solo un capitulo del manga especificado, en el ejemplo seria el capitulo numero 3  
``` python3 scraper.py -n 'one piece' -s 3 ```

### 4. Descargar desde un capitulo x hasta el ulttimo
El siguiente comando descargara una serie de capitulos iniciando e incluyendo al especificado en la bandera -i hasta el ultimo  
``` python3 scraper.py -n 'Trigun' -i 4 -f last ```

### 5. Descargar solo el ultimo capitulo de un manga
El siguiente comando solo descargara el ultimo capitulo existente del manga   
``` python3 scraper.py -n 'Vinland Saga' -l true ```

## Significado de banderitas
* *-n* : Nombre del manga, es obligatorio en todos los comandos, el nombre de los mangas debe ir **SIEMPRE** entre comillas
* *-i* : Capitulo inicial del manga, indica desde que capitulo se comenzara a descargar, es de caracter opcional, pero 


Los mangas quedaran guardados en la raiz del proyecto en carpetas con el mismo nombre  
![image](https://user-images.githubusercontent.com/27713965/232956045-bb0bf0b7-cbdc-411c-8f82-c13c7cfd0e68.png)

Cada capitulo queda guardado en una carpeta independiente con el numero correspondiente  
![image](https://user-images.githubusercontent.com/27713965/232956210-3df096a1-b131-47ff-a4c8-a393e681b748.png)  

Las carpetas quedan listas para ser importadas directamente en el software de [KindleComicConverter](https://kcc.iosphe.re/) a formato MOBI o EPUB y luego subidas a la kindle ya sea por correo o usando [Calibre](https://calibre-ebook.com/)


***
## Construido con 🛠️
* [Python 3.8](https://www.python.org) - Lenguaje de programación

***


## Autores ✒️
* [Francisca Osores](https://www.linkedin.com/in/francisca-osores-ortiz-152347149/) - Desarrollo completo de la aplicación
* Ante cualquier duda o comentario escribir a fmosoresortiz@gmail.com

## Agradecimientos
* Este proyecto ha sido fuertemente inspirado por el trabajo de [Carleslc](https://github.com/Carleslc) y su repositorio https://github.com/Carleslc/InMangaKindle 
> en caso de que al usar mi script no puedas descargar algun manga te recomiendo revisar el trabajo de Carleslc ya que la obtencion de los mangas la hacemos a distintas paginas


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
