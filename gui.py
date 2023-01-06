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
        self.iconbitmap("")

        # configure grid layout (4x4)
        self.grid_columnconfigure((4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        #funtions to change pages 
        #main page function
        def groupEtage():
            # create boxes for each entry  on row 0 column 1
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=0, column=1, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)


            # create boxes for each entry  on row 0 column 2
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=0, column=2, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)


            # create boxes for each entry  on row 0 column 3
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=0, column=3, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)


            # create boxes for each entry  on row 0 column 4
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=0, column=4, columnspan=1, rowspan=1, padx=(20, 20), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)


            # create boxes for each entry on row 1 column 1
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=1, column=1, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Teams")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)


            # create boxes for each entry  on row 1 column 2
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=1, column=2, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)



            # create boxes for each entry  on row 1 column 3
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=1, column=3, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)


            # create boxes for each entry  on row 1 column 4
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=1, column=4, columnspan=1, rowspan=1, padx=(20, 20), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)


            # create boxes for each entry on row 2 columnm 1
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=2, column=1, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Teams")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)


            # create boxes for each entry  on row 2 column 2
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=2, column=2, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)


            # create boxes for each entry  on row 2 column 3
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=2, column=3, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)


            # create boxes for each entry  on row 2 column 4
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=2, column=4, columnspan=1, rowspan=1, padx=(20, 20), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)


            # create boxes for each entry on row 3 column 1
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=3, column=1, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)


            # create boxes for each entry  on row 3 column 2
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=3, column=2, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)


            # create boxes for each entry  on row 3 column 3
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=3, column=3, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)

            # create boxes for each entry  on row 3 column 4
            self.slider_progressbar_frame = customtkinter.CTkFrame(self)
            self.slider_progressbar_frame.grid(row=3, column=4, columnspan=1, rowspan=1, padx=(20, 20), pady=(10, 10), sticky="nsew")
            self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
            self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")

            self.teamEntry = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
            self.teamEntry.grid_columnconfigure(5, weight=1)
        
        #group etage page function
        def mainpage():
            self.groupEtage_Frame = customtkinter.CTkFrame(self)
            
            self.groupEtage_Frame = customtkinter.CTkFrame(self)
            self.groupEtage_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
            self.groupEtage_Frame.grid_columnconfigure(0, weight=1)
            self.groupEtage_Frame.grid_rowconfigure((1,2), weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.groupEtage_Frame, text="main page")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))

            self.teamEntry = customtkinter.CTkEntry(self.groupEtage_Frame)
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20))
            self.teamEntry.grid_columnconfigure(5, weight=1)

            #group etage pagefunction
        def sixteenound():
            self.groupEtage_Frame = customtkinter.CTkFrame(self)
            
            self.groupEtage_Frame = customtkinter.CTkFrame(self)
            self.groupEtage_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
            self.groupEtage_Frame.grid_columnconfigure(0, weight=1)
            self.groupEtage_Frame.grid_rowconfigure((1,2), weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.groupEtage_Frame, text="16 round")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))

            self.teamEntry = customtkinter.CTkEntry(self.groupEtage_Frame)
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20))
            self.teamEntry.grid_columnconfigure(5, weight=1)

            #group etage pagefunction
        def eightround():
            self.groupEtage_Frame = customtkinter.CTkFrame(self)
            
            self.groupEtage_Frame = customtkinter.CTkFrame(self)
            self.groupEtage_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
            self.groupEtage_Frame.grid_columnconfigure(0, weight=1)
            self.groupEtage_Frame.grid_rowconfigure((1,2), weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.groupEtage_Frame, text="8 round")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))

            self.teamEntry = customtkinter.CTkEntry(self.groupEtage_Frame)
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20))
            self.teamEntry.grid_columnconfigure(5, weight=1)

        #group etage pagefunction
        def semifinals():
            self.groupEtage_Frame = customtkinter.CTkFrame(self)
            
            self.groupEtage_Frame = customtkinter.CTkFrame(self)
            self.groupEtage_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
            self.groupEtage_Frame.grid_columnconfigure(0, weight=1)
            self.groupEtage_Frame.grid_rowconfigure((1,2), weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.groupEtage_Frame, text="Semifinals")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))

            self.teamEntry = customtkinter.CTkEntry(self.groupEtage_Frame)
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20))
            self.teamEntry.grid_columnconfigure(5, weight=1)

        #group etage pagefunction
        def thirdplace():
            self.groupEtage_Frame = customtkinter.CTkFrame(self)
            
            self.groupEtage_Frame = customtkinter.CTkFrame(self)
            self.groupEtage_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
            self.groupEtage_Frame.grid_columnconfigure(0, weight=1)
            self.groupEtage_Frame.grid_rowconfigure((1,2), weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.groupEtage_Frame, text="3th Place")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))

            self.teamEntry = customtkinter.CTkEntry(self.groupEtage_Frame)
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20))
            self.teamEntry.grid_columnconfigure(5, weight=1)

        #group etage pagefunction
        def final():
            self.groupEtage_Frame = customtkinter.CTkFrame(self)
            
            self.groupEtage_Frame = customtkinter.CTkFrame(self)
            self.groupEtage_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
            self.groupEtage_Frame.grid_columnconfigure(0, weight=1)
            self.groupEtage_Frame.grid_rowconfigure((1,2), weight=1)

            self.seg_button_1 = customtkinter.CTkLabel(self.groupEtage_Frame, text="Final")
            self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))

            self.teamEntry = customtkinter.CTkEntry(self.groupEtage_Frame)
            self.teamEntry.grid(row=1, column=0, padx=(10, 10), pady=(0, 20))
            self.teamEntry.grid_columnconfigure(5, weight=1)


        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(
            self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=11, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(7, weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Options", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=(20,0), pady=(20, 10))

        #Botones de acccion 
        self.sidebar_button_2 = customtkinter.CTkButton(
            self.sidebar_frame, text="Main", command=mainpage)
        self.sidebar_button_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.sidebar_button_3 = customtkinter.CTkButton(
            self.sidebar_frame, text="Group Etage", command=groupEtage)
        self.sidebar_button_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.sidebar_button_3 = customtkinter.CTkButton(
            self.sidebar_frame, text="16 round", command=sixteenound)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        
        self.sidebar_button_3 = customtkinter.CTkButton(
            self.sidebar_frame, text="8 round", command=eightround)
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=10)
        
        self.sidebar_button_3 = customtkinter.CTkButton(
            self.sidebar_frame, text="Semifinals", command=semifinals)
        self.sidebar_button_3.grid(row=5, column=0, padx=20, pady=10)
        
        self.sidebar_button_3 = customtkinter.CTkButton(
            self.sidebar_frame, text="3th and 4th place", command=thirdplace)
        self.sidebar_button_3.grid(row=6, column=0, padx=20, pady=10)
        
        self.sidebar_button_3 = customtkinter.CTkButton(
            self.sidebar_frame, text="Final", command=final)
        self.sidebar_button_3.grid(row=7, column=0, padx=20, pady=10)

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

        # #codigo de guia para el grid
        # for i in range(4):
        #     for j in range(1,5):
        #         frame = customtkinter.CTkFrame(self)
        #         frame.grid(row=i, column=j, padx=5, pady=5)
        #         label = customtkinter.CTkLabel(master=frame, text=f"Row {i}\nColumn {j}")
        #         label.pack()

        #bottom buttom to continue adding teams        
        self.main_button_1 = customtkinter.CTkButton(master=self, text="Next", text_color=("gray10", "#DCE4EE"), command=self.NextButtonEvent    )
        self.main_button_1.grid(row=4, column=2,columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

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
