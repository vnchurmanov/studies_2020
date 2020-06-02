import simplegui

# define global variables
time = 0
success = 0
stops = 0
started = False


def formats(t):
    # convert time (xywz) from timer to x minutes, y ten of seconds, w - seconds, z - ms
    minutes = t // 600
    tens_of_sec = (t - minutes * 600) // 100
    seconds = ((t - minutes * 600) % 100) // 10
    ms = (t - minutes * 600) % 10
    return str(minutes) + ':' + str(tens_of_sec) + str(seconds) + '.' + str(ms)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global started
    started = True
    timer.start()


def stop():
    global stops, success, started
    timer.stop()
    if started:
        stops += 1
    if (time - (time // 600) * 600) % 10 == 0 and started:
        success += 1
        started = False
    started = False


def reset():
    global time, stops, success, started
    timer.stop()
    time = 0
    stops = 0
    success = 0
    started = False

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1


# define draw handler
def draw(canvas):
    canvas.draw_text(formats(time), [180, 200], 80, "Red")
    canvas.draw_text('Successful attempts: ' + str(success), [130, 30], 30, "Green")
    canvas.draw_text('All stops: ' + str(stops), [260, 60], 30, "Green")


# create frame
f = simplegui.create_frame("StopWatch", 500, 300)

# register event handlers
f.add_button("Start", start, 200)
f.add_button("Stop", stop, 200)
f.add_button("Reset", reset, 200)
f.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
f.start()
