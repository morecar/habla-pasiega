# Digitalización de El Habla Pasiega
Este repo contiene una digitalización a LaTeX (PDF) del libro "El Habla Pasiega" (Londres, 1969) de Ralph J. Penny.

## ¿Por qué?
El objetivo es ofrecer al autor y su familia la posibilidad de una reimpresión, y acabar con la especulación en el mercado de segunda mano. 

## Cómo compilar este proyecto a PDF
Prerrequisitos:
- `pdflatex`, viene con las distribucionies LaTeX, [descarga aquí la tuya](https://www.latex-project.org/get/). 
- Una copia de este repositorio. 

Desde la línea de comandos, en el directorio raíz:
```bash
$ pdflatex el-habla-pasiega.tex
```
Si quieres actializar la tabla de contenidos (fichero `.top`, el índice) deberás correr el comando dos veces para que se reflejen los cambios. 

Si sólo quieres el documento en el estado más moderno, intentaré que se compile el documento automáticamente tras cada nueva contribución y se publique en la sección de *Releases*. 

## Cómo contribuir
Existen tres formas fundamentales en las que puedes contribuir:
* Transcribiendo texto. El libro se estructura por párrafos; yo te pasaría un escaneado de un párrafo y tú me devolverías texto. Te dejo escoger el párrafo, van por temática.
* Digitalizando imágenes. El libro contiene unas pocas imágenes, fundamentalmente mapas y algún diagrama o dibujo. Son dibujos a mano alzada del autor. Yo te pasaría un escaneo y me devolverías un SVG. Te dejo escoger el dibujo.
* Con el propio formato en LaTeX. Esto es, de lejos, el documento de LaTeX más complejo que yo he hecho.

Si has encontrado una errata, simplemente contáctame y yo mismo lo arreglaré. 

## Cómo ponerse en contacto conmigo
La opción más fácil es por Twitter, en [@morecar89](https://twitter.com/morecar89), o un email a [igualquetwitter]@gmail.com.
