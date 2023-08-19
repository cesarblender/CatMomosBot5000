from src.settings import getGraphAPI


def create_post(message: str) -> str:
    graph = getGraphAPI()
    post = graph.put_object(
        parent_object='me', connection_name='feed', message=message)

    return post["id"]


def create_comment(post_id: str, message: str) -> str:
    graph = getGraphAPI()
    comment = graph.put_comment(object_id=post_id, message=message)
    return comment["id"]


def create_post_with_image(image: str, content: str) -> str:
    graph = getGraphAPI()
    photo = graph.put_photo(image=image, message=content)
    return photo["id"]
