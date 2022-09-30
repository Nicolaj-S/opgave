import sys
import signal
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

'''color of hour minute second clock'''
hour_color = (255, 0, 0)
minute_color = (0, 255, 0)
second_color = (0, 0, 255)
off = (0, 0, 0)

sense.clear()
sense.show_message("Programmet starter")


def update_screen():
    '''update screen/clear screen'''
    sense.clear()

def direction(event):
    '''event handler for joystick'''
    true = True
    true2 = True
    '''if joysticks event is pressed do the following'''
    if event.action == "pressed":
            if event.direction == "right":
                '''press stick right run clock 24 hour format in one line'''
                while true:
                    t = datetime.now()
                    display_time_in_binary(t.hour, 2, hour_color) 
                    display_time_in_binary(t.minute, 3, minute_color)
                    display_time_in_binary(t.second, 4, second_color)
                    for event in sense.stick.get_events():
                        '''press middle to go back'''
                        if event.action == "pressed":
                            if event.direction == "middle":
                                true = False
                        elif event.direction == "right":
                            true2 = True
                            '''press right again for running two row clock'''
                            sense.clear()
                            while true2:
                                t = datetime.now().time()
                                hour,min,sec = str(t).split(":")
            
                                hour1 = hour[:1]
                                hour2 = hour[-1:]
                                min1 = min[:1]
                                min2 = min[-1:]
                                sec = sec.split(".")[0]
                                sec1 = sec[:1]
                                sec2 = sec[-1:]
            
                                display_time_in_binary(int(hour1), 0, hour_color)
                                display_time_in_binary(int(hour2), 1, hour_color)
                                display_time_in_binary(int(min1), 3, minute_color)
                                display_time_in_binary(int(min2), 4, minute_color)
                                display_time_in_binary(int(sec1), 6, second_color)
                                display_time_in_binary(int(sec2), 7, second_color)
                                for event in sense.stick.get_events():
                                    '''press middle to go back'''
                                    if event.action == "pressed":
                                        if event.direction == "middle":
                                            true2 = False
                                            sense.clear()

            elif event.direction == "left":
                '''press stick left run clock 12 hour format in one line'''
                while true:
                    t = datetime.now()
                    t12 = t.strftime("%I")
                    t12 = int(t12)
                    display_time_in_binary(t12, 2, hour_color) 
                    display_time_in_binary(t.minute, 3, minute_color)
                    display_time_in_binary(t.second, 4, second_color)
                    for event in sense.stick.get_events():
                        '''press middle to go back'''
                        if event.action == "pressed":
                            if event.direction == "middle":
                                true = False
                        elif event.direction == "left":
                            '''press left again for running two row clock'''
                            sense.clear()
                            true2 = True
                            while true2:
                                t = datetime.now()
                                hour,min,sec = str(t).split(":")
                                hour = t.strftime("%I")
                            
                                hour1 = hour[:1]
                                hour2 = hour[-1:]
                                min1 = min[:1]
                                min2 = min[-1:]
                                sec = sec.split(".")[0]
                                sec1 = sec[:1]
                                sec2 = sec[-1:]

                                display_time_in_binary(int(hour1), 0, hour_color)
                                display_time_in_binary(int(hour2), 1, hour_color)
                                display_time_in_binary(int(min1), 3, minute_color)
                                display_time_in_binary(int(min2), 4, minute_color)
                                display_time_in_binary(int(sec1), 6, second_color)
                                display_time_in_binary(int(sec2), 7, second_color)
                                for event in sense.stick.get_events():
                                    '''press middle to go back'''
                                    if event.action == "pressed":
                                        if event.direction == "middle":
                                            true2 = False
                                            sense.clear()
                

            elif event.direction == "middle":
                '''press middle to end program'''
                print("Programmet slutter")
                sense.show_message("Programmet slutter")
                sys.exit(0)

            elif event.direction == "up":
                sense.show_message("Hello this is a guid for how to use me, 1) time for mat is sec/min/houre. 2) up is for this guid. 3) left is for am/pm format in a row click ones more for two rows. 4) right is for 24 format click ones more for two rows. 5) middle button goes back ones")



def display_time_in_binary(value, row, color):
    '''display time in binary'''
    binary_str = '{0:8b}'.format(value)
    for x in range(0, 8):
        if binary_str[x] == '1':
            sense.set_pixel(x, row, color)
        else:
            sense.set_pixel(x, row, off)


def end_program(signal, frame):
    '''function to close program with a end text'''
    print("Programmet slutter")
    sense.show_message("Programmet slutter")
    sys.exit(0)
signal.signal(signal.SIGINT, end_program)

'''while loop for the programm to run the clock'''
while True:
    sense.show_message("MENU")
    for event in sense.stick.get_events():
        direction(event)
        update_screen()