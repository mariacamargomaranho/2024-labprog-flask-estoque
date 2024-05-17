from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required

from src.forms.categoria import NovoCategoriaForm, EditCategoriaForm
from src.modules import db
from src.models.categoria import Categoria
import  sqlalchemy as sa

bp = Blueprint('categoria', __name__, url_prefix='/categoria')


@bp.route('/', methods=['GET',])
def lista():
    senteca = sa.select(Categoria).order_by(Categoria.nome)
    rset = db.session.execute(senteca).scalars()

    return render_template('categoria/lista.jinja2',
                           rset=rset)


@bp.route('/add', methods=['GET','POST'])
@login_required
def add():
    form = NovoCategoriaForm()
    if form.validate_on_submit():
        categoria = Categoria()
        categoria.nome = form.nome.data
        db.session.add(categoria)
        flash(f"Categoria '{form.nome.data}' adicionada")
        return redirect(url_for('categoria.lista'))


    return render_template('categoria/add_edit.jinja2',
                           title='Nova Categoria',
                           form=form)

@bp.route('/edit/<uuid:categoria_id>', methods=['GET','POST'])
@login_required
def edit(categoria_id):
    categoria = Categoria.get_by_id(categoria_id)

    if categoria is None:
        flash("Categoria inexistente", category="warning")
        return redirect(url_for('categoria.lista'))

    form = EditCategoriaForm(request.values,obj=categoria)
    if form.validate_on_submit():
        categoria.nome = form.nome.data
        db.session.commit()
        return redirect(url_for('categoria.lista'))
        flash("Categoria alterada", category='success')

    return render_template('categoria/add_edit.jinja2',
                           title='Editar categoria',form=form)

@bp.route('/del/<uuid:categoria_id>', methods=['GET', 'POST'])
@login_required
def remove(categoria_id):
    categoria = Categoria.get_by_id(categoria_id)
    if categoria is None:
        flash("Categoria inexistente", category="warning")
        return redirect(url_for('categoria.lista'))

    db.session.delete(categoria)
    db.session.commit()
    flash("Categoria removida", category='success')
    return redirect(url_for('categoria.lista'))















