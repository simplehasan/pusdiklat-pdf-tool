import os
import pandas as pd


def get_user_input():
    folder_path = input("Enter the folder path where the PDF files are located: ")
    old_file_pattern = input("Enter the old file name pattern (e.g., 'file_'): ")
    excel_file_name = input(
        "Enter the Excel file name (without extension) containing the new file names: "
    )
    column_name = input(
        "Enter the column name in Excel containing the new file names: "
    )
    return folder_path, old_file_pattern, excel_file_name, column_name


def rename_pdf(folder_path, old_file_pattern, excel_file_name, column_name):
    folder_path = os.path.join(os.getcwd(), folder_path)
    excel_file_path = os.path.join(os.getcwd(), f"{excel_file_name}.xlsx")

    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return

    if not os.path.exists(excel_file_path):
        print(f"Error: File '{excel_file_name}.xlsx' not found.")
        return

    excel_data = pd.read_excel(excel_file_path)

    for index, row in excel_data.iterrows():
        old_file_name = os.path.join(folder_path, f"{old_file_pattern}{index+1}.pdf")
        if not os.path.exists(old_file_name):
            print(f"Error: File '{os.path.basename(old_file_name)}' not found.")
            continue

        new_file_name = os.path.join(folder_path, f"{row[column_name]}.pdf")
        os.rename(old_file_name, new_file_name)
        print(
            f"Rename sukses {os.path.basename(old_file_name)} menjadi {os.path.basename(new_file_name)}"
        )


def main():
    print("Welcome to the PDF Renamer!")
    folder_path, old_file_pattern, excel_file_name, column_name = get_user_input()
    rename_pdf(folder_path, old_file_pattern, excel_file_name, column_name)


if __name__ == "__main__":
    main()
