import numpy as np
import matplotlib.pyplot as plt



FS = int(input("sampling frequency : "))
F_Max = int(input("max frequency : "))
amp = 1
duration = 1         

def nyquist(FS, F_Max):
    if FS >= F_Max * 2:
        print("NO ALIASING")
    else:
        print("ALIASING")

nyquist(FS, F_Max)

# "true" signal -- densely evaluated just so we have a smooth reference curve
t_true = np.linspace(0, duration, 2000)
signal_true = amp * np.sin(2 * np.pi * F_Max * t_true)

# the ACTUAL samples, spaced 1/FS apart, sampling that same F_Max signal
t_samples = np.arange(0, duration, 1 / FS)
signal_samples = amp * np.sin(2 * np.pi * F_Max * t_samples)

plt.plot(t_true, signal_true, 'k--', linewidth=1, label="original signal (F_max=" + str(F_Max) + " Hz)")
plt.stem(t_samples, signal_samples, linefmt='r-', markerfmt='ro', basefmt=' ')
plt.plot(t_samples, signal_samples, 'r', linewidth=1, label="reconstructed from samples (FS=" + str(FS) + " Hz)")
plt.xlabel("time (s)")
plt.ylabel("amplitude")
plt.legend()
plt.title("Nyquist sampling demo")
plt.show()
