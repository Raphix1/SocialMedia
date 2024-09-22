from fastapi import APIRouter
from database.postservice import add_comment_to_post_db, get_comment_by_post_id_db, delete_comment_db, change_comment_text_db
from api import result_message
comment_router = APIRouter(prefix="/comment", tags=["Comment API"])


@comment_router.post("/add_comment_to_post")
async def add_comment_api(user_id: int, post_id: int, text: str):
    result = add_comment_to_post_db(user_id, post_id, text)
    return result_message(result)

@comment_router.get("/get_comment")
async def get_comment_api(post_id: int):
    result = get_comment_by_post_id_db(post_id)
    return result_message(result)

@comment_router.put("/change_comment")
async def change_comment(comment_id: int, new_text: str):
    result = change_comment_text_db(comment_id, new_text)
    return result_message(result)

@comment_router.delete("/delete_comment")
async def delete_comment(comment_id: int):
    result = delete_comment_db(comment_id)
    return result_message(result)