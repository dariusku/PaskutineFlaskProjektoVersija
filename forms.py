from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, BooleanField, FloatField,SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length
from wtforms_sqlalchemy.fields import QuerySelectField
from Reservation_system.main import app
from Reservation_system.models import Staliukas


# Sukuriama Kliento rezervacijos forma
class KlientoRegForma(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    el_pastas = StringField('El. pašto adresas', [DataRequired()])
    telefonas = StringField('Telefono numeris', [DataRequired(), Length(max=12)])
    slaptazodis = PasswordField('Slaptažodis', [DataRequired()])
    patvirtintas_slaptazodis = PasswordField('Pakartokite slaptažodį',
                                             [EqualTo('slaptazodis', 'Slaptažodis turi sutapti')])
    submit = SubmitField('Prisiregistruoti')

    def tikrinti_vartotoja(self, vardas, telefonas, el_pastas):
        klientas = app.Klientas.query.filter_by(vardas=vardas.data).first()
        if klientas:
            raise ValidationError('Vartotojas su tokiu vardu jau egzistuoja!')
        klientas = app.Klientas.query.filter_by(telefonas=telefonas.data).first()
        if klientas:
            raise ValidationError('Šis telefono numeris, jau užregistruotas! Įveskite kitą telefono numerį')
        klientas = app.Klientas.query.filter_by(el_pastas=el_pastas.data).first()
        if klientas:
            raise ValidationError('Vartotojas su tokiu el. paštu jau egzistuoja! Pasirinkite kitą.')


# Kliento prisijungimo forma
class KlientoPrisijungimoForma(FlaskForm):
    el_pastas = StringField('El. pašto adresas', [DataRequired()])
    slaptazodis = PasswordField('Slaptažodis', [DataRequired()])
    prisiminti = BooleanField('Prisiminti mane')
    submit = SubmitField('Prisijungti')


# Kliento paskyros redagavimo forma

class KlientoPaskyrosRedagavimoForma(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    el_pastas = StringField('El. pašto adresas', [DataRequired()])
    nuotrauka = FileField('Pridėkite profilio nuotrauką', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Atnaujinti')

    def tikrinti_varda(self, vardas):
        if vardas.data != app.current_user.vardas:
            restoranas = app.Restoranas.query.filter_by(vardas=vardas.data).first()
            if restoranas:
                raise ValidationError('Šis vardas panaudotas. Pasirinkite kitą.')

    def tikrinti_pasta(self, el_pastas):
        if el_pastas.data != app.current_user.el_pastas:
            restoranas = app.Restoranas.query.filter_by(el_pastas=el_pastas.data).first()
            if restoranas:
                raise ValidationError('Šis el. paštas jau panaudotas. Pasirinkite kitą.')


# Restorano formos

# Restorano paskyros redagavimo forma
class RestoranoPaskyrosRedagavimoForma(FlaskForm):
    pavadinimas = StringField('Restorano pavadinimas', [DataRequired()])
    res_el_pastas = StringField('El. pašto adresas', [DataRequired()])
    res_nuotrauka = FileField('Restorano logo', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Atnaujinti')

    def tikrinti_pavadinima(self, pavadinimas):
        if pavadinimas.data != app.current_user.vardas:
            restoranas = app.Restoranas.query.filter_by(pavadinimas=pavadinimas.data).first()
            if restoranas:
                raise ValidationError('Šis restorano pavadinimas jau panaudotas. Pasirinkite kitą.')

    def tikrinti_res_pasta(self, res_el_pastas):
        if res_el_pastas.data != app.current_user.res_el_pastas:
            restoranas = app.Restoranas.query.filter_by(email=res_el_pastas.data).first()
            if restoranas:
                raise ValidationError('Šis el. paštas jau panaudotas. Pasirinkite kitą.')


# Restorano meniu forma
class RestoranoMeniuForma(FlaskForm):
    patiekalo_pavadinimas = StringField('Patiekalo pavadinimas')
    patiekalo_tipas = SelectField(u'Patiekalo tipas', choices=[('Starteris', 'Starteris'), ('Pagrindinis','Pagrindinis'), ('Desertas', 'Desertas')])
    sudetis = StringField('Patiekalo sudetis')
    alergenai = BooleanField('Ar patiekale yra alergenų?')
    vegetariskas = BooleanField('Ar patiekalas tinka vegetarams?')
    kaina = FloatField('Įveskite patiekalo kainą')
    submit = SubmitField('Įvesti')


class RestoranoStaliukoForma(FlaskForm):
    staliukas = StringField('Staliuko numeris')
    staliuko_vietu_skaicius = StringField('Staliuko vietų skaičius')
    vieta = SelectField(u'Vieta', choices=[('Kavinė', 'Kavinė'), ('Pagrindinė salė','Pagrindinė salė'), ('Ložė', 'Ložė'),('Terasa','Terasa')])
    submit = SubmitField('Pridėti staliuką')


class RestoranoRegForma(FlaskForm):
    pavadinimas = StringField('Restorano pavadinimas', [DataRequired()])
    restorano_el_pastas = StringField('El. pašto adresas', [DataRequired()])
    telefonas = StringField('Telefono numeris', [DataRequired()])
    slaptazodis = PasswordField('Slaptažodis', [DataRequired()])
    patvirtintas_slaptazodis = PasswordField('Pakartokite slaptažodį',
                                             [EqualTo('slaptazodis', 'Slaptažodis turi sutapti')])
    submit = SubmitField('Prisiregistruoti')






    def tikrinti_pavadinima(self, pavadinimas):
        restoranas = app.Restoranas.query.filter_by(res_pavadinimas=pavadinimas.data).first()
        if restoranas:
            raise ValidationError('Restoranas su tokiu pavadinimu jau egzistuoja!')

    def tikrinti_res_telefona(self, res_telefonas):
        restoranas = app.Restoranas.query.filter_by(res_telefonas=res_telefonas.data).first()
        if restoranas:
            raise ValidationError('Šis telefono numeris, jau užregistruotas! Įveskite kitą telefono numerį')

    def tikrinti_res_pasta(self, restorano_el_pastas):
        restoranas = app.Restoranas.query.filter_by(res_el_pastas=restorano_el_pastas.data).first()
        if restoranas:
            raise ValidationError('Restoranas su tokiu el. paštu jau egzistuoja! Pasirinkite kitą.')


# Restorano prisijungimo forma
class RestoranoPrisijungimoForma(FlaskForm):
    restorano_el_pastas = StringField('El. pašto adresas', [DataRequired()])
    slaptazodis = PasswordField('Slaptažodis', [DataRequired()])
    prisiminti = BooleanField('Prisiminti')
    submit = SubmitField('Prisijungti')





# rezervacijos forma
def staliukas_query():
    return Staliukas.query
class StaliukoRezervacijosForma(FlaskForm):
    staliukas=QuerySelectField(query_factory=staliukas_query, allow_blank=True, get_label='staliukas', get_pk=lambda obj: str(obj))
    rezervuoja=StringField('Kieno vardu rezervuojama?')
    submit = SubmitField('Pateikti')