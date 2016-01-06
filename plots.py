import numpy as np
import pandas as pd

def id(x):
    return x


def abs_force(x, y, z):
    return np.sqrt(x ** 2 + y ** 2 + z ** 2)


def plot_acc(data, plt):
    forcex = np.vectorize(id)(data['acc_x'].dropna())
    forcey = np.vectorize(id)(data['acc_y'].dropna())
    forcez = np.vectorize(id)(data['acc_z'].dropna())
    forces = np.vectorize(abs_force)(forcex, forcey, forcez)
    plt.plot(forces, label='Total force', linewidth=0.7)
    plt.plot(forcex, label='x force', linewidth=0.3)
    plt.plot(forcey, label='y force', linewidth=0.3)
    plt.plot(forcez, label='z force', linewidth=0.3)
    plt.ylabel('Force in $m/s^2$')
    plt.legend()
    plt.show()
    
def plot_lin_acc(data, plt):
    forcex = np.vectorize(id)(data['lin_acc_x'].dropna())
    forcey = np.vectorize(id)(data['lin_acc_y'].dropna())
    forcez = np.vectorize(id)(data['lin_acc_z'].dropna())
    forces = np.vectorize(abs_force)(forcex, forcey, forcez)
    plt.plot(forces, label='Total force', linewidth=0.7)
    plt.plot(forcex, label='x force', linewidth=0.3)
    plt.plot(forcey, label='y force', linewidth=0.3)
    plt.plot(forcez, label='z force', linewidth=0.3)
    plt.ylabel('Force in $m/s^2$')
    plt.legend()
    plt.show()
    
def plot_rot(data, plt):
    rotx = np.vectorize(id)(data['rot_x'].dropna())
    roty = np.vectorize(id)(data['rot_y'].dropna())
    rotz = np.vectorize(id)(data['rot_z'].dropna())
    plt.plot(rotx, label='x rotation', linewidth=0.3)
    plt.plot(roty, label='y rotation', linewidth=0.3)
    plt.plot(rotz, label='z rotation', linewidth=0.3)
    plt.legend()
    plt.show()
    
def plot_gyr(data, plt):
    gyrx = np.vectorize(id)(data['gyr_x'].dropna())
    gyry = np.vectorize(id)(data['gyr_y'].dropna())
    gyrz = np.vectorize(id)(data['gyr_z'].dropna())
    plt.plot(rotx, label='x gyroscope', linewidth=0.3)
    plt.plot(roty, label='y gyroscope', linewidth=0.3)
    plt.plot(rotz, label='z gyroscope', linewidth=0.3)
    plt.ylabel('Speed in $deg/s$')
    plt.legend()
    plt.show()
    
def plot_

fun_dict = {
        'plot_acc': plot_acc,
        'plot_lin_acc': plot_lin_acc,
        'plot_rot': plot_rot,
        'plot_gyr': plot_gyr,
    }
    
def plots(name):
    return fun_dict[name]