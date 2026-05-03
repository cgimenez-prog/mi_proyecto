# Mi Proyecto

## ¿Qué es?
Se trata del Práctico 2 de la materia Programación Analítica II realizado por Clara Gimenez.

## ¿Qué hace?
Filtra números pares e impares de una lista.

## ¿Cómo probarlo?
1. Clonar el repositorio:
git clone https://github.com/cgimenez-prog/mi_proyecto.git
2. Importar la función que quieras usar:
from src.operaciones import filtrar_pares
print(filtrar_pares([1,2,3,4,5]))

## Organización de la entrega:
Se entregaron un link al repositorio en GitHub y dos notebooks de Colab.

En cuanto a la división en 2 notebooks, esto se hizo para evitar problemas con Git. Y cada uno de ellos corresponde a lo siguiente:


**1er notebook: ESTRUCTURA + INIT**

El primer notebook busca estructurar el proyecto en el Colab con sus debidas carpetas y funciones. Luego, este proyecto es subido a GitHub con el comando de inicialización `(!git init)`.


**2do notebook: REPOSITORIO CLONADO**

El segundo notebook va a clonar el repositorio de GitHub desde Colab y efectuar y subir cambios desde este ultimo.

--> Se precisan hacer estos últimos pasos en otro Colab a parte para evitar problemas con Git. Porque, de lo contrario, tendría un repositorio dentro de otro, lo que no me permitiría ejecutar el notebook o realizar cambios.
