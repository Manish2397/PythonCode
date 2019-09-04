import pyautogui
import pyperclip


def doCommand(command, text=""):
    if command == "paste":
        pyautogui.hotkey("ctrl", "v")
    elif command == "copy":
        pyperclip.copy(text)
    elif command == "caps":
        pyautogui.press("capslock")
    elif command == "tab":
        pyautogui.press("tab")
    elif command == "up":
        pyautogui.press("pageup")
    elif command == "down":
        pyautogui.press("pagedown")
    else:
        print("unknown command")


def getcommands(commands, text=""):
    try:
        commandList = commands.split(" ")
        command = commandList[1]
        doCommand(command.lower(), text)
    except:
        print("error!!!")
