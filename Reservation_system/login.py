from flask_login import current_user, login_user
from flask import redirect, url_for, flash, render_template
from Reservation_system.models import Klientas, Restoranas
from Reservation_system.restaurant_auth import bcrypt, r_auth
from flask import Blueprint
from flask_bcrypt import Bcrypt

login = Blueprint('login', __name__)
bcrypt = Bcrypt()
# Kliento prisijungimas prie puslapio
@login.route('/prisijungti', methods=['POST', 'GET'])
def prisijungti():
    import forms
    if current_user.is_authenticated:
        return redirect(url_for('client.kliento_main'))
    form = forms.KlientoPrisijungimoForma()
    if form.validate_on_submit():
        user = Klientas.query.filter_by(email=form.el_pastas.data).first()
        if user and bcrypt.check_password_hash(user.slaptazodis, form.slaptazodis.data):
            login_user(user, remember=form.prisiminti.data)
            return redirect(url_for('client.kliento_main'))
            from . import db
            db.session.add(klientas)
            db.session.commit()
        else:
            flash('Nesekmingas prisijungtimas. Patikrinkite el.pasta ir slaptazodi.', 'danger')
    return render_template('prisijungti.html', form=form)


# Restorano prisijungimas
@r_auth.route('/restorano_prisijungimas', methods=['POST', 'GET'])
def rest_login():
    import forms
    if current_user.is_authenticated:
        return redirect(url_for('restaurant.rest_main'))
    form = forms.RestoranoPrisijungimoForma()
    if form.validate_on_submit():
        user = Restoranas.query.filter_by(email=form.restorano_el_pastas.data).first()
        if user and bcrypt.check_password_hash(user.slaptazodis, form.slaptazodis.data):
            login_user(user, remember=form.prisiminti.data)
        return redirect(url_for('restaurant.rest_main'))
        from . import db
        db.session.add(restoranas)
        db.session.commit()
        flash('Sekmingai prisiregistravote! Galite prisijungti', 'success')
    return render_template('restorano_prisijungimas.html', form=form)

