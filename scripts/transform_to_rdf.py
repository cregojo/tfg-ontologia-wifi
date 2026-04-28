import json
from pathlib import Path
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, XSD

# Rutas adaptadas a tu repo
INPUT_FILE = Path("../data/raw/wifi_valencia.geojson")
OUTPUT_FILE = Path("../data/rdf/wifi_valencia.ttl")

# Namespace de tu ontología
WIFI = Namespace("https://w3id.org/wifi-ontology#")

def main():
    graph = Graph()
    graph.bind("wifi", WIFI)

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    features = data.get("features", [])

    for feature in features:
        props = feature.get("properties", {})
        geom = feature.get("geometry", {})

        gid = props.get("gid")
        nombre = props.get("descripcion")
        tipo = props.get("tipo")

        coords = geom.get("coordinates", [])

        if not gid or len(coords) < 2:
            continue

        lon = coords[0]
        lat = coords[1]

        # Crear URI única
        wifi_uri = URIRef(WIFI[f"PuntoWifi_{gid}"])

        # Tipo de clase
        graph.add((wifi_uri, RDF.type, WIFI.PuntoWifi))

        # Propiedades
        if nombre:
            graph.add((wifi_uri, WIFI.nombrePunto, Literal(nombre, datatype=XSD.string)))

        graph.add((wifi_uri, WIFI.tieneLatitud, Literal(lat, datatype=XSD.decimal)))
        graph.add((wifi_uri, WIFI.tieneLongitud, Literal(lon, datatype=XSD.decimal)))

        # opcional
        graph.add((wifi_uri, WIFI.estadoPunto, Literal("activo", datatype=XSD.string)))

        if tipo is not None:
            graph.add((wifi_uri, WIFI.tipoPunto, Literal(tipo, datatype=XSD.integer)))

    # Crear carpeta si no existe
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Guardar archivo RDF
    graph.serialize(destination=OUTPUT_FILE, format="turtle")

    print("RDF generado correctamente")
    print(f"Total puntos: {len(features)}")

if __name__ == "__main__":
    main()
