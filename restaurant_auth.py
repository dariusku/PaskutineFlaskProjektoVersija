import bcrypt
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from flask_login import current_user, login_user, logout_user
from Reservation_system.models import Restoranas
from sqlalchemy.exc import IntegrityError

r_auth = Blueprint('rest_auth', __name__)
bcrypt = Bcrypt()

@r_auth.route('/restorano_reg', methods=['POST', 'GET'])
def res_registruotis():
    from Reservation_system import db
    from . import forms
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for('base_routes.index'))
    form = forms.RestoranoRegForma()
    if form.validate_on_submit():
        try:
            koduotas_slaptazodis = bcrypt.generate_password_hash(form.slaptazodis.data).decode('utf-8')
            restoranas = Restoranas(title=form.pavadinimas.data, email=form.restorano_el_pastas.data,
                                slaptazodis=koduotas_slaptazodis, telefonas=form.telefonas.data)
            db.session.add(restoranas)
            db.session.commit()
            flash('Sekmingai prisiregistravote! Galite prisijungti', 'success')
        except IntegrityError:
            db.session.rollback()
            flash('Restoranas su tokiu pavadinimu jau egzistuoja', 'warning')
            return redirect((url_for('rest_auth.res_registruotis')))
        return redirect(url_for('rest_auth.rest_login'))
    flash('Įvyko klaida. Patikrinkite įvestus duomenis ir bandykite vėl.')
    return render_template('restorano_reg.html', form=form)

@r_auth.route('/r_atsijungti')
def r_atsijungti():
    logout_user()
    return redirect(url_for('base_routes.index'))