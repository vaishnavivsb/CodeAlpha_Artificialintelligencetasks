import customtkinter as ctk
from googletrans import Translator, LANGUAGES
from tkinter import messagebox

# Theme Settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class FullScreenTranslator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Set to Full Screen (Maximized)
        self.after(0, lambda: self.state('zoomed')) # Works for Windows
        self.title("CodeAlpha AI - Professional Language Translator")

        self.translator = Translator()

        # --- UI FONTS ---
        self.header_font = ("Helvetica", 48, "bold")
        self.label_font = ("Helvetica", 24)
        self.text_font = ("Helvetica", 20)
        self.button_font = ("Helvetica", 22, "bold")

        # Main Scrollable Frame to keep things centered
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=40, padx=60, fill="both", expand=True)

        # Header
        self.header = ctk.CTkLabel(self.main_frame, text="LANGUAGE TRANSLATION TOOL", font=self.header_font)
        self.header.pack(pady=(50, 30))

        # --- INPUT SECTION ---
        self.input_label = ctk.CTkLabel(self.main_frame, text="Enter Text Below:", font=self.label_font)
        self.input_label.pack(pady=10)
        
        self.source_text = ctk.CTkTextbox(self.main_frame, height=200, width=1000, font=self.text_font)
        self.source_text.pack(pady=10, padx=50)

        # --- SELECTION & ACTION ---
        # Language Dropdown
        self.lang_list = [lang.capitalize() for lang in LANGUAGES.values()]
        self.dest_lang_combo = ctk.CTkComboBox(self.main_frame, values=self.lang_list, width=300, height=50, font=self.button_font)
        self.dest_lang_combo.set("Tamil")
        self.dest_lang_combo.pack(pady=20)

        # Translate Button
        self.translate_btn = ctk.CTkButton(self.main_frame, text="TRANSLATE", 
                                          command=self.translate_text, 
                                          font=self.button_font,
                                          height=60, width=300, corner_radius=15)
        self.translate_btn.pack(pady=20)

        # --- OUTPUT SECTION ---
        self.output_label = ctk.CTkLabel(self.main_frame, text="Translated Result:", font=self.label_font)
        self.output_label.pack(pady=10)
        
        self.output_text = ctk.CTkTextbox(self.main_frame, height=200, width=1000, font=self.text_font, fg_color="#1e1e1e")
        self.output_text.pack(pady=10, padx=50)

    def translate_text(self):
        try:
            text = self.source_text.get("1.0", "end-1c").strip()
            target_lang = self.dest_lang_combo.get().lower()

            if not text:
                messagebox.showwarning("Input Required", "Please enter some text to translate.")
                return

            # Show a "Translating..." hint
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", "Processing...")
            self.update_idletasks()

            # Logic
            res = self.translator.translate(text, dest=target_lang)
            
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", res.text)
        except Exception as e:
            messagebox.showerror("Error", "Check your internet connection and try again.")

if __name__ == "__main__":
    app = FullScreenTranslator()
    app.mainloop()
