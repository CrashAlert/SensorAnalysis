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
    plt.plot(gyrx, label='x gyroscope', linewidth=0.3)
    plt.plot(gyry, label='y gyroscope', linewidth=0.3)
    plt.plot(gyrz, label='z gyroscope', linewidth=0.3)
    plt.ylabel('Speed in $deg/s$')
    plt.legend()
    plt.show()
    
def plot_mag(data, plt):
    magx = np.vectorize(id)(data['mag_x'].dropna())
    magy = np.vectorize(id)(data['mag_y'].dropna())
    magz = np.vectorize(id)(data['mag_z'].dropna())
    plt.plot(magx, label='x magnetic field', linewidth=0.3)
    plt.plot(magy, label='y magnetic field', linewidth=0.3)
    plt.plot(magz, label='z magnetic field', linewidth=0.3)
    plt.ylabel('Field force in uT')
    plt.legend()
    plt.show()
    
def plot_bearing(data, plt):
    course = np.vectorize(id)(data['bearing'].dropna())
    plt.plot(course, label='GPS reported course', linewidth=0.7)
    plt.ylabel('Course in degree')
    plt.legend()
    plt.show()
    
def plot_gps_errors(data, plt):
    errlat = np.vectorize(id)(data['err_lat'].dropna())
    errlng = np.vectorize(id)(data['err_lng'].dropna())
    plt.plot(errlat, label='lat error', linewidth=0.5)
    plt.plot(errlng, label='lng error', linewidth=0.5)
    plt.ylabel('GPS error in meters')
    plt.legend()
    plt.show()
    
def plot_pressure(data, plt):
    pressure = np.vectorize(id)(data['pressure'].dropna())
    plt.plot(pressure, label='Pressure')
    plt.ylabel('Pressure in mBar')
    plt.legend()
    plt.show()                 
    
def plot_altitude(data, plt):
    altitude = np.vectorize(id)(data['alt'].dropna())
    plt.plot(altitude, label='GPS reported altitude', linewidth=0.7)
    plt.ylabel('Height in meters')
    plt.legend()
    plt.show()

fun_dict = {
        'Acceleration': plot_acc,
        'Linear Acceleration': plot_lin_acc,
        'Rotation': plot_rot,
        'Gyroscope': plot_gyr,
        'Magnetometer': plot_mag,
        'GPS Bearing': plot_bearing,
        'GPS Errors': plot_gps_errors,
        'Pressure': plot_pressure,
        'GPS Altitude': plot_altitude,
    }