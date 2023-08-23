from .database import SessionLocal
from .models import Todo


class SqliteTools:
    @classmethod
    def add_todo(cls, title, description, completed=False):
        todo = Todo(title=title, description=description, completed=completed)
        with SessionLocal() as session:
            session.add(todo)
            session.commit()
            todo = session.query(Todo).get(todo.id)
        return todo

    @classmethod
    def get_todo_by_id(cls, id):
        with SessionLocal() as session:
            todo = session.query(Todo).get(id)
        return todo

    @classmethod
    def delete_todo_by_id(cls, id):
        with SessionLocal() as session:
            todo = session.query(Todo).get(id)

            if not todo:
                return False

            session.delete(todo)
            session.commit()
        return True

    @classmethod
    def update_todo_by_id(cls, id, title, description, completed):
        with SessionLocal() as session:
            todo = session.query(Todo).get(id)

            if not todo:
                return False

            todo.title = title
            todo.description = description
            todo.completed = completed
            session.commit()
            todo = session.query(Todo).get(id)
        return todo
