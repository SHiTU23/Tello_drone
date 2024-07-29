import threading
import cv2
from djitellopy import Tello
import keyboard


condition = threading.Condition()
save_pic = False
tello = Tello()
tello.connect()
tello.streamon()

running = True
last_key = ''
def key_press():
    global save_pic
    global running
    global last_key
    rotation_degree = 10
    movement_distance = 20 ## in cm
    
    while running:
        print("KEY_ PRESSES**********")
        if keyboard.is_pressed('s') :
            print("Save pic state changed")
            save_pic = True
            skip_holdDown_key('s')

        elif keyboard.is_pressed('q'):
            print("break the loop")
            running = False
        ############ CONTROL COMMANDS ############
        ##########################################
        elif keyboard.is_pressed('up'):
            tello.takeoff()
            #skip_holdDown_key('up')
        elif keyboard.is_pressed('down'):
            tello.land()
            #skip_holdDown_key('down')
        elif keyboard.is_pressed('right'):
            tello.rotate_clockwise(rotation_degree)
            #skip_holdDown_key('right')
        elif keyboard.is_pressed('left'):
            tello.rotate_counter_clockwise(rotation_degree)
            #skip_holdDown_key('left')
        elif keyboard.is_pressed('w'):  ### move forward
            tello.move_forward(movement_distance)
            #skip_holdDown_key('w')
        elif keyboard.is_pressed('z'):  ### move backward
            tello.move_back(movement_distance)
            #skip_holdDown_key("z")
        elif keyboard.is_pressed('a'):  ### move to the left
            tello.move_left(movement_distance)
            #skip_holdDown_key('a')
        elif keyboard.is_pressed('d'):  ### move to the right
            tello.move_right(movement_distance)
            #skip_holdDown_key("d")



def skip_holdDown_key(key):
    while keyboard.is_pressed(key):
        pass

def stream_camera():
    global save_pic
    global last_key
    global running

    counter = 0
    counter_show = 0
    # running = True
    while running:
        counter_show += 1
        frame_read = tello.get_frame_read()

        if frame_read is not None:
            print("show pic", counter_show)
            frame = frame_read.frame
            cv2.imshow("picture.png", frame)

        if cv2.waitKey(1) & save_pic:
            last_key = ''
            save_pic = False
            counter += 1
            picture_name = './pics/pic' + str(counter) + '.jpg'
            print("PICTURE SAVED",picture_name)
            cv2.imwrite(picture_name, frame)
            
            
            
        


stream_thread = threading.Thread(target=stream_camera)
key_press_thread = threading.Thread(target=key_press)

stream_thread.start()
key_press_thread.start()

key_press_thread.join()
stream_thread.join()

cv2.destroyAllWindows() 
exit()