Para correr local se debe clonar el repo. 

Una vez clonado, la primera vez correrlo de la siguiente manera 
```
docker-compose up --build
```
Luego 
Para porbar la api podes ir a 
http://localhost:8080/docs#/

Y ahi tenes expuesto la api. Por una cuestion que no me funcionaba la api que debia consumir, hice un mock de vuelos para tener info. En el archivo flight_service.py esta comentado la linea que hace consumo de la api.

Me di cuenta despues que no era consumir una api, si no era ese openapi, por eso no me funcionaba, pero honestamente no supe como sacar la info del yaml ese. Capaz aca estoy mas perdido que turco en la neblina.

