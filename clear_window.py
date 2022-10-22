def clear_window(tk):
    for widget in tk.winfo_children():
        widget.destroy()
