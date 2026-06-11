import customtkinter as ctk

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Ooh my shop!")
        self.geometry("1200x700")
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.create_header()
    
    def create_header(self):
        """This is where the header will go"""
        header = ctk.CTkFrame(self, height=50)
        header.pack(fill="x")
        

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()