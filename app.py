from random import choice
from flask import Flask, redirect, render_template, request, abort

from data import db_session
from data.products import Products
from forms.add_code import AddCodeForm
from forms.input_form import FindForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/", methods=["POST", "GET"])
def index():
    form = FindForm()
    result = []
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        result = db_sess.query(Products).filter(Products.code == form.code.data).all()

        # print(result)
    return render_template("index.html", form=form, result=result)


@app.route("/add_code", methods=["POST", "GET"])
def add_code():
    form = AddCodeForm()

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        print(f"title={form.title.data}, about=form.about.data, price=form.price.data, code={form.code.data}")
        product = Products(title=form.title.data, about=form.about.data, price=form.price.data, code=form.code.data)
        db_sess.add(product)
        db_sess.commit()
        return redirect("/")
    return render_template("add_code.html", form=form)


if __name__ == '__main__':
    # a = """
    # <p>
    #         {{ form.about.label }}<br>
    #         {{ form.about(class="form-control") }}<br>
    #         {% for error in form.about.errors %}
    #             <p content="alert alert-danger" role="alert">
    #                 {{ error }}
    #             </p>
    #         {% endfor %}
    #     </p>
    # """
    # print(a.replace("about", "price"))
    db_session.global_init("db/mars.db")
    app.run()