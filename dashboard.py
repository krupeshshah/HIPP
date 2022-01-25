# from doctest import master
# from logging import root
# from tkinter import Canvas
from flask import Blueprint, render_template, redirect, url_for, send_file
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dashboard = Blueprint("Dashboard", __name__)

@dashboard.route('/')
@dashboard.route('/home')
def index():
    # render_template(url_for("dashboard/smoker"))
    return render_template("dashboard.html")

insurance_dataset = pd.read_csv("./insurance.csv")

@dashboard.route('ageDistribution')
def ageDistribution():
    # insurance_dataset = pd.read_csv("./insurance.csv")
    sns.set()
    sns.set_style(style="darkgrid")
    plt.figure(figsize=(4,4))
    somker_fig = sns.distplot(insurance_dataset['age'])
    plt.title('Age Distribution')
    somker_img = BytesIO()
    plt.savefig(somker_img)
    somker_img.seek(0)
    return send_file(somker_img, mimetype="img/png")

@dashboard.route('gender')
def gender():
    # insurance_dataset = pd.read_csv("./insurance.csv")
    sns.set()
    sns.set_style(style="darkgrid")
    plt.figure(figsize=(4,4))
    gender_fig = sns.countplot(x='sex', data=insurance_dataset)
    plt.title('Sex Distribution')
    gender_img = BytesIO()
    plt.savefig(gender_img)
    gender_img.seek(0)
    return send_file(gender_img, mimetype="img/png")

@dashboard.route('bmiDistribution')
def bmiDistribution():
    # insurance_dataset = pd.read_csv("./insurance.csv")
    bmi_ax = sns.set_style(style="darkgrid")
    sns.set()
    plt.figure(figsize=(4,4))
    bmi_fig = sns.distplot(insurance_dataset['bmi'])
    plt.title('BMI Distribution')
    bmi_img = BytesIO()
    plt.savefig(bmi_img)
    bmi_img.seek(0)
    return send_file(bmi_img, mimetype="img/png")

@dashboard.route('children')
def children():
    # insurance_dataset = pd.read_csv("./insurance.csv")
    children_ax = sns.set_style(style="darkgrid")
    print("3")
    sns.set()
    plt.figure(figsize=(4,4))
    children_fig = sns.countplot(x='children', data=insurance_dataset)
    plt.title('Children')
    children_img = BytesIO()
    plt.savefig(children_img)
    children_img.seek(0)
    return send_file(children_img, mimetype="img/png")

    

# @dashboard.route('/<name>')
# def user(name):
#     # redirect(url_for("index"))
#     return f"Hello {name}!"