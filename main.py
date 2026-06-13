import sys, ctypes, os, shutil, subprocess
import customtkinter as ctk
from tkinter import messagebox
from scanner import scan_files, scan_browser_data

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SShiderShower | Integrity Tool")
        self.geometry("700x600")
        self.utils = {
            "Everything": r"",
            "Shellbag": r""
        }
        self.mode_selector = ctk.CTkSegmentedButton(self, values=["PC Scan", "Browser Scan", "Utilities"], command=self.render_ui)
        self.mode_selector.set("PC Scan")
        self.mode_selector.pack(pady=10)
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)
        self.render_ui("PC Scan")

    def render_ui(self, value):
        for widget in self.content_frame.winfo_children(): widget.destroy()
        if value in ["PC Scan", "Browser Scan"]:
            ctk.CTkButton(self.content_frame, text="Run Scan", command=self.run_scan).pack(pady=10)
            self.result_area = ctk.CTkTextbox(self.content_frame, width=600, height=250)
            self.result_area.pack(pady=10)
            self.remove_button = ctk.CTkButton(self.content_frame, text="Remove Found Items", fg_color="red", state="disabled", command=self.remove_items)
            self.remove_button.pack(pady=10)
        else:
            cheat_list = "exloader | com.swiftsoft | xone | interium | skinchanger | extrimhack | nix | memesense | mvploader | sharkhack | exhack | neverkernel | vredux | mason | predator | aquila | luno | fecurity | cartel | aimstar | tkazer | naim | pellix | pussycat | axios | onemacro | softhub | proext | sapphire | interwebz | plague | vapehook | smurfwrecker | iniuria | yeahnot | legendware | hauntedproject | phoenixhack | onebyteradar | reborn | onebyte | osiris | ev0lve | ghostware | dexterion | basicmultihack | pudra | iCheat | sneakys | krazyhack | muhprime | drcheats | rootcheat | aeonix | zedt.pw | devcore | legifard | katebot | imxnoobx | w1nner | ekknod | neoxahack | warware | weave | aimmy | paradise | xenon | easysp | en1gma | Injector | .ahk | macros | bhop | bunnyhop | espd2x | avira | pphud | primordial | nonagon | legit | hvh | aimbot | s1mple | semirage | cheat | cs2.glow | invision | undetek | spurdo | webradar"
            ctk.CTkLabel(self.content_frame, text="Tools & Cheat Database Reference:").pack(pady=5)
            tb = ctk.CTkTextbox(self.content_frame, width=600, height=120)
            tb.insert("0.0", cheat_list); tb.configure(state="disabled"); tb.pack(pady=10)
            ctk.CTkButton(self.content_frame, text="Copy List", command=lambda: self.clipboard_append(cheat_list)).pack(pady=5)
            ctk.CTkButton(self.content_frame, text="Launch Everything", command=lambda: subprocess.Popen(self.utils['Everything'])).pack(pady=5)
            ctk.CTkButton(self.content_frame, text="Launch Shellbag", command=lambda: subprocess.Popen(self.utils['Shellbag'])).pack(pady=5)

    def run_scan(self):
        self.result_area.delete("0.0", "end")
        self.found_files = scan_files() if self.mode_selector.get() == "PC Scan" else scan_browser_data()
        if self.found_files:
            for p in self.found_files: self.result_area.insert("end", f"[!] {p}\n")
            self.remove_button.configure(state="normal")
        else: self.result_area.insert("end", "System clean.")

    def remove_items(self):
        if messagebox.askyesno("Confirm", "Remove identified items?"):
            for p in self.found_files:
                if os.path.exists(p):
                    try: shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
                    except: pass
            self.result_area.delete("0.0", "end"); self.result_area.insert("end", "Cleanup complete.")

if __name__ == "__main__":
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{os.path.abspath(sys.argv[0])}"', None, 1)
        sys.exit()
    App().mainloop()