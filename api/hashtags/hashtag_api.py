from fastapi import APIRouter
from database.postservice import (get_hashtag_db, get_post_by_hashtags_db, add_hashtags_db)
from api import result_message

hashtags_router = APIRouter(prefix='/hashtags', tags=['Hashtags API'])


@hashtags_router.get('/get_hashtags')
async def get_hashtags_api(hashtag_name: str):
    result = get_hashtag_db(hashtag_name)
    return result_message(result)


@hashtags_router.get('/post_by_hashtag')
async def get_post_by_hashtag_api(size: int, hashtag_name: str):
    result = get_post_by_hashtags_db(size, hashtag_name)
    return result_message(result)


@hashtags_router.put('/add_hashtag')
async def add_hashtag_api(text: str):
    result = add_hashtags_db(text)
    if result:
        return {'status': 1, 'message': result}
    return {'status': 0, 'message': False}


from fastapi import APIRouter
from database.postservice import delete_post_db
from api import result_message

post_router = APIRouter(prefix='/post', tags=['Post API'])


@post_router.delete('/delete_post')
async def delete_post_api(post_id: int):
    result = delete_post_db(post_id)
    return result_message(result)