import simplegui

counter = 0
total_stops = 0
success_stops = 0

def format(t):
    tenth_second = (t) % 10
    seconds = int(t / 10) % 10
    minutes = int(t / 600) % 600
    tenth_minute = int(t / 100) % 6
    stop_time = str(minutes) + ":" + str(tenth_minute) + str(seconds) + "." + str(tenth_second)
    return stop_time


def start():
    timer.start()

def stop():
    global total_stops, success_stops
    if timer.is_running()== True:
        if counter % 10 == 0 and counter != 0 :
            success_stops += 1
            total_stops +=1
        elif counter != 0 :
            total_stops +=1
    timer.stop()
def reset():
    global total_stops, success_stops,counter
    counter = 0
    total_stops = 0
    success_stops = 0
    timer.stop()


def mytimer():
    global counter
    counter += 1

def draw(canvas):
    message = format(counter)
    canvas.draw_text(message, (50,100), 36, "Red")
    canvas.draw_text(str(success_stops) + '/' + str(total_stops), (150,30), 24, "Green")


frame = simplegui.create_frame("StopWatch",200,200)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, mytimer)


frame.start()
