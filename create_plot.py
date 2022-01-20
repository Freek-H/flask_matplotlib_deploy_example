import matplotlib.pyplot as plt
import pandas as pd


def create_plot():
    data = pd.read_csv('plot_data.csv')

    # Maak plot
    plt.scatter(data['Calcium (Ca)'], data['Phosphorus (P)'])
    plt.title('Ca vs. P in voedsel')
    plt.xlabel('Ca [mg/100g]')
    plt.ylabel('P [mg/100g]')
    plt.savefig('static/plot.png')
    plt.close()

    print('Created plot')
