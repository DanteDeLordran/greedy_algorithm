# Greedy Algorithm for Knapsack Problem
This Python script provides implementations for different greedy algorithms to solve the knapsack problem using a dataset from a CSV file. The script sorts the data and applies greedy algorithms based on different criteria: highest value, lowest weight, and highest value-to-weight ratio.

## Prerequisites

- Python 3.x
- pandas library
- numpy library

## Installation

1. Ensure that you have Python 3 installed on your system.
2. Install the required pandas library using pip:
```
   pip install pandas numpy
```

## Usage
1. Place your CSV file (data.csv) in the same directory as the script. The CSV file should have three columns without headers: vi (values), wi (weights), and W (maximum weight capacity).
2. Run the script:

python script_name.py  
Follow the prompts:

Choose the greedy strategy:

1 - Highest value  
2 - Lowest weight  
3 - Highest value by weight ratio  
The script will display the total value and total weight of the selected items.

Choose whether to run the script again:

1 - Yes  
2 - No  
Functions  
sort_data(by: str, ascending: bool = False) -> pd.DataFrame  
Sorts the data by a specified column.

by - Column name to sort by.  
ascending - Sort order, default is descending.  
greedy(localdata: pd.DataFrame, W: float)  
Applies the greedy algorithm based on the sorted data.

localdata - DataFrame sorted by a specific criterion.  
W - Maximum weight capacity.  
greedy_by_vw(data: pd.DataFrame, W: float)  
Applies the greedy algorithm based on the value-to-weight ratio.

data - Original DataFrame.  
W - Maximum weight capacity.  
main()  
Main function to run the script, handle user input, and execute the chosen greedy strategy.

## Example
Here's an example of what the data in data.csv might look like:

Copiar código  
60,10,50  
100,20,50  
120,30,50  
When you run the script, it will prompt you to choose a greedy strategy, compute the total value and weight of the selected items, and ask if you want to run the script again.  