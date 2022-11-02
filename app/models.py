from app.extensions import db


class ModelMixin:
    __abstract__ = True

    def save(self):
        """Сохранение модели в БД."""
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """Удаление модели из БД."""
        db.session.delete(self)
        db.session.commit()
        return self
