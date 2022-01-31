import pyautogui
import pydirectinput
import time

images = {
    "lemonade" : "images\lemonade.png",
    "upgrade" : "images\\upgrade.png",
    "pizza" : "images\pizza.png",
    "donut" : "images\donut.png",
    "shrimp" : "images\shrimp.png",
    "hockey" : "images\hockey.png",
    "movieStudio" : "images\movieStudio.png",
    "bank" : "images\\bank.png",
    "oilCompany" : "images\oilCompany.png"
}

def main():
    while True:
        if pyautogui.locateOnScreen(image=images.get("lemonade"), confidence=0.99, grayscale=True):
            click_button(images.get("lemonade"))
        if pyautogui.locateOnScreen(image=images.get("pizza"), confidence=0.97, grayscale=True):
            click_button(images.get("pizza"))
        if pyautogui.locateOnScreen(image=images.get("donut"), confidence=0.97, grayscale=True):
            click_button(images.get("donut"))
        if pyautogui.locateOnScreen(image=images.get("shrimp"), confidence=0.97, grayscale=True):
            click_button(images.get("shrimp"))
        if pyautogui.locateOnScreen(image=images.get("hockey"), confidence=0.97, grayscale=True):
            click_button(images.get("hockey"))
        if pyautogui.locateOnScreen(image=images.get("movieStudio"), confidence=0.97, grayscale=True):
            click_button(images.get("movieStudio"))
        if pyautogui.locateOnScreen(image=images.get("bank"), confidence=0.97, grayscale=True):
            click_button(images.get("bank"))
        if pyautogui.locateOnScreen(image=images.get("oilCompany"), confidence=1, grayscale=True):
            click_button(images.get("oilCompany"))
        if pyautogui.locateOnScreen(image=images.get("upgrade"), confidence=0.4, grayscale=True):
            click_button(images.get("upgrade"))

def click(loc, delay=0.2, button="left"):
    pyautogui.moveTo(x=loc[0], y=loc[1], duration=delay, tween=pyautogui.easeInSine)
    pydirectinput.mouseDown()
    time.sleep(0.05)
    pydirectinput.mouseUp()           

def click_button(image, delay=0.2, timeout=5, button="left"):
    start_time = time.time()
    loc = None
    while time.time() - start_time < timeout:
        loc = pyautogui.locateCenterOnScreen(image=image, confidence=0.8, grayscale=True)
        if loc is not None:
            break
    if loc is None:
        print("No button matching image " + image + " was found. Continuing...")
        return False
    click(loc, delay, button)
    print("Button matching image " + image + " was found.")
    return True

if __name__ == "__main__":
    main()