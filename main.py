    import customtkinter
    import os
    from PIL import Image
    import tkinter.messagebox
    import webbrowser

    customtkinter.set_appearance_mode("dark")

    scrn = customtkinter.CTk()
    def move_window(event):
        scrn.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
    scrn.geometry("1100x640+100+100")
    scrn.maxsize(width=1100,
                 height=640)
    scrn.minsize(width=800,
                 height=640)
    scrn.title("Test")
    ### Uygulamanın pencere kısmı kaldırıldı
    scrn.overrideredirect(1)

    ###########################################################################################################################################
    #                                                           GAME SAFE
    ###########################################################################################################################################
    def game():

        # Uygulama İconları eklendi
        ubisoft_img=customtkinter.CTkImage(dark_image=Image.open ("images/pngwing.com (1).png"),
                                           size=(80,80))
        steam_img = customtkinter.CTkImage(dark_image=Image.open ("images/pngwing.com.png"),
                                           size=(50,50))
        ea_img = customtkinter.CTkImage(dark_image=Image.open ("images/pngwing.com (3).png"),
                                           size=(60,60))
        epic_img = customtkinter.CTkImage(dark_image=Image.open ("images/pngwing.com (4).png"),
                                           size=(60,60))

        #uygulamalara erişim için dosya yolları belirtildi
        def epic():
            try:
                os.startfile("C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="Epic Games Uygulaması Cihazınız Bulunmamakta !!!")

        def steam():
            try:
                os.startfile("C:\\Program Files (x86)\\Steam\\steam.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="Steam Uygulaması Cihazınız Bulunmamakta !!!")

        def ea():
            try:
                os.startfile("C:\\Program Files\\Electronic Arts\\EA Desktop\\EA Desktop\\EALauncher.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="Ea Games Uygulaması Cihazınız Bulunmamakta !!!")

        def ubisoft():
            try:
                os.startfile("C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\UbisoftConnect.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="Ubisoft Uygulaması Cihazınız Bulunmamakta !!!")



        game = customtkinter.CTkFrame(master=main_frame,
                                           width=1029,
                                           height=600,
                                           fg_color="#333333"

                                          )
        game.place(relx=0.5,
                   rely=0.5,
                   anchor = customtkinter.CENTER)

        ############### STEAM ADD

        steam_button = customtkinter.CTkButton(master=game,
                                               width=80,
                                               height=100,
                                               text=" ",
                                               command=steam,
                                               image=steam_img,
                                               fg_color="#333333",
                                               bg_color="#333333",)

        steam_button.place(relx=0.1,
                           rely=0.125,
                           anchor = customtkinter.CENTER)

        name_steam_label=customtkinter.CTkLabel(master=steam_button,
                                                text="Steam")
        name_steam_label.place(relx=0.45,
                           rely=0.93,
                           anchor = customtkinter.CENTER)

        ############ UBISOFT ADD

        ubisoft_button = customtkinter.CTkButton(master=game,
                                               width=80,
                                               height=100,
                                               text=" ",
                                               command=ubisoft,
                                               image=ubisoft_img,
                                               fg_color="#333333",
                                               bg_color="#333333")
        ubisoft_button.place(relx=0.25,
                           rely=0.125,
                           anchor = customtkinter.CENTER)

        name_ubisoft_label=customtkinter.CTkLabel(master=ubisoft_button,
                                                text="Ubisoft")
        name_ubisoft_label.place(relx=0.45,
                           rely=0.93,
                           anchor = customtkinter.CENTER)

        ########### EPIC GAMES ADD

        epic_button = customtkinter.CTkButton(master=game,
                                               width=80,
                                               height=100,
                                               text=" ",
                                               command=epic,
                                               image=epic_img,
                                               fg_color="#333333",
                                               bg_color="#333333")
        epic_button.place(relx=0.4,
                           rely=0.125,
                           anchor = customtkinter.CENTER)

        name_epic_label=customtkinter.CTkLabel(master=epic_button,
                                                text="Epic Game")
        name_epic_label.place(relx=0.45,
                           rely=0.93,
                           anchor = customtkinter.CENTER)

        ########## EA GAME ADD

        ea_button = customtkinter.CTkButton(master=game,
                                               width=80,
                                               height=100,
                                               text=" ",
                                               command=ea,
                                               image=ea_img,
                                               fg_color="#333333",
                                               bg_color="#333333")
        ea_button.place(relx=0.55,
                           rely=0.125,
                           anchor = customtkinter.CENTER)

        name_ea_label=customtkinter.CTkLabel(master=ea_button,
                                                text="EA")
        name_ea_label.place(relx=0.45,
                           rely=0.93,
                           anchor = customtkinter.CENTER)


    ###########################################################################################################################################
    #                                                           GAME SAFE FINALLY
    ###########################################################################################################################################


    ###########################################################################################################################################
    #                                                           BROWSER SAFE
    ###########################################################################################################################################
    def browser():
        browser = customtkinter.CTkFrame(master=main_frame,
                                           width=1029,
                                           height=600,
                                           fg_color="#333333")
        browser.place(relx=0.5,
                        rely=0.5,
                        anchor=customtkinter.CENTER)
        # Uygulama İconları eklendi
        brave_img=customtkinter.CTkImage(dark_image=Image.open ("images/brave-browser-icon.png"),
                                         size=(50,55))
        edge_img = customtkinter.CTkImage(dark_image=Image.open ("images/edge-browser-icon.png"),
                                         size=(50,50))

        # uygulamalara erişim için dosya yolları belirtildi
        def brav():
            try:
                os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="Brave Uygulaması Cihazınız Bulunmamakta !!!")

        def edge():
            try:
                os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="Microsoft Edge Uygulaması Cihazınız Bulunmamakta !!!")


            ############### brave ADD

        brave_button = customtkinter.CTkButton(master=browser,
                                               width=80,
                                               height=100,
                                               text=" ",
                                               command=brav,
                                               image=brave_img,
                                               fg_color="#333333",
                                               bg_color="#333333",


                                               )
        brave_button.place(relx=0.1,
                           rely=0.125,
                           anchor = customtkinter.CENTER)



        name_brave_label=customtkinter.CTkLabel(master=brave_button,
                                                text="Brave")
        name_brave_label.place(relx=0.45,
                           rely=0.93,
                           anchor = customtkinter.CENTER)

        ############ edge ADD

        edge_button = customtkinter.CTkButton(master=browser,
                                               width=80,
                                               height=100,
                                               text=" ",
                                               command=edge,
                                               image=edge_img,
                                               fg_color="#333333",
                                               bg_color="#333333")
        edge_button.place(relx=0.25,
                           rely=0.125,
                           anchor = customtkinter.CENTER)

        name_edge_label=customtkinter.CTkLabel(master=edge_button,
                                                text="Edge")
        name_edge_label.place(relx=0.45,
                           rely=0.93,
                           anchor = customtkinter.CENTER)



    ###########################################################################################################################################
    #                                                           BROWSER SAFE FINALLY
    ###########################################################################################################################################

    ###########################################################################################################################################
    #                                                           OFF�CE SAFE
    ###########################################################################################################################################
    def office():
        office = customtkinter.CTkFrame(master=main_frame,
                                           width=1029,
                                           height=600,
                                           fg_color="#333333")
        office.place(relx=0.5,
                        rely=0.5,
                        anchor=customtkinter.CENTER)
        # Uygulama İconları eklendi
        librew_img=customtkinter.CTkImage(dark_image=Image.open ("images/LibreOffice_Writer-Logo.wine.png"),
                                          size=(100,75))
        libreb_img=customtkinter.CTkImage(dark_image=Image.open ("images/LibreOffice_Base-Logo.wine.png"),
                                          size=(100,75))
        librec_img=customtkinter.CTkImage(dark_image=Image.open ("images/LibreOffice_Calc-Logo.wine.png"),
                                          size=(100,75))
        libred_img=customtkinter.CTkImage(dark_image=Image.open ("images/LibreOffice_Draw-Logo.wine.png"),
                                          size=(100,75))
        librei_img=customtkinter.CTkImage(dark_image=Image.open ("images/libreofficeimpress_94297.png"),
                                          size=(50,50))
        librem_img=customtkinter.CTkImage(dark_image=Image.open ("images/libreoffice_math_icon_181054.png"),
                                          size=(50,50))

        # uygulamalara erişim için dosya yolları belirtildi

        def librew():
            try:
                os.startfile("C:\\Program Files\\LibreOffice\\program\\swriter.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="LibreOffice Writter Uygulaması Cihazınız Bulunmamakta !!!")

        def libreb():
            try:
                os.startfile("C:\\Program Files\\LibreOffice\\program\\sbase.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="LibreOffice Base Uygulaması Cihazınız Bulunmamakta !!!")

        def librec():
            try:
                os.startfile("C:\\Program Files\\LibreOffice\\program\\scalc.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="LibreOffice Calc Uygulaması Cihazınız Bulunmamakta !!!")

        def libred():
            try:
                os.startfile("C:\\Program Files\\LibreOffice\\program\\sdraw.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="LibreOffice Draw Uygulaması Cihazınız Bulunmamakta !!!")

        def librei():
            try:
                os.startfile("C:\\Program Files\\LibreOffice\\program\\simpress.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="LibreOffice Impress Uygulaması Cihazınız Bulunmamakta !!!")

        def librem():
            try:
                os.startfile("C:\\Program Files\\LibreOffice\\program\\smath.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="LibreOffice Math Uygulaması Cihazınız Bulunmamakta !!!")


            ############### writer ADD

        librew_button = customtkinter.CTkButton(master=office,
                                               width=80,
                                               height=100,
                                               text=" ",
                                               command=librew,
                                               image=librew_img,
                                               fg_color="#333333",
                                               bg_color="#333333",


                                               )
        librew_button.place(relx=0.1,
                           rely=0.125,
                           anchor = customtkinter.CENTER)



        name_librew_label=customtkinter.CTkLabel(master=librew_button,
                                                text="Writer")
        name_librew_label.place(relx=0.45,
                           rely=0.93,
                           anchor = customtkinter.CENTER)

                ############### base ADD

        libreb_button = customtkinter.CTkButton(master=office,
                                               width=80,
                                               height=100,
                                               text=" ",
                                               command=libreb,
                                               image=libreb_img,
                                               fg_color="#333333",
                                               bg_color="#333333",


                                               )
        libreb_button.place(relx=0.25,
                           rely=0.125,
                           anchor = customtkinter.CENTER)



        name_libreb_label=customtkinter.CTkLabel(master=libreb_button,
                                                text="Base")
        name_libreb_label.place(relx=0.45,
                           rely=0.93,
                           anchor = customtkinter.CENTER)

                    ############### calc ADD

        librec_button = customtkinter.CTkButton(master=office,
                                               width=80,
                                               height=100,
                                               text=" ",
                                               command=librec,
                                               image=librec_img,
                                               fg_color="#333333",
                                               bg_color="#333333",
                                               )
        librec_button.place(relx=0.40,
                           rely=0.125,
                           anchor = customtkinter.CENTER)



        name_librec_label=customtkinter.CTkLabel(master=librec_button,
                                                text="Calc")
        name_librec_label.place(relx=0.45,
                           rely=0.93,
                           anchor = customtkinter.CENTER)
                    ############### draw ADD

        libred_button = customtkinter.CTkButton(master=office,
                                               width=80,
                                               height=100,
                                               text=" ",
                                               command=libred,
                                               image=libred_img,
                                               fg_color="#333333",
                                               bg_color="#333333",
                                               )
        libred_button.place(relx=0.55,
                           rely=0.125,
                           anchor = customtkinter.CENTER)



        name_libred_label=customtkinter.CTkLabel(master=libred_button,
                                                text="Draw")
        name_libred_label.place(relx=0.45,
                           rely=0.93,
                           anchor = customtkinter.CENTER)
                    ############### impress ADD

        librei_button = customtkinter.CTkButton(master=office,
                                               width=80,
                                               height=100,
                                               text=" ",
                                               command=librei,
                                               image=librei_img,
                                               fg_color="#333333",
                                               bg_color="#333333",
                                               )
        librei_button.place(relx=0.70,
                           rely=0.125,
                           anchor = customtkinter.CENTER)



        name_librei_label=customtkinter.CTkLabel(master=librei_button,
                                                text="Impress")
        name_librei_label.place(relx=0.45,
                           rely=0.93,
                           anchor = customtkinter.CENTER)
                    ############### math ADD

        librem_button = customtkinter.CTkButton(master=office,
                                               width=80,
                                               height=100,
                                               text=" ",
                                               command=librem,
                                               image=librem_img,
                                               fg_color="#333333",
                                               bg_color="#333333",
                                               )
        librem_button.place(relx=0.85,
                           rely=0.125,
                           anchor = customtkinter.CENTER)



        name_librem_label=customtkinter.CTkLabel(master=librem_button,
                                                text="Math")
        name_librem_label.place(relx=0.45,
                           rely=0.93,
                           anchor = customtkinter.CENTER)


    ###########################################################################################################################################
    #                                                           OFF�CE SAFE FINALLY
    ###########################################################################################################################################

    ###########################################################################################################################################
    #                                                           PROGRAMING SAFE
    ###########################################################################################################################################

    def programing():
        programing = customtkinter.CTkFrame(master=main_frame,
                                           width=1029,
                                           height=600,
                                           fg_color="#333333")
        programing.place(relx=0.5,
                        rely=0.5,
                        anchor=customtkinter.CENTER)

        # Uygulama İconları eklendi

        p1_img=customtkinter.CTkImage(dark_image=Image.open ("images/pycharm.png"),
                                      size=(50,50))
        p2_img=customtkinter.CTkImage(dark_image=Image.open ("images/visual.png"),
                                      size=(50,50))
        p3_img=customtkinter.CTkImage(dark_image=Image.open ("images/emeditor.png"),
                                      size=(50,50))
        p4_img=customtkinter.CTkImage(dark_image=Image.open ("images/eclipse.png"),
                                      size=(50,50))
        p5_img=customtkinter.CTkImage(dark_image=Image.open ("images/filezilla.png"),
                                      size=(50,50))
        p6_img=customtkinter.CTkImage(dark_image=Image.open ("images/git.png"),
                                      size=(50,50))
        p7_img=customtkinter.CTkImage(dark_image=Image.open ("images/github.png"),
                                      size=(70,70))
        p8_img=customtkinter.CTkImage(dark_image=Image.open ("images/unreal.png"),
                                      size=(60,60))
        p9_img=customtkinter.CTkImage(dark_image=Image.open ("images/unity.png"),
                                      size=(50,50))

        # uygulamalara erişim için dosya yolları belirtildi

        def p1_func():
            try:
                os.startfile("C:\\Program Files\\JetBrains\\PyCharm 2024.1.3\\bin\\pycharm64.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="PyCharm Uygulaması Cihazınız Bulunmamakta !!!")


        def p2_func():
            try:
                os.startfile("C:\\Users\\CHARON\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="VS Code Uygulaması Cihazınız Bulunmamakta !!!")


        def p3_func():
            try:
                os.startfile("C:\\Users\\CHARON\\AppData\\Local\\Programs\\EmEditor\\EmEditor.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="Em Editor Uygulaması Cihazınız Bulunmamakta !!!")


        def p4_func():
            try:
                os.startfile("C:\\Users\\CHARON\\eclipse\\cpp-2023-122\\eclipse\\eclipse.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="Eclipse IDE Uygulaması Cihazınız Bulunmamakta !!!")


        def p5_func():
            try:
                os.startfile("C:\\Program Files\\FileZilla FTP Client\\filezilla.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="Filezilla Uygulaması Cihazınız Bulunmamakta !!!")


        def p6_func():
            try:
                os.startfile("C:\\Program Files\\Git\\git-bash.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="GİT Uygulaması Cihazınız Bulunmamakta !!!")


        def p7_func():
            try:
                os.startfile("C:\\Users\\CHARON\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="GitHub Uygulaması Cihazınız Bulunmamakta !!!")


        def p8_func():
            try:
                os.startfile("C:\\Program Files\\Epic Games\\UE_5.3\\Engine\\Binaries\\Win64\\UnrealEditor.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="Unreal Engine Uygulaması Cihazınız Bulunmamakta !!!")


        def p9_func():
            try:
                os.startfile("C:\\Program Files\\Unity Hub\\Unity Hub.exe")
            except:
                tkinter.messagebox.showinfo(title="Uyarı", message="Unity Uygulaması Cihazınız Bulunmamakta !!!")


            ############### PyCharm ADD

        p1_button = customtkinter.CTkButton(master=programing,
                                                width=80,
                                                height=100,
                                                text=" ",
                                                command=p1_func,
                                                image=p1_img,
                                                fg_color="#333333",
                                                bg_color="#333333",

                                                )
        p1_button.place(relx=0.1,
                            rely=0.125,
                            anchor=customtkinter.CENTER)

        name_p1_label = customtkinter.CTkLabel(master=p1_button,
                                                   text="PyCharm")
        name_p1_label.place(relx=0.45,
                                rely=0.93,
                                anchor=customtkinter.CENTER)

            ############### Visual Studio ADD

        p2_button = customtkinter.CTkButton(master=programing,
                                                width=80,
                                                height=100,
                                                text=" ",
                                                command=p2_func,
                                                image=p2_img,
                                                fg_color="#333333",
                                                bg_color="#333333",

                                                )
        p2_button.place(relx=0.25,
                            rely=0.125,
                            anchor=customtkinter.CENTER)

        name_p2_label = customtkinter.CTkLabel(master=p2_button,
                                                   text="Visual")
        name_p2_label.place(relx=0.45,
                                rely=0.93,
                                anchor=customtkinter.CENTER)

            ############### em editor  ADD

        p3_button = customtkinter.CTkButton(master=programing,
                                                width=80,
                                                height=100,
                                                text=" ",
                                                command=p3_func,
                                                image=p3_img,
                                                fg_color="#333333",
                                                bg_color="#333333",

                                                )
        p3_button.place(relx=0.40,
                            rely=0.125,
                            anchor=customtkinter.CENTER)

        name_p3_label = customtkinter.CTkLabel(master=p3_button,
                                                   text="Em Editor")
        name_p3_label.place(relx=0.45,
                                rely=0.93,
                                anchor=customtkinter.CENTER)

            ############### eclipse  ADD

        p4_button = customtkinter.CTkButton(master=programing,
                                                width=80,
                                                height=100,
                                                text=" ",
                                                command=p4_func,
                                                image=p4_img,
                                                fg_color="#333333",
                                                bg_color="#333333",

                                                )
        p4_button.place(relx=0.55,
                            rely=0.125,
                            anchor=customtkinter.CENTER)

        name_p4_label = customtkinter.CTkLabel(master=p4_button,
                                                   text="Eclipse")
        name_p4_label.place(relx=0.45,
                                rely=0.93,
                                anchor=customtkinter.CENTER)

            ############### fizezilla  ADD

        p5_button = customtkinter.CTkButton(master=programing,
                                                width=80,
                                                height=100,
                                                text=" ",
                                                command=p5_func,
                                                image=p5_img,
                                                fg_color="#333333",
                                                bg_color="#333333",

                                                )
        p5_button.place(relx=0.70,
                            rely=0.125,
                            anchor=customtkinter.CENTER)

        name_p5_label = customtkinter.CTkLabel(master=p5_button,
                                                   text="Filezilla")
        name_p5_label.place(relx=0.45,
                                rely=0.93,
                                anchor=customtkinter.CENTER)

            ############### Git  ADD

        p6_button = customtkinter.CTkButton(master=programing,
                                                width=80,
                                                height=100,
                                                text=" ",
                                                command=p6_func,
                                                image=p6_img,
                                                fg_color="#333333",
                                                bg_color="#333333",

                                                )
        p6_button.place(relx=0.1,
                            rely=0.3,
                            anchor=customtkinter.CENTER)

        name_p6_label = customtkinter.CTkLabel(master=p6_button,
                                                   text="Git")
        name_p6_label.place(relx=0.45,
                                rely=0.93,
                                anchor=customtkinter.CENTER)

            ############### Github  ADD

        p7_button = customtkinter.CTkButton(master=programing,
                                                width=80,
                                                height=100,
                                                text=" ",
                                                command=p7_func,
                                                image=p7_img,
                                                fg_color="#333333",
                                                bg_color="#333333",

                                                )
        p7_button.place(relx=0.25,
                            rely=0.3,
                            anchor=customtkinter.CENTER)

        name_p7_label = customtkinter.CTkLabel(master=p7_button,
                                                   text="Github")
        name_p7_label.place(relx=0.45,
                                rely=0.93,
                                anchor=customtkinter.CENTER)

            ############### Unreal  ADD

        p8_button = customtkinter.CTkButton(master=programing,
                                                width=80,
                                                height=100,
                                                text=" ",
                                                command=p8_func,
                                                image=p8_img,
                                                fg_color="#333333",
                                                bg_color="#333333",

                                                )
        p8_button.place(relx=0.4,
                            rely=0.3,
                            anchor=customtkinter.CENTER)

        name_p8_label = customtkinter.CTkLabel(master=p8_button,
                                                   text="Unreal")
        name_p8_label.place(relx=0.45,
                                rely=0.93,
                                anchor=customtkinter.CENTER)

            ############### Git  ADD

        p9_button = customtkinter.CTkButton(master=programing,
                                                width=80,
                                                height=100,
                                                text=" ",
                                                command=p9_func,
                                                image=p9_img,
                                                fg_color="#333333",
                                                bg_color="#333333",

                                                )
        p9_button.place(relx=0.55,
                            rely=0.30,
                            anchor=customtkinter.CENTER)

        name_p9_label = customtkinter.CTkLabel(master=p9_button,
                                                   text="Unity")
        name_p9_label.place(relx=0.45,
                                rely=0.93,
                                anchor=customtkinter.CENTER)


    ###########################################################################################################################################
    #                                                           PROGRAMING SAFE FINALLY
    ###########################################################################################################################################


    ###########################################################################################################################################
    #                                                   TOP BUTTON
    ###########################################################################################################################################
    ################## uygulamay� kapatmak i�in kapatma fonksiyonu olu�turuldu


    ################# uygulamay� simge durumunu getirmek i�in fonksiyon tan�mland�
    def ICONFY():
        scrn.iconify()

    title_bar = customtkinter.CTkFrame(master=scrn,
                                       width=1029,
                                       height=40,
                                       fg_color="#333333")
    title_bar.place(relx=0.53,rely=0.025,anchor=customtkinter.CENTER)
    title_bar.bind('<B1-Motion>', move_window)

    syborg = customtkinter.CTkImage(dark_image=Image.open ("images/cyborg.png"),
                                        size=(30,30))
    syborg_label = customtkinter.CTkLabel(master=title_bar,
                                          text=" ",
                                          image=syborg)
    syborg_label.place(relx=0.04,rely=0.5,anchor=customtkinter.CENTER)

    syborg_label1 = customtkinter.CTkLabel(master=title_bar,
                                          text="Cyborg App",
                                          text_color="grey")
    syborg_label1.place(relx=0.09,rely=0.5,anchor=customtkinter.CENTER)



    exit_button = customtkinter.CTkButton(master=title_bar,
                                          width=30,
                                          height=25,
                                          text="x",
                                          font=("Arial",12,"normal"),
                                          fg_color="#4B4B4B",
                                          command=scrn.quit,
                                          )
    exit_button.place(relx=0.98,
                      rely=0.5,
                      anchor=customtkinter.CENTER)

    tab_button = customtkinter.CTkButton(master=title_bar,
                                          width=30,
                                          height=25,
                                          text="-",
                                          font=("Arial",12,"normal"),
                                          fg_color="#4B4B4B",
                                          command=ICONFY
                                          )
    tab_button.place(relx=0.95,
                      rely=0.5,
                      anchor=customtkinter.CENTER)


    ###########################################################################################################################################
    #                                                   TOP BUTTON FINALLY
    ###########################################################################################################################################



    ###########################################################################################################################################
    #                                                   LEFT MENU
    ###########################################################################################################################################

    FONT_1 =("Arial" , 18, "normal")

    left_menu_frame = customtkinter.CTkFrame(master=scrn,
                                             width=140,
                                             height=640,
                                             fg_color="#4B4B4B")
    left_menu_frame.place(relx=0,
                          rely=0.5,
                          anchor=customtkinter.CENTER)

    gameMenu_img=customtkinter.CTkImage(dark_image=Image.open ("images/gaming-gamepad-icon.png"),
                                        size=(40,30))
    progMenu_img=customtkinter.CTkImage(dark_image=Image.open ("images/code-icon.png"),
                                        size=(40,30))
    browMenu_img=customtkinter.CTkImage(dark_image=Image.open ("images/browser-safari-icon.png"),
                                        size=(40,40))
    officeMenu_img=customtkinter.CTkImage(dark_image=Image.open ("images/briefcase-icon.png"),
                                          size=(40,30))
    spotify_img=customtkinter.CTkImage(dark_image=Image.open ("images/spotify.png"),
                                       size=(60,60))
    youtube_img=customtkinter.CTkImage(dark_image=Image.open ("images/youtube.png"),
                                       size=(40,40))
    gpt_img=customtkinter.CTkImage(dark_image=Image.open ("images/gpt.png"),
                                       size=(35,35))

    def spotify():
        try:
            url = "spotify.com"
            webbrowser.open_new(url)
        except:
            tkinter.messagebox.showinfo(title="Uyarı",
                                        message="Cihazınızda Spotify Bulunmamaktadır !!!")


    left_buuton1 = customtkinter.CTkButton(master=left_menu_frame,
                                           width=40,
                                           height=30,
                                           text=" ",
                                           font = FONT_1,
                                           command=game,
                                           image=gameMenu_img,
                                           bg_color="#4B4B4B",
                                           fg_color="#4B4B4B")

    left_buuton1.place(relx=0.75,
                       rely=0.2,
                       anchor = customtkinter.CENTER)

    left_buuton2 = customtkinter.CTkButton(master=left_menu_frame,
                                           width=40,
                                           height=30,
                                           text=" ",
                                           font = FONT_1,
                                           command=programing,
                                           image=progMenu_img,
                                           bg_color="#4B4B4B",
                                           fg_color="#4B4B4B")

    left_buuton2.place(relx=0.75,
                       rely=0.3,
                       anchor = customtkinter.CENTER)

    left_buuton3 = customtkinter.CTkButton(master=left_menu_frame,
                                           width=40,
                                           height=40,
                                           text=" ",
                                           font = FONT_1,
                                           command=browser,
                                           image=browMenu_img,
                                           fg_color="#4B4B4B",
                                           bg_color="#4B4B4B")

    left_buuton3.place(relx=0.75,
                       rely=0.4,
                       anchor = customtkinter.CENTER)

    left_buuton4 = customtkinter.CTkButton(master=left_menu_frame,
                                           width=40,
                                           height=30,
                                           text=" ",
                                           font = FONT_1,
                                           command=office,
                                           image=officeMenu_img,
                                           fg_color="#4B4B4B",
                                           bg_color="#4B4B4B")

    left_buuton4.place(relx=0.75,
                       rely=0.5,
                       anchor = customtkinter.CENTER)

    spotify_button = customtkinter.CTkButton(master=left_menu_frame,
                                             width=40,
                                             height=30,
                                             text=" ",
                                             font=FONT_1,
                                             command=spotify,
                                             image=spotify_img,
                                             fg_color="#4B4B4B",
                                             bg_color="#4B4B4B"
                                             )
    spotify_button.place(relx=0.75,
                       rely=0.6,
                       anchor = customtkinter.CENTER)

    def youtube():
        url="youtube.com"
        webbrowser.open(url)

    youtube_button = customtkinter.CTkButton(master=left_menu_frame,
                                             width=40,
                                             height=30,
                                             text=" ",
                                             font=FONT_1,
                                             command=youtube,
                                             image=youtube_img,
                                             fg_color="#4B4B4B",
                                             bg_color="#4B4B4B"
                                             )
    youtube_button.place(relx=0.75,
                       rely=0.7,
                       anchor = customtkinter.CENTER)

    def gpt():
        url = "https://chatgpt.com/"
        webbrowser.open_new(url)

    gpt_button = customtkinter.CTkButton(master=left_menu_frame,
                                             width=40,
                                             height=30,
                                             text=" ",
                                             font=FONT_1,
                                             command=gpt,
                                             image=gpt_img,
                                             fg_color="#4B4B4B",
                                             bg_color="#4B4B4B"
                                             )
    gpt_button.place(relx=0.75,
                       rely=0.8,
                       anchor = customtkinter.CENTER)

    ###########################################################################################################################################
    #                                                   LEFT MENU FINALLY
    ###########################################################################################################################################

    ###########################################################################################################################################
    #                                                    MAIN MENU
    ###########################################################################################################################################

    main_frame = customtkinter.CTkFrame(master=scrn,
                                        width=1029,
                                        height=600,
                                        )
    main_frame.place(relx=0.534,
                     rely=0.53,
                     anchor = customtkinter.CENTER)

    win_frame = customtkinter.CTkFrame(master=main_frame,
                                       width=3,
                                       height=603,
                                       fg_color="#4B4B4B"
                                       )
    win_frame.place(relx=0.5,
                    rely=0.5,
                    anchor=customtkinter.CENTER)

    FONT__1 = ("Arial" , 28, "bold")
    lab1 = customtkinter.CTkLabel(master=main_frame,
                                  font=FONT__1,
                                  text="GitHub Profili",
                                  text_color="#4B4B4B")
    lab1.place(relx=0.75,
               rely=0.2,
               anchor=customtkinter.CENTER)
    def web():

        url = "https://github.com/mhmt44ylpr"
        # Web sitesi linkini aç
        webbrowser.open(url)

    profile_button = customtkinter.CTkButton(master=main_frame,
                                             width=200,
                                             height=60,
                                             text="Ziyaret Et",
                                             command=web,
                                             fg_color="#4B4B4B")

    profile_button.place(relx=0.75,
                         rely=0.6,
                         anchor=customtkinter.CENTER)

    lab2 = customtkinter.CTkLabel(master=main_frame,
                                  font=FONT__1,
                                  text="Donate",
                                  text_color="#4B4B4B")
    lab2.place(relx=0.25,
               rely=0.2,
               anchor=customtkinter.CENTER)
    def web():
        pass

    profile_button = customtkinter.CTkButton(master=main_frame,
                                             width=200,
                                             height=60,
                                             text="Ziyaret Et",
                                             command=web,
                                             fg_color="#4B4B4B")

    profile_button.place(relx=0.25,
                         rely=0.6,
                         anchor=customtkinter.CENTER)


    ###########################################################################################################################################
    #                                                   MAIN MENU FINALLY
    ###########################################################################################################################################
    if __name__ == "__main__":
        scrn.mainloop()
