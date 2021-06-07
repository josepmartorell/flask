"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import (request, render_template, url_for, redirect) 
from flaskproject import app
from flaskproject.models import Note
from flaskproject.forms import NoteForm
from flaskproject import db

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    notes = Note.query.filter_by(is_deleted=False).all()

    return render_template(
        'index.html',
        title='Note List',
        year=datetime.now().year,
        notes = notes,
    )

@app.route('/new-note', methods=['GET','POST'])
def create_note():

     if request.method == 'POST':        
         form = NoteForm(request.form)
         if form.validate():             
              note = Note(form.subject.data, form.detail.data)         
              db.session.add(note)
              db.session.commit()
              return redirect(url_for('home'))
     else:        
         form  = NoteForm()
         return render_template(
           'create_note.html',
           title='Create New Note',
           year=datetime.now().year,
           form = form
         )

@app.route('/note/<int:id>/detail/')
def note_detail(id):  
    note = Note.query.get(id)
    return render_template(
        'note_detail.html',
        title='Note Detail',
        year=datetime.now().year,
        note =note
    )

@app.route('/note/<int:id>/edit/', methods=['GET','POST'])
def edit_note(id):
    
    if request.method == 'POST':
         note = Note.query.get(id)
         form = NoteForm(request.form)
         if form.validate(): 
              note.edit(form.subject.data, form.detail.data)
              db.session.commit()
              return redirect(url_for('home'))
    else:
         note = Note.query.get(id)
         form  = NoteForm()
         form.subject.data= note.subject
         form.detail.data = note.detail

         return render_template(
          'edit_note.html',
          title='Edit Note',
          year=datetime.now().year,
          form = form,
          note_id = note.id,
          ) 
     
@app.route('/note/<int:id>/delete/')
def delete_note(id):
    note = Note.query.get(id)
    note.delete()
    db.session.commit()
    return redirect(url_for('home'))
