import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import string
import random

def compare_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                 xlabel: str,ylabel:str,title:str,label1:str,label2:str):
    """
    Funkcja do porównywania dwóch wykresów typu *plot*.  
    Szczegółowy opis znajduje się w zadaniu 3.

    Parameters
    ----------
    x1 : np.ndarray  
        Wektor wartości osi X dla pierwszego wykresu.  
    y1 : np.ndarray  
        Wektor wartości osi Y dla pierwszego wykresu.  
    x2 : np.ndarray  
        Wektor wartości osi X dla drugiego wykresu.  
    y2 : np.ndarray  
        Wektor wartości osi Y dla drugiego wykresu.  
    xlabel : str  
        Etykieta osi X.  
    ylabel : str  
        Etykieta osi Y.  
    title : str  
        Tytuł wykresu.  
    label1 : str  
        Opis serii danych z pierwszego wykresu (legenda).  
    label2 : str  
        Opis serii danych z drugiego wykresu (legenda).  

    Returns
    -------
    matplotlib.pyplot.figure  
        Wykres porównujący dane (x1, y1) i (x2, y2), zgodny z opisem z zadania 3.  
    """

    if x1.shape != x2.shape or y1.shape != y2.shape or min(x1.shape)==0 or min(x2.shape)==0 or min(y1.shape)==0 or min(y2.shape)==0 :
        return None
    fig, ax = plt.subplots()
    ax.plot(x1, y1, 'b', label=label1)
    ax.plot(x2, y2, 'r', label=label2)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.legend()
    return fig


def parallel_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                  x1label:str,y1label:str,x2label:str,y2label:str,title:str,orientation:str):
    """
    Funkcja do tworzenia dwóch wykresów typu *plot* w układzie subplot.  
    Wykresy mogą być ustawione pionowo lub poziomo.  
    Szczegółowy opis znajduje się w zadaniu 5.

    Parameters
    ----------
    x1 : np.ndarray  
        Wektor wartości osi X dla pierwszego wykresu.  
    y1 : np.ndarray  
        Wektor wartości osi Y dla pierwszego wykresu.  
    x2 : np.ndarray  
        Wektor wartości osi X dla drugiego wykresu.  
    y2 : np.ndarray  
        Wektor wartości osi Y dla drugiego wykresu.  
    x1label : str  
        Etykieta osi X dla pierwszego wykresu.  
    y1label : str  
        Etykieta osi Y dla pierwszego wykresu.  
    x2label : str  
        Etykieta osi X dla drugiego wykresu.  
    y2label : str  
        Etykieta osi Y dla drugiego wykresu.  
    title : str  
        Tytuł całej figury.  
    orientation : str  
        Określa układ subplotów:  
        - `'-'` → dwa wiersze (układ pionowy),  
        - `'|'` → dwie kolumny (układ poziomy).  

    Returns
    -------
    matplotlib.pyplot.figure  
        Figura z dwoma wykresami (x1, y1) i (x2, y2), zgodna z opisem z zadania 5.  
    """
    
    if x1.size == 0 or y1.size == 0 or x2.size == 0 or y2.size == 0:
        return None
    if  x2.size != y2.size or x1.size != y1.size:
        return None
    if len(np.unique(x1)) != x1.size or len(np.unique(x2)) != x2.size:
        return None
    if orientation == '-':
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    elif orientation == '|':
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 12))
    else:
        return None
    
    ax1.plot(x1, y1)
    ax2.plot(x2, y2)
    ax1.set(xlabel=x1label, ylabel=y1label)
    ax2.set(xlabel=x2label, ylabel=y2label)
    fig.suptitle(title)
    plt.show()
    return fig

def log_plot(x:np.ndarray,y:np.ndarray,xlabel:np.ndarray,ylabel:str,title:str,log_axis:str):
    if x.size == 0 or y.size == 0 or x.size != y.size:
        return None

    if log_axis not in ['x', 'y', 'xy']:
        return None

    mask = (x > 0) & (y > 0) if log_axis == 'xy' else \
           (x > 0) if log_axis == 'x' else \
           (y > 0) if log_axis == 'y' else np.ones_like(x, dtype=bool)

    x = x[mask]
    y = y[mask]

    fig, ax = plt.subplots()
    ax.plot(x, y)

    if log_axis == 'x':
        ax.set_xscale('log')
    elif log_axis == 'y':
        ax.set_yscale('log')
    elif log_axis == 'xy':
        ax.set_xscale('log')
        ax.set_yscale('log')

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    plt.show()
    return fig
