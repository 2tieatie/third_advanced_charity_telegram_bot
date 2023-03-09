from asyncpg import UniqueViolationError

from classes import *
from uuid import uuid4


def dist(x,y):
    latitude= float(x)
    longtitude= float(y)
    origin = (latitude, longtitude)
    actual_distance_car= []
    for destination in destinations:
        result = gmaps.distance_matrix(origin, destination,
                                       mode='driving')["rows"][0]["elements"][0]["distance"]["value"]
        result = result / 1000
        actual_distance_car.append(result)
    return actual_distance_car

async def set_default_commands(dp: dp):
    await dp.bot.set_my_commands([
        types.BotCommand('/start', 'Розпочати'),
    ])


async def db2_test():
    await db.set_bind(config.POSTGRES_URI)


async def edit_message(message: types.Message, text):
    new_mess = await message.edit_text(text, parse_mode='Markdown')
    return new_mess


def create_uuid():
    return str(uuid4())


async def select_all_admins():
    admins = await Admins.query.gino.all()
    return admins


async def select_all_pets():
    admins = await Finded_Pets.query.gino.all()
    return admins


async def add_admin(token, id):
    try:
        admin = Admins(id=id, token=token)
        await admin.create()
    except UniqueViolationError:
        pass


async def add_finded_pet(photo, city, kind, sex, breed, contact):
    try:
        pet = Finded_Pets(photo=photo, city=city, kind=kind, sex=sex, breed=breed, contact=contact)
        await pet.create()
    except UniqueViolationError:
        pass



