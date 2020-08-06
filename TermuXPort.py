import os
import time

lt = 1
while lt == 1:
    os.system("clear")
    print("TermuXPort")
    print("Created by Fr0styDev420 0.1 ")
    print("")
    print("This will import and export Termux Files. Exported files will be stored in a folder called TermuXPort on your internal storage drive!")
    print("")
    print("[1]Import")
    print("[2]Export")
    print("[3]Exit")
    print("")
    choice = input("Choice:")
    if choice == "3":
        print(" ")
        lt = 2
    elif choice == "2":
        ltt = 1
        while ltt == 1:
            os.system("clear")
            print("TermuXPort")
            print("Created by freetheorange905 0.1 ")
            print("")
            print("This will import and export Termux Files. Exported files will be stored in a folder called TermuXPort on your internal storage drive!")
            print("")
            print("[1]Export File")
            print("[2]Export Folder")
            print("[3]Export All")
            print("[4]Return")
            print("")
            option = input("Choice:")
            if option == "1":
                print("")
                filee = input("File Path:")
                print("")
                cmdd = "mkdir -p /sdcard/TermuXPort && cp " + filee + " /sdcard/TermuXPort/"
                print("Exporting File...")
                os.system(cmdd)
                time.sleep(1.0)
                print("Done! Returning to Menu...")
                time.sleep(2.4)
                ltt = 2
            elif option == "2":
                print("")
                dirr = input("Folder Path:")
                print("")
                print("Exporting Folder...")
                cm = "mkdir -p /sdcard/TermuXPort && cp -r " + dirr + " /sdcard/TermuXPort/"
                os.system(cm)
                time.sleep(1.0)
                print("Done! Returning to Menu...")
                time.sleep(2.4)
                ltt = 2
            elif option == "3":
                print("")
                print("Exporting All Termux Files...")
                os.system("cp -r ./ /sdcard/TermuXPort")
                time.sleep(1.0)
                print("Done! Returning to Menu...")
                ltt = 2
                time.sleep(2.4)
            elif option == "4":
                ltt = 2
    elif choice == "1":
        lttt = 1
        while lttt == 1:
            os.system("clear")
            print("TermuXPort")
            print("Created by freetheorange905 0.1 ")
            print("")
            print("This will import and export Termux Files. Exported files will be stored in a folder called TermuXPort on your internal storage drive!")
            print("")
            print("[1]Import File")
            print("[2]Import Folder")
            print("[3]Return")
            print("")
            optionn = input("Choice:")
            if optionn == "3":
                lttt = 2
            elif optionn == "2":
                ("")
                fill = input("Folder Path:")
                print("")
                cmm = "cp -r " + fill + " ./"
                print("Importing Folder...")
                os.system(cmm)
                time.sleep(1.0)
                print("Done! Returning to Menu...")
                time.sleep(2.4)
                lttt = 2
            elif optionn == "1":
                print("")
                filey = input("File Path:")
                print("")
                cmd = "cp " + filey + " ./"
                print("Importing File...")
                os.system(cmd)
                time.sleep(1.0)
                print("Done! Returning to Menu...")
                time.sleep(2.4)
                lttt = 2
