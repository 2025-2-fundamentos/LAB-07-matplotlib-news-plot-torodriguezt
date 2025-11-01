"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os
import pandas as pd
import matplotlib.pyplot as plt


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

     # Configuración de estilos para cada medio
    colors = {
        "Television": "dimgray",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "lightgrey"
    }

    zorder = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }

    linewidths = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 4,
        "Radio": 2,
    }

    # Leer datos
    df = pd.read_csv("files/input/news.csv", index_col=0)
    
    # Crear figura
    plt.figure(figsize=(10, 6))
    
    # Plotear líneas para cada medio
    for col in df.columns:
        plt.plot(
            df.index,
            df[col],
            color=colors[col],
            label=col,
            zorder=zorder[col],
            linewidth=linewidths[col],
        )
    
    # Configurar título y ejes
    plt.title("How people get their news", fontsize=16, loc="left", pad=20)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    # Añadir etiquetas y puntos en los extremos
    first_year = df.index[0]
    last_year = df.index[-1]
    
    for col in df.columns:
        # Punto y etiqueta al inicio
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col],
            s=50,
        )

        plt.text(
            first_year - 0.2,
            df[col][first_year],
            f"{col} {df[col][first_year]:.0f}%",
            ha="right",
            va="center",
            color=colors[col],
            fontsize=10,
        )

        # Punto y etiqueta al final
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
            zorder=zorder[col],
            s=50,
        )
        
        plt.text(
            last_year + 0.2,
            df[col][last_year],
            f"{df[col][last_year]:.0f}%",
            ha="left",
            va="center",
            color=colors[col],
            fontsize=10,
        )

    # Configurar xticks
    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha="center"
    )

    # Ajustar layout y guardar
    plt.tight_layout()
    os.makedirs("files/plots", exist_ok=True)
    plt.savefig("files/plots/news.png", dpi=300, bbox_inches='tight')
    plt.close()

pregunta_01()