from listener import Listener
import time

def eventHandler(event):
    print(event)

def main():
    listener = Listener(eventHandler)
    listener.listen()

    try:
        while True:
            if (listener.isPressed(0x1b)):
                print("ESC pressed, Quitting")
                listener.stop()
                break

            time.sleep(0.00001)
    except KeyboardInterrupt:
        print("KeyboardInterrupt , Quitting")
        listener.stop()

if __name__ == "__main__":
    main()
