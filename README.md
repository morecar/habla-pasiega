# Digitalización de El Habla Pasiega
Este repo contiene una digitalización a LaTeX (PDF) del libro "El Habla Pasiega" (Londres, 1969) de Ralph J. Penny.

## ¿Por qué?
El objetivo es:
1. ofrecer al autor y su familia la posibilidad de una reimpresión, y acabar con la especulación en el mercado de segunda mano de una obra fundamental para la difusión del patrimonio lingüístico pasiego.
2. Re-editar la obra transliterándola automaticamente al Alfabeto Fonético Internacional y a texto plano, lo que permitirá su uso por lingüistas sin el conocimiento del viejo alfabeto de la Revista de Filología Española (RFE) y por el publico general, respectivamente. 
3. Poner a disposición de la comunidad una digitalización de calidad del corpus contenido en esta obra, que pueda ser base para la creación de otros contenidos, como un diccionario descriptivo o un corpus digital. 


## Cómo compilar este proyecto a PDF
Prerrequisitos:
- `pdflatex`, viene con las distribuciones LaTeX, [descarga aquí la tuya](https://www.latex-project.org/get/).
- Una copia de este repositorio. 

Desde la línea de comandos, en el directorio raíz de este repositorio:
```bash
$ pdflatex el-habla-pasiega.tex
```

Cada pull request comprueba automáticamente que el documento se puede compilar. Cuando un cambio llega a la rama `main`, se genera una nueva edición numerada y el PDF resultante se publica en la sección [Releases](../../releases/latest).

## Cómo ponerse en contacto conmigo
La opción más fácil es [un email](mailto:morecar89@gmail.com).
