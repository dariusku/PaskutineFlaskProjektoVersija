from flask import render_template, Blueprint, flash
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError

from Reservation_system.models import Klientas, Patiekalas, Staliukas, Rezervacijos_talonelis

client = Blueprint('client', __name__)

@client.route('/about')
def about():
    return render_template('about.html')

# Kliento index

@client.route('/kliento_index')

def kliento_index():
    return render_template('kliento_index.html')


# Kliento main
@client.route('/kliento_main')
@login_required
def kliento_main():
    return render_template('kliento_main.html')


# Kliento paskyros skiltis
@client.route('/paskyra')
@login_required
def paskyra():
    klientas= Klientas.query.first()
    return render_template('paskyra.html', klientas=klientas)


# Kliento rezervaciju skiltis
@client.route('/rezervacijos', methods=['POST', 'GET'])
@login_required
def rezervacijos_kurimas():
    from Reservation_system import db
    from . import forms
    staliukas = Rezervacijos_talonelis.query.all()
    db.create_all()
    form = forms.StaliukoRezervacijosForma()
    if form.validate_on_submit():
        klientas = current_user.id
        try:
            #pakeistas formatas
            strstaliukas=str(form.staliukas.data)
            staliukas = Rezervacijos_talonelis(staliukas=strstaliukas,
                                  rezervuoja=form.rezervuoja.data)
            db.session.add(staliukas)
            db.session.commit()
            flash('Staliukas pridėtas', 'success')
        except IntegrityError:
            flash('Toks staliukas jau rezervuotas, bandykite pakeisti duomenis')
        return render_template('rezervacijos.html', form=form, staliukas=staliukas)

    return render_template('rezervacijos.html', form=form, staliukas=staliukas)
# Pagrindinis puslapis

@client.route('/klientui_meniu', methods=['GET'])
@login_required
def meniu():
    patiekalai = Patiekalas.query.all()
    return render_template('klientui_meniu.html', patiekalai=patiekalai)