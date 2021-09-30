from Tkinter import *
from PIL import Image, ImageTk
from itertools import combinations
import string
import random

rnd = random.randint

ww = 600
hh = 600
alpha = list(string.letters)

# combinations() needs to be replace... very limited by out of memory is the main issue
combos = ['+'.join(z) for z in list(combinations(alpha, 4))]

ttt = 'alpha_art = lambda zzz : '

abc = []
for zzz in combos:
    zzz = '('+zzz+')'
    abc += [zzz]

0
abc = ttt+'['+','.join(abc)+']'

exec(abc)
# print len(abc),ww*hh

root = Tk()
root.title("Tk_Alpha_Art.py")
root.geometry("%dx%d+0+0" % (ww, hh))


def draw():
    image.putdata(rgb)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=photo, anchor=NW)
    canvas.update()


0

canvas = Canvas(root, width=ww, height=hh)
canvas.pack()

image = Image.new("RGB", (ww, hh), (255, 255, 255))

while 1:
    for zzz in alpha:
        ttt = str(rnd(0, 16777215))
        exec(zzz+'='+ttt)
    rgb = alpha_art(0)
    print len(rgb), ww*hh
    draw()
