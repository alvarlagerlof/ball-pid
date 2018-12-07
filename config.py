# servo
class Conf:
    
    # Servo
    servo_startup = 0.5
    servo_sleep = 0.15
    
    # 0.3s for 90deg
    # 0.5s for 180deg
    
    
    servo_max = 175
    servo_min = 5
    servo_range = servo_max - servo_min
	
	
    # Camera
    cam_width = 250
    cam_height = cam_width * 0.75
    
    cam_buffer = 128
    cam_ball_min = 3
    
    cam_x_min = -150
    cam_x_max = 150
    cam_y_min = -100
    cam_y_max = 100
    cam_x_range = (cam_x_max-(cam_x_min))
    cam_y_range = (cam_y_max-(cam_y_min))
    
	
	
    # PID
    P = 0.3
    I = 0.00045
    D = 0.4
    PID_iteration_time = 70

    #P = 0.0001
    #I = 200
    #D = 7
    #PID_iteration_time = 100
	
	
conf = Conf()

