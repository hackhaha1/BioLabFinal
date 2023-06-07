# sampling frequency = 200Hz
import csv
from scipy import signal
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import numpy as np


def FFT_process(lst):
    # sample spacing
    fs = 60   # Hz
    T = 1/fs
    time = 10  # sec
    N = fs*time
    ydata = []

    # read data
    sig = lst
    sig = np.array(sig)

    # process
    order = 3

    sos = signal.butter(order, [8, 13], 'bp', fs=fs, output='sos')
    alpha_exp = signal.sosfilt(sos, sig)
    sos = signal.butter(order, [12, 28], 'bp', fs=fs, output='sos')
    beta_exp = signal.sosfilt(sos, sig)
    sos = signal.butter(order, [4, 7], 'bp', fs=fs, output='sos')
    theta_exp = signal.sosfilt(sos, sig)

    # filter
    wave = [alpha_exp, beta_exp, theta_exp]
    for i in wave:
        yf = fft(i)
        yf = (2.0/N * np.abs(yf[0:]))[0:(fs//2*time)]
        xf = fftfreq(N, T)[:]
        xf = xf[0:(fs//2*time)]
        ydata.append("{:.6f}".format(max(yf)))

    ydata = [float(i) for i in ydata]
    ydata = np.array([ydata])
    return ydata


# l = []
# with open('test.csv', 'r', encoding="utf-8") as f:
#     rows = csv.reader(f, )
#     for row in rows:
#         l.append(int(row[0]))

# print(FFT_process(l))
