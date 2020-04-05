import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt

class Plot(object):
    def __init__(self, title = None, xlabel = None):
        # create canvas
        self._fig = plt.figure()
        self._canvas = self._fig.add_subplot(111)
        self._title = title if title is not None else ""
        if not isinstance(self._title, str):
            raise TypeError("plots.utils.Plot.Plot: title: a string is required not %s" % type(value))

        self._xlabel = xlabel if xlabel is not None else ""
        if not isinstance(self._xlabel, str):
            raise TypeError("plots.utils.Plot.Plot: xlabel: a string is required not %s" % type(value))


    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("plots.utils.Plot.title: a string is required not %s" % type(value))
        self._title = value


    @property
    def canvas(self):
        return self._canvas


    @property
    def xlabel(self):
        return self._xlabel

    @xlabel.setter
    def xlabel(self, value):
        print "xlabel set"
        if not isinstance(value, str):
            raise TypeError("plots.utils.Plot.xlabel: a string is required not %s" % type(value))
        self._xlabel = value


    def add_curve(self, legend, x, y, format):
        self._canvas.plot(x, y, format, label=legend)


    def save(self, filename):
        self._canvas.set_title(self._title)
        self._canvas.set_xlabel(self._xlabel)
        self._canvas.legend()
        self._fig.savefig(filename)
        

def lower_bound_float(data, bound):
    index_lower_bound = 1
    while data[index_lower_bound] < bound:
        index_lower_bound += 1

    # intrapolate to find exact lower_bound                                     
    # exact_lower_bound = (bound - c)/m,  m = slope,  c = y - m*x               
    m = (data[index_lower_bound] - data[index_lower_bound - 1])
    c = data[index_lower_bound] - m * index_lower_bound
    return (bound - c)/m


def lower_bound_float_integral(data, bound):
    index_lower_bound = 1
    while sum(data[:index_lower_bound]) < bound:
        index_lower_bound += 1

    # intrapolate to find exact lower_bound                                     
    # exact_lower_bound = (bound - c)/m,  m = slope,  c = y - m*x               
    m = (sum(data[:index_lower_bound]) - sum(data[:index_lower_bound - 1]))
    c = sum(data[:index_lower_bound]) - m * index_lower_bound
    return (bound - c)/m

def next_color():
    """ Cycling through plot data, return a different one on every invocation. Wrapping around when all colors are used. """
    if not hasattr(next_color, "current_color_index"):
        next_color.colors = ["y", "b", "g", "r", "c", "m", "k"]
        next_color.current_color_index = 0

    next_color.current_color_index += 1
    if next_color.current_color_index == len(next_color.colors):
        next_color.current_color_index = 0
    return next_color.colors[next_color.current_color_index]

next_color()

def reset_next_color():
    next_color.current_color_index = 0

