#MAIN!

from app import app
from db_setup import init_db, db_session
from forms import ToolSearchForm, ToolForm
from flask import flash, render_template, request, redirect
from models import Tool, Bin
from tables import Results, Delete

init_db()

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    """
    Delete the item in the database
    """
    qry = db_session.query(Bin).filter(
        Bin.id==id)
    bin = qry.first()
    delete = Delete(qry)
    delete.border = True
    
    if bin:
        form = ToolForm(formdata=request.form, obj=bin)
        if request.method == 'POST' and form.validate():
            # delete the item from the databse
            db_session.delete(bin)
            db_session.commit()

            flash('Tool listing deleted successfully.')
            return redirect('/')
        return render_template('delete_tool.html', table=delete)
    else:
        return 'Error deleting #{id}'.format(id=id)

@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Bin).filter(
        Bin.id==id)
    bin = qry.first()

    if bin:
        form = ToolForm(formdata=request.form, obj=bin)
        if request.method == 'POST' and form.validate():
            # save edit
            save_changes(bin, form)
            flash('Tool listing updated successfully.')
            return redirect('/')
        return render_template('edit_tool.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)

@app.route('/', methods=['GET', 'POST'])
def index():
    search = ToolSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Tool Number':
            qry = db_session.query(Bin, Tool).filter(
                Tool.id==Bin.partnumber_id).filter(
                    Tool.name.contains(search_string))
            results = [item[0] for item in qry.all()]
            print('number search qry:')
            print(qry)
        elif search.data['select'] == 'Location':
            qry = db_session.query(Bin).filter(
                Bin.location.contains(search_string))
            results = qry.all()
            print('location search qry:')
            print(qry)
        else:
            qry = db_session.query(Bin)
            results = qry.all()
            print('search data else qry:')
            print(qry)
    else:
        qry = db_session.query(Bin)
        results = qry.all()
        print('search_string qry:')
        print(qry)

    if not results:
        print('not results')
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)

@app.route('/new_tool', methods=['GET', 'POST'])
def new_tool():
    """
    Add a new special tool
    """
    form = ToolForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the tool
        bin = Bin()
        save_changes(bin, form, new=True)
        flash('Tool listing created successfully.')
        return redirect('/')

    return render_template('new_tool.html', form=form)
    
def save_changes(bin, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    tool = Tool()
    tool.name = form.partnumber.data

    bin.partnumber = tool
    bin.location = form.location.data

    if new:
        # Add the new album to the database
        db_session.add(bin)

    # commit the data to the database
    db_session.commit()
    
if __name__ == '__main__':
    app.run(host= '0.0.0.0')
