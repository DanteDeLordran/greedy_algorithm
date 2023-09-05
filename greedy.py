import pandas as pd
import time

data = pd.read_csv("data.csv", names=["vi", "wi", "W"])
vi = data["vi"]
wi = data["wi"]
W = data["W"][0]
v = len(data)

def sort_data(by: str, ascending: bool = False) -> pd.DataFrame:
    sorted_data = data.sort_values(by=by, ascending=ascending)
    return sorted_data

def greedy(localdata: pd.DataFrame, W: float):
    T = []
    totalW = 0
    totalV = 0
    for i, row in localdata.iterrows():
        if totalW + row["wi"] <= W:
            T.append(i)
            totalW += row["wi"]
            totalV += row["vi"]

    print("Selected objects :")
    for i in T:
        print(f"Object {i}: vi {localdata.at[i, 'vi']}, wi {localdata.at[i, 'wi']}")

    print(f"Total value : {totalV}")
    print(f"Total weight : {totalW}")
    
def greedy_by_vw(data: pd.DataFrame, W: float):
    
    data["vw_ratio"] = data["vi"] / data["wi"]
    
    sorted_data = data.sort_values(by="vw_ratio", ascending=False)
    
    T = []          
    totalW = 0      
    totalV = 0      
    
    for i, row in sorted_data.iterrows():
        if totalW + row["wi"] <= W:
            T.append(i)
            totalW += row["wi"]
            totalV += row["vi"]
    
    print("Selected objects :")
    for i in T:
        print(f"Object {i}: vi {data.at[i, 'vi']}, wi {data.at[i, 'wi']}, relation v/w {data.at[i, 'vw_ratio']}")

    print(f"Total value : {totalV}")
    print(f"Total weight : {totalW}")

def main():
    print("Greedy by : ")
    print("1-Highest value")
    print("2-Lowest weight")
    print("3-Highest value by weight")
    option = int(input())
    
    exec_start = time.process_time()
    
    if option == 1:
        greedy(sort_data("vi", ascending=False), W)
    elif option == 2:
        greedy(sort_data("wi"), W)
    elif option == 3:
        greedy_by_vw( data , W )
    else:
        print("Invalid option")
        
    exec_end = time.process_time()
    print("Processing time finished at : ", exec_end - exec_start)

if __name__ == "__main__":
    main()
