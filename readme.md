## Pasos para ejecutar proyecto

Construir imagen del proyecto:
docker build -t otm-ecoservice .

Ejecutar docker:
docker-compose up

La API REST es accesible desde http://127.0.0.1:8080/

Por ejemplo:
GET http://127.0.0.1:8080/regions

POST http://127.0.0.1:8080/electricity
body : 
{
  "dbh_cm": 50.8,
  "region": "InlEmpCLM",
  "genus": "Ficus",
  "species": "carica" 
}

