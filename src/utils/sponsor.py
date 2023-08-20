from src.facebook.create_content import create_comment


def promote_github(post_id: str):
    github_link = "https://github.com/seokkuuu/CatMomosBot5000"

    comment_text = (
        "pueden acceder al código del bot en GitHub. "
        "el proyecto es de código abierto bajo la licencia MIT.\n\n"
        "{}".format(github_link)
    )

    create_comment(post_id, comment_text)
