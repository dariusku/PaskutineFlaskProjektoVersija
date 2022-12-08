from flask_login import UserMixin

from Reservation_system import db


class Restoranas(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'restoranas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column('Pavadinimas', db.String(80), nullable=False, unique=True)
    email = db.Column('El.pastas', db.String(80), nullable=False, unique=True)
    slaptazodis = db.Column('Slaptazodis', db.String(80), unique=True, nullable=False)
    telefonas = db.Column('Telefonas', db.String(11), unique=True, nullable=False)

    #one to many relationship
class Patiekalas(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'patiekalas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pavadinimas = db.Column('Pavadinimas', db.String(80), nullable=False)
    patiekalo_tipas = db.Column('Patiekalo tipas', db.String(80), nullable=False)
    sudetis = db.Column('Sudėtis', db.String(300), nullable=False)
    alergenai = db.Column('Alergenai', db.Boolean, nullable=False)
    vegetariskas = db.Column('Vegetariškas', db.Boolean, nullable=False)
    kaina = db.Column('Kaina', db.Float(10), nullable=False)


    #many-to-many
    def __init__(self, pavadinimas, patiekalo_tipas, sudetis, alergenai, vegetariskas, kaina):
        self.pavadinimas = pavadinimas
        self.patiekalo_tipas = patiekalo_tipas
        self.sudetis = sudetis
        self.alergenai = alergenai
        self.vegetariskas = vegetariskas
        self.kaina = kaina



# Kliento kurimas
class Klientas(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'klientas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Vardas', db.String(80), nullable=False)
    email = db.Column('El.pastas', db.String(80), nullable=False, unique=True)
    slaptazodis = db.Column('Slaptazodis', db.String(80), nullable=False)
    telefonas = db.Column('Telefonas', db.String(11), unique=True, nullable=False)
#
# class Rezervacija(db.Model):
#     __table_args__ = {'extend_existing': True}
#     __tablename__ = 'rezervacija'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     data = db.Column(db.SelectField('Data', db.Integer(10), nullable=False))
#     staliuko_vietu_skaicus = db.Column('Staliuko vietų skaičius', db.Integer(10), nullable=False, unique=True)
#     vieta = db.Column(db.SelectField('Pasirinkite, kur yra staliukas'))
#     # prideti relationship ir selectfielda
class Staliukas(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'staliukas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staliukas = db.Column('Staliuko numeris', db.Integer, nullable=False)
    staliuko_vietu_skaicius = db.Column('Staliuko vietų skaičius', db.Integer, nullable=False, unique=True)
    vieta = db.Column('Vieta', db.String,nullable=False)


class Rezervacijos_talonelis(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'talonelis'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staliukas = db.Column('Staliukas', db.Integer, nullable=False)
    rezervuoja = db.Column('Kieno vardu rezervuojama?', db.String, nullable=False)


    # data = db.Column(db.SelectField('Pasirinkite data, kada bus galima užsakyti pasirinktą staliuką'))
# #prie datos sukurti menesius su dienom ir laiku kas 2h, is kuriu pasiriktu kada rezervuoti.


# class Atsiliepimas(db.Model):
#     __table_args__ = {'extend_existing': True}
#     __tablename__ = 'talonelis'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     atsiliepimas = db.Column('Jūsų atsiliepimas:',db.String(300), nullable=False)
#     data = db.Column('Data: ', db.String(12), nullable=False)
