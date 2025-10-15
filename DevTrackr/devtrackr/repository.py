from .db import SessionLocal
from .models import Developer, Project, Session, Hiccup
from datetime import datetime
def create_developer(name, email=None):
    with SessionLocal() as db:
        dev = Developer(name=name, email=email)
        db.add(dev)
        db.commit()
        db.refresh(dev)
        return dev
def list_developers():
    with SessionLocal() as db:
        return db.query(Developer).order_by(Developer.id).all()
def get_developer(dev_id):
    with SessionLocal() as db:
        return db.get(Developer, dev_id)
def edit_developer(dev_id, name=None, email=None):
    with SessionLocal() as db:
        dev = db.get(Developer, dev_id)
        if not dev:
            return None
        if name:
            dev.name = name
        if email is not None:
            dev.email = email
        db.add(dev)
        db.commit()
        db.refresh(dev)
        return dev
def delete_developer(dev_id):
    with SessionLocal() as db:
        dev = db.get(Developer, dev_id)
        if not dev:
            return False
        db.delete(dev)
        db.commit()
        return True
def create_project(title, developer_id, description=None):
    with SessionLocal() as db:
        proj = Project(title=title, developer_id=developer_id, description=description)
        db.add(proj)
        db.commit()
        db.refresh(proj)
        return proj
def list_projects(developer_id=None):
    with SessionLocal() as db:
        q = db.query(Project)
        if developer_id:
            q = q.filter(Project.developer_id == developer_id)
        return q.order_by(Project.id).all()
def get_project(project_id):
    with SessionLocal() as db:
        return db.get(Project, project_id)
def edit_project(project_id, title=None, description=None):
    with SessionLocal() as db:
        p = db.get(Project, project_id)
        if not p:
            return None
        if title:
            p.title = title
        if description is not None:
            p.description = description
        db.add(p)
        db.commit()
        db.refresh(p)
        return p
def delete_project(project_id):
    with SessionLocal() as db:
        p = db.get(Project, project_id)
        if not p:
            return False
        db.delete(p)
        db.commit()
        return True
def start_session(project_id, notes=None):
    with SessionLocal() as db:
        s = Session(project_id=project_id, notes=notes, started_at=datetime.utcnow(), active=True)
        db.add(s)
        db.commit()
        db.refresh(s)
        return s
def stop_session(session_id):
    with SessionLocal() as db:
        s = db.get(Session, session_id)
        if not s or not s.active:
            return None
        s.stopped_at = datetime.utcnow()
        delta = s.stopped_at - s.started_at
        s.duration_hours = round(delta.total_seconds() / 3600, 3)
        s.active = False
        db.add(s)
        db.commit()
        db.refresh(s)
        return s
def add_session_manual(project_id, duration_hours, notes=None, started_at=None):
    started = started_at or datetime.utcnow()
    with SessionLocal() as db:
        s = Session(project_id=project_id, duration_hours=duration_hours, notes=notes, started_at=started, active=False, stopped_at=started)
        db.add(s)
        db.commit()
        db.refresh(s)
        return s
def list_sessions(project_id=None, active=None):
    with SessionLocal() as db:
        q = db.query(Session)
        if project_id:
            q = q.filter(Session.project_id == project_id)
        if active is not None:
            q = q.filter(Session.active == active)
        return q.order_by(Session.started_at.desc()).all()
def get_session(session_id):
    with SessionLocal() as db:
        return db.get(Session, session_id)
def delete_session(session_id):
    with SessionLocal() as db:
        s = db.get(Session, session_id)
        if not s:
            return False
        db.delete(s)
        db.commit()
        return True
def total_hours_for_project(project_id):
    with SessionLocal() as db:
        rows = db.query(Session).filter(Session.project_id == project_id, Session.duration_hours != None).all()
        return round(sum(r.duration_hours for r in rows), 3)
def total_hours_for_developer(developer_id):
    with SessionLocal() as db:
        rows = db.query(Session).join(Project).filter(Project.developer_id == developer_id, Session.duration_hours != None).all()
        return round(sum(r.duration_hours for r in rows), 3)
def add_hiccup(project_id, title, details=None):
    with SessionLocal() as db:
        h = Hiccup(project_id=project_id, title=title, details=details)
        db.add(h)
        db.commit()
        db.refresh(h)
        return h
def list_hiccups(project_id=None, resolved=None):
    with SessionLocal() as db:
        q = db.query(Hiccup)
        if project_id:
            q = q.filter(Hiccup.project_id == project_id)
        if resolved is not None:
            q = q.filter(Hiccup.resolved == resolved)
        return q.order_by(Hiccup.created_at.desc()).all()
def edit_hiccup(hiccup_id, title=None, details=None, resolved=None):
    with SessionLocal() as db:
        h = db.get(Hiccup, hiccup_id)
        if not h:
            return None
        if title:
            h.title = title
        if details is not None:
            h.details = details
        if resolved is not None:
            h.resolved = resolved
        db.add(h)
        db.commit()
        db.refresh(h)
        return h
def delete_hiccup(hiccup_id):
    with SessionLocal() as db:
        h = db.get(Hiccup, hiccup_id)
        if not h:
            return False
        db.delete(h)
        db.commit()
        return True
