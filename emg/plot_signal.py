from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema
from scipy.interpolate import make_interp_spline

def savitzky_golay(y, window_size, order, deriv=0, rate=1):
    r"""Smooth (and optionally differentiate) data with a Savitzky-Golay filter.
    The Savitzky-Golay filter removes high frequency noise from data.
    It has the advantage of preserving the original shape and
    features of the signal better than other types of filtering
    approaches, such as moving averages techniques.
    Parameters
    ----------
    y : array_like, shape (N,)
        the values of the time history of the signal.
    window_size : int
        the length of the window. Must be an odd integer number.
    order : int
        the order of the polynomial used in the filtering.
        Must be less then `window_size` - 1.
    deriv: int
        the order of the derivative to compute (default = 0 means only smoothing)
    Returns
    -------
    ys : ndarray, shape (N)
        the smoothed signal (or it's n-th derivative).
    Notes
    -----
    The Savitzky-Golay is a type of low-pass filter, particularly
    suited for smoothing noisy data. The main idea behind this
    approach is to make for each point a least-square fit with a
    polynomial of high order over a odd-sized window centered at
    the point.
    Examples
    --------
    t = np.linspace(-4, 4, 500)
    y = np.exp( -t**2 ) + np.random.normal(0, 0.05, t.shape)
    ysg = savitzky_golay(y, window_size=31, order=4)
    import matplotlib.pyplot as plt
    plt.plot(t, y, label='Noisy signal')
    plt.plot(t, np.exp(-t**2), 'k', lw=1.5, label='Original signal')
    plt.plot(t, ysg, 'r', label='Filtered signal')
    plt.legend()
    plt.show()
    References
    ----------
    .. [1] A. Savitzky, M. J. E. Golay, Smoothing and Differentiation of
       Data by Simplified Least Squares Procedures. Analytical
       Chemistry, 1964, 36 (8), pp 1627-1639.
    .. [2] Numerical Recipes 3rd Edition: The Art of Scientific Computing
       W.H. Press, S.A. Teukolsky, W.T. Vetterling, B.P. Flannery
       Cambridge University Press ISBN-13: 9780521880688
    """
    import numpy as np
    from math import factorial
    
    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError:
        raise ValueError("window_size and order have to be of type int")
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')

with open('signal2.txt') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

sensor1 = []
sensor2 = []
for valor in lines:
    valores=valor.split()
    sensor1.append(int(valores[0]))
    sensor2.append(int(valores[1]))

# f1 = interp1d(list(range(len(sensor1))), sensor1, kind='cubic', fill_value='extrapolate')
# f2 = interp1d(list(range(len(sensor2))), sensor2, kind='cubic', fill_value='extrapolate')
# xnew = np.linspace(0, len(sensor1), num=500, endpoint=True)
# yhat = savitzky_golay(np.array(sensor1), 51, 3) 
x = np.array(list(range(len(sensor1))))
# sensor1 = np.array(sensor1)
# sensor2 = np.array(sensor2)
# X_Y_Spline = make_interp_spline(x, sensor1)
# X_Y_Spline2 = make_interp_spline(x, sensor2)
# X_ = np.linspace(x.min(), x.max(), 500)
# Y_ = X_Y_Spline(X_)
# Y_2 = X_Y_Spline2(X_)
# for i in range(len(Y_)):
#     if Y_[i] < 0:
#         Y_[i] = 0
#     if Y_2[i] < 0:
#         Y_2[i] = 0
# plt.plot(X_, Y_, X_, Y_2)

plt.plot(x, sensor1)
plt.legend(['Sensor 1'])
plt.savefig('Sensor1.png')