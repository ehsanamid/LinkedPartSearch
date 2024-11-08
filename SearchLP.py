import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def search_text_in_sdx_files(folder_path, search_text):
    # List to store the names of files containing the search text
    files_with_text = []

    # Iterate over all files in the given folder
    for filename in os.listdir(folder_path):
        # Check if the file has a .sdx extension
        if filename.endswith('.sdx'):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)
            
            # Open and read the file
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Check if the search text is in the file content
                if search_text in content:
                    files_with_text.append(filename)
    
    return files_with_text

def get_folder_and_search_text():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask the user to select a folder
    folder_path = filedialog.askdirectory(title="Select Folder")

    if not folder_path:
        messagebox.showerror("Error", "No folder selected.")
        return

    # Ask the user to enter the text to search
    search_text = simpledialog.askstring("Input", "Enter the text to search:")

    if not search_text:
        messagebox.showerror("Error", "No search text entered.")
        return

    # Search for the text in .vdx files in the selected folder
    files_found = search_text_in_sdx_files(folder_path, search_text)

    # Display the result to the user
    if files_found:
        messagebox.showinfo("Result", f"Files containing '{search_text}':\n" + "\n".join(files_found))
    else:
        messagebox.showinfo("Result", f"No files containing '{search_text}' found.")

# Run the function to get folder and search text from user
get_folder_and_search_text()
