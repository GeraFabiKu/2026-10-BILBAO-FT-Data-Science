# Proyecto Data Analysis

## Data Science Bootcamp

En este proyecto vas a aplicar todo lo aprendido en el Ramp Up y el módulo de Data Analysis del bootcamp. Tendrás que realizar un análisis exploratorio de datos y presentar los resultados. Ten en cuenta lo siguiente:

***Miembros**: El proyecto es individual

***Datos**: Tienes que conseguir los datos por tu cuenta (ver abajo)

## Objetivo

Lo que queremos mediante este tipo de análisis es resolver un problema real apoyándonos en datos, por lo que tendrás que plantearte primero qué es lo que quieres resolver, y a partir de ahí ir trabajando con los datos para acabar llegando a una conclusión. Plantea tus hipótesis antes de realizar el análisis exploratorio y después verifica si se han cumplido, o si has descubierto mediante los datos que lo que ocurría era justamente lo opuesto a lo que pensabas.

## Evaluación

***Presentación** (60%) no más de 15 minutos donde expondrás tu caso (ver apartado Presentación)

***Memoria** (30%) de no más de 10 páginas donde explicarás qué es lo que has hecho (ver apartado Memoria)

***Código** (10%) hay que entregar todo el código desarrollado. También se tiene en cuenta (tipo solución, limpieza, documentar...)

## Entregable

Enlace al repositorio GitHub:

* Presentación
* Memoria
* Código
* Documentación utilizada
* Se debe crear un repositorio en GitHub para este proyecto personal. En caso de que el proyecto se componga de datos sensibles o no se quiera publicar, se puede mantener en repositorio privado.

El codigo deberá seguir la siguiente estructura de carpetas:

1. src/: aquí irá todo el código
2. src/data: todos los archivos de datos utilizados en el analisis. No subir a GitHub archivos demasiado pesados.
3. src/notebooks: los notebooks usados para pruebas (si los hay).
4. src/utils: todos los modulos y funciones auxiliares creados para el desarrollo del proyecto (si los hay).
5. src/main.ipynb: en este notebook tendrás que resumir todos los pasos de la analítica..

**GitHub**: hay que crear un README con una descripción de tu proyecto. Breve. El objetivo de este README es enterarse de forma rápida de qué va tu proyecto y qué tecnologías has utilizado para llevarlo a cabo, no es más que un escaparate de tu trabajo. Hay que ir documentando bien los trabajos para acabar el bootcamp con un buen portfolio. En [este enlace](https://github.com/alexhuang1117/Data-Science-Portfolio) tienes un ejemplo de cómo tener documentados los proyectos en tu GitHub. Encontrarás en el notebook de markdown todo lo que necesitas para crear un README decente.

## Presentación

Puesto que en la vida real la mayoría de presentaciones se realizan a un público no técnico, ésta no va a ser menos. Si tienes que explicar algo técnico, cuéntalo, pero para alguien que no sabe lo que significa. Por ejemplo, ¿cómo contarías qué es una matriz de correlación? No queremos ver código, ni cómo estructuraste el proyecto en carpetas, ni cómo de difícil ha sido limpiarlo. Al cliente/tu jefe le da igual :). Explicar cosas técnicas lleva tiempo por lo que piensa muy bien en lo que vas a decir y en cómo lo sintetizarás.

Tendrás que exponer bien tu caso de uso (~30% del tiempo), explicar qué es lo que has hecho para resolverlo (~50%), y acabar la presentación con unas conclusiones y oportunidades que nos brinda el proyecto (~20%), para cerrar el plantemiento inicial del caso de uso. **Los % son orientativos...**

**¿Formatos de la presentación?** Nada de Notebooks, ni informes en pdf o HTML. Formato presentación en PowerPoint, Prezi o la plataforma que mejor conozcas, siendo perfectamente combinable con un dashboard desarrollado mediante alguna de las herramientas aprendidas durante el curso.

**Consejos**: Si usas un PowerPoint... será tu apoyo a la hora de presentar, aquí el protagonista es tu discurso. Por favor, que la presentación no sea un conjunto de puntos inconexos. Intenta llevar un hilo, como si de una historia se tratase. Véndete, destaca las fortalezas de tu trabajo sobre las debilidades. Interactúa con el público. Si vas a contar algo de negocio, ¿puedes traducirlo a números? ¿Qué impacto tendrá tu analítica?. Muestra algunos datos concretos (estadísticos simples) para justificar tu business case o para cerrar tu presentación. Si has elegido una temática que está acorde con tus gustos/background, aprovecha al principio para contarlo y empatizar mucho más con el público. Si vas a hacer una demo, grábala por si te falla algo en la presentación (conexión a Internet). Prepárate las respuestas a algunas posibles preguntas en un anexo de la presentación.

**NOTA**: existen muchas plantillas gratuitas en la web para hacer presentaciones. [Aquí tienes unas cuantas](https://www.free-powerpoint-templates-design.com/free-powerpoint-templates-design/).

## Memoria

Simplemente es un documento que complemente a la presentación. Nada serio. Ya que en la presentación no se va a ver reflejado todo el esfuerzo dedicado al proyecto, utiliza este documento para describir todo tu trabajo, qué técnicas has utilizado, con qué dificultades te has encontrado. No más de 10 páginas. Recuerda documentar bien las fuentes de datos utilizadas en la memoria.

## Pasos del proyecto

1. Elegir temática

1.**Elegir una temática y buscar datos en función de la misma**. Es algo más complejo que la segunda opción ya que puede ocurrir que no encuentres datos que te sirvan para tu propósito, o que tengas que conseguirlos mediante APIs, scrapping, descarga de BBDD.... No obstante, esta opción es la que más se asemejaría a un caso real, ya que una gran problemática en este tipo de proyectos es encontrar datos.

2.**Directamente ir a páginas de datos abiertos y escoger un dataset de tu interés**. Si no tienes clara la temática puedes buscar en alguno de los enlaces de datos (recomendable Kaggle) y escoger un tema que te motive.

2. Obtención de datos. ¿Puedes llevar a cabo el proyecto con estos datos?
3. Define tu hipótesis. ¿Qué piensas que puedes obtener de estos datos? ¿Qué vas a poder resolver? ¿Cómo lo vas a llevar a cabo?
4. Preprocesado: obtén todos los datos de las diferentes fuentes que hayas utilizado, juntalos y ponlos en un formato entendible.
5. Limpia los datos: duplicados, missings, columnas inútiles...
6. Exploratorio: obtén todos los estadísticos y gráficos que necesites para entender bien tu dataset.
7. Concluye con tu análisis si estabas o no en lo cierto acerca de tu planteamiento y tu hipótesis.
8. Documenta tu proyecto y súbelo a GitHub.

## Datos

¿De dónde saco los datos? Posibles fuentes:

- [API de Idealista](https://www.idealista.com/labs/)
- [API de Booking](https://developers.booking.com/api/index.html)
- [API de Tripadvisor](http://developer-tripadvisor.com/content-api/)
- [API de Facebook](https://developers.facebook.com/docs/apis-and-sdks?locale=es_ES)
- [API de Twitter](https://developer.twitter.com/en/docs)
- [API de Instagram](https://www.instagram.com/developer/)
- [APIs de Google Maps](https://cloud.google.com/maps-platform?hl=es)
- [Google Timeline](https://www.google.es/maps/timeline?pb). Todo tu registro de actividad de Google, como los lugares que has visitado
- [Alexa. Tráfico de webs](https://www.alexa.com/siteinfo)
- [Catastro](https://ovc.catastro.meh.es/ovcservweb/OVCSWLocalizacionRC/OVCCoordenadas.asmx)
- [Airbnb](http://insideairbnb.com/index.html)
- Web scrapping. Acceso automatizado a cualquier web.
- Kaggle: página con competiciones de data scientists. Muchísimos datasets.
- QPython 3L: APP para ejecutar código Python en el movil. Podrás sacar datos de tu actividad con el teléfono (horarios, geoposicionamiento)
- Coronavirus. Se están empezando a librerar muchísimos datasets con datos del coronavirus en todo el mundo. En Kaggle hay varios.
- [Web de datos abiertos del gobierno](https://datos.gob.es/)
- [OpenStreetMap](https://wiki.openstreetmap.org/wiki/API). Datos de ubicaciones (como Google Maps) abiertos
- [Obtención de datos bursátiles](https://financetrain.com/best-python-librariespackages-finance-financial-data-scientists/)
- [ESRI Datos abiertos España](https://opendata.esri.es/)
- [INE](https://www.ine.es/nomen2/ficheros.do)
- [Red.es](https://www.red.es/redes/es/que-hacemos/datos-abiertos)
- [Datos abiertos gobierno](<https://www.hacienda.gob.es/es-ES/GobiernoAbierto/Datos%20Abiertos/Paginas/Catalogodedatosabiertos.aspx>)
- [Ayuntamiento de Madrid](https://datos.madrid.es/portal/site/egob/)
- [Ayuntamiento de Barcelona](https://opendata-ajuntament.barcelona.cat/es)
- [Metro de Madrid](https://data-crtm.opendata.arcgis.com/)
- [Portal datos europeo I](https://data.europa.eu/euodp/es/home)
- [Portal datos europeo II](https://www.europeandataportal.eu/data/datasets?locale=en&minScoring=0)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [Indicadores macro mundiales](https://databank.worldbank.org/home)
- [Indicadores macro mundiales](https://ilostat.ilo.org/data/country-profiles/)
- [Amplio repositorio de Datasets](https://datacommons.org/)
- [Datos macro mundiales](https://www.gapminder.org/data/)
- [GitHub con gran cantidad de APIs públicas](https://github.com/public-apis/public-apis)
- [Datos sobre migraciónn](https://migrationdataportal.org/es/node/2955)
- [Web de datos abiertos de España](https://www.epdata.es/)
- [Redapi: Plataforma de APIs con amplia capa gratuita](https://rapidapi.com/blog/most-popular-api/)
- [Artículo para trabajar con histórico de bolsa](https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75)
- [Otro gran repo de datasets](https://www.paperswithcode.com/datasets)
