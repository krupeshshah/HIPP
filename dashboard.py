# from doctest import master
# from logging import root
# from tkinter import Canvas
from flask import Blueprint, render_template, redirect, url_for, send_file
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dashboard = Blueprint("Dashboard", __name__)

@dashboard.route('/')
@dashboard.route('/home')
def index():
    # render_template(url_for("dashboard/smoker"))
    return render_template("dashboard.html")

insurance_dataset = pd.read_csv("./insurance.csv")

# @dashboard.route("/<argument>")
# def dashboardHome(argument):
#     print("1")
#     fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(8,8))
#     print("2")
#     if argument == "ageDistribution":
#         print(1)
#         ageDistribution()
#         ax1.set_title('Age Distribution')
#         # ax1. title('Age Distribution')
#     elif argument == "sexDistribution" :
#         gender()
#         ax2.title('Sex Distribution')
#         "gender"
#     elif argument == "bmiDistribution" :
#         gender()
#         ax3.title('BMI Distribution')
#     elif argument == "children" :
#         gender()
#         ax4.title('Children')
#         "gender"
#     else :
#         # axs[0,0] = ageDistribution()
#         sns.distplot(insurance_dataset['age'])
#         ax1.set_title('Age Distribution')
#         print("Age Distribution")

#         # axs[0,1] = gender()
#         sns.countplot(x='sex', data=insurance_dataset)
#         ax2.set_title('Sex Distribution')
#         print("gender Distribution")
    
#         # axs[1,0] = bmiDistribution()
#         sns.distplot(insurance_dataset['bmi'])
#         ax3.set_title('BMI Distribution')
#         print("BMI Distribution")

#         # axs[1,1] = children()
#         sns.countplot(x='children', data=insurance_dataset)
#         ax4.set_title('Children')
#         print("Children Distribution")
#         finalfig = plt.figure
#     print("3")
#     finalfig = BytesIO()
#     print("3")
#     plt.savefig(finalfig)
#     print("3")
#     finalfig.seek(0)
#     print("3")
#     return send_file(finalfig, mimetype="img/png")

@dashboard.route("/<argument>")
def dashboardHome(argument):
    
    if argument == "ageDistribution":
        fig, axs = plt.subplots(1, 1, figsize=(5,5))
        sns.distplot(insurance_dataset['age'])
        axs.set_title('Age Distribution')

    elif argument == "sexDistribution" :
        fig, axs = plt.subplots(1, 1, figsize=(5,5))
        sns.countplot(x='sex', data=insurance_dataset)
        axs.set_title('Sex Distribution')

    elif argument == "bmiDistribution" :
        fig, axs = plt.subplots(1, 1, figsize=(5,5))
        sns.distplot(insurance_dataset['bmi'])
        axs.set_title('BMI Distribution')

    elif argument == "children" :
        fig, axs = plt.subplots(1, 1, figsize=(5,5))
        sns.countplot(x='children', data=insurance_dataset)
        axs.set_title('Children')

    elif argument == "smoker" :
        fig, axs = plt.subplots(1, 1, figsize=(5,5))
        sns.countplot(x='smoker', data=insurance_dataset)
        axs.set_title('Smoker')
        
    elif argument == "region" :
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))
        sns.countplot(x='region', data=insurance_dataset, ax=ax1)
        ax1.set_title('Region')

        regions = np.unique(insurance_dataset['region'])

        print(regions)
        region1 = insurance_dataset[insurance_dataset['region'] == regions[0]]['region']
        region2 = insurance_dataset[insurance_dataset['region']== regions[1]]['region']
        region3 = insurance_dataset[insurance_dataset['region']== regions[2]]['region']
        region4 = insurance_dataset[insurance_dataset['region']== regions[3]]['region']
        regions_count = [region1.count(),region2.count(),region3.count(),region4.count()]
    
        print(regions_count)
        # ax2.pie(regions_count,labels = regions)
        ax2.set_title('Region')

        # Creating color parameters
        colors = ( "orange", "cyan", "brown","grey")
        # Creating explode data
        explode = (0.1, 0.0, 0.2, 0.3)
        wp = { 'linewidth' : 1, 'edgecolor' : "green" }

        def func(pct, allvalues):
            absolute = int(pct / 100.*np.sum(allvalues))
            return "{:.1f}%\n({:d} )".format(pct, absolute)
 
        # Creating plot
        wedges, texts, autotexts = ax2.pie(regions_count,
                                        autopct = lambda pct: func(pct, regions_count),
                                        labels = regions,
                                        shadow = True,
                                        colors = colors,
                                        explode = explode,
                                        startangle = 90,
                                        wedgeprops = wp,
                                        textprops = dict(color ="magenta"))

    else :
        # print("Age Distribution")
        fig, axs = plt.subplots(2, 3, figsize=(20,10))
        sns.distplot(insurance_dataset['age'], ax=axs[0,0])
        axs[0,0].set_title('Age Distribution')

        # print("Sex Distribution")
        sns.countplot(x='sex', data=insurance_dataset, ax=axs[0,1])
        axs[0,1].set_title('Sex Distribution')
    
        # print("BMI Distribution")
        sns.distplot(insurance_dataset['bmi'], ax=axs[0,2])
        axs[0,2].set_title('BMI Distribution')

        # print("Children Distribution")
        sns.countplot(x='children', data=insurance_dataset, ax=axs[1,0])
        axs[1,0].set_title('Children')

        # smoker Count
        sns.countplot(x='smoker', data=insurance_dataset, ax=axs[1,1])
        axs[1,1].set_title('Smoker')

        #Region 
        sns.countplot(x='region', data=insurance_dataset,ax=axs[1,2])
        axs[1,2].set_title('Region')
        
        # finalfig = plt.figure

    finalfig = BytesIO()
    plt.savefig(finalfig)
    finalfig.seek(0)
    return send_file(finalfig, mimetype="img/png")
  

# @dashboard.route('/<name>')
# def user(name):
#     # redirect(url_for("index"))
#     return f"Hello {name}!"