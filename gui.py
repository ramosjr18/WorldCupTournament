import tkinter 
from tkinter import *
import tkinter.messagebox as messagebox
import customtkinter
import os
from PIL import Image
import team as tm
import group as grp
import random as rnd

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
        #self.iconbitmap("logoico.ico")

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
        self.home_Frame.grid_columnconfigure((0,1,2,3), weight=1)
        self.home_Frame.grid_rowconfigure((1,2,3,4,5), weight=1)
        self.TittleLabel = customtkinter.CTkLabel(self.home_Frame, text="Welcome", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.TittleLabel.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(20, 10))
        self.inslabel = customtkinter.CTkLabel(self.home_Frame,
                                            text="Here you can add, auto generate the teams \n and also add the group etage results \n also see the diferent etages by clicking the  buttons in the side bar",
                                            font=customtkinter.CTkFont(size=15))
        self.inslabel.grid(row=1, column=1, columnspan=2, padx=(10, 10), pady=(10, 10))
        #bottom buttom to continue adding teams
        self.main_button_1 = customtkinter.CTkButton(master=self.home_Frame, text="Add Teams", text_color=("gray10", "#DCE4EE"), command=self.Addteams1)
        self.main_button_1.grid(row=2, column=1,columnspan=2,padx=(20, 20), pady=(10, 20), sticky="nsew")
        #bottom buttom to continue adding teams
        self.main_button_1 = customtkinter.CTkButton(master=self.home_Frame, text="Auto Generate \n teams", text_color=("gray10", "#DCE4EE"), command=self.NextButtonEvent    )
        self.main_button_1.grid(row=3, column=1,columnspan=2,padx=(20, 20), pady=(10, 20), sticky="nsew")
        #bottom buttom to continue adding teams
        self.main_button_1 = customtkinter.CTkButton(master=self.home_Frame, text="Add Group Etage \n Results", text_color=("gray10", "#DCE4EE"), command=self.NextButtonEvent    )
        self.main_button_1.grid(row=4, column=1,columnspan=2,padx=(20, 20), pady=(10, 20), sticky="nsew")
        
        #Frame to add Teams
        self.AddTeams_Frame = tkinter.Frame(self)
        self.AddTeams_Frame.grid(row=0, column=1,  columnspan=4, rowspan=4, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.AddTeams_Frame.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.AddTeams_Frame.grid_rowconfigure((1,2,3), weight=1)

        # create boxes for each entry  on row 0 column 1
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=0, column=1, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 1")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry1 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry1.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry1.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 0 column 2
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=0, column=2, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 2")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry2 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry2.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry2.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 0 column 3
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=0, column=3, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 3")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry3 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry3.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry3.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 0 column 4
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=0, column=4, columnspan=1, rowspan=1, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 4")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry4 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry4.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry4.grid_columnconfigure(5, weight=1)

        # create boxes for each entry on row 1 column 1
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=1, column=1, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Teams 5")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry5 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry5.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry5.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 1 column 2
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=1, column=2, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 6")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry6 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry6.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry6.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 1 column 3
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=1, column=3, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 7")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry7 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry7.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry7.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 1 column 4
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=1, column=4, columnspan=1, rowspan=1, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 8")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry8 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry8.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry8.grid_columnconfigure(5, weight=1)

        # create boxes for each entry on row 2 columnm 1
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=2, column=1, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Teams 9")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry9 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry9.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry9.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 2 column 2
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=2, column=2, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 10")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry10 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry10.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry10.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 2 column 3
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=2, column=3, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 11")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry11 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry11.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry11.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 2 column 4
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=2, column=4, columnspan=1, rowspan=1, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 12")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry12 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry12.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry12.grid_columnconfigure(5, weight=1)

        # create boxes for each entry on row 3 column 1
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=3, column=1, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 13")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry13 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry13.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry13.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 3 column 2
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=3, column=2, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 14")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry14 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry14.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry14.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 3 column 3
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=3, column=3, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 15")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry15 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry15.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry15.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 3 column 4
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams_Frame)
        self.slider_progressbar_frame.grid(row=3, column=4, columnspan=1, rowspan=1, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 16")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry16 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry16.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry16.grid_columnconfigure(5, weight=1)

        #button to continue adding teams
        self.continuebutton = customtkinter.CTkButton(master=self.AddTeams_Frame, text="Continue", text_color=("gray10", "#DCE4EE"), command=self.Addteams2)
        self.continuebutton.grid(row=4, column=2, columnspan=2, padx=(20, 10), pady=(10, 20), sticky="nsew")

        #Frame to add Teams 2
        self.AddTeams2_Frame = tkinter.Frame(self)
        self.AddTeams2_Frame.grid(row=0, column=1,  columnspan=4, rowspan=4, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.AddTeams2_Frame.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.AddTeams2_Frame.grid_rowconfigure((1,2,3), weight=1)

        # create boxes for each entry  on row 0 column 1
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=0, column=1, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 17")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry17 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry17.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry17.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 0 column 2
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=0, column=2, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 18")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry18 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry18.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry18.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 0 column 3
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=0, column=3, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 19")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry19 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry19.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry19.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 0 column 4
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=0, column=4, columnspan=1, rowspan=1, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 20")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry20 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry20.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry20.grid_columnconfigure(5, weight=1)

        # create boxes for each entry on row 1 column 1
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=1, column=1, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Teams 21")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry21 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry21.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry21.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 1 column 2
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=1, column=2, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 22")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry22 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry22.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry22.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 1 column 3
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=1, column=3, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 23")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry23 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry23.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry23.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 1 column 4
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=1, column=4, columnspan=1, rowspan=1, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 24")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry24 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry24.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry24.grid_columnconfigure(5, weight=1)

        # create boxes for each entry on row 2 columnm 1
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=2, column=1, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 25")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry25 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry25.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry25.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 2 column 2
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=2, column=2, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 26")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry26 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry26.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry26.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 2 column 3
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=2, column=3, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 27")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry27 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry27.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry27.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 2 column 4
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=2, column=4, columnspan=1, rowspan=1, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 28")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry28 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry28.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry28.grid_columnconfigure(5, weight=1)

        # create boxes for each entry on row 3 column 1
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=3, column=1, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 29")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry29 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry29.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry29.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 3 column 2
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=3, column=2, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 30")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry30 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry30.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry30.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 3 column 3
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=3, column=3, columnspan=1, rowspan=1, padx=(20, 0), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 31")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry31 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry31.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry31.grid_columnconfigure(5, weight=1)

        # create boxes for each entry  on row 3 column 4
        self.slider_progressbar_frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        self.slider_progressbar_frame.grid(row=3, column=4, columnspan=1, rowspan=1, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(1, weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Add Team 32")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        self.teamEntry32 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter team")
        self.teamEntry32.grid(row=1, column=0, padx=(10, 10), pady=(0, 20), sticky="ew")
        self.teamEntry32.grid_columnconfigure(5, weight=1)
        
        def SaveTeams() ->list:
            #List to store every team 
            self.teams = []
            self.teams.append(self.teamEntry1.get())
            self.teams.append(self.teamEntry2.get())
            self.teams.append(self.teamEntry3.get())
            self.teams.append(self.teamEntry4.get())
            self.teams.append(self.teamEntry5.get())
            self.teams.append(self.teamEntry6.get())
            self.teams.append(self.teamEntry7.get())
            self.teams.append(self.teamEntry8.get())
            self.teams.append(self.teamEntry9.get())
            self.teams.append(self.teamEntry10.get())
            self.teams.append(self.teamEntry11.get())
            self.teams.append(self.teamEntry12.get())
            self.teams.append(self.teamEntry13.get())
            self.teams.append(self.teamEntry14.get())
            self.teams.append(self.teamEntry15.get())
            self.teams.append(self.teamEntry16.get())
            self.teams.append(self.teamEntry17.get())
            self.teams.append(self.teamEntry18.get())
            self.teams.append(self.teamEntry19.get())
            self.teams.append(self.teamEntry20.get())
            self.teams.append(self.teamEntry21.get())
            self.teams.append(self.teamEntry22.get())
            self.teams.append(self.teamEntry23.get())
            self.teams.append(self.teamEntry24.get())
            self.teams.append(self.teamEntry25.get())
            self.teams.append(self.teamEntry26.get())
            self.teams.append(self.teamEntry27.get())
            self.teams.append(self.teamEntry28.get())
            self.teams.append(self.teamEntry29.get())
            self.teams.append(self.teamEntry30.get())
            self.teams.append(self.teamEntry31.get())
            self.teams.append(self.teamEntry32.get())
            
            print(self.teams)
            with open("text.txt", "w") as f:
                f.writelines("%s\n" % l for l in self.teams)
            self.destroy()
            self.__init__()
            self.select_frame_by_name("groupEtage")
            
        self.saveButton = customtkinter.CTkButton(master=self.AddTeams2_Frame, text="Save", text_color=("gray10", "#DCE4EE"), command=SaveTeams)
        self.saveButton.grid(row=4, column=2, columnspan=2, padx=(20, 10), pady=(10, 20), sticky="nsew")

        lines_list = []
        with open('text.txt', 'r') as file:
            lines = file.readlines()

        #variables for team labels 
        self.one = lines[0]
        self.two = lines[1]
        self.three = lines[2]
        self.four = lines[3]
        self.five = lines[4]
        self.six = lines[5]
        self.seven = lines[6]
        self.ocho = lines[7]
        self.nine = lines[8]
        self.ten = lines[9]
        self.once = lines[10]
        self.doce = lines[11]
        self.trece = lines[12]
        self.catorce = lines[13]
        self.quince = lines[14]
        self.dieciseis = lines[15]
        self.diezsiete = lines[16]
        self.diezocho = lines[17]
        self.dieznine = lines[18]
        self.veinte = lines[19]
        self.dosuno = lines[20]
        self.dosdos = lines[21]
        self.dostres = lines[22]
        self.doscuatro = lines[23]
        self.doscinco = lines[24]
        self.dosseis = lines[25]
        self.dossiete = lines[26]
        self.dosocho = lines[27]
        self.dosnine = lines[28]
        self.treinta = lines[29]
        self.tresuno = lines[30]
        self.tresdos = lines[31]

        #Group etage Frame
        self.groupEtage_Frame = customtkinter.CTkFrame(self)
        self.groupEtage_Frame.grid(row=0, column=1, columnspan=4, rowspan=5, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.groupEtage_Frame.grid_columnconfigure((0,1), weight=1)
        self.groupEtage_Frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)
        self.titlelable = customtkinter.CTkLabel(self.groupEtage_Frame, text="Group Etage")
        self.titlelable.grid(row=0, column=0, columnspan= 2, padx=(20, 20), pady=(10, 10))

        self.groupA_frame = customtkinter.CTkFrame(self.groupEtage_Frame)
        self.groupA_frame.grid(row=1, column=0, rowspan=2)
        self.groupA_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupA_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)
        self.labelgroupA = customtkinter.CTkLabel(self.groupA_frame, text="Group A")
        self.labelgroupA.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupA_frame, text="Team")
        self.labelTeamA.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupA_frame, text="PJ")
        self.labelPjA.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupA_frame, text="W")
        self.labelgroupAw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupA_frame, text="L")
        self.labelTeamAl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupA_frame, text="D")
        self.labelTeamAd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupA_frame, text="PTS")
        self.labelPtsA.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamAone = customtkinter.CTkLabel(self.groupA_frame, text="")
        self.labelTeamAone.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPjA.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelgroupAw.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAl.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAd.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPtsA.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamAtwo = customtkinter.CTkLabel(self.groupA_frame, text="")
        self.labelTeamAtwo.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPjA.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelgroupAw.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAl.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAd.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPtsA.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamAthree = customtkinter.CTkLabel(self.groupA_frame, text="")
        self.labelTeamAthree.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPjA.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelgroupAw.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAl.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAd.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPtsA.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamAfour = customtkinter.CTkLabel(self.groupA_frame, text="")
        self.labelTeamAfour.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPjA.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelgroupAw.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAl.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAd.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPtsA.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        self.groupB_frame = customtkinter.CTkFrame(self.groupEtage_Frame)
        self.groupB_frame.grid(row=3, column=0, rowspan=2)
        self.groupB_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupB_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)
        self.labelgroupA = customtkinter.CTkLabel(self.groupB_frame, text="Group B")
        self.labelgroupA.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupB_frame, text="Team")
        self.labelTeamA.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupB_frame, text="PJ")
        self.labelPjA.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupB_frame, text="W")
        self.labelgroupAw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupB_frame, text="L")
        self.labelTeamAl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupB_frame, text="D")
        self.labelTeamAd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupB_frame, text="PTS")
        self.labelPtsA.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamBone = customtkinter.CTkLabel(self.groupB_frame, text="")
        self.labelTeamBone.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPjA.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelgroupAw.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAl.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAd.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPtsA.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamBtwo = customtkinter.CTkLabel(self.groupB_frame, text="")
        self.labelTeamBtwo.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPjA.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelgroupAw.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAl.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAd.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPtsA.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamBthree = customtkinter.CTkLabel(self.groupB_frame, text="")
        self.labelTeamBthree.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPjA.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelgroupAw.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAl.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAd.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPtsA.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamBfour = customtkinter.CTkLabel(self.groupB_frame, text="")
        self.labelTeamBfour.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPjA.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelgroupAw.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAl.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAd.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPtsA.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        self.groupC_frame = customtkinter.CTkFrame(self.groupEtage_Frame)
        self.groupC_frame.grid(row=1, column=1, columnspan=2, rowspan=2)
        self.groupC_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupC_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)
        self.labelgroupA = customtkinter.CTkLabel(self.groupC_frame, text="Group C")
        self.labelgroupA.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupC_frame, text="Team")
        self.labelTeamA.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupC_frame, text="PJ")
        self.labelPjA.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupC_frame, text="W")
        self.labelgroupAw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupC_frame, text="L")
        self.labelTeamAl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupC_frame, text="D")
        self.labelTeamAd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupC_frame, text="PTS")
        self.labelPtsA.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupC_frame, text="Holanda")
        self.labelTeamA.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPjA.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelgroupAw.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAl.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAd.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPtsA.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupC_frame, text="Ecuador")
        self.labelTeamA.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPjA.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelgroupAw.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAl.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAd.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPtsA.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupC_frame, text="Senegal")
        self.labelTeamA.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPjA.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelgroupAw.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAl.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAd.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPtsA.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupC_frame, text="Qatar")
        self.labelTeamA.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPjA.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelgroupAw.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAl.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAd.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPtsA.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        self.groupD_frame = customtkinter.CTkFrame(self.groupEtage_Frame)
        self.groupD_frame.grid(row=3, column=1, columnspan=2, rowspan=2)
        self.groupD_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupD_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)
        self.labelgroupA = customtkinter.CTkLabel(self.groupD_frame, text="Group D")
        self.labelgroupA.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupD_frame, text="Team")
        self.labelTeamA.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupD_frame, text="PJ")
        self.labelPjA.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupD_frame, text="W")
        self.labelgroupAw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupD_frame, text="L")
        self.labelTeamAl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupD_frame, text="D")
        self.labelTeamAd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupD_frame, text="PTS")
        self.labelPtsA.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupD_frame, text="Holanda")
        self.labelTeamA.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPjA.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelgroupAw.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAl.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAd.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPtsA.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupD_frame, text="Ecuador")
        self.labelTeamA.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPjA.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelgroupAw.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAl.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAd.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPtsA.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupD_frame, text="Senegal")
        self.labelTeamA.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPjA.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelgroupAw.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAl.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAd.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPtsA.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupD_frame, text="Qatar")
        self.labelTeamA.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPjA.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelgroupAw.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAl.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAd.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPtsA.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        #bottom buttom to continue seeing
        self.nextEtage = customtkinter.CTkButton(master=self.groupEtage_Frame, text="Next", text_color=("gray10", "#DCE4EE"), command=self.NextButtonEvent    )
        self.nextEtage.grid(row=6, column=0, columnspan= 2, padx=(20, 20), pady=(10, 10))

        #Group etage 2 Frame
        self.groupEtage2_Frame = customtkinter.CTkFrame(self)
        self.groupEtage2_Frame.grid(row=0, column=1, columnspan=4, rowspan=5, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.groupEtage2_Frame.grid_columnconfigure((0,1), weight=1)
        self.groupEtage2_Frame.grid_rowconfigure((1,2,3,4), weight=1)
        self.titlelable = customtkinter.CTkLabel(self.groupEtage2_Frame, text="Group Etage")
        self.titlelable.grid(row=0, column=0, columnspan= 2, padx=(20, 20), pady=(10, 10))
        self.groupA_frame = customtkinter.CTkFrame(self.groupEtage2_Frame)
        self.groupA_frame.grid(row=1, column=0, rowspan=2)
        self.groupA_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupA_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)
        self.labelgroupA = customtkinter.CTkLabel(self.groupA_frame, text="Group E")
        self.labelgroupA.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupA_frame, text="Team")
        self.labelTeamA.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupA_frame, text="PJ")
        self.labelPjA.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupA_frame, text="W")
        self.labelgroupAw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupA_frame, text="L")
        self.labelTeamAl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupA_frame, text="D")
        self.labelTeamAd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupA_frame, text="PTS")
        self.labelPtsA.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupA_frame, text="Holanda")
        self.labelTeamA.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPjA.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelgroupAw.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAl.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAd.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPtsA.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupA_frame, text="Ecuador")
        self.labelTeamA.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPjA.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelgroupAw.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAl.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAd.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPtsA.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupA_frame, text="Senegal")
        self.labelTeamA.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPjA.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelgroupAw.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAl.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAd.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPtsA.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupA_frame, text="Qatar")
        self.labelTeamA.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPjA.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelgroupAw.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAl.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAd.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPtsA.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        self.groupB_frame = customtkinter.CTkFrame(self.groupEtage2_Frame)
        self.groupB_frame.grid(row=3, column=0, rowspan=2)
        self.groupB_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupB_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)
        self.labelgroupA = customtkinter.CTkLabel(self.groupB_frame, text="Group F")
        self.labelgroupA.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupB_frame, text="Team")
        self.labelTeamA.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupB_frame, text="PJ")
        self.labelPjA.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupB_frame, text="W")
        self.labelgroupAw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupB_frame, text="L")
        self.labelTeamAl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupB_frame, text="D")
        self.labelTeamAd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupB_frame, text="PTS")
        self.labelPtsA.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupB_frame, text="Holanda")
        self.labelTeamA.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPjA.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelgroupAw.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAl.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAd.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPtsA.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupB_frame, text="Ecuador")
        self.labelTeamA.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPjA.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelgroupAw.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAl.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAd.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPtsA.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupB_frame, text="Senegal")
        self.labelTeamA.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPjA.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelgroupAw.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAl.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAd.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPtsA.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupB_frame, text="Qatar")
        self.labelTeamA.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPjA.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelgroupAw.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAl.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamAd.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPtsA.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        self.groupC_frame = customtkinter.CTkFrame(self.groupEtage2_Frame)
        self.groupC_frame.grid(row=1, column=1, columnspan=2, rowspan=2)
        self.groupC_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupC_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)
        self.labelgroupA = customtkinter.CTkLabel(self.groupC_frame, text="Group G")
        self.labelgroupA.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupC_frame, text="Team")
        self.labelTeamA.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupC_frame, text="PJ")
        self.labelPjA.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupC_frame, text="W")
        self.labelgroupAw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupC_frame, text="L")
        self.labelTeamAl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupC_frame, text="D")
        self.labelTeamAd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupC_frame, text="PTS")
        self.labelPtsA.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupC_frame, text="Holanda")
        self.labelTeamA.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPjA.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelgroupAw.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAl.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAd.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPtsA.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupC_frame, text="Ecuador")
        self.labelTeamA.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPjA.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelgroupAw.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAl.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAd.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPtsA.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupC_frame, text="Senegal")
        self.labelTeamA.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPjA.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelgroupAw.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAl.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAd.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPtsA.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupC_frame, text="Qatar")
        self.labelTeamA.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPjA.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelgroupAw.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAl.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamAd.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPtsA.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        self.groupD_frame = customtkinter.CTkFrame(self.groupEtage2_Frame)
        self.groupD_frame.grid(row=3, column=1, columnspan=2, rowspan=2)
        self.groupD_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupD_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)
        self.labelgroupA = customtkinter.CTkLabel(self.groupD_frame, text="Group H")
        self.labelgroupA.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupD_frame, text="Team")
        self.labelTeamA.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupD_frame, text="PJ")
        self.labelPjA.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupD_frame, text="W")
        self.labelgroupAw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupD_frame, text="L")
        self.labelTeamAl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupD_frame, text="D")
        self.labelTeamAd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupD_frame, text="PTS")
        self.labelPtsA.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupD_frame, text="Holanda")
        self.labelTeamA.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPjA.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelgroupAw.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAl.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAd.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPtsA.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupD_frame, text="Ecuador")
        self.labelTeamA.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPjA.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelgroupAw.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAl.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAd.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPtsA.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupD_frame, text="Senegal")
        self.labelTeamA.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPjA.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelgroupAw.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAl.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAd.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPtsA.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))
        self.labelTeamA = customtkinter.CTkLabel(self.groupD_frame, text="Qatar")
        self.labelTeamA.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPjA.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAw = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelgroupAw.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAl = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAl.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAd = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamAd.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsA = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPtsA.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        #16 round Frame
        self.sixteenround_Frame = customtkinter.CTkFrame(self)
        self.sixteenround_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.sixteenround_Frame.grid_columnconfigure(0, weight=1)
        self.sixteenround_Frame.grid_rowconfigure((1,2), weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.sixteenround_Frame, text="16 round")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))

        #8 round Frame
        self.eightround_Frame = customtkinter.CTkFrame(self)
        self.eightround_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.eightround_Frame.grid_columnconfigure(0, weight=1)
        self.eightround_Frame.grid_rowconfigure((1,2), weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.eightround_Frame, text="8 round")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))

        #Semifinals Frame
        self.semifinals_Frame = customtkinter.CTkFrame(self)
        self.semifinals_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.semifinals_Frame.grid_columnconfigure(0, weight=1)
        self.semifinals_Frame.grid_rowconfigure((1,2), weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.semifinals_Frame, text="Semifinals")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))

        #3rd Place Frame
        self.thirdplace_Frame = customtkinter.CTkFrame(self)
        self.thirdplace_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.thirdplace_Frame.grid_columnconfigure(0, weight=1)
        self.thirdplace_Frame.grid_rowconfigure((1,2), weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.thirdplace_Frame, text="3th Place")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))

        #Final Frame
        self.final_Frame = customtkinter.CTkFrame(self)
        self.final_Frame.grid(row=1, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.final_Frame.grid_columnconfigure(0, weight=1)
        self.final_Frame.grid_rowconfigure((1,2), weight=1)
        self.seg_button_1 = customtkinter.CTkLabel(self.final_Frame, text="Final")
        self.seg_button_1.grid(row=0, column=0, padx=(20, 20), pady=(10, 10))


        #update labels etage group
        self.labelTeamAone.configure(text=self.one)
        self.labelTeamAtwo.configure(text=self.two)
        self.labelTeamAthree.configure(text=self.three)
        self.labelTeamAfour.configure(text=self.four)
        self.labelTeamBone.configure(text=self.five)
        self.labelTeamBtwo.configure(text=self.six)
        self.labelTeamBthree.configure(text=self.seven)
        self.labelTeamBfour.configure(text=self.ocho)

        #codigo de guia para el grid
        # for i in range(4):
        #     for j in range(0,5):
        #         frame = customtkinter.CTkFrame(self.AddTeams2_Frame)
        #         frame.grid(row=i, column=j, padx=(0, 0), pady=(0, 0))
        #         label = customtkinter.CTkLabel(master=frame, text=f"Row {i}\nColumn {j}")
        #         label.pack()

        #bottom buttom to continue adding teams
        # self.main_button_1 = customtkinter.CTkButton(master=self.groupEtage_Frame, text="Next", text_color=("gray10", "#DCE4EE"), command=self.NextButtonEvent    )
        # self.main_button_1.grid(row=6, column=1,columnspan=2, pady=(10, 20), sticky="nsew")

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
            self.home_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        else:
            self.home_Frame.grid_forget()
        if name == "AddTeams":
            self.AddTeams_Frame.grid(row=0, column=1,  columnspan=4, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        else:
            self.AddTeams_Frame.grid_forget()
        if name == "AddTeams2":
            self.AddTeams2_Frame.grid(row=0, column=1,  columnspan=4, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        else:
            self.AddTeams2_Frame.grid_forget()
        if name == "groupEtage":
            self.groupEtage_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        else:
            self.groupEtage_Frame.grid_forget()
        if name == "groupEtage2":
            self.groupEtage2_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        else:
            self.groupEtage2_Frame.grid_forget()
        if name == "sixteenround":
            self.sixteenround_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        else:
            self.sixteenround_Frame.grid_forget()
        if name == "eightround":
            self.eightround_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        else:
            self.eightround_Frame.grid_forget()
        if name == "semifinals":
            self.semifinals_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        else:
            self.semifinals_Frame.grid_forget()
        if name == "thirdplace":
            self.thirdplace_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
        else:
            self.thirdplace_Frame.grid_forget()
        if name == "final":
            self.final_Frame.grid(row=0, column=1, columnspan=4, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")
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

    #Add teams page function
    def Addteams1(self):
        self.select_frame_by_name("AddTeams")

    #Add teams page function 2
    def Addteams2(self):
        self.select_frame_by_name("AddTeams2")



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
        self.select_frame_by_name("groupEtage2")
        # messagebox.showinfo(title="Alert", message="There is no other window!")

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

    def show(self):
        return 0

if __name__ == "__main__":
    app = App()
    app.mainloop()
