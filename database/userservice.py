from database.models import User
from database import get_db

def check_user_db(name, phone_number, email):
    with next(get_db()) as db:
        check_name = db.query(User).filter_by(name=name).first()
        check_phone_number = db.query(User).filter_by(phone_number=phone_number).first()
        check_email = db.query(User).filter_by(email=email).first()
        if check_name:
            return "Юзернейм занят"
        if check_phone_number:
            return "Телефон номер занят"
        if check_email:
            return "Почта занята"
        return True

def register_user_db(name, phone_number, email, password, birthday, user_city):
    with next(get_db()) as db:
        checker = check_user_db(name, phone_number, email)
        if checker == True:
            new_user = User(name=name, phone_number=phone_number, email=email, password=password, birthday=birthday, user_city=user_city)
            db.add(new_user)
            db.commit()
        return checker

def login_user_db(login, password):
    with next(get_db()) as db:
        user_by_phone = db.query(User).filter_by(phone_number=login).first()
        user_by_email = db.query(User).filter_by(email=login).first()
        if user_by_phone:
            if user_by_phone.password == password:
                return user_by_phone.id
        elif user_by_email:
            if user_by_email.password == password:
                return user_by_email.id
        return "Неправильные данные"

def profile_info_db(user_id):
    with next(get_db()) as db:
        user = db.query(User).filter_by(id=user_id).first()
        if user:
            return user
        return False

def change_user_db(user_id, change_info, new_info):
    with next(get_db()) as db:
        user = db.query(User).filter_by(id=user_id).first()
        if user:
            if change_info == "name":
                user.name = new_info
            elif change_info == "phone_number":
                user.phone_number = new_info
            elif change_info == "email":
                user.email = new_info
            elif change_info == "birthday":
                user.birthday = new_info
            elif change_info == "city":
                user.user_city = new_info
            elif change_info == "password":
                user.password = new_info
            db.commit()
            return True
        return "Неправильные данные"

def delete_user_db(user_id):
    with next(get_db()) as db:
        user_to_delete = db.query(User).filter_by(id=user_id).first()
        if user_to_delete:
            db.delete(user_to_delete)
            db.commit()
            return True
        return "Неверный id"