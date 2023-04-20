import matplotlib.pyplot as plt

#Funciones de visualizaciones:

def create_scatter():
    plt.scatter([1,2,3],[4,5,6])

    filename = "fig1.png"
    plt.savefig(filename)
    print(f"Saved as {filename}")
    plt.close()

Buenísimas

def create_bar_plot():
    plt.bar(['A','B','C','D'],[4,3,4,5],)

    filename = "fig2.png"
    plt.savefig(filename)
    print(f"Saved as {filename}")
    plt.close()
