from database.models import UserPost, Comment, Hashtags
from database import get_db

def add_user_post_db(user_id, main_text, hashtags=None):
    with next(get_db()) as db:
        new_post = UserPost(user_id=user_id, main_text=main_text, hashtags=hashtags)
        db.add(new_post)
        db.commit()
        return new_post.id

def get_all_posts_db():
    with next(get_db()) as db:
        all_posts = db.query(UserPost).all()
        return all_posts

def get_exact_post_db(post_id):
    with next(get_db()) as db:
        post = db.query(UserPost).filter_by(id=post_id).first()
        if post:
            return post
        return "Такого поста нет"

def change_post_db(post_id, change_info, new_info):
    with next(get_db()) as db:
        post = db.query(UserPost).filter_by(id=post_id).first()
        if post:
            if change_info == "text":
                post.main_text = new_info
            elif change_info == "hashtags":
                post.hashtags = new_info
            db.commit()
            return True
        return "Такого поста нет"



def delete_post_db(post_id):
    with next(get_db()) as db:
        post_to_delete = db.query(UserPost).filter_by(id=post_id).first()
        if post_to_delete:
            db.delete(post_to_delete)
            db.commit()
            return True
        return "Такого поста нет"


#comment section
def add_comment_to_post_db(user_id, post_id, text):
    with next(get_db()) as db:
        new_comment = Comment(comment=text, user_id=user_id, post_id=post_id)
        db.add(new_comment)
        return new_comment.id

def get_comment_by_post_id_db(post_id):
    with next(get_db()) as db:
        exact_post = db.query(UserPost).filter_by(id=post_id).first()
        if exact_post:
            get_comment = db.query(Comment).filter_by(post_id=post_id).all()
            return get_comment
        return False

def change_comment_text_db(comment_id, new_text):
    with next(get_db()) as db:
        comment = db.query(Comment).filter_by(id=comment_id).first()
        if comment:
            comment.comment = new_text
            db.commit()
            return True
        return False

def delete_comment_db(comment_id):
    with next(get_db()) as db:
        delete_comment = db.query(Comment).filter_by(id=comment_id).first()
        if delete_comment:
            db.delete(delete_comment)
            db.commit()
            return True
        return False

#hashtag section
def add_hashtags_db(hashtag_name):
    with next(get_db()) as db:
        new_hashtags = Hashtags(hashtag_name=hashtag_name)
        db.add(new_hashtags)
        db.commit()
        return new_hashtags.id

def get_post_by_hashtags_db(size, hashtag_name):
    with next(get_db()) as db:
        exact_hashtag = db.query(Hashtags).filter_by(hashtag_name=hashtag_name).first()
        if exact_hashtag:
            exact_posts = db.query(UserPost).filter_by(hashtags=hashtag_name).limit(size).all() #hashtag
            return exact_posts
        return False

def get_hashtag_db(hashtag_name):
    with next(get_db()) as db:
        exact_hashtag = db.query(Hashtags).filter_by(hashtag_name=hashtag_name).first()
        if exact_hashtag:
            return exact_hashtag
        return False
