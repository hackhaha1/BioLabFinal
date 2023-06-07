import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# import sklearn
import joblib
import serial
import csv
# import keyboard
# import time
import sys

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score, confusion_matrix
from collections import Counter
from EEG_def import FFT_process
from tkinter import *

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM8'

ser.open()

print("serial begin!")

counter = 0
output_flag = False

clf1 = joblib.load('svc1.pkl')
clf2 = joblib.load('svc2.pkl')
clf3 = joblib.load('svc3.pkl')
clf4 = joblib.load('svc4.pkl')
clf5 = joblib.load('svc5.pkl')

window = Tk()
window.title('Lie Detection')
window.geometry('640x480')
# window.resizable(False, False)
# window.iconbitmap('icon.ico')

data = []

# with open('0530/0530_output_7.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["alpha_max", "beta_max", "theta"])

def startClicked():
    global counter
    data = []
    ser.reset_input_buffer()
    for i in range(600):
        # lbl.configure(text="Result is...")
        h1 = ser.read().decode("utf-8")
        f1 = ord(h1)
        data.append(f1)

    X = FFT_process(data)

    print(X)
    counter += 1
    print(counter)
    # with open('0530/0530_output_7.csv', 'a', newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(X[0])
    
    result = np.array([])

    result = np.append(clf1.predict(X).astype(int), result)
    result = np.append(clf2.predict(X).astype(int), result)
    result = np.append(clf3.predict(X).astype(int), result)
    result = np.append(clf4.predict(X).astype(int), result)
    result = np.append(clf5.predict(X).astype(int), result)
    result = result.astype(int).tolist()
    print(result)
    result = Counter(result)

    x = result.most_common(1)[0][0]

    if (x==0):
        lbl.configure(text="Truth!")
    else:
        lbl.configure(text="Lie!")


def clearClicked():
    # sys.exit()
    lbl.configure(text="Result is...")


btn_start = Button(window, text="Start trial", bg="orange", fg="red",
                   font=("Arial", 32), command=startClicked)
btn_start.grid(column=0, row=0)

btn_stop = Button(window, text="Clear",
                  font=("Arial", 32), command=clearClicked)
btn_stop.grid(column=1, row=0)

lbl = Label(window, text="Lie Test", font=("Arial", 32))
lbl.grid(column=0, row=1)

window.mainloop()

# while not keyboard.is_pressed('s'):
#     if (counter < 600):
#         #   print(ser.isOpen())
#         h1 = ser.read().decode("utf-8")
#         f1 = ord(h1)
#         # print(f1)
#         data.append(f1)

#         counter += 1

#     else:
#         h1 = ser.read().decode("utf-8")
#         if not output_flag:
#             # print(len(data))
#             X = FFT_process(data)

#             result = np.array([])

#             result = np.append(clf1.predict(X).astype(int), result)
#             result = np.append(clf2.predict(X).astype(int), result)
#             result = np.append(clf3.predict(X).astype(int), result)
#             result = result.astype(int).tolist()
#             result = Counter(result)

#             x = result.most_common(1)[0][0]
#             # window.control(x)
#             # print(x)
#             if (x == 0):
#                 print('Truth!')
#             if (x == 1):
#                 print('Lie!')
#             # if (x==0):
#             #     l = tk.Label(window, text="True!")
#             #     l.config(font=("Courier", 80))
#             # if (x==1):
#             #     l = tk.Label(window, text="Lie!!")
#             #     l.config(font=("Courier", 80))
#             # l.place(x=190, y=200, anchor=CENTER)
#             output_flag = True
#         if (keyboard.is_pressed('a')):
#             data = []
#             counter = 0
#             x = 2
#             # window.control(x)
#             output_flag = False

# window.mainloop()
