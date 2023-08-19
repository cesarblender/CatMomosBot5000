def get_info(params: str, image_source: str):
    return """
    ⚠🤖 Texto generado por inteligencia artificial, en caso de ser ofensivo, o muy extraño, comentar !report para que sea revisada la publicación.

    ℹ Información del modelo
    Modelo: BigScience/bloom
    Parámetros {}
    Fuente de la imagen: {}
    """.format(params, image_source)
