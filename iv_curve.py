import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Manually parsing the data since pandas is having trouble with the file format
def load_and_parse_all_columns_manually(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Splitting each line by tab and creating a list of lists
    parsed_data = [line.strip().split('\t') for line in lines]

    # Extracting voltage and current columns
    voltage_columns = []
    current_columns = []

    for row in parsed_data[1:]:
        voltages = [float(row[i]) for i in range(0, len(row), 2)]
        currents = [float(row[i + 1]) for i in range(0, len(row), 2)]
        voltage_columns.append(voltages)
        current_columns.append(currents)

    voltage_columns = np.array(voltage_columns)
    current_columns = np.array(current_columns)

    # Assuming all voltage columns have the same values, take the first one as the representative
    voltages = voltage_columns[:, 0]

    # Calculating the average current across all current columns
    average_currents = current_columns.mean(axis=1)

    return voltages, average_currents


# Load and process data for double19
file_path_19 = './data/double_crocv2_19/2024_06_07/LastIV_double19.csv'
voltages_19, average_currents_19 = load_and_parse_all_columns_manually(file_path_19)

# Load and process data for double20
file_path_20 = './data/double_crocv2_20/2024_06_07/LastIV_double20.csv'
voltages_20, average_currents_20 = load_and_parse_all_columns_manually(file_path_20)

# Taking the absolute values of the average currents for plotting
abs_average_currents_19 = average_currents_19
abs_average_currents_20 = average_currents_20

# Plotting the average IV curves in log scale for current
plt.figure(figsize=(10, 5))

# Plot for double19
plt.plot(np.abs(voltages_19), np.abs(average_currents_19), label='Double19', color='orange', marker="o")

# Plot for double20
plt.plot(np.abs(voltages_20), average_currents_20, label='Double20', color='b', marker="s")

#plt.yscale('log')
plt.xlabel('Voltage (V)', fontsize=16)
plt.ylabel('Current (A)', fontsize=16)
plt.title('IV Curves double', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)
plt.grid(True)

# Set font size for axis scale labels (offset text)
ax = plt.gca()
ax.yaxis.get_offset_text().set_fontsize(14)
plt.savefig("IV_doubles_19_20.pdf", format="pdf")
plt.show()

