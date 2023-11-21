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

## Zonas

Interior West (InterWABQ)
Temperate Interior West (TpIntWBOI)
Pacific Northwest (PacfNWLOG)
Inland valleys (InlValMOD)
Southwest desert (SWDsrtGDL)
Southern california coast (SoCalCSMA)
Inland empire (InlEmpCLM)
tropical (TropicPacXXX)
central florida (CenFlaXXX)
Northeast (NoEastXXX)
Lower Midwest (LoMidWXXX)
Midwest (MidWstMSP)
Northern california coast (GulfCoCHS)
North (PiedmtCLT)
Coastal plain (CaNCCoJBK)
South (NMtnPrFNL) <---

## Notas

Lagerstroemia indica existe en la mayoria de areas excepto en NMtnPrFNL
Acer buergerianum existe en la mayoria de areas excepto en NMtnPrFNL
Ligustrum lucidum aureo NO EXISTE. Solo existe Ligustrum lucidum en muchas areas, excepto en NMtnPrFNL
Cercis siliquastrum - InlValMOD
Albizzia julibrissim existe en la mayoria de areas excepto en NMtnPrFNL
Fraxinus americana existe en la mayoria de areas excepto en NMtnPrFNL 
Callistemon citrinus existe en la mayoria de areas excepto en NMtnPrFNL 

## Factores

Factor	                    Descripción						
pm10_avoided_it	            Cantidad de partículas PM10 evitadas por los árboles en la industria.						
sox_avoided_mf	            Cantidad de óxidos de azufre evitados por los árboles en el sector forestal.						
voc_avoided_sf	            Cantidad de compuestos orgánicos volátiles evitados por los árboles en el sector residencial.						
species_codes	              Códigos de especies de árboles.						
electricity-sfr	            Electricidad ahorrada por los árboles en el sector residencial.						
electricity-mfr	            Electricidad ahorrada por los árboles en el sector manufacturero.						
aq_sox_dep	                Deposición de óxidos de azufre en los árboles.						
aq_sox_avoided	            Cantidad de óxidos de azufre evitados por los árboles en el aire.						
sox_avoided_ci	            Cantidad de óxidos de azufre evitados por los árboles en el sector comercial e institucional.						
natural_gas-ci	            Gas natural ahorrado por los árboles en el sector comercial e institucional.						
voc_avoided_it	            Cantidad de compuestos orgánicos volátiles evitados por los árboles en la industria.						
co2_decomp	                Descomposición de CO2 por los árboles.						
co2_maint	                  Mantenimiento de CO2 por los árboles.						
pm10_avoided_mf	            Cantidad de partículas PM10 evitadas por los árboles en el sector manufacturero.						
sox_avoided_it	            Cantidad de óxidos de azufre evitados por los árboles en la industria.						
natural_gas-mfr	            Gas natural ahorrado por los árboles en el sector manufacturero.						
nox_avoided_it	            Cantidad de óxidos de nitrógeno evitados por los árboles en la industria.						
cpa	                        Potencial de reducción de la contaminación del aire.						
aq_pm10_dep	                Deposición de partículas PM10 en los árboles.						
aq_voc_avoided	            Cantidad de compuestos orgánicos volátiles evitados por los árboles en el aire.						
property_value	            Aumento del valor de la propiedad por la presencia de árboles.						
nox_avoided_sf	            Cantidad de óxidos de nitrógeno evitados por los árboles en el sector residencial.						
net_vocs	                  Compuestos orgánicos volátiles netos.						
co2_avoided-ci	            Cantidad de CO2 evitado por los árboles en el sector comercial e institucional.						
hydro_interception	        Intercepción de la lluvia por los árboles.						
co2_avoided-mfr	            Cantidad de CO2 evitado por los árboles en el sector manufacturero.						
bvoc	                      Compuestos orgánicos volátiles biogénicos.						
sox_avoided_sf	            Cantidad de óxidos de azufre evitados por los árboles en el sector residencial.						
electricity-it	            Electricidad ahorrada por los árboles en la industria.						
pm10_avoided_ci	            Cantidad de partículas PM10 evitadas por los árboles en el sector comercial e institucional.						
numbers	                    Números.						
voc_avoided_mf	            Cantidad de compuestos orgánicos volátiles evitados por los árboles en el sector manufacturero.						
nox_avoided_ci	            Cantidad de óxidos de nitrógeno evitados por los árboles en el sector comercial e institucional.						
aq_ozone_dep	              Deposición de ozono en los árboles.						
co2_avoided-sfr	            Cantidad de CO2 evitado por los árboles en el sector residencial.						
natural_gas-sfr	            Gas natural ahorrado por los árboles en el sector residencial.						
dbh_by_age_class	          Diámetro a la altura del pecho por clase de edad de los árboles.						
co2_storage	                Almacenamiento de CO2 por los árboles.						
co2_sequestered	            CO2 secuestrado por los arboles.						



