import pyautogui as auto
from PIL import ImageGrab as imggrab
from time import sleep
from keyboard import press_and_release


def agent_select():
    global agent_X
    global agent_Y
    agent_X = 626
    agent_Y = 925

    slotInput = input("Select agent slot number: ")
    if slotInput.strip().isdigit():
        slotInput = int(slotInput)
    else:
        slotInput = 18

    while slotInput < 1 or slotInput > 18:
        print("Ivalid number, has to be between 1-18")
        slotInput = int(input("Select agent slot number: "))

    if slotInput == 18:
        print("yoru selected")
    else:
        print(f"agent {slotInput} selected")

    if 1 < slotInput < 10:
        agent_X = agent_X+84*(slotInput-1)
    elif slotInput > 9:
        agent_X = agent_X+84*(slotInput-10)
        agent_Y = agent_Y + 84


def wait_for_select():
    while True:
        img = imggrab.grab(bbox=(841, 784, 841+1, 784+1))
        img2 = imggrab.grab(bbox=(950, 866, 950+1, 866+1))

        rgb_pixel_value = img.getpixel((0, 0))
        rgb_pixel_value2 = img2.getpixel((0, 0))

        if rgb_pixel_value == (255,255,255) and rgb_pixel_value2 == (234,238,178):
            return
        

def lockin():
    auto.click(agent_X, agent_Y)
    auto.click(clicks=1)
    sleep(0.02)
    auto.moveTo(1000,820)
    auto.drag(-15,0,duration=0.02)
    auto.click(clicks=2)


def wait_for_buy():
    while True:
        img = imggrab.grab(bbox=(1000, 1045, 1000+1, 1045+1)) # single tp charge

        rgb_pixel_value = img.getpixel((0, 0))

        if rgb_pixel_value == (95, 238, 184):
            return


def yoru_buy():
    press_and_release("b")
    # auto.moveTo(467, 434) # frenzy
    # auto.click(467, 434) # frenzy
    auto.moveTo(467, 550) # ghost
    auto.click(467, 550) # ghost
    auto.click(clicks=1)
    sleep(0.02)
    auto.moveTo(950,904) # flash
    auto.drag(-15,0,duration=0.02)
    auto.click(clicks=2)
    sleep(0.02)
    # auto.moveTo(590,883) # decoy
    # auto.drag(-15,0,duration=0.02)
    auto.click(clicks=2)
    sleep(1)
    press_and_release("b")
    sleep(0.5)
    press_and_release("3")


def main():
    agent_select()
    try:
        wait_for_select()
        lockin()
    except KeyboardInterrupt:
        pass
    print("agent locked")
    print("waiting for game load")
    sleep(5)
    wait_for_buy()
    sleep(1)
    yoru_buy()
    print("items bought")
    print("quiting program...")
    quit()


if __name__ == "__main__":
    main()
