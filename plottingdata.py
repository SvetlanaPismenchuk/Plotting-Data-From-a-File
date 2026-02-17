import matplotlib.pyplot as plt

def read_data(infile, xfield, yfield): #input outputs docstrings
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
    x, y = read_data(infile, xfield, yfield)  # calls function and stores the results # sends back two lists

    plt.scatter(y,x)  # makes a scatter plot x-horizontal y-vertical
    plt.xlabel(yfield)  # labels the x-axis
    plt.ylabel(xfield)  # labels the y-axis
    plt.show()  # displays graph


plot_data("auto-mpg[1].csv", "mpg", "displacement")
input()

'''
```python

code

```

'''
