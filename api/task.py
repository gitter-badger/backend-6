import connexion
from connexion import NoContent
from db import orm_handler, Task
from decorators import access_checks

db_session = orm_handler.init_db()

def get(limit, search_term=None):
    q = db_session.query(Task)
    if search_term:
        q = q.filter(Task.name == search_term)
    return [p.dump() for p in q][:limit]


def get_one(project_id=None):
    task = db_session.query(Task).filter(Task.id == task_id).one_or_none()
    return task.dump() if project is not None else ('Not found', 404)

@access_checks.ensure_key
def create(task):
    logging.info('Creating task ')
    print(task)
    db_session.add(Task(**task))
    db_session.commit()
    return NoContent, 201

@access_checks.ensure_key
def delete(task_id):
    project = db_session.query(Task).filter(Task.id == task_id).one_or_none()
    if project is not None:
        logging.info('Deleting task %s..', project_id)
        db_session.query(Task).filter(Task.id == task_id).delete()
        db_session.commit()
        return {msg: 'Deleted'}, 200
    else:
        return NoContent, 404