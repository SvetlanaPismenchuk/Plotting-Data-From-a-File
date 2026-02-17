import matplotlib.pyplot as plt

def read_data(infile, xfield, yfield):  # input outputs docstrings
    """
    Reads a CSV file and extracts two specified columns.

    Parameters:
        infile (str): name of the CSV data file
        xfield (str): column name for x-axis data
        yfield (str): column name for y-axis data

    Returns:
        tuple: two lists (x values, y values) as floats
    """
    
    x = []
    y = []
     
    with open(infile, 'r') as f:
        header = f.readline().strip().split(',')  # reads first line, removes newline/spaces, turns into list

        x_index = header.index(xfield)
        y_index = header.index(yfield)
        # finds where a column name appears in the header row
        
        for line in f:
            words = line.strip().split(',')
            
            x.append(float(words[x_index]))
            y.append(float(words[y_index]))
            
    return x, y
    


def plot_data(infile, xfield, yfield):
    """
    Plots a scatter plot using two columns from a CSV file.

    Parameters:
        infile (str): name of the CSV data file
        xfield (str): column name for x-axis
        yfield (str): column name for y-axis

    Returns:
        None
    """

    x, y = read_data(infile, xfield, yfield)  # calls function and stores the results # sends back two lists

    plt.scatter(x, y)  # makes a scatter plot x-horizontal y-vertical
    plt.xlabel(xfield)  # labels the x-axis
    plt.ylabel(yfield)  # labels the y-axis
    plt.show()  # displays graph


plot_data("auto-mpg[1].csv", "mpg", "displacement")
input()
