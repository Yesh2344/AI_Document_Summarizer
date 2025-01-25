import tkinter as tk
from tkinter import filedialog, messagebox
from transformers import pipeline
import PyPDF2

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def summarize_text(text, max_length=150, min_length=30):
    """Generate a summary of the given text."""
    try:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(
            text, 
            max_length=max_length, 
            min_length=min_length, 
            do_sample=False
        )
        return summary[0]["summary_text"]
    except Exception as e:
        return f"Error during summarization: {str(e)}"

def summarize_pdf():
    """Handle the summarization of a selected PDF file."""
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return
    
    text = extract_text_from_pdf(file_path)
    if text.startswith("Error"):
        messagebox.showerror("Error", text)
        return
    
    summary = summarize_text(text)
    if summary.startswith("Error"):
        messagebox.showerror("Error", summary)
        return
    
    # Display the summary in the text box
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, summary)

# GUI Setup
root = tk.Tk()
root.title("AI Document Summarizer")
root.geometry("800x600")

# Add a button to select the PDF file
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
select_file_btn = tk.Button(
    button_frame, 
    text="Select PDF File", 
    command=summarize_pdf, 
    width=20, 
    height=2
)
select_file_btn.pack()

# Add a text box to display the summary
text_box = tk.Text(root, wrap=tk.WORD, width=100, height=30)
text_box.pack(pady=20)

# Run the application
root.mainloop()
