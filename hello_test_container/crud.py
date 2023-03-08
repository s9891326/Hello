from sqlalchemy.orm import Session

from hello_test_container import models


def create_user(db: Session, user):
    db_user = models.User(uid=user.uid, name=user.name, picture=user.picture)
    db.add(db_user)
    db.commit()
    return db_user
