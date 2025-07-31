from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


class ORMManager:
    def __init__(self, db_url, model_class=None):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        self.model_class = model_class

    def create_table(self):
        """Создаёт таблицы, связанные с моделью."""
        if hasattr(self.model_class, "metadata"):
            self.model_class.metadata.create_all(self.engine)

    def add_instance(self, **kwargs):
        """Добавляет экземпляр модели в БД."""
        session = self.Session()
        try:
            instance = self.model_class(**kwargs)
            session.add(instance)
            session.commit()
            print(f"✅ Добавлено: {instance}")
            return instance
        except SQLAlchemyError as e:
            session.rollback()
            print(f"❌ Ошибка при добавлении: {e}")
            return None
        finally:
            session.close()

    def find_instance(self, **kwargs):
        """Ищет объекты модели по указанным атрибутам."""
        session = self.Session()
        try:
            results = session.query(self.model_class).filter_by(**kwargs).all()
            if results:
                print(f"🔍 Найдено: {len(results)}")
            else:
                print("⚠️ Нет совпадений")
            return results
        except SQLAlchemyError as e:
            session.rollback()
            print(f"❌ Ошибка при поиске: {e}")
            return []
        finally:
            session.close()
