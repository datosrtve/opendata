import csv
import json

csv_file_path = 'https://raw.githubusercontent.com/datosrtve/opendata/main/2024/mapa%20playas/code/data/filtros_playas_prueba_foto.csv'
geojson_file_path = 'playas.geojson'

features = []

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(row["X"]), float(row["Y"])]
            },
            "properties": {
                "OBJECTID": row["OBJECTID"],
                "nombre_completo": row["nombre_completo"],
                "nombre_mun": row["nombre_mun"],
                "comunidad": row["Comunidad"],
                "provincia_isla": row["Provincia_isla"],
                "municipio": row["Municipio"],
                "equipamiento": float(row["slider_equipamiento"]),
                "ocupacion": row["slider_ocupacion"],
                "accesible_sillas_ruedas": row["filtro_accesible_sillas_ruedas"] == 's',
                "aseos": row["filtro_aseos"] == 's',
                "alquiler_sombrillas_hamacas": row["filtro_alquiler_sombrillas_hamacas"] == 's',
                "aparcamiento": row["filtro_aparcamiento"] == 's',
                "chiringuito": row["filtro_chiringuito"] == 's',
                "duchas_lavapies": row["filtro_duchas_lavapies"] == 's',
                "socorrista": row["filtro_socorrista"] == 's',
                "zona_infantil": row["filtro_zona_infantil"] == 's',
                "aguas_tranquilas": row["filtro_aguas_tranquilas"] == 's',
                "baja_ocupacion": row["filtro_baja_ocupacion"] == 's',
                "banderas_azules": row["filtro_banderas_azules"] == 's',
                "nudista": row["filtro_nudista"] == 's',
                "playa_piedras": row["filtro_playa_piedras"] == 's',
                "playa_arena": row["filtro_playa_arena"] == 's',
                "extensas_1km": row["filtro_extensas_1km"] == 's',
                "acantilado_montana": row["filtro_acantilado_montana"] == 's',
                "dunas": row["filtro_dunas"] == 's',
                "paseo_completo": row["filtro_paseo_completo"] == 's',
                "playa_aislada": row["filtro_playa_aislada"] == 's',
                "alquiler_nautico": row["filtro_alquiler_nautico"] == 's',
                "club_nautico": row["filtro_club_nautico"] == 's',
                "fondo_barcos": row["filtro_fondo_barcos"] == 's',
                "submarinismo": row["filtro_submarinismo"] == 's',
                "surf": row["filtro_surf"] == 's',
                "zona_deportiva": row["filtro_zona_deportiva"] == 's',
                "tipo_playa": row["ficha_tipo_playa"],
                "longitud": row["ficha_longitud"],
                "anchura_max": row["ficha_anchura_max"],
                "entorno": row["ficha_entorno"],
                "hospital": row["hospital"],
                "distancia_hospital": row["distancia_hospital"],
                "carretera": row["carretera"],
                "formas_acceso": row["formas_acceso"],
                "transporte_publico": row["transporte_publico"],
                "advertencia_acceso": row["advertencia_acceso"],
                "oleaje": row["ficha_oleaje"],
                "urbanizacion": row["ficha_urbanizacion"],
                "entorno_protegido": row["ficha_entorno_protegido"],
                "foto": row["foto"]
            }
        }
        features.append(feature)

geojson = {
    "type": "FeatureCollection",
    "features": features
}

with open(geojson_file_path, 'w', encoding='utf-8') as f:
    json.dump(geojson, f, ensure_ascii=False, indent=4)