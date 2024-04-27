import numpy as np
import pandas as pd


def combine_mean_std_from_csv(filename, output_filename):
    colns = ["25", "35", "45", "55", "65", "75", "85", "100"]

    df = pd.read_csv(filename)
    # df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 0, inplace = True)
    for index, row in df.iterrows():
        if index%2==1:
            continue

        columns = []
        metric_name = row[0].split('_')[0]
        columns.append(metric_name)

        mean = df[colns].iloc[index]
        std = df[colns].iloc[index+1]
        for i in range(len(mean)):
            combined_data = f"{mean[i]:.2f} ± {std[i]:.2f}"
            columns.append(combined_data)

        columns = pd.DataFrame(columns).T

        columns.to_csv(output_filename, mode = "a", header = False, index=False)



# Example usage
output_filename = "/home/anju_chhetri/Desktop/Major/MetricCSV/empty.csv"  # Replace with your desired output filename

# Example usage
filename = "/home/anju_chhetri/Desktop/Major/MetricCSV/empty.csv"  # Replace with your actual CSV file name
combined_data = combine_mean_std_from_csv(filename, output_filename)

