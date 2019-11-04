import tkinter as tk

WIDTH = 400
HEIGHT = 200

text_size = 15
for_text = "for"
dollar_text = "$"

def calculate(tl, tr, bl, br, answer):
	try:
		top = float(tr) / float(tl)
		bottom = float(br) / float(bl)

		if top == bottom:
			answer["text"] = "Both are the same"
		elif top > bottom:
			answer["text"] = "%s for $%s is better" % (bl, br)
		elif bottom > top:
			answer["text"] = "%s for $%s is better" % (tl, tr)
	except:
		answer["text"] = "Invalid"



root = tk.Tk()
root.resizable(False, False)
root.title("Better Deal")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

frame = tk.Frame(root, bg="#66ffff")
frame.place(relwidth=1, relheight=1, relx=0, rely=0, height=-10, width=-10, x=5, y=5)

tl_Entry = tk.Entry(frame, font=("normal", text_size), justify="center")
tl_Entry.place(relwidth=0.2, relheight=0.2, relx=0.25, rely=0.1, anchor="n")

for1 = tk.Label(frame, font=("normal", text_size), justify="center", text=for_text, bg="#66ffff")
for1.place(relwidth=0.2, relheight=0.2, relx=0.5, rely=0.1, anchor="n")

dollar_label = tk.Label(frame, font=("normal", text_size), justify="center", text=dollar_text, bg="#66ffff")
dollar_label.place(relwidth=0.05, relheight=0.2, relx=0.66, rely=0.1, anchor="ne")

tr_Entry = tk.Entry(frame, font=("normal", text_size), justify="center")
tr_Entry.place(relwidth=0.2, relheight=0.2, relx=0.75, rely=0.1, anchor="n")

bl_Entry = tk.Entry(frame, font=("normal", text_size), justify="center")
bl_Entry.place(relwidth=0.2, relheight=0.2, relx=0.25, rely=0.4, anchor="n")

for2 = tk.Label(frame, font=("normal", text_size), justify="center", text=for_text, bg="#66ffff")
for2.place(relwidth=0.2, relheight=0.2, relx=0.5, rely=0.4, anchor="n")

dollar_label2 = tk.Label(frame, font=("normal", text_size), justify="center", text=dollar_text, bg="#66ffff")
dollar_label2.place(relwidth=0.05, relheight=0.2, relx=0.66, rely=0.4, anchor="ne")

br_Entry = tk.Entry(frame, font=("normal", text_size), justify="center")
br_Entry.place(relwidth=0.2, relheight=0.2, relx=0.75, rely=0.4, anchor="n")

answer = tk.Label(frame, font=("normal", text_size), justify="center")
answer.place(relwidth=0.7, relheight=0.2, relx=0.5, rely=0.7, anchor="n")

button = tk.Button(frame, font=("normal", text_size), justify="center", text="Go", command=lambda: calculate(tl_Entry.get(), tr_Entry.get(), bl_Entry.get(), br_Entry.get(), answer))
button.place(relwidth=0.1, relheight=0.2, relx=0.93, rely=0.7, anchor="n")

root.mainloop()