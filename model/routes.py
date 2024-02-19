from flask import render_template, redirect, request, url_for, flash
from model import app
from model.algorithm import Recommendation
from model.forms import DataEntry
from model.poster import fetch_poster, default_movies

@app.route('/', methods=['GET','POST'])
def home_page():
    form = DataEntry()
    if request.method == 'POST':
        if form.validate_on_submit():
            category = form.category.data
            value = form.value.data
            return redirect(url_for('result_page', value=value, category=category))

    return render_template('base.html', form=form, movies=default_movies)
    


@app.route('/recommendations', methods=['GET','POST'])
def result_page():
    category = str(request.args.get('category'))
    value = str(request.args.get('value'))
    
    form = DataEntry()
    if request.method == 'POST':
        if form.validate_on_submit():
            category = form.category.data
            value = form.value.data
            return redirect(url_for('result_page', value=value, category=category))

    rec = Recommendation()
    category, value = rec.rectification(category, value)
    
    movies = rec.recommend(category, value)
    if movies is not None:
        print('movies not null')
        movies = fetch_poster(movies)
    else: 
        flash('Data for the filter is unavailble in the database')
        movies = default_movies
    return render_template('recommended.html', movies=movies, form=form)
    
