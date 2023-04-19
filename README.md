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
---

### 2. Ejecucion
En la raiz del proyecto ejecutar el comando ```python3 scraper.py``` esto mostrara un menu como el siguiente
![image](https://user-images.githubusercontent.com/27713965/232952185-26e02ac2-336a-47fd-9924-1622343eaee8.png)
* Opcion 1: Descarga todos los capitulos del manga que ingreses
* Opcion 2: Descarga solo los mangas que indiques entre x e y, 
* Opcion 3: Descarga solo un capitulo del manga
* Opcion 4: Descarga solo el ultimo capitulo

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
- [ ] Optimizar la busqueda del ultimo capitulo
- [ ] Opcion para descargar solo imagenes o transformarlas ya a MOBI
