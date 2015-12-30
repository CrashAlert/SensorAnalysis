"""spec:
{
    'row_name' : ['name', 'format']
}"""

sensor_dict = {
    'unix_time' : ['time', 'ms'],
    'acc_x' : ['x-axis acceleration', '$m/s^2$'],
    'acc_y' : ['y-axis acceleration', '$m/s^2$'],
    'acc_z' : ['z-axis acceleration', '$m/s^2$'],
    'lin_acc' : ['linear acceleration', '$m/s^2'],
    'gyr_x' : ['x-axis gyro acceleration', '$rad/s$'],
    'gyr_y' : ['y-axis gyro acceleration', '$rad/s$'],
    'gyr_z' : ['z-axis gyro acceleration', '$rad/s$'],
    'rot_x' : ['rotation x', 'scalar'],
    'rot_y' : ['rotation y', 'scalar'],
    'rot_z' : ['rotation z', 'scalar'],
    'mag_x' : ['field force x', '$\mu T$'],
    'mag_y' : ['field force y', '$\mu T$'],
    'mag_z' : ['field force z', '$\mu T$'],
    'lat' : ['Latitude', 'deg'],
    'lng' : ['Longitude', 'deg'],
    'bearing' : ['Bearing', 'deg'],
    'speed' : ['Speed', '$m/s$'],
    'alt' : ['Altitude', 'm'],
    'gnss_err' : ['GPS reported error', 'm']
}