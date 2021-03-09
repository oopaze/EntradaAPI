from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime

from app.config.db import Model


class Entrada(Model):
    __tablename__ = 'Entradas'

    id = Column(Integer, primary_key=True, index=True)
    update_id = Column(Integer)
    link = Column(String)
    action = Column(String)
    data = Column(DateTime, default=datetime.now)

    def __init__(self, link: str, action:str, update_id: int, **kwargs):
        self.update_id = update_id
        self.link = link
        self.action = action

    def __repr__(self):
        return f"< Entrada {self.update_id} - {self.data}>"