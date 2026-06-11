import customtkinter as ctk

class Header(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.configure(height=50)
        self.pack(fill="x")
        
