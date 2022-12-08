from sqlalchemy.exc import IntegrityError
import bcrypt
from flask import Blueprint, redirect, render_template, url_for, flash
from flask_login import current_user, logout_user
from flask_bcrypt import Bcrypt

c_auth = Blueprint('c_auth', __name__)
bcrypt=Bcrypt()


# Kliento registracijos puslapis
@c_auth.route('/kliento_reg', methods=['POST', 'GET'])
def registruotis():
    from . import db,forms
    from models import Klientas
    db.create_all()
    if current_user.is_authenticated:
        return redirect(url_for('base_routes.index'))
    form = forms.KlientoRegForma()
    if form.validate_on_submit():
        try:
            koduotas_slaptazodis = bcrypt.generate_password_hash(form.slaptazodis.data).decode('utf-8')
            klientas = Klientas(name=form.vardas.data, email=form.el_pastas.data, slaptazodis=koduotas_slaptazodis,
                                telefonas=form.telefonas.data)
            db.session.add(klientas)
            db.session.commit()
            flash('Sekmingai prisiregistravote! Galite prisijungti', 'success')
            return redirect(url_for('login.prisijungti'))
        except IntegrityError:
            db.session.rollback()
            flash('Toks vartotojas jau egzistuoja', 'warning')
    return render_template('kliento_reg.html', form=form)




# Kliento atsijungimas nuo puslapio
@c_auth.route('/atsijungti')
def atsijungti():
    logout_user()
    return redirect(url_for('base_routes.index'))