from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()
DB_URL = "sqlite:///emotions.db"

class ChatLog(Base):
    __tablename__ = "chat_logs"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    user_input = Column(String)
    emotion = Column(String)
    prompt = Column(String)
    ai_reply = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

engine = create_engine(DB_URL)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

def add_log(username, user_input, emotion, prompt, ai_reply):
    session = SessionLocal()
    log = ChatLog(
        username=username,
        user_input=user_input,
        emotion=emotion,
        prompt=prompt,
        ai_reply=ai_reply
    )
    session.add(log)
    session.commit()
    session.close()
