\# Reglas SWRL de la ontología WiFi



\## Introducción



Con el objetivo de complementar el razonamiento basado en OWL, se han implementado reglas SWRL (Semantic Web Rule Language) que permiten generar nuevo conocimiento a partir de las relaciones semánticas existentes en la ontología. Estas reglas facilitan la clasificación automática de puntos WiFi según determinadas características de cobertura.



\---



\## Regla 1: Clasificación de puntos WiFi con alta cobertura



\*\*Nombre de la regla:\*\* `ReglaAltaCobertura`



```swrl

PuntoWifi(?p) ^ tieneCobertura(?p, cobertura\_Alta100Mbps) -> PuntoWifiAltaCobertura(?p)

```



\*\*Descripción:\*\*



Esta regla clasifica automáticamente como `PuntoWifiAltaCobertura` aquellos puntos WiFi que tienen asociada una cobertura de alta capacidad.



\*\*Ejemplo de inferencia:\*\*



El individuo `wifi\_Centro\_001`, al tener la relación `tieneCobertura` con `cobertura\_Alta100Mbps`, es clasificado automáticamente como `PuntoWifiAltaCobertura`.



\---



\## Regla 2: Clasificación de puntos WiFi con baja cobertura



\*\*Nombre de la regla:\*\* `ReglaBajaCobertura`



```swrl

PuntoWifi(?p) ^ tieneCobertura(?p, cobertura\_Baja40Mbps) -> PuntoWifiBajaCobertura(?p)

```



\*\*Descripción:\*\*



Esta regla clasifica automáticamente como `PuntoWifiBajaCobertura` aquellos puntos WiFi que tienen asociada una cobertura de baja capacidad.



\*\*Ejemplo de inferencia:\*\*



El individuo `wifi\_Centro\_002`, al tener la relación `tieneCobertura` con `cobertura\_Baja40Mbps`, es clasificado automáticamente como `PuntoWifiBajaCobertura`.



\---



\## Conclusiones



Las reglas SWRL implementadas permiten enriquecer el modelo ontológico mediante la generación automática de nuevas clasificaciones semánticas. De este modo, la ontología no solo almacena información estructurada, sino que también es capaz de inferir nuevo conocimiento a partir de las relaciones definidas entre sus entidades.



