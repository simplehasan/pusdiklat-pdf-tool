from split_pdf import split_pdf
from rename_pdf import rename_pdf


def display_home_screen():
    print(
        r"""


    $$$$$$\     $$\                     $$\                                                  
  $$$ ___$$$\   \__|                    \__|                                                 
 $$ _/   \_$$\  $$\ $$$$$$$\  $$\   $$\ $$\ $$$$$$$\   $$$$$$$\ $$$$$$\  $$$$$$$\   $$$$$$\  
$$ / $$$$$\ $$\ $$ |$$  __$$\ $$ |  $$ |$$ |$$  __$$\ $$  _____|\____$$\ $$  __$$\ $$  __$$\ 
$$ |$$  $$ |$$ |$$ |$$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |\$$$$$$\  $$$$$$$ |$$ |  $$ |$$$$$$$$ |
$$ |$$ /$$ |$$ |$$ |$$ |  $$ |$$ |  $$ |$$ |$$ |  $$ | \____$$\$$  __$$ |$$ |  $$ |$$   ____|
$$ |\$$$$$$$$  |$$ |$$ |  $$ |\$$$$$$  |$$ |$$ |  $$ |$$$$$$$  \$$$$$$$ |$$ |  $$ |\$$$$$$$\ 
\$$\ \________/ \__|\__|  \__| \______/ \__|\__|  \__|\_______/ \_______|\__|  \__| \_______|
 \$$$\   $$$\                                                                                
  \_$$$$$$  _|                                                                               
    \______/                                                                                 

        


    inuinsane PDF Tool
    
    1. Split PDF
    2. Rename PDF files
    3. Exit
    """
    )

    choice = input("Enter your choice (1/2/3): ")
    return choice


def main():
    while True:
        choice = display_home_screen()

        if choice == "1":
            pdf_file_name = input(
                "Masukkan nama file yang akan di-split (tanpa ekstensi usahakan 1 kata): "
            )
            chunk_size = int(input("Masukkan jumlah halaman per-split (contoh: 8): "))
            output_folder = input(
                "Masukkan nama folder hasil split (boleh folder baru, usahakan 1 kata): "
            )
            output_filename = input(
                "Masukkan nama file output (contoh: file, maka output akan file_1, file_2, dst): "
            )
            split_pdf(pdf_file_name, chunk_size, output_folder, output_filename)
        elif choice == "2":
            folder_path = input(
                "Masukkan nama folder dimana file pdf berada (usahakan 1 direktori dengan file .exe ini): "
            )
            old_file_pattern = input(
                "Masukkan pattern nama file yang ada (contoh: 'file_'): "
            )
            excel_file_name = input(
                "Masukkan nama file excel (tanpa ekstensi) yang memuat nama file baru: "
            )
            column_name = input(
                "Masukkan nama kolom di dalam file excel yang memuat list nama file baru: "
            )
            rename_pdf(folder_path, old_file_pattern, excel_file_name, column_name)
        elif choice == "3":
            print("Thank you for using inuinsane PDF Tool!")
            input("Type anything to close the app ...")  # Wait for user input
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

        # After using a feature, ask the user if they want to go back to the home screen or exit
        while True:
            response = input("Do you want to go back to the home screen? (y/n): ")
            if response.lower() == "y":
                break
            elif response.lower() == "n":
                print("Exitting inuinsane PDF Tool.")
                input("Type anything to close the app ...")  # Wait for user input
                exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
