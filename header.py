import customtkinter as ctk
from datetime import datetime
from PIL import Image
import os

class Header(ctk.CTkFrame):
    """Header component with real PNG icons"""
    
    def __init__(self, parent):
        super().__init__(parent)
        
        # Get the path to icons folder
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icons_dir = os.path.join(current_dir, "icons")
        
        self.search_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(icons_dir, "search.png")),
            dark_image=Image.open(os.path.join(icons_dir, "search.png")),
            size=(18, 18)
        )
        
        self.dark_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(icons_dir, "dark.png")),
            dark_image=Image.open(os.path.join(icons_dir, "dark.png")),
            size=(18, 18)
        )
        
        self.settings_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(icons_dir, "settings.jpg")),
            dark_image=Image.open(os.path.join(icons_dir, "settings.jpg")),
            size=(18, 18)
        )
        
        self.minimize_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(icons_dir, "minimize.png")),
            dark_image=Image.open(os.path.join(icons_dir, "minimize.png")),
            size=(18, 18)
        )
        
        self.close_icon = ctk.CTkImage(
            light_image=Image.open(os.path.join(icons_dir, "close.png")),
            dark_image=Image.open(os.path.join(icons_dir, "close.png")),
            size=(18, 18)
        )
        
        # Make header transparent
        self.configure(fg_color="transparent", height=100)
        self.pack(fill="x", padx=20, pady=(10, 0))
        self.pack_propagate(False)
        
        # Top row
        top_row = ctk.CTkFrame(self, fg_color="transparent")
        top_row.pack(fill="x", pady=(10, 5))
        
        # LEFT: Logo and name
        left = ctk.CTkFrame(top_row, fg_color="transparent")
        left.pack(side="left", fill="y")
        
        ctk.CTkLabel(left, text="■", font=("Segoe UI", 28, "bold"), 
                     text_color="#3B82F6").pack(side="left", padx=(0, 10))
        
        ctk.CTkLabel(left, text="SHOP PRO", font=("Segoe UI", 22, "bold"),
                     text_color="#FFFFFF").pack(side="left")
        
        ctk.CTkLabel(left, text="•", font=("Segoe UI", 18),
                     text_color="#6B7280").pack(side="left", padx=10)
        
        ctk.CTkLabel(left, text="My Store", font=("Segoe UI", 18),
                     text_color="#9CA3AF").pack(side="left")
        
        middle = ctk.CTkFrame(top_row, fg_color="transparent")
        middle.pack(side="left", expand=True, fill="x", padx=40)
        
        self.search_entry = ctk.CTkEntry(
            middle,
            placeholder_text="Search products...",
            font=("Segoe UI", 14),
            height=40,
            corner_radius=8
        )
        self.search_entry.pack(side="left", fill="x", expand=True)
        
        right = ctk.CTkFrame(top_row, fg_color="transparent")
        right.pack(side="right", fill="y")
        
        self.dark_btn = ctk.CTkButton(
            right,
            text="",
            image=self.dark_icon,
            width=40,
            height=40,
            corner_radius=8,
            fg_color="#1F2937",
            hover_color="#374151"
        )
        self.dark_btn.pack(side="left", padx=5)
        
        # Settings button
        settings_btn = ctk.CTkButton(
            right,
            text="",
            image=self.settings_icon,
            width=40,
            height=40,
            corner_radius=8,
            fg_color="#1F2937",
            hover_color="#374151"
        )
        settings_btn.pack(side="left", padx=5)
        
        # Minimize button
        min_btn = ctk.CTkButton(
            right,
            text="",
            image=self.minimize_icon,
            width=40,
            height=40,
            corner_radius=8,
            fg_color="#1F2937",
            hover_color="#374151"
        )
        min_btn.pack(side="left", padx=5)
        
        close_btn = ctk.CTkButton(
            right,
            text="",
            image=self.close_icon,
            width=40,
            height=40,
            corner_radius=8,
            fg_color="#EF4444",
            hover_color="#DC2626"
        )
        close_btn.pack(side="left", padx=5)
        
        min_btn.configure(command=self.minimize_app)
        close_btn.configure(command=self.close_app)
        
        bottom = ctk.CTkFrame(self, fg_color="transparent")
        bottom.pack(fill="x", pady=(5, 10))
        
        ctk.CTkFrame(bottom, height=1, fg_color="#374151").pack(fill="x", pady=(0, 10))
        
        dt_container = ctk.CTkFrame(bottom, fg_color="transparent")
        dt_container.pack(anchor="w")
        
        ctk.CTkLabel(dt_container, text="📅", font=("Segoe UI", 12),
                     text_color="#6B7280").pack(side="left", padx=(0, 8))
        
        date_str = datetime.now().strftime("%A, %B %d, %Y")
        ctk.CTkLabel(dt_container, text=date_str, font=("Segoe UI", 13),
                     text_color="#9CA3AF").pack(side="left")
        
        ctk.CTkLabel(dt_container, text="|", font=("Segoe UI", 13),
                     text_color="#4B5563").pack(side="left", padx=10)
        
        ctk.CTkLabel(dt_container, text="🕐", font=("Segoe UI", 12),
                     text_color="#6B7280").pack(side="left", padx=(0, 8))
        
        self.time_label = ctk.CTkLabel(dt_container, text="", font=("Segoe UI", 13),
                                       text_color="#9CA3AF")
        self.time_label.pack(side="left")
        
        self.update_time()
    
    def minimize_app(self):
        self.winfo_toplevel().iconify()
    
    def close_app(self):
        self.winfo_toplevel().destroy()
    
    def update_time(self):
        from datetime import datetime
        self.time_label.configure(text=datetime.now().strftime("%I:%M %p"))
        self.after(1000, self.update_time)
    
    def get_search_text(self):
        return self.search_entry.get()