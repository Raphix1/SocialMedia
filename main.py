from fastapi import FastAPI
from api.photo.photo_api import photo_router
from api.users.user_api import user_router
from api.comments.comment_api import comment_router
from api.posts.post_api import post_router
from api.hashtags.hashtag_api import hashtags_router
from database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI(docs_url="/")

app.include_router(photo_router)
app.include_router(user_router)
app.include_router(comment_router)
app.include_router(post_router)
app.include_router(hashtags_router)
