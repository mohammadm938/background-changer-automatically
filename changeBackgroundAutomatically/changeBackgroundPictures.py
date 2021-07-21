import os
import random
import time
import emoji
import pathlib
import psutil
from colorama import Fore


picNames = []
path = ""


class emojies:
    poker = emoji.emojize(':neutral_face:')


class colors:
    # bg = '\x1b[0m'
    starter = Fore.LIGHTBLUE_EX
    success = Fore.LIGHTGREEN_EX
    error = Fore.LIGHTRED_EX
    msg = Fore.LIGHTYELLOW_EX
    # equal = Fore.LIGHTBLACK_EX


class app():
    def wellcomeMsg():
        print(colors.starter+"[1] select img from path")
        print(colors.starter+"[2] select all img from path")
        print(colors.starter+"[3] select all img from default path (/pic)")

    def wellcome():
        app.wellcomeMsg()
        try:
            result = int(
                input(colors.starter+"Which method do you want to run? "))
        except:
            os.system("clear")
            app.wellcomeMsg()
            result = int(
                input(colors.starter+"Which method do you want to run? "))
        return result

    def setPath():
        os.system("clear")
        print(colors.starter +
              "your images in which location ?? (please write like example)")
        print(colors.starter+"example: /home/mohammad/Pictures/Wallpapers/")
        result = str(input(colors.starter+"your path => "))
        if len(result) == 0:
            exit()
        else:
            return result

    def showUsage():
        cpu_Usage = psutil.cpu_percent()
        ram_Usage = psutil.virtual_memory().percent
        print(colors.msg+f"Cpu: {cpu_Usage}%")
        print(colors.msg+f"Ram: {ram_Usage}%"+colors.starter)

    def setPicNames():
        isCountinue = True
        names = []
        while isCountinue == True:
            # show names of pic that already set
            if not len(names) == 0:
                for item in names:
                    print(item, ' ')

            # asked for add file or not
            result = str(
                input(colors.starter+"Do you want to continue to add more pic ? (y/n)"))
            if result == "n" or result == "N" or result == "NO" or result == "no":
                if len(names) == 0:
                    exit()  # if don't want to add names it mean he/she want to leave this app and it code do that

                isCountinue = False
                os.system('clear')
            else:
                os.system("clear")
                filename = str(
                    input(colors.starter+"Enter your image NAME.FORMAT : "))
                exts = ['.jpeg', '.png', '.jpg']
                name, ext = os.path.splitext(filename)
                if ext in exts:
                    names.append(filename)  # add img Name to the array
                os.system('clear')
        return names

    def load_images_from_folder(folder):
        names = []
        exts = ['.jpeg', '.png', '.jpg']
        for filename in os.listdir(folder):
            name, ext = os.path.splitext(filename)
            if ext in exts:
                names.append(filename)

        if len(names) == 0:
            exit()

        return names

    def setTimeBetweenPic():
        os.system("clear")
        try:
            result = int(
                input(colors.starter+"What is the time interval between photos? (write just minuts number)"))
        except:
            print(colors.error+f"it's not a number{emojies.poker} try again")
            result = int(
                input(colors.starter+"What is the time interval between photos? (write just minuts number)"))
        return result

    def functor(path, picNames):
        interval = app.setTimeBetweenPic()
        lenPic = len(picNames)
        counter = 1
        lastNum = -1
        picShow=[]
        while counter <= 2*(lenPic):
            app.showUsage();
            generatNum = random.randint(0, lenPic-1)
            while lastNum == generatNum:  # use lastNum becuase we want always change pic
                generatNum = random.randint(0, lenPic-1)
            os.system(
                f"gsettings set org.gnome.desktop.background picture-uri 'file://{path}{picNames[generatNum]}'")
            
            picShow.append(picNames[generatNum])
            for item in picShow:
                print(colors.success +f"changed to {item}"+colors.starter)

            time.sleep(interval*60)
            lastNum = generatNum
            counter += 1
            os.system("clear")



class methods:
    def selectPictures():
        path = app.setPath()
        picNames = app.setPicNames()
        app.functor(path, picNames)

    def allImgOnFile():
        path = app.setPath()
        picNames = app.load_images_from_folder(path)
        app.functor(path, picNames)

    def defaultPath():
        path = pathlib.Path(__file__).parent.absolute()
        path = (f"{path}/pic/")
        picNames = app.load_images_from_folder(path)
        app.functor(path, picNames)


result = app.wellcome()
if result == 1:
    methods.selectPictures()
elif result == 2:
    methods.allImgOnFile()
elif result == 3:
    methods.defaultPath()