import keyboardListener
import time

def eventHandler(event, foo, foo1):
    print(event, foo, foo1)

def main():
    listener = keyboardListener.Listener(eventHandler, foo="hei", foo1="world")
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
