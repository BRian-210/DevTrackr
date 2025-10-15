from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, Float, Text, ForeignKey, Boolean
from datetime import datetime
Base = declarative_base()
class Developer(Base):
    __tablename__ = 'developers'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    email = Column(String(255), nullable=True)
    projects = relationship('Project', back_populates='developer', cascade='all, delete-orphan')
    def __repr__(self):
        return f"<Developer id={self.id} name={self.name}>"
class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    developer_id = Column(Integer, ForeignKey('developers.id'), nullable=False)
    developer = relationship('Developer', back_populates='projects')
    sessions = relationship('Session', back_populates='project', cascade='all, delete-orphan')
    hiccups = relationship('Hiccup', back_populates='project', cascade='all, delete-orphan')
    def __repr__(self):
        return f"<Project id={self.id} title={self.title}>"
class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    started_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    stopped_at = Column(DateTime, nullable=True)
    duration_hours = Column(Float, nullable=True)
    notes = Column(Text, nullable=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    active = Column(Boolean, default=True)
    project = relationship('Project', back_populates='sessions')
    def __repr__(self):
        return f"<Session id={self.id} project_id={self.project_id} hours={self.duration_hours} active={self.active}>"
class Hiccup(Base):
    __tablename__ = 'hiccups'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    details = Column(Text, nullable=True)
    resolved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    project = relationship('Project', back_populates='hiccups')
    def __repr__(self):
        return f"<Hiccup id={self.id} title={self.title} resolved={self.resolved}>"
