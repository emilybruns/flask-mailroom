'''
Flask mailroom main file
'''

import os
from flask import Flask, render_template, request, redirect, url_for
from model import Donation
from model import Donor

app = Flask(__name__)

@app.route('/')
def home():
    '''
    Go to all donations page
    '''
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    '''
    All donations page
    '''
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/create', methods=['GET', 'POST'])
def create():
    '''
    Add a donation page
    '''
    if request.method == 'POST':
        try:
            donor = Donor.get(Donor.name == request.form['donor'])
        except Donor.DoesNotExist:
            donor = Donor(name=request.form['donor'])
            donor.save()

        donation=Donation(donor=donor, value=request.form['value'])
        donation.save()
        return redirect(url_for('all'))
    return render_template('create.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
