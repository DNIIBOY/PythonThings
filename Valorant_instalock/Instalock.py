import pyautogui as auto
from PIL import ImageGrab as imggrab
from time import sleep


def agent_select():
    global agent_X
    global agent_Y
    agent_X = 626
    agent_Y = 925

    slotInput = input("Select agent slot number: ")
    if slotInput.strip().isdigit():
        slotInput = int(slotInput)
    else:
        print("Not a number")
        quit()

    while slotInput < 1 or slotInput > 18:
        print("Ivalid number, has to be between 1-18")
        slotInput = int(input("Select agent slot number: "))


    if 1 < slotInput < 10:
        agent_X = agent_X+84*(slotInput-1)
    elif slotInput > 9:
        agent_X = agent_X+84*(slotInput-10)
        agent_Y = agent_Y + 84


def wait_for_load():
    while True:
        img = imggrab.grab(bbox=(841, 784, 841+1, 784+1))
        img2 = imggrab.grab(bbox=(950, 866, 950+1, 866+1))

        rgb_pixel_value = img.getpixel((0, 0))
        rgb_pixel_value2 = img2.getpixel((0, 0))

        if rgb_pixel_value == (255,255,255) and rgb_pixel_value2 == (234,238,178):
            return
        sleep(0.2)

def lockin():
    auto.click(agent_X, agent_Y)
    auto.click(clicks=1)
    sleep(0.02)
    auto.moveTo(1085,820)
    auto.drag(-15,0,duration=0.02)
    auto.click(clicks=2)
        

def main():
    agent_select()
    
    while True:
        print("waiting...")
        wait_for_load()
        lockin()
        print("agent locked")
        sleep(2)

        while True:
            answer = str(input('Run again? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
        if answer == 'y':
            continue
        else:
            print("Mojn")
            break

if __name__ == "__main__":
    main()
