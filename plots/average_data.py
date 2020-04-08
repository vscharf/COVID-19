from utils import lower_bound_float, next_color, reset_next_color, Plot, differences

def _moving_average(data):
    return sum(data)/float(len(data))

def plot_historic_normalized_average_data(title, filename, normalization_fraction, average_time_span, *args):
    """ Plots cases average over @average_time_span days normalized to the first @normalization_fraction cases of the smallest total case count. Plot is saved as an png image to @filename .

Data to plot is passed in in *args. The format for each data set is a tuple (legend, data), where @legend is the title that should appear on the legend, and @data is a list of cases per day."""

    smallest_case_count = min([data[-1] for _, data in args])
    normalization_boundary = normalization_fraction * smallest_case_count

    print "Using normalization point %.0f cases" % normalization_boundary
    
    # create plot
    plot = Plot(title=title)

    # figure out the index where all greater indices account for 95% of the total cases (round up)
    start_index = int(min([lower_bound_float(data, 0.05*data[-1]) for _, data in args]) + 0.5)

    if start_index < average_time_span:
        start_index = average_time_span

    reset_next_color()
    # plot data is a list of x-points, y-point, format
    for (legend, data) in args:
        normalization_offset = lower_bound_float(data, normalization_boundary)
        # x-points
        x = [idx - normalization_offset for idx in range(len(data))][start_index:]
        # y-points
        y = [_moving_average(data[idx - average_time_span:idx]) for idx in range(start_index, len(data))]
        # format
        format = next_color()

        plot.add_curve(legend, x, y, format)

    plot.xlabel = "Days since %d cases (%.0f%% of smallest dataset)" % (normalization_boundary, 100.*normalization_fraction)
    plot.save(filename)


def plot_historic_normalized_average_delta(title, filename, normalization_fraction, average_time_span, *args):
    """ Plots daily difference of cases average over @average_time_span days normalized to the first @normalization_fraction cases of the smallest total case count. Plot is saved as an png image to @filename .

Data to plot is passed in in *args. The format for each data set is a tuple (legend, data), where @legend is the title that should appear on the legend, and @data is a list of cases per day."""

    smallest_case_count = min([data[-1] for _, data in args])
    normalization_boundary = normalization_fraction * smallest_case_count

    print "Using normalization point %.0f cases" % normalization_boundary
    
    # create plot
    plot = Plot(title=title)

    # figure out the index where all greater indices account for 95% of the total cases (round up)
    start_index = int(min([lower_bound_float(data, 0.05*data[-1]) for _, data in args]) + 0.5)

    if start_index < average_time_span + 1:
        start_index = average_time_span + 1

    reset_next_color()
    # plot data is a list of x-points, y-point, format
    for (legend, data) in args:
        normalization_offset = lower_bound_float(data, normalization_boundary)
        # x-points
        x = [idx - normalization_offset for idx in range(len(data))][start_index:]
        # y-points
        y = [_moving_average(differences(data[idx - average_time_span - 1:idx])) for idx in range(start_index, len(data))]
        # format
        format = next_color()

        plot.add_curve(legend, x, y, format)

    plot.xlabel = "Days since %d cases (%.0f%% of smallest dataset)" % (normalization_boundary, 100.*normalization_fraction)
    plot.save(filename)
    

