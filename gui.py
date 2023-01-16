import tkinter
import tkinter.messagebox as messagebox
import customtkinter
import customtkinter as ctk
import os
import main
from PIL import Image

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

#class to set up the GUI
class App(customtkinter.CTk):

    groups =[""]

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

        #Botones de accion sidebar
        self.home_button = customtkinter.CTkButton(self.sidebar_frame, text="Home", command=self.homepage)
        self.home_button.grid(row=1, column=0, padx=20, pady=10)
        self.groupEtage_button = customtkinter.CTkButton(self.sidebar_frame, text="Group Stage", command=self.groupEtage)
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
                                            text="Here you can add, auto generate the teams \n \n also see the diferent stages by clicking the buttons in the side bar",
                                            font=customtkinter.CTkFont(size=15))
        self.inslabel.grid(row=1, column=1, columnspan=2, padx=(10, 10), pady=(10, 10))

        #bottom buttom to continue adding teams
        self.main_button_1 = customtkinter.CTkButton(master=self.home_Frame, text="Add Teams", text_color=("gray10", "#DCE4EE"), command=self.Addteams1)
        self.main_button_1.grid(row=2, column=1,columnspan=2,padx=(20, 20), pady=(10, 20), sticky="nsew")

        #bottom buttom to continue adding teams
        self.main_button_1 = customtkinter.CTkButton(master=self.home_Frame, text="Auto Generate \n teams", text_color=("gray10", "#DCE4EE"), command=self.AutoGenerateButtonEvent)
        self.main_button_1.grid(row=3, column=1,columnspan=2,padx=(20, 20), pady=(10, 20), sticky="nsew")


        #Group etage Frame
        self.groupEtage_Frame = customtkinter.CTkFrame(self)
        self.groupEtage_Frame.grid(row=0, column=1, columnspan=4, rowspan=5, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.groupEtage_Frame.grid_columnconfigure((0,1), weight=1)
        self.groupEtage_Frame.grid_rowconfigure((1,2,3,4), weight=1)
        self.titlelable = customtkinter.CTkLabel(self.groupEtage_Frame, text="Group Etage", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.titlelable.grid(row=0, column=0, columnspan= 2, padx=(20, 20), pady=(10, 10))

        #Group etage Frame for group A
        self.groupA_frame = customtkinter.CTkFrame(self.groupEtage_Frame)
        self.groupA_frame.grid(row=1, column=0, rowspan=2)
        self.groupA_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupA_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)

        #Group etage labels titles for group A
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

        # team labels 
        self.labelTeamAone = customtkinter.CTkLabel(self.groupA_frame, text="Holanda")
        self.labelTeamAone.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjAone = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPjAone.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAwone = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelgroupAwone.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAlone = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAlone.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAdone = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAdone.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsAone = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPtsAone.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))

        # team labels
        self.labelTeamAtwo = customtkinter.CTkLabel(self.groupA_frame, text="Ecuador")
        self.labelTeamAtwo.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjAtwo = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPjAtwo.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAwtwo = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelgroupAwtwo.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAltwo = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAltwo.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAdtwo = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAdtwo.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsAtwo = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPtsAtwo.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))

        # team labels
        self.labelTeamAthree = customtkinter.CTkLabel(self.groupA_frame, text="Senegal")
        self.labelTeamAthree.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjAthree = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPjAthree.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAwthree = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelgroupAwthree.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAlthree = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAlthree.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAdthree = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAdthree.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsAthree = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPtsAthree.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))

        # team labels
        self.labelTeamAfour = customtkinter.CTkLabel(self.groupA_frame, text="Qatar")
        self.labelTeamAfour.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjAfour = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPjAfour.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupAwfour = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelgroupAwfour.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamAlfour = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAlfour.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamAdfour = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelTeamAdfour.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsAfour = customtkinter.CTkLabel(self.groupA_frame, text="0")
        self.labelPtsAfour.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        #Button to Add Results Group A
        self.AddResultsButton = customtkinter.CTkButton(self.groupA_frame, text="Add Results", command=self.get_input_Group_A)
        self.AddResultsButton.grid(row=6, column=1, columnspan=3)
        
        #Group etage Frame for group B
        self.groupB_frame = customtkinter.CTkFrame(self.groupEtage_Frame)
        self.groupB_frame.grid(row=3, column=0, rowspan=2)
        self.groupB_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupB_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)

        #Group etage labels titles for group B
        self.labelgroupB = customtkinter.CTkLabel(self.groupB_frame, text="Group B")
        self.labelgroupB.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamB = customtkinter.CTkLabel(self.groupB_frame, text="Team")
        self.labelTeamB.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjB = customtkinter.CTkLabel(self.groupB_frame, text="PJ")
        self.labelPjB.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupBw = customtkinter.CTkLabel(self.groupB_frame, text="W")
        self.labelgroupBw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamBl = customtkinter.CTkLabel(self.groupB_frame, text="L")
        self.labelTeamBl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamBd = customtkinter.CTkLabel(self.groupB_frame, text="D")
        self.labelTeamBd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsB = customtkinter.CTkLabel(self.groupB_frame, text="PTS")
        self.labelPtsB.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamBone = customtkinter.CTkLabel(self.groupB_frame, text="Holanda")
        self.labelTeamBone.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjBone = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPjBone.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupBwone = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelgroupBwone.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamBlone = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamBlone.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamBdone = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamBdone.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsBone = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPtsBone.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamBtwo = customtkinter.CTkLabel(self.groupB_frame, text="Ecuador")
        self.labelTeamBtwo.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjBtwo = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPjBtwo.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupBwtwo = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelgroupBwtwo.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamBltwo = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamBltwo.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamBdtwo = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamBdtwo.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsBtwo = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPtsBtwo.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamBthree = customtkinter.CTkLabel(self.groupB_frame, text="Senegal")
        self.labelTeamBthree.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjBthree = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPjBthree.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupBwthree = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelgroupBwthree.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamBlthree = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamBlthree.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamBdthree = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamBdthree.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsBthree = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPtsBthree.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamBfour = customtkinter.CTkLabel(self.groupB_frame, text="Qatar")
        self.labelTeamBfour.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjBfour = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPjBfour.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupBwfour = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelgroupBwfour.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamBlfour = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamBlfour.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamBdfour = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelTeamBdfour.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsBfour = customtkinter.CTkLabel(self.groupB_frame, text="0")
        self.labelPtsBfour.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        #Button to Add Results Group B
        self.AddResultsButton = customtkinter.CTkButton(self.groupB_frame, text="Add Results", command='self.get_input_Group_B')
        self.AddResultsButton.grid(row=6, column=1, columnspan=3)

        #Group etage Frame for group C
        self.groupC_frame = customtkinter.CTkFrame(self.groupEtage_Frame)
        self.groupC_frame.grid(row=1, column=1, columnspan=2, rowspan=2)
        self.groupC_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupC_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)

        #Group etage labels titles for group C
        self.labelgroupC = customtkinter.CTkLabel(self.groupC_frame, text="Group C")
        self.labelgroupC.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamC = customtkinter.CTkLabel(self.groupC_frame, text="Team")
        self.labelTeamC.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjC = customtkinter.CTkLabel(self.groupC_frame, text="PJ")
        self.labelPjC.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupCw = customtkinter.CTkLabel(self.groupC_frame, text="W")
        self.labelgroupCw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamCl = customtkinter.CTkLabel(self.groupC_frame, text="L")
        self.labelTeamCl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamCd = customtkinter.CTkLabel(self.groupC_frame, text="D")
        self.labelTeamCd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsC = customtkinter.CTkLabel(self.groupC_frame, text="PTS")
        self.labelPtsC.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))

        #team labels
        self.labelTeamCone = customtkinter.CTkLabel(self.groupC_frame, text="Holanda")
        self.labelTeamCone.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjCone = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPjCone.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupCwone = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelgroupCwone.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamClone = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamClone.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamCdone = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamCdone.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsCone = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPtsCone.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))

        #team lables
        self.labelTeamCtwo = customtkinter.CTkLabel(self.groupC_frame, text="Ecuador")
        self.labelTeamCtwo.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjCtwo = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPjCtwo.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupCwtwo = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelgroupCwtwo.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamCltwo = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamCltwo.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamCdtwo = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamCdtwo.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsCtwo = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPtsCtwo.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))

        #team labels
        self.labelTeamCthree = customtkinter.CTkLabel(self.groupC_frame, text="Senegal")
        self.labelTeamCthree.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjCthree = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPjCthree.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupCwthree = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelgroupCwthree.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamClthree= customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamClthree.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamCdthree = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamCdthree.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsCthree= customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPtsCthree.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))

        #team labels
        self.labelTeamCfour = customtkinter.CTkLabel(self.groupC_frame, text="Qatar")
        self.labelTeamCfour.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjCfour = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPjCfour.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupCwfour = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelgroupCwfour.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamClfour = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamClfour.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamCdfour = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelTeamCdfour.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsCfour = customtkinter.CTkLabel(self.groupC_frame, text="0")
        self.labelPtsCfour.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        #Button to Add Results Group C
        self.AddResultsButton = customtkinter.CTkButton(self.groupC_frame, text="Add Results", command='self.get_input_Group_C')
        self.AddResultsButton.grid(row=6, column=1, columnspan=3)

        #Group etage Frame for group D
        self.groupD_frame = customtkinter.CTkFrame(self.groupEtage_Frame)
        self.groupD_frame.grid(row=3, column=1, columnspan=2, rowspan=2)
        self.groupD_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupD_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)

        #Group etage labels titles for group D
        self.labelgroupD = customtkinter.CTkLabel(self.groupD_frame, text="Group D")
        self.labelgroupD.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamD = customtkinter.CTkLabel(self.groupD_frame, text="Team")
        self.labelTeamD.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjD = customtkinter.CTkLabel(self.groupD_frame, text="PJ")
        self.labelPjD.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupDw = customtkinter.CTkLabel(self.groupD_frame, text="W")
        self.labelgroupDw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamDl = customtkinter.CTkLabel(self.groupD_frame, text="L")
        self.labelTeamDl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamDd = customtkinter.CTkLabel(self.groupD_frame, text="D")
        self.labelTeamDd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsD = customtkinter.CTkLabel(self.groupD_frame, text="PTS")
        self.labelPtsD.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamDone = customtkinter.CTkLabel(self.groupD_frame, text="Holanda")
        self.labelTeamDone.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjDone = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPjDone.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupDwone = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelgroupDwone.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamDlone = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamDlone.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamDdone = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamDdone.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsDone = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPtsDone.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamDtwo = customtkinter.CTkLabel(self.groupD_frame, text="Ecuador")
        self.labelTeamDtwo.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjDtwo = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPjDtwo.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupDwtwo = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelgroupDwtwo.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamDltwo = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamDltwo.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamDdtwo = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamDdtwo.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsDtwo = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPtsDtwo.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamDthree = customtkinter.CTkLabel(self.groupD_frame, text="Senegal")
        self.labelTeamDthree.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjDthree = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPjDthree.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupDwthree = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelgroupDwthree.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamDlthree = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamDlthree.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamDdthree = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamDdthree.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsDthree = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPtsDthree.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamDfour = customtkinter.CTkLabel(self.groupD_frame, text="Qatar")
        self.labelTeamDfour.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjDfour = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPjDfour.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupDwfour = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelgroupDwfour.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamDlfour = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamDlfour.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamDdfour = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamDdfour.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsDfour = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelPtsDfour.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        #Button to Add Results Group D
        self.AddResultsButton = customtkinter.CTkButton(self.groupD_frame, text="Add Results", command='self.get_input_Group_D')
        self.AddResultsButton.grid(row=6, column=1, columnspan=3)

        #bottom buttom to continue seeing
        self.nextEtage = customtkinter.CTkButton(master=self.groupEtage_Frame, text="Next", text_color=("gray10", "#DCE4EE"), command=self.NextButtonEvent)
        self.nextEtage.grid(row=6, column=0, columnspan= 2, padx=(20, 20), pady=(10, 10))

        #Group etage 2 Frame
        self.groupEtage2_Frame = customtkinter.CTkFrame(self)
        self.groupEtage2_Frame.grid(row=0, column=1, columnspan=4, rowspan=5, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.groupEtage2_Frame.grid_columnconfigure((0,1), weight=1)
        self.groupEtage2_Frame.grid_rowconfigure((1,2,3,4), weight=1)
        self.titlelable = customtkinter.CTkLabel(self.groupEtage2_Frame, text="Group Etage", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.titlelable.grid(row=0, column=0, columnspan= 2, padx=(20, 20), pady=(10, 10))

         #Group etage Frame for group E
        self.groupE_frame = customtkinter.CTkFrame(self.groupEtage2_Frame)
        self.groupE_frame.grid(row=1, column=0, rowspan=2)
        self.groupE_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupE_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)

        #Group etage labels titles for group E
        self.labelgroupE = customtkinter.CTkLabel(self.groupE_frame, text="Group E")
        self.labelgroupE.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamE = customtkinter.CTkLabel(self.groupE_frame, text="Team")
        self.labelTeamE.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjE = customtkinter.CTkLabel(self.groupE_frame, text="PJ")
        self.labelPjE.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupEw = customtkinter.CTkLabel(self.groupE_frame, text="W")
        self.labelgroupEw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamEl = customtkinter.CTkLabel(self.groupE_frame, text="L")
        self.labelTeamEl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamEd = customtkinter.CTkLabel(self.groupE_frame, text="D")
        self.labelTeamEd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsE = customtkinter.CTkLabel(self.groupE_frame, text="PTS")
        self.labelPtsE.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))

        # team labels 
        self.labelTeamEone = customtkinter.CTkLabel(self.groupE_frame, text="Holanda")
        self.labelTeamEone.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjEone = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelPjEone.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupEwone = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelgroupEwone.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamElone = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelTeamElone.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamEdone = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelTeamEdone.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsEone = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelPtsEone.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))

        # team labels
        self.labelTeamEtwo = customtkinter.CTkLabel(self.groupE_frame, text="Ecuador")
        self.labelTeamEtwo.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjEtwo = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelPjEtwo.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupEwtwo = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelgroupEwtwo.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamEltwo = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelTeamEltwo.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamEdtwo = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelTeamEdtwo.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsEtwo = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelPtsEtwo.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))

        # team labels
        self.labelTeamEthree = customtkinter.CTkLabel(self.groupE_frame, text="Senegal")
        self.labelTeamEthree.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjEthree = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelPjEthree.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupEwthree = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelgroupEwthree.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamElthree = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelTeamElthree.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamEdthree = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelTeamEdthree.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsEthree = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelPtsEthree.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))

        # team labels
        self.labelTeamEfour = customtkinter.CTkLabel(self.groupE_frame, text="Qatar")
        self.labelTeamEfour.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjEfour = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelPjEfour.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupEwfour = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelgroupEwfour.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamElfour = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelTeamElfour.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamEdfour = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelTeamEdfour.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsEfour = customtkinter.CTkLabel(self.groupE_frame, text="0")
        self.labelPtsEfour.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        #Button to Add Results Group E
        self.AddResultsButton = customtkinter.CTkButton(self.groupE_frame, text="Add Results", command='self.get_input_Group_E')
        self.AddResultsButton.grid(row=6, column=1, columnspan=3)

        #Group etage Frame for group F
        self.groupF_frame = customtkinter.CTkFrame(self.groupEtage2_Frame)
        self.groupF_frame.grid(row=3, column=0, rowspan=2)
        self.groupF_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupF_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)

        #Group etage labels titles for group F
        self.labelgroupF = customtkinter.CTkLabel(self.groupF_frame, text="Group F")
        self.labelgroupF.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamF = customtkinter.CTkLabel(self.groupF_frame, text="Team")
        self.labelTeamF.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjF = customtkinter.CTkLabel(self.groupF_frame, text="PJ")
        self.labelPjF.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupFw = customtkinter.CTkLabel(self.groupF_frame, text="W")
        self.labelgroupFw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamFl = customtkinter.CTkLabel(self.groupF_frame, text="L")
        self.labelTeamFl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamFd = customtkinter.CTkLabel(self.groupF_frame, text="D")
        self.labelTeamFd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsF = customtkinter.CTkLabel(self.groupF_frame, text="PTS")
        self.labelPtsF.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamFone = customtkinter.CTkLabel(self.groupF_frame, text="Holanda")
        self.labelTeamFone.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjFone = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelPjFone.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupFwone = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelgroupFwone.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamFlone = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelTeamFlone.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamFdone = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelTeamFdone.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsFone = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelPtsFone.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamFtwo = customtkinter.CTkLabel(self.groupF_frame, text="Ecuador")
        self.labelTeamFtwo.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjFtwo = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelPjFtwo.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupFwtwo = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelgroupFwtwo.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamFltwo = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelTeamFltwo.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamFdtwo = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelTeamFdtwo.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsFtwo = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelPtsFtwo.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamFthree = customtkinter.CTkLabel(self.groupF_frame, text="Senegal")
        self.labelTeamFthree.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjFthree = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelPjFthree.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupFwthree = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelgroupFwthree.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamFlthree = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelTeamFlthree.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamFdthree = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelTeamFdthree.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsFthree = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelPtsFthree.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamFfour = customtkinter.CTkLabel(self.groupF_frame, text="Qatar")
        self.labelTeamFfour.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjFfour = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelPjFfour.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupFwfour = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelgroupFwfour.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamFlfour = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelTeamFlfour.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamFdfour = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelTeamFdfour.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsFfour = customtkinter.CTkLabel(self.groupF_frame, text="0")
        self.labelPtsFfour.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        #Button to Add Results Group F
        self.AddResultsButton = customtkinter.CTkButton(self.groupF_frame, text="Add Results", command='self.get_input_Group_F')
        self.AddResultsButton.grid(row=6, column=1, columnspan=3)

        #Group etage Frame for group G
        self.groupG_frame = customtkinter.CTkFrame(self.groupEtage2_Frame)
        self.groupG_frame.grid(row=1, column=1, columnspan=2, rowspan=2)
        self.groupG_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupG_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)

        #Group etage labels titles for group G
        self.labelgroupG = customtkinter.CTkLabel(self.groupG_frame, text="Group G")
        self.labelgroupG.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamG = customtkinter.CTkLabel(self.groupG_frame, text="Team")
        self.labelTeamG.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjG = customtkinter.CTkLabel(self.groupG_frame, text="PJ")
        self.labelPjG.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupGw = customtkinter.CTkLabel(self.groupG_frame, text="W")
        self.labelgroupGw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamGl = customtkinter.CTkLabel(self.groupG_frame, text="L")
        self.labelTeamGl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamGd = customtkinter.CTkLabel(self.groupG_frame, text="D")
        self.labelTeamGd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsG = customtkinter.CTkLabel(self.groupG_frame, text="PTS")
        self.labelPtsG.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))

        #team labels
        self.labelTeamGone = customtkinter.CTkLabel(self.groupG_frame, text="Holanda")
        self.labelTeamGone.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjGone = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelPjGone.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupGwone = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelgroupGwone.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamGlone = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelTeamGlone.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamGdone = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelTeamGdone.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsGone = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelPtsGone.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))

        #team lables
        self.labelTeamGtwo = customtkinter.CTkLabel(self.groupG_frame, text="Ecuador")
        self.labelTeamGtwo.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjGtwo = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelPjGtwo.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupGwtwo = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelgroupGwtwo.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamGltwo = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelTeamGltwo.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamGdtwo = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelTeamGdtwo.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsGtwo = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelPtsGtwo.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))

        #team labels
        self.labelTeamGthree = customtkinter.CTkLabel(self.groupG_frame, text="Senegal")
        self.labelTeamGthree.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjGthree = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelPjGthree.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupGwthree = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelgroupGwthree.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamGlthree= customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelTeamGlthree.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamGdthree = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelTeamGdthree.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsGthree= customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelPtsGthree.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))

        #team labels
        self.labelTeamGfour = customtkinter.CTkLabel(self.groupG_frame, text="Qatar")
        self.labelTeamGfour.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjGfour = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelPjGfour.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupGwfour = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelgroupGwfour.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamGlfour = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelTeamGlfour.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamGdfour = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelTeamGdfour.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsGfour = customtkinter.CTkLabel(self.groupG_frame, text="0")
        self.labelPtsGfour.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        #Button to Add Results Group G
        self.AddResultsButton = customtkinter.CTkButton(self.groupG_frame, text="Add Results", command='self.get_input_Group_G')
        self.AddResultsButton.grid(row=6, column=1, columnspan=3)

        #Group etage Frame for group H
        self.groupH_frame = customtkinter.CTkFrame(self.groupEtage2_Frame)
        self.groupH_frame.grid(row=3, column=1, columnspan=2, rowspan=2)
        self.groupH_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.groupH_frame.grid_rowconfigure((1,2,3,4,5,6), weight=1)

        #Group etage labels titles for group H
        self.labelgroupH = customtkinter.CTkLabel(self.groupH_frame, text="Group H")
        self.labelgroupH.grid(row=0, column=1, columnspan=3, padx=(0, 0), pady=(0, 0))
        self.labelTeamH = customtkinter.CTkLabel(self.groupH_frame, text="Team")
        self.labelTeamH.grid(row=1, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjH = customtkinter.CTkLabel(self.groupH_frame, text="PJ")
        self.labelPjH.grid(row=1, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupHw = customtkinter.CTkLabel(self.groupH_frame, text="W")
        self.labelgroupHw.grid(row=1, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamHl = customtkinter.CTkLabel(self.groupH_frame, text="L")
        self.labelTeamHl.grid(row=1, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamHd = customtkinter.CTkLabel(self.groupH_frame, text="D")
        self.labelTeamHd.grid(row=1, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsH = customtkinter.CTkLabel(self.groupH_frame, text="PTS")
        self.labelPtsH.grid(row=1, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamHone = customtkinter.CTkLabel(self.groupH_frame, text="Holanda")
        self.labelTeamHone.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjHone = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelPjHone.grid(row=2, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupHwone = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelgroupHwone.grid(row=2, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamHlone = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelTeamHlone.grid(row=2, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamHdone = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelTeamHdone.grid(row=2, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsHone = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelPtsHone.grid(row=2, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamHtwo = customtkinter.CTkLabel(self.groupH_frame, text="Ecuador")
        self.labelTeamHtwo.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjHtwo = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelPjHtwo.grid(row=3, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupHwtwo = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelgroupHwtwo.grid(row=3, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamHltwo = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelTeamHltwo.grid(row=3, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamHdtwo = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelTeamHdtwo.grid(row=3, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsHtwo = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelPtsHtwo.grid(row=3, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamHthree = customtkinter.CTkLabel(self.groupH_frame, text="Senegal")
        self.labelTeamHthree.grid(row=4, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjHthree = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelPjHthree.grid(row=4, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupHwthree = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelgroupHwthree.grid(row=4, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamHlthree = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelTeamHlthree.grid(row=4, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamHdthree = customtkinter.CTkLabel(self.groupD_frame, text="0")
        self.labelTeamHdthree.grid(row=4, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsHthree = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelPtsHthree.grid(row=4, column=6, padx=(2, 2), pady=(0, 0))

        #team label
        self.labelTeamHfour = customtkinter.CTkLabel(self.groupH_frame, text="Qatar")
        self.labelTeamHfour.grid(row=5, column=0, padx=(0, 0), pady=(0, 0))
        self.labelPjHfour = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelPjHfour.grid(row=5, column=2, padx=(2, 2), pady=(0, 0))
        self.labelgroupHwfour = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelgroupHwfour.grid(row=5, column=3, padx=(2, 2), pady=(0, 0))
        self.labelTeamHlfour = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelTeamHlfour.grid(row=5, column=4, padx=(2, 2), pady=(0, 0))
        self.labelTeamHdfour = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelTeamHdfour.grid(row=5, column=5, padx=(2, 2), pady=(0, 0))
        self.labelPtsHfour = customtkinter.CTkLabel(self.groupH_frame, text="0")
        self.labelPtsHfour.grid(row=5, column=6, padx=(2, 2), pady=(0, 0))

        #Button to Add Results Group H
        self.AddResultsButton = customtkinter.CTkButton(self.groupH_frame, text="Add Results", command='self.get_input_Group_H')
        self.AddResultsButton.grid(row=6, column=1, columnspan=3)

        #bottom buttom to go Back
        self.nextEtage = customtkinter.CTkButton(master=self.groupEtage2_Frame, text="Back", text_color=("gray10", "#DCE4EE"), command=self.BackButtonEvent)
        self.nextEtage.grid(row=6, column=0, columnspan= 2, padx=(20, 20), pady=(10, 10))

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
        
        #function to save the teams given by the User
        def SaveTeams():
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
            
            self.groups = main.add_teams_list(self.teams)
            
            #Update team Labels for actual names 
            #Group A
            self.labelTeamAone.configure(text=self.teams[0])
            self.labelTeamAtwo.configure(text=self.teams[1])
            self.labelTeamAthree.configure(text=self.teams[2])
            self.labelTeamAfour.configure(text=self.teams[3])
            #Group B
            self.labelTeamBone.configure(text=self.teams[4])
            self.labelTeamBtwo.configure(text=self.teams[5])
            self.labelTeamBthree.configure(text=self.teams[6])
            self.labelTeamBfour.configure(text=self.teams[7])
            #Group C
            self.labelTeamCone.configure(text=self.teams[8])
            self.labelTeamCtwo.configure(text=self.teams[9])
            self.labelTeamCthree.configure(text=self.teams[10])
            self.labelTeamCfour.configure(text=self.teams[11])
            #Group D
            self.labelTeamDone.configure(text=self.teams[12])
            self.labelTeamDtwo.configure(text=self.teams[13])
            self.labelTeamDthree.configure(text=self.teams[14])
            self.labelTeamDfour.configure(text=self.teams[15])
            #Group E
            self.labelTeamEone.configure(text=self.teams[16])
            self.labelTeamEtwo.configure(text=self.teams[17])
            self.labelTeamEthree.configure(text=self.teams[18])
            self.labelTeamEfour.configure(text=self.teams[19])
            #Group F
            self.labelTeamFone.configure(text=self.teams[20])
            self.labelTeamFtwo.configure(text=self.teams[21])
            self.labelTeamFthree.configure(text=self.teams[22])
            self.labelTeamFfour.configure(text=self.teams[23])
            #Group G
            self.labelTeamGone.configure(text=self.teams[24])
            self.labelTeamGtwo.configure(text=self.teams[25])
            self.labelTeamGthree.configure(text=self.teams[26])
            self.labelTeamGfour.configure(text=self.teams[27])
            #Group H
            self.labelTeamHone.configure(text=self.teams[28])
            self.labelTeamHtwo.configure(text=self.teams[29])
            self.labelTeamHthree.configure(text=self.teams[30])
            self.labelTeamHfour.configure(text=self.teams[31])

            #sends you back to group Etage page
            self.select_frame_by_name("groupEtage")


        self.saveButton = customtkinter.CTkButton(master=self.AddTeams2_Frame, text="Save", text_color=("gray10", "#DCE4EE"), command=SaveTeams)
        self.saveButton.grid(row=4, column=2, columnspan=2, padx=(20, 10), pady=(10, 20), sticky="nsew")

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

    #   funcion para avanzar a la siguiente pag 
    def NextButtonEvent(self):
        self.select_frame_by_name("groupEtage2")
        # messagebox.showinfo(title="Alert", message="There is no other window!")

    #   funcion para avanzar a la siguiente pag de añadir
    def BackButtonEvent(self):
        self.select_frame_by_name("groupEtage")
        # messagebox.showinfo(title="Alert", message="There is no other window!")

    #   funcion para auto genrar los 32 equipos
    def AutoGenerateButtonEvent(self):
        teams = ["Netherlands", "Senegal", "Ecuador", "Qatar", "England", "Usa", "Iran", "Wales", "Argentina",
         "Poland", "Mexico", "Saudi arabia", "France", "Australia", "Tunisia", "Denmark", "Japan", "Spain", "Germany", "Costa Rica",
         "Morocco", "Croatia", "Belgium", "Canada", "Brazil", "Switzerland", "Cameroon", "Serbia", "Portugal", "South Korea", "Uruguay", "Ghana"]

        self.groups = main.add_teams_list(teams)
            
        #Update team Labels for actual names 
        #Group A
        self.labelTeamAone.configure(text=teams[0])
        self.labelTeamAtwo.configure(text=teams[1])
        self.labelTeamAthree.configure(text=teams[2])
        self.labelTeamAfour.configure(text=teams[3])
        #Group B
        self.labelTeamBone.configure(text=teams[4])
        self.labelTeamBtwo.configure(text=teams[5])
        self.labelTeamBthree.configure(text=teams[6])
        self.labelTeamBfour.configure(text=teams[7])
        #Group C
        self.labelTeamCone.configure(text=teams[8])
        self.labelTeamCtwo.configure(text=teams[9])
        self.labelTeamCthree.configure(text=teams[10])
        self.labelTeamCfour.configure(text=teams[11])
        #Group D
        self.labelTeamDone.configure(text=teams[12])
        self.labelTeamDtwo.configure(text=teams[13])
        self.labelTeamDthree.configure(text=teams[14])
        self.labelTeamDfour.configure(text=teams[15])
        #Group E
        self.labelTeamEone.configure(text=teams[16])
        self.labelTeamEtwo.configure(text=teams[17])
        self.labelTeamEthree.configure(text=teams[18])
        self.labelTeamEfour.configure(text=teams[19])
        #Group F
        self.labelTeamFone.configure(text=teams[20])
        self.labelTeamFtwo.configure(text=teams[21])
        self.labelTeamFthree.configure(text=teams[22])
        self.labelTeamFfour.configure(text=teams[23])
        #Group G
        self.labelTeamGone.configure(text=teams[24])
        self.labelTeamGtwo.configure(text=teams[25])
        self.labelTeamGthree.configure(text=teams[26])
        self.labelTeamGfour.configure(text=teams[27])
        #Group H
        self.labelTeamHone.configure(text=teams[28])
        self.labelTeamHtwo.configure(text=teams[29])
        self.labelTeamHthree.configure(text=teams[30])
        self.labelTeamHfour.configure(text=teams[31])

        #tells the user that he atu genearted the teams succesfully
        messagebox.showinfo(title="Alert", message="You have auto generated the teams!")

        #sends you back to group Etage page
        self.select_frame_by_name("groupEtage")

    answers = []

    def ask_question(self,question,team1,team2,group):
        top = ctk.CTkToplevel()
        top.title("Input")

        label = ctk.CTkLabel(top, text=question)
        label.pack()

        entry = ctk.CTkEntry(top, placeholder_text="team 1 score")
        entry.pack()

        entry2 = ctk.CTkEntry(top, placeholder_text="team 2 score")
        entry2.pack()

        def submit():
            answer = entry.get()
            answer2 = entry2.get()
            # print(group.get_teams())
            def compare_numbers(a ,b):
                if a > b:
                    group.get_team(team1)[0].match_won_setter()
                    group.get_team(team2)[0].match_lost_setter()
                elif a < b:
                    group.get_team(team2)[0].match_won_setter()
                    group.get_team(team1)[0].match_lost_setter()
                else:
                    group.get_team(team1)[0].match_drawed_setter()
                    group.get_team(team1)[0].match_drawed_setter()

                group.add_goals_for(group.get_team(team1)[0],a)
                group.add_goals_for(group.get_team(team2)[0],b)
                group.add_goals_agains(group.get_team(team1)[0],b)
                group.add_goals_agains(group.get_team(team2)[0],a)
                group.points()
                
            

            compare_numbers(int(answer), int(answer2))
            top.destroy()
 

        submit_button = ctk.CTkButton(top, text="Submit", command=submit)
        submit_button.pack()
        top.wait_window()

    def get_input_Group_A(self):

        #ask question for match 1
        #index 0 vs 1
        self.ask_question(self.groups[0].get_teams()[0] +" vs "+ self.groups[0].get_teams()[1],self.groups[0].get_teams()[0],self.groups[0].get_teams()[1], self.groups[0])
        #update the default label variables for team 1
        self.labelPjAone.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_Played_getter())
        self.labelgroupAwone.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_won_getter())
        self.labelTeamAlone.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_lost_getter())
        self.labelTeamAdone.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_drawed_getter())
        self.labelPtsAone.configure(text=self.groups[0].get_points(self.groups[0].get_teams()[0]))
        #update the default label variables for team 2
        self.labelPjAtwo.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[1])[0].match_Played_getter())
        self.labelgroupAwtwo.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[1])[0].match_won_getter())
        self.labelTeamAltwo.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[1])[0].match_lost_getter())
        self.labelTeamAdtwo.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[1])[0].match_drawed_getter())
        self.labelPtsAtwo.configure(text=self.groups[0].get_points(self.groups[0].get_teams()[1]))

        #ask question for match 2
        #index 0 vs 2
        self.ask_question(self.groups[0].get_teams()[0] +" vs "+ self.groups[0].get_teams()[2],self.groups[0].get_teams()[0],self.groups[0].get_teams()[2], self.groups[0])
        #update the default label variables for team 1
        self.labelPjAone.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_Played_getter())
        self.labelgroupAwone.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_won_getter())
        self.labelTeamAlone.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_lost_getter())
        self.labelTeamAdone.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_drawed_getter())
        self.labelPtsAone.configure(text=self.groups[0].get_points(self.groups[0].get_teams()[0]))
        #update the default label variables for team 2
        self.labelPjAthree.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_Played_getter())
        self.labelgroupAwthree.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_won_getter())
        self.labelTeamAlthree.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_lost_getter())
        self.labelTeamAdthree.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_drawed_getter())
        self.labelPtsAthree.configure(text=self.groups[0].get_points(self.groups[0].get_teams()[0]))

        #ask question for match 3
        #index 0 vs 3
        self.ask_question(self.groups[0].get_teams()[0] +" vs "+ self.groups[0].get_teams()[3],self.groups[0].get_teams()[0],self.groups[0].get_teams()[1], self.groups[0])
        #update the default label variables for team 1
        self.labelPjAone.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_Played_getter())
        self.labelgroupAwone.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_won_getter())
        self.labelTeamAlone.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_lost_getter())
        self.labelTeamAdone.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_drawed_getter())
        self.labelPtsAone.configure(text=self.groups[0].get_points(self.groups[0].get_teams()[0]))
        #update the default label variables for team 2
        self.labelPjAfour.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_Played_getter())
        self.labelgroupAwfour.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_won_getter())
        self.labelTeamAlfour.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_lost_getter())
        self.labelTeamAdfour.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_drawed_getter())
        self.labelPtsAfour.configure(text=self.groups[0].get_points(self.groups[0].get_teams()[0]))

        #ask question for match 4
        #index 1 vs 2
        self.ask_question(self.groups[0].get_teams()[1] +" vs "+ self.groups[0].get_teams()[2],self.groups[0].get_teams()[0],self.groups[0].get_teams()[1], self.groups[0])
        #update the default label variables for team 1
        self.labelPjAtwo.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_Played_getter())
        self.labelgroupAwtwo.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_won_getter())
        self.labelTeamAltwo.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_lost_getter())
        self.labelTeamAdtwo.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_drawed_getter())
        self.labelPtsAtwo.configure(text=self.groups[0].get_points(self.groups[0].get_teams()[0]))
        #update the default label variables for team 2
        self.labelPjAthree.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_Played_getter())
        self.labelgroupAwthree.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_won_getter())
        self.labelTeamAlthree.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_lost_getter())
        self.labelTeamAdthree.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_drawed_getter())
        self.labelPtsAthree.configure(text=self.groups[0].get_points(self.groups[0].get_teams()[0]))

        #ask question for match 5
        #index 1 vs 3
        self.ask_question(self.groups[0].get_teams()[1] +" vs "+ self.groups[0].get_teams()[3],self.groups[0].get_teams()[0],self.groups[0].get_teams()[1], self.groups[0])
        #update the default label variables for team 1
        self.labelPjAtwo.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_Played_getter())
        self.labelgroupAwtwo.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_won_getter())
        self.labelTeamAltwo.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_lost_getter())
        self.labelTeamAdtwo.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_drawed_getter())
        self.labelPtsAtwo.configure(text=self.groups[0].get_points(self.groups[0].get_teams()[0]))
        #update the default label variables for team 2
        self.labelPjAfour.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_Played_getter())
        self.labelgroupAwfour.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_won_getter())
        self.labelTeamAlfour.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_lost_getter())
        self.labelTeamAdfour.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_drawed_getter())
        self.labelPtsAfour.configure(text=self.groups[0].get_points(self.groups[0].get_teams()[0]))

        #ask question for match 6
        #index 2 vs 3
        self.ask_question(self.groups[0].get_teams()[2] +" vs "+ self.groups[0].get_teams()[3],self.groups[0].get_teams()[0],self.groups[0].get_teams()[1], self.groups[0])
        #update the default label variables for team 1
        self.labelPjAthree.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_Played_getter())
        self.labelgroupAwthree.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_won_getter())
        self.labelTeamAlthree.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_lost_getter())
        self.labelTeamAdthree.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_drawed_getter())
        self.labelPtsAthree.configure(text=self.groups[0].get_points(self.groups[0].get_teams()[0]))
        #update the default label variables for team 2
        self.labelPjAfour.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_Played_getter())
        self.labelgroupAwfour.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_won_getter())
        self.labelTeamAlfour.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_lost_getter())
        self.labelTeamAdfour.configure(text=self.groups[0].get_team(self.groups[0].get_teams()[0])[0].match_drawed_getter())
        self.labelPtsAfour.configure(text=self.groups[0].get_points(self.groups[0].get_teams()[0]))

if __name__ == "__main__":
    app = App()
    app.mainloop()
