from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps=0
    window.after_cancel(timer)
    timer_label.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    if reps&1:
        timer_label.config(text="Work",fg=GREEN)
        count_down(60*WORK_MIN)
    elif reps%8==0:
        timer_label.config(text="Break",fg=RED)
        count_down(60*LONG_BREAK_MIN)
    else:
        timer_label.config(text="Break",fg=PINK)
        count_down(60*SHORT_BREAK_MIN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    if count==-1:
        if reps%2==0:
            t="✔"*(int)((reps%8)/2)
            check_mark.config(text=t)
        start_timer()
        return
    min=int(count/60)
    sec=count%60
    if min<10:
        min=f"0{min}"
    if sec<10:
        sec=f"0{sec}"
    canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    global timer
    timer=window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold")) 
canvas.grid(row=1,column=1)

timer_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
timer_label.grid(row=0,column=1)

start_button=Button(text="Start",command=start_timer)
start_button.grid(row=2,column=0)

Reset_button=Button(text="Reset",command=reset_timer)
Reset_button.grid(row=2,column=2)

check_mark=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
check_mark.grid(row=3,column=1)

window.mainloop()

# ✔