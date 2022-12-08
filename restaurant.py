from flask import Blueprint, render_template, flash
from flask_login import login_required, login_manager, current_user
from sqlalchemy.exc import IntegrityError
from Reservation_system.models import Restoranas, Patiekalas, Staliukas

restaurant = Blueprint('restaurant', __name__)


# Restorano main
@restaurant.route('/restorano_main')
@login_required
def rest_main():
    return render_template('restorano_main.html')


# Restorano registracijos puslapis


# Restorano index

@login_required
def load_user(restorano_id):
    return Restoranas.query.get(int(restorano_id))


@restaurant.route('/restorano_index')
def rest_index():
    return render_template('restorano_index.html')


@restaurant.route('/patiekalas', methods=['POST', 'GET'])
@login_required
def patiekalas_kurimas():
    from Reservation_system import db
    from . import forms
    db.create_all()
    form = forms.RestoranoMeniuForma()
    if form.validate_on_submit():
        try:
            patiekalas = Patiekalas(pavadinimas=form.patiekalo_pavadinimas.data,
                                    patiekalo_tipas=form.patiekalo_tipas.data,
                                    sudetis=form.sudetis.data,
                                    alergenai=form.alergenai.data, vegetariskas=form.vegetariskas.data,
                                    kaina=form.kaina.data)
            db.session.add(patiekalas)
            db.session.commit()
            flash('Patiekalas pridėtas', 'success')
        except IntegrityError:
            flash('Toks patiekalas egistuoja, bandykite pakeisti duomenis')

    return render_template('patiekalas.html', form=form)



@restaurant.route('/restorano_staliukas', methods=['POST', 'GET'])
@login_required
def staliukas_kurimas():
    from Reservation_system import db
    from . import forms
    db.create_all()
    form = forms.RestoranoStaliukoForma()
    if form.validate_on_submit():
        restoranas = current_user.id
        try:
            staliukas = Staliukas(staliukas=form.staliukas.data,
                                  staliuko_vietu_skaicius=form.staliuko_vietu_skaicius.data, vieta=form.vieta.data)
            db.session.add(staliukas)
            db.session.commit()
            flash('Staliukas pridėtas', 'success')
        except IntegrityError:
            flash('Toks staliukas jau egzistuoja, bandykite pakeisti duomenis')

    return render_template('restorano_staliukas.html', form=form)


@restaurant.route('/restorano_meniu', methods=['GET'])
@login_required
def meniu():
    patiekalai = Patiekalas.query.all()
    return render_template('restorano_meniu.html', patiekalai=patiekalai)
@restaurant.route('/r_paskyra')
@login_required
def paskyra():
    restoranas= Restoranas.query.first()
    return render_template('r_paskyra.html', restoranas=restoranas)

@restaurant.route('/prideti_talonelis')
@login_required
def prideti_taloneli():
    return render_template('prideti_restorano_taloneli.html')