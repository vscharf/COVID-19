import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt

from utils import lower_bound_float, next_color, reset_next_color

def plot_normalized_cumulative_data(title, suffix, normalization_fraction, *args):
    """ Plots cumulative cases normalized to the first @normalization_fraction cases of the smallest total case count. Plot is saved as an png image. The name is '<@title>_normalized_cumulative_cases_<@suffix>.png ."""
    reset_next_color()

    smallest_case_count = min([data[-1] for data in args])
    normalization_boundary = normalization_fraction * smallest_case_count

    print "Using normalization point %.0f cases" % normalization_boundary
    
    # plot data is a list of x-points, y-point, format
    plot_data = []
    for data in args:
        normalization_offset = lower_bound_float(data, normalization_boundary)
        # x-points
        plot_data.append([idx - normalization_offset for idx in range(len(data))])
        # y-points
        plot_data.append(data)

        # format
        plot_data.append(next_color())

    fig = plt.figure()
    canvas = fig.add_subplot(111)
    canvas.plot(*plot_data)
    fig.savefig("%s_cumulative_normalized_%s.png" % (title, suffix))
    
    
