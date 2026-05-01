# Proyecto_git_stephaniesilva1-sofianuñez2-camilasalazar3
Photo Campus es un emprendimiento enfocado en la fotografía profesional, cuyo objetivo es ofrecer diferentes servicios fotográficos para distintos tipos de eventos como bodas, retratos y fotografía de productos. Este proyecto consiste en el desarrollo de un sistema que permite agregar, editar y eliminar servicios fotográficos, facilitando la organización de la información y mejorando el control interno del negocio, también utilizamos Git y GitHub para llevar un control de versiones adecuado y mejorar nuestro trabajo en grupo

Funcionalidades que tiene nuestro proyecto:
-Agregar nuevos servicios fotográficos
-Editar servicios existentes(duración y precio)
-Eliminar servicios que ya no se ofrecen

Para el desarrollo del proyecto se utilizó Git con la siguiente organización de ramas:

main → rama principal
feature/add-services → agregar servicios
feature/edit-services → editar servicios
feature/delete-services → eliminar servicios

Durante el proyecto, nos aparece un conflicto y lo resolvimos

Cómo resolvimos el conflicto:

-Intentamos hacer merge entre ramas
-Git detectó conflictos en archivos compartidos (rama Camila y Sofía)
-Se revisó el conflicto en la rama de Camila (feature/delete-services) donde se utilizó el comando:
Accept Both Changes: Permite conservar los dos cambios (el tuyo y el de la otra rama) en un mismo archivo cuando hay un conflicto, cuando dos personas modifican la misma parte del código, Git no sabe cuál dejar, entonces aparecen opciones como:

- Accept Current Change → deja tu cambio
- Accept Incoming Change → deja el del otro
- Accept Both Changes → une ambos cambios

Con este comando resolvimos el de ella pero afectando la rama de Sofía (feature/edit-services)

-Resolvimos el conflicto de la rama de Sofía (feature/edit-services), volviendo a realizar la rama y los cambios que ya se había realizado


Flujo de trabajo de nuestro proyecto:
-Creamos una rama para cada funcionalidad
-Desarrollamos cambios en la rama correspondiente
-Hicimos commits frecuentes
-Integramos cambios a la rama main
-Resolvimos conflictos
