from sqlmodel import Session, select


class CrudBase:
    def __init__(self, model):
        self.model = model

    def create(self, db: Session, obj_in):
        db_obj = self.model(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, id):
        return db.get(self.model, id)

    def get_multi(self, db: Session, skip=0, limit=100):
        return db.exec(select(self.model).offset(skip).limit(limit)).all()

    def filter_by(self, db: Session, filter_data):
        return db.exec(select(self.model).filter_by(**filter_data)).all()

