"""
PDF Page Remover
Written by Matan Cohen

This script allows users to upload a PDF, remove specified pages, and save the modified PDF to a chosen directory with a chosen file name.
"""


import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def upload_file():
    """Prompt the user to select a PDF file and specify pages to remove."""
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pages_to_remove = simpledialog.askstring("Input", "Enter page numbers to remove (comma-separated):")
        if pages_to_remove:
            remove_pages(file_path, pages_to_remove)

def remove_pages(file_path, pages_to_remove):
    """Remove specified pages from the selected PDF file."""
    pages_to_remove = {int(page.strip()) - 1 for page in pages_to_remove.split(',')}  # Convert to 0-based index

    reader = PdfFileReader(file_path)
    writer = PdfFileWriter()

    # Add all pages except the ones to be removed
    for i in range(reader.numPages):
        if i not in pages_to_remove:
            writer.addPage(reader.getPage(i))

    # Allow the user to choose the output directory and file name
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if not output_dir:
        return

    output_file_name = simpledialog.askstring("Input", "Enter the output file name (without extension):")
    if not output_file_name:
        return

    output_file_path = os.path.join(output_dir, f"{output_file_name}.pdf")

    # Write the modified PDF to the chosen location
    with open(output_file_path, 'wb') as output_pdf:
        writer.write(output_pdf)

    messagebox.showinfo("Success", f"Modified PDF saved to {output_file_path}")

# Create the main window
root = tk.Tk()
root.title("PDF Page Remover")
root.geometry("300x150")

# Create a label and button for file upload
label = tk.Label(root, text="Please upload a PDF file:")
label.pack(pady=10)

upload_button = tk.Button(root, text="Upload PDF", command=upload_file)
upload_button.pack(pady=10)

# Run the application
root.mainloop()
