import os.path
from sqlalchemy import create_engine, Column, Integer, Text, select, update
from sqlalchemy.orm import sessionmaker, declarative_base
from db_handler.handler import Users, Data, Base, engine, Session
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def delete_user(user_telegram_id: int):
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(Users).filter(Users.id == user_telegram_id).first()
        data = db.query(Data).filter(Data.id == user_telegram_id).first()
        if user is not None:
            db.delete(user)
            db.delete(data)
            db.commit()

def start_user(user_telegram_id: int):
    with Session(autoflush=False, bind=engine) as db:
        delete_user(user_telegram_id)
        new_user = Users(id=user_telegram_id)
        new_error = Data(id=user_telegram_id, oobe=0, error=0)
        db.add(new_user)
        db.add(new_error)
        db.commit()


def OOBE_Part1(Klass, user_telegram_id: int):
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(Users).filter(Users.id == user_telegram_id).first()
        data = db.query(Data).filter(Data.id == user_telegram_id).first()
        if user != None and data != None:
            user.klass = Klass
            data.oobe = 1
            db.commit()


def OOBE_Part2(Level, user_telegram_id: int):
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(Users).filter(Users.id == user_telegram_id).first()
        data = db.query(Data).filter(Data.id == user_telegram_id).first()
        if user != None and data != None:
            user.level = Level
            data.oobe = 2
            db.commit()


def OOBE_Part3(Width, user_telegram_id: int):
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(Users).filter(Users.id == user_telegram_id).first()
        data = db.query(Data).filter(Data.id == user_telegram_id).first()
        if user != None and data != None:
            user.width = Width
            data.oobe = 3
            db.commit()


def data_tester(user_telegram_id: int):
    with Session(autoflush=True, bind=engine) as db:
        current = db.query(Data).filter(Data.id == user_telegram_id).first()
        if current != None:
            #print(current.id, current.oobe, current.error)
            return [current.oobe, current.error]
        return [None, None]

def get_settings(user_telegram_id: int):
    with Session(autoflush=True, bind=engine) as db:
        current = db.query(Users).filter(Users.id == user_telegram_id).first()
        if current != None:
            #print(current.id, current.klass, current.level, current.width)
            return [current.klass, current.level, current.width]
        return [None, None, None]


def commit_error(user_telegram_id: int):
    with Session(autoflush=True, bind=engine) as db:
        current = db.query(Data).filter(Data.id == user_telegram_id).first()
        if current != None:
            current.error = 1
            db.commit()


def uncommit_error(user_telegram_id: int):
    with Session(autoflush=True, bind=engine) as db:
        current = db.query(Data).filter(Data.id == user_telegram_id).first()
        if current != None:
            current.error = 0
            db.commit()
