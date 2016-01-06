"""spec:
{
    'row_name' : ['name', 'format'],
    'row_name' : 'name'
}"""

sensor_dict = {
    'time' : ['time', 'ns'],
    'acc_x' : ['x-axis acceleration', '$m/s^2$'],
    'acc_y' : ['y-axis acceleration', '$m/s^2$'],
    'acc_z' : ['z-axis acceleration', '$m/s^2$'],
    'lin_acc_x' : ['x-axis linear acceleration (android)', '$m/s^2'],
    'lin_acc_y' : ['y-axis linear acceleration (android)', '$m/s^2'],
    'lin_acc_z' : ['z-axis linear acceleration (android)', '$m/s^2'],
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
    'err_lat' : ['GPS reported lat error', 'm'],
    'err_lng' : ['GPS reported lng error', 'm'],
    'pressure' : ['Pressure', 'mBar'],
    'station' : 'Sys State iOS',
    'run' : 'Sys State iOS',
    'walk' : 'Sys State iOS',
    'auto' : 'Sys State iOS',
    'cycling' : 'Sys State iOS',
    'unknown' : 'Sys State iOS'
}