import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt

from utils import lower_bound_float, next_color, reset_next_color

def plot_normalized_death_rate(title, suffix, normalization_time_span, cases, deaths):
    reset_next_color()
    """ Plots the number of deaths normalized to the number of case-days in the previous @normalization_time_span days."""
    
    normalized_death_rate = [float(death) / sum(cases[:idx+normalization_time_span]) for idx, death in enumerate(deaths[normalization_time_span:])]
#    normalized_death_rate = [float(death) / sum(cases[idx:idx+normalization_time_span]) for idx, death in enumerate(deaths[normalization_time_span:])]

    fig = plt.figure()
    canvas = fig.add_subplot(111)
    canvas.plot(range(len(normalized_death_rate)), normalized_death_rate, next_color())
    fig.savefig("death_rate_normalized_%s.png" % (suffix,))

