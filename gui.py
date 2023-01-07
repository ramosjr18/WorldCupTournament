import tkinter
import tkinter.messagebox as messagebox
import customtkinter
import os
from PIL import Image

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("World Cup Tournament")
        self.geometry(f"{914}x{601}")
        self.iconbitmap("./logoico.ico")

        # configure grid layout (4x4)
        self.grid_columnconfigure((4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(
            self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=11, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(7, weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Options", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=(20,0), pady=(20, 10))

        #Botones de acccion 
        self.home_button = customtkinter.CTkButton(self.sidebar_frame, text="Home", command=self.homepage)
        self.home_button.grid(row=1, column=0, padx=20, pady=10)
        
        self.groupEtage_button = customtkinter.CTkButton(self.sidebar_frame, text="Group Etage", command=self.groupEtage)
        self.groupEtage_button.grid(row=2, column=0, padx=20, pady=10)
        
        self.sixteenround_button = customtkinter.CTkButton(self.sidebar_frame, text="16 round", command=self.sixteenround)
        self.sixteenround_button.grid(row=3, column=0, padx=20, pady=10)
        
        self.eightround_button = customtkinter.CTkButton(self.sidebar_frame, text="8 round", command=self.eightround)
        self.eightround_button.grid(row=4, column=0, padx=20, pady=10)
        
        self.semis_button = customtkinter.CTkButton(self.sidebar_frame, text="Semifinals", command=self.semifinals)
        self.semis_button.grid(row=5, column=0, padx=20, pady=10)
        
        self.thirdPlace_button = customtkinter.CTkButton(self.sidebar_frame, text="3th and 4th place", command=self.thirdplace)
        self.thirdPlace_button.grid(row=6, column=0, padx=20, pady=10)
        
        self.final_button = customtkinter.CTkButton(self.sidebar_frame, text="Final", command=self.final)
        self.final_button.grid(row=7, column=0, padx=20, pady=10)

        #acciones de la propia aplicacion 
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["System", "Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(
            row=9, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=10, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=11, column=0, padx=20, pady=(10, 20))

        #Home Frame
        self.home_Frame = customtkinter.CTkFrame(self)
        self.home_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.home_Frame.grid_columnconfigure(0, weight=1)
        self.home_Frame.grid_rowconfigure((1,2), weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.home_Frame, text="Instructions")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))
        self.teamEntry = customtkinter.CTkEntry(self.home_Frame)
        self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20))
        self.teamEntry.grid_columnconfigure(5, weight=1)

        #Group etage Frame
        self.groupEtage_Frame = customtkinter.CTkFrame(self)
        self.groupEtage_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.groupEtage_Frame.grid_columnconfigure(0, weight=1)
        self.groupEtage_Frame.grid_rowconfigure((1,2), weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.groupEtage_Frame, text="Group Etage")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))
        self.teamEntry = customtkinter.CTkEntry(self.groupEtage_Frame)
        self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20))
        self.teamEntry.grid_columnconfigure(5, weight=1)

        #16 round Frame
        self.sixteenround_Frame = customtkinter.CTkFrame(self)
        self.sixteenround_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.sixteenround_Frame.grid_columnconfigure(0, weight=1)
        self.sixteenround_Frame.grid_rowconfigure((1,2), weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.sixteenround_Frame, text="16 round")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))
        self.teamEntry = customtkinter.CTkEntry(self.sixteenround_Frame)
        self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20))
        self.teamEntry.grid_columnconfigure(5, weight=1)

        #8 round Frame
        self.eightround_Frame = customtkinter.CTkFrame(self)
        self.eightround_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.eightround_Frame.grid_columnconfigure(0, weight=1)
        self.eightround_Frame.grid_rowconfigure((1,2), weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.eightround_Frame, text="8 round")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))
        self.teamEntry = customtkinter.CTkEntry(self.eightround_Frame)
        self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20))
        self.teamEntry.grid_columnconfigure(5, weight=1)

        #Semifinals Frame
        self.semifinals_Frame = customtkinter.CTkFrame(self)
        self.semifinals_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.semifinals_Frame.grid_columnconfigure(0, weight=1)
        self.semifinals_Frame.grid_rowconfigure((1,2), weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.semifinals_Frame, text="Semifinals")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))
        self.teamEntry = customtkinter.CTkEntry(self.semifinals_Frame)
        self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20))
        self.teamEntry.grid_columnconfigure(5, weight=1)

        #3rd Place Frame 
        self.thirdplace_Frame = customtkinter.CTkFrame(self)
        self.thirdplace_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.thirdplace_Frame.grid_columnconfigure(0, weight=1)
        self.thirdplace_Frame.grid_rowconfigure((1,2), weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.thirdplace_Frame, text="3th Place")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))
        self.teamEntry = customtkinter.CTkEntry(self.thirdplace_Frame)
        self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20))
        self.teamEntry.grid_columnconfigure(5, weight=1)

        #Final Frame
        self.final_Frame = customtkinter.CTkFrame(self)
        self.final_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.final_Frame.grid_columnconfigure(0, weight=1)
        self.final_Frame.grid_rowconfigure((1,2), weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.final_Frame, text="Final")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))
        self.teamEntry = customtkinter.CTkEntry(self.final_Frame)
        self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20))
        self.teamEntry.grid_columnconfigure(5, weight=1)

        # #codigo de guia para el grid
        # for i in range(4):
        #     for j in range(1,5):
        #         frame = customtkinter.CTkFrame(self)
        #         frame.grid(row=i, column=j, padx=5, pady=5)
        #         label = customtkinter.CTkLabel(master=frame, text=f"Row {i}\nColumn {j}")
        #         label.pack()

        #bottom buttom to continue adding teams        
        self.main_button_1 = customtkinter.CTkButton(master=self, text="Next", text_color=("gray10", "#DCE4EE"), command=self.NextButtonEvent    )
        self.main_button_1.grid(row=4, column=2,columnspan=2, pady=(20, 20), sticky="nsew")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.groupEtage_button.configure(fg_color=("gray75", "gray25") if name == "groupEtage" else "transparent")
        self.sixteenround_button.configure(fg_color=("gray75", "gray25") if name == "sixteenround" else "transparent")
        self.eightround_button.configure(fg_color=("gray75", "gray25") if name == "eightround" else "transparent")
        self.semis_button.configure(fg_color=("gray75", "gray25") if name == "semifinals" else "transparent")
        self.thirdPlace_button.configure(fg_color=("gray75", "gray25") if name == "thirdplace" else "transparent")
        self.final_button.configure(fg_color=("gray75", "gray25") if name == "final" else "transparent")

        # show selected frame
        if name == "home":
            self.home_Frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_Frame.grid_forget()
        if name == "groupEtage":
            self.groupEtage_Frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.groupEtage_Frame.grid_forget()
        if name == "sixteenround":
            self.sixteenround_Frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.sixteenround_Frame.grid_forget()
        if name == "eightround":
            self.eightround_Frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.eightround_Frame.grid_forget()
        if name == "semifinals":
            self.semifinals_Frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.semifinals_Frame.grid_forget()
        if name == "thirdplace":
            self.thirdplace_Frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.thirdplace_Frame.grid_forget()
        if name == "final":
            self.final_Frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.final_Frame.grid_forget()

    #funtions to change pages 
    #main page function
    def homepage(self):
        self.select_frame_by_name("home")

    #group etage page function
    def groupEtage(self):
        self.select_frame_by_name("groupEtage")

    #group etage pagefunction
    def sixteenround(self):
        self.select_frame_by_name("sixteenround")

    #group etage pagefunction
    def eightround(self):
        self.select_frame_by_name("eightround")

    #group etage pagefunction
    def semifinals(self):
        self.select_frame_by_name("semifinals")

    #group etage pagefunction
    def thirdplace(self):
        self.select_frame_by_name("thirdplace")

    #group etage pagefunction
    def final(self):
        self.select_frame_by_name("final")



    #   Funciones de los botenes de la interfaz grafica
    #   funcion para cambiar la apariencia de la app
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    #   funcion para cambiar el tamaño del contenido dentro de la app
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    #   funcion para avanzar a la siguiente pag de añadir
    def NextButtonEvent(self):
        messagebox.showinfo(title="Alert", message="There is no other window!")

    #   funcion para añadir los 32 equipos
    def AddButtonEvent(self):
        messagebox.showinfo(title="Alert", message="Imagine that you have added an item")

    #   funcion para auto genrar los 32 equipos
    def AutoGenerateButtonEvent(self):
        messagebox.showinfo(title="Alert", message="Imagine that you have auto generated the teams!")

    #   Funcion para salir/cerrar la app
    def ExitButtonEvent(self):
        messagebox.showinfo(title="Warning", message="You are leaving the app")
        exit()

    

if __name__ == "__main__":
    app = App()
    app.mainloop()
