from fastapi import APIRouter
from api import result_message
from database.postservice import add_user_post_db, get_all_posts_db, get_exact_post_db, change_post_db

post_router = APIRouter(prefix="/post", tags=["Post API"])

@post_router.post("/add_user_post")
async def add_post_api(user_id: int, main_text: str, hashtags:str = None):
    result = add_user_post_db(user_id, main_text, hashtags)
    return result_message(result)

@post_router.get("/get_all_posts")
async def get_all_posts_api():
    return get_all_posts_db()


@post_router.get("/get_exact_post")
async def get_exact_post_api(post_id: int):
    result = get_exact_post_db(post_id)
    return result_message(result)

@post_router.put("/change_post")
async def change_post_api(post_id: int, change_info: str, new_info:str):
    result = change_post_db(post_id, change_info, new_info)
    return result_message(result)