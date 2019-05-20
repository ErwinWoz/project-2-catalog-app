import sys
import os
import httplib2
import json
import datetime
import uuid
import requests
from functools import wraps
from flask import Flask, session, redirect, render_template, request, url_for
from flask import flash, jsonify, make_response
from flask import session as login_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, User, Categories, Items
from oauth2client import client
from oauth2client.client import flow_from_clientsecrets, verify_id_token
from oauth2client.client import FlowExchangeError
# from apiclient import discovery

APP_PATH = os.path.dirname(os.path.abspath(__file__))

CLIENT_ID = json.load(open('client_secret.json', 'r'))['web']['client_id']

app = Flask(__name__)


# Connect to Database and create database session
engine = create_engine('sqlite:///catalog.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create default view
@app.route('/')
@app.route('/catalog')
def home():
    categories = session.query(Categories).all()
    recentItems = session.query(Items).order_by(Items.updated.desc()).limit(5).all()
    return render_template('home.html', categories=categories,
                           recentItems=recentItems, login = False if  'username' not in login_session else True)


# Create a state token to stop forgery
@app.route('/signin')
def signin():
    state = uuid.uuid4()
    login_session['state'] = unicode(str(state),'utf-8')
    return render_template('signin.html', state=state)


@app.route('/signout')
def signout():
    print(type(login_session))
    del login_session["username"]
    return render_template('signout.html')


# Validate state token
@app.route('/gconnect', methods=['POST'])
def gconnect():
    print(request.args.get("state") ,"==", login_session["state"])
    if(str(request.args.get("state")) != str(login_session["state"])):
        print("Invalid State")
        response = make_response(json.dumps("Invalid State parameter"),401)
        response.headers["Content-Type"] = "application/json"
        return response

    code = request.data
    try:
        print("code", code)
        oauth_flow = flow_from_clientsecrets( os.path.join(APP_PATH, "client_secret.json"), scope="")
        oauth_flow.redirect_uri = 'postmessage'
        oauth_flow.access_type ='offline'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError as e:
        print('Authentication has failed: {}'.format(str(e)))
        response = make_response(json.dumps("Failed to upgrade"),401)
        response.headers["Content-Type"] = "application/json"
        return response

    access_token = credentials.access_token

    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    print(result)

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                    200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = access_token
    #login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    # flash("you are now logged in as %s" % login_session['username'])
    print("done!")
    return output


# View category with its items
@app.route('/catalog/<string:category>/items/')
@app.route('/catalog/<string:category>/')
def categoryView(category):
    categories = session.query(Categories).all()
    category = session.query(Categories).filter_by(name=category).one()
    items = session.query(Items).filter_by(categories_id=category.id).all()
    return render_template('category.html', items=items, categories=categories, category=category, login = False if  'username' not in login_session else True)


# Item description
@app.route('/catalog/<string:category>/<string:item>/')
def itemView(category, item):
    category_id = session.query(Categories).filter_by(name=category).one().id
    item = session.query(Items).filter_by(categories_id=category_id, title=item).one()
    return render_template('item.html', item=item, category=category, login = False if  'username' not in login_session else True)


# Edit existing item in catalog
@app.route('/catalog/<string:category>/<string:item>/edit', methods=['GET', 'POST'])
def editItem(category, item):
    if 'username' not in login_session:
        flash("Please log in to continue.")
        return redirect(url_for('signin'))

    editedItem = session.query(Items).filter_by(title=item).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.title = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        # if request.form['category']:
        #     editedItem.categories = request.form['category']
        session.add(editedItem)
        session.commit()
        #flash('ITEM UPDATED')
        return redirect(url_for('categoryView', category=category))
    else:
        return render_template('item-edit.html', category=category, item=item, i=editedItem, login = False if  'username' not in login_session else True)


# Add new item to catalog
@app.route('/catalog/new/', methods=['GET', 'POST'])
def newItem():
    if 'username' not in login_session:
        flash("Please log in to continue.")
        return redirect('/signin')
    else:
        if request.method == 'POST':
            newItem = Items(title=request.form['name'],
                            description=request.form['description'],
                            updated=datetime.datetime.now(),
                            categories_id=int(request.form['category']))
            session.add(newItem)
            session.commit()
            # flash('NEW ITEM ADDED')
            return redirect(url_for('home'))
        else:
            categories = session.query(Categories).all()
            return render_template('item-new.html', categories=categories, login = False if  'username' not in login_session else True)


# Delete item from catalog
@app.route('/catalog/<string:category>/<string:item>/delete', methods=['GET', 'POST'])
def deleteItem(category, item):
    if 'username' not in login_session:
        flash("Please log in to continue.")
        return redirect('/signin')
    else:
        category_id = session.query(Categories).filter_by(name=category).one().id
        itemToDelete = session.query(Items).filter_by(categories_id=category_id, title=item).one()
        if request.method == 'POST':
            session.delete(itemToDelete)
            session.commit()
            # flash('ITEM DELETED')
            return redirect(url_for('categoryView', category=category))
        else:
            categories = session.query(Categories).all()
            return render_template('item-delete.html', item=item, category=category, login = False if  'username' not in login_session else True)


# When using Google Chrome, the popular extention to format json object
# in the browser is JSONView:
# https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?hl=en

# JSON APIs to view all categories
@app.route('/catalog/JSON')
def categoryJSON():
    categories = session.query(Categories).all()
    return jsonify(categories=[c.serialize for c in categories])


# JSON APIs to view all items in category
@app.route('/catalog/<string:category>/JSON')
def categoryItemData(category):
    category_id = session.query(Categories).filter_by(name=category).one().id
    items = session.query(Items).filter_by(categories_id=category_id).all()
    return jsonify(items=[i.serialize for i in items])


# JSON APIs to view item
@app.route('/catalog/<string:category>/<string:item>/JSON')
def itemJSON(category, item):
    category_id = session.query(Categories).filter_by(name=category).one().id
    item = session.query(Items).filter_by(title=item, categories_id=category_id).one()
    return jsonify(item=item.serialize)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
