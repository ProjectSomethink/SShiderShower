import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, change_game_callback, **kwargs):
        super().__init__(master, **kwargs)
        self.change_game_callback = change_game_callback
        
        ctk.CTkLabel(self, text="SShiderShower", font=("Arial", 20, "bold")).pack(pady=20)
        
        # CS2 Button - Triggers 'cs2' mode
        self.btn_cs2 = ctk.CTkButton(self, text="CS2 Checker", 
                                     command=lambda: self.change_game_callback("cs2"))
        self.btn_cs2.pack(pady=10, padx=20)
        
        # Minecraft Button - Triggers 'minecraft' mode
        self.btn_mc = ctk.CTkButton(self, text="Minecraft Checker", 
                                    command=lambda: self.change_game_callback("minecraft"))
        self.btn_mc.pack(pady=10, padx=20)