import os
import pandas as pd


def read_stock_data(stock_folder_path):
    """
    Reads data from a stock folder and consolidates it into a single DataFrame.

    Parameters:
    - stock_folder_path (str): The path to the stock folder.

    Returns:
    - pd.DataFrame: The consolidated DataFrame for the stock.
    """
    stock_data = pd.DataFrame()

    # Iterate through files in the stock folder
    for root, dirs, files in os.walk(stock_folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Assuming each file contains the stock data
            try:
                data = pd.read_csv(file_path)  # Update this line based on your file format
                stock_data = pd.concat([stock_data, data], ignore_index=True)
            except pd.errors.EmptyDataError:
                print(f"Empty file: {file_path}")
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")

    return stock_data


def consolidate_and_save(data_folder):
    """
    Consolidates data for each stock and saves it to a new Excel file in the respective stock folder.

    Parameters:
    - data_folder (str): The path to the data folder containing stock folders.
    """
    # Iterate through stock folders in the data folder
    for stock_folder in os.listdir(data_folder):
        stock_folder_path = os.path.join(data_folder, stock_folder)

        if os.path.isdir(stock_folder_path):
            stock_data = read_stock_data(stock_folder_path)

            if not stock_data.empty:
                # Save consolidated data to an Excel file in the stock folder
                output_file_path = os.path.join(stock_folder_path, f"{stock_folder}_consolidated.xlsx")
                stock_data.to_excel(output_file_path, index=False)
                print(f"Consolidated data saved for {stock_folder} in {output_file_path}")
            else:
                print(f"No data found for {stock_folder}")


# Example usage:
data_folder_path = r"C:\Users\user\Desktop\Data"
consolidate_and_save(data_folder_path)
