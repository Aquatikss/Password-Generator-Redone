import tkinter as tk

from passwordgen import generate_new_password


class Window(tk.Tk):
    def __init__(self, title: str, width: int, height: int):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(False, False)
        self.configure(bg="white")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.destroy()
        self.quit()


window = Window("My Application", 800, 600)

uppercase_check_box_var = tk.BooleanVar()
uppercase_check_box = tk.Checkbutton(window, text="Use Uppercase Character", bg="white", variable=uppercase_check_box_var)
uppercase_check_box.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

lowercase_check_box_var = tk.BooleanVar()
lowercase_check_box = tk.Checkbutton(window, text="Use Lowercase Character", bg="white", variable=lowercase_check_box_var)
lowercase_check_box.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

digits_check_box_var = tk.BooleanVar()
digits_check_box = tk.Checkbutton(window, text="Use Digits", bg="white", variable=digits_check_box_var)
digits_check_box.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)

special_chars_check_box_var = tk.BooleanVar()
special_chars_check_box = tk.Checkbutton(window, text="Use Special Characters", bg="white", variable=special_chars_check_box_var)
special_chars_check_box.grid(row=0, column=3, padx=10, pady=10, sticky=tk.W)

length_label = tk.Label(window, text="Password Length:", bg="white")
length_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

length_entry = tk.Entry(window)
length_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

# Configure output label with minimum width and column span
output_label = tk.Label(window, text="Generated Password:", bg="white", width=50, anchor='w')
output_label.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky=tk.W)

def generate_password():
    length = int(length_entry.get())
    include_upper_case = uppercase_check_box_var.get()
    include_lower_case = lowercase_check_box_var.get()
    include_digits = digits_check_box_var.get()
    include_special_chars = special_chars_check_box_var.get()

    password = generate_new_password(length, include_upper_case, include_lower_case, include_digits, include_special_chars)
    output_label.config(text=f"Generated Password: {password}")

generate_button = tk.Button(window, text="Generate Password", bg="white", command=lambda: generate_password())
generate_button.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

def copy_to_clipboard():
    password = output_label.cget("text").replace("Generated Password: ", "")
    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()  # Keeps the clipboard content until the program is closed
    output_label.config(text="Password copied to clipboard!")

copy_button = tk.Button(window, text="Copy to Clipboard", bg="white", command=copy_to_clipboard)
copy_button.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

window.mainloop()