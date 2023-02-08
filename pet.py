import random
import tkinter as tk

cycle = 0
check = 1

idle_num = [1, 2, 3, 4, 6, 7, 8, 9]
sleep_num = [16, 17, 19, 20, 21]
wave_num = [10, 11]
kiss_num = [12, 13]
blink_num = [14, 15]

event_number = 1
impath = 'D:\\VSCodeProjects\\Pet Widget\\gifs\\'
# transfer random no. to event


def event(cycle, check, event_number, x):
    if event_number in idle_num:
        check = 0
        print('idle')
        window.after(400, update, cycle, check,
                     event_number, x)  # no. 1,2,3,4 = idle
    elif event_number == 5:
        check = 1
        print('from idle to sleep')
        # no. 5 = idle to sleep
        window.after(100, update, cycle, check, event_number, x)

    elif event_number in sleep_num:
        check = 2
        print('sleep')
        # no. 12,13,15,16,17 = sleep
        window.after(300, update, cycle, check, event_number, x)

    elif event_number == 18:
        check = 3
        print('from sleep to idle')
        # no. 15 = sleep to idle
        window.after(100, update, cycle, check, event_number, x)

    elif event_number in wave_num:
        check = 4
        print('wave')
        # no. 6,7 = wave
        window.after(100, update, cycle, check, event_number, x)

    elif event_number in kiss_num:
        check = 5
        print('kiss')
        # no 8,9 = kiss
        window.after(100, update, cycle, check, event_number, x)

    elif event_number in blink_num:
        check = 6
        print('blinking')
        window.after(200, update, cycle, check, event_number, x)
    else:
        check = 0
        print('idle')
        window.after(400, update, cycle, check,
                     event_number, x)
# making gif work


def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num+1, 1)
    return cycle, event_number


def update(cycle, check, event_number, x):
    # idle
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number, 1, 15)

    # idle to sleep
    elif check == 1:
        frame = idle_to_sleep[cycle]
        cycle, event_number = gif_work(
            cycle, idle_to_sleep, event_number, 16, 16)
    # sleep
    elif check == 2:
        frame = sleep[cycle]
        cycle, event_number = gif_work(cycle, sleep, event_number, 16, 21)
    # sleep to idle
    elif check == 3:
        frame = sleep_to_idle[cycle]
        cycle, event_number = gif_work(
            cycle, sleep_to_idle, event_number, 1, 1)
    # wave
    elif check == 4:
        frame = wave[cycle]
        cycle, event_number = gif_work(
            cycle, wave, event_number, 1, 15)
    # kissing
    elif check == 5:
        frame = kissing[cycle]
        cycle, event_number = gif_work(
            cycle, kissing, event_number, 1, 15)
    # blinking
    elif check == 6:
        frame = blinking[cycle]
        cycle, event_number = gif_work(
            cycle, blinking, event_number, 1, 15)

    window.geometry('100x100+'+f'{x-200}'+f'+{screen_height-115}')
    label.configure(image=frame, bg='red')
    window.after(1, event, cycle, check, event_number, x)


window = tk.Tk()
# call buddy's action gif
idle = [tk.PhotoImage(file=impath+'idle.gif', format='gif -index %i' % (i))
        for i in range(2)]  # idle gif
idle_to_sleep = [tk.PhotoImage(file=impath+'idle_to_sleep.gif',
                               format='gif -index %i' % (i)) for i in range(2)]  # idle to sleep gif
sleep = [tk.PhotoImage(file=impath+'sleep.gif', format='gif -index %i' % (i))
         for i in range(5)]  # sleep gif
sleep_to_idle = [tk.PhotoImage(file=impath+'sleep_to_idle.gif',
                               format='gif -index %i' % (i)) for i in range(2)]  # sleep to idle gif
wave = [tk.PhotoImage(file=impath+'wave.gif',
                      format='gif -index %i' % (i)) for i in range(9)]  # wave gif
kissing = [tk.PhotoImage(file=impath+'kissing.gif',
                         format='gif -index %i' % (i)) for i in range(7)]  # kissing gif
blinking = [tk.PhotoImage(file=impath+'blinking.gif',
                          format='gif -index %i' % (i)) for i in range(5)]  # blinking gif
# window configuration
label = tk.Label(window, bg='red')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', 'red')
label.pack()

screen_height = window.winfo_screenheight()
x = window.winfo_screenwidth()

# loop the program
window.after(1, update, cycle, check, event_number, x)
window.mainloop()
