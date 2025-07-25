
  # import speech_recognition as sr
# from pyfirmata import Arduino, util
# import time
# import pyttsx3

# # Set up Arduino board
# board = Arduino('COM4')  # Replace with your port
# red_led_pin = 3
# green_led_pin = 6
# blue_led_pin = 9

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# # Function to provide auditory feedback
# def speak(message):
#     engine.say(message)
#     engine.runAndWait()

# #wish me function
# def wishme():
#     speak("Hello, Mr Stark. All systems are operational. How can I assist you?")

# # Function to toggle LED state
# def toggle_led(led_pin, state):
#     board.digital[led_pin].write(state)

# # Function to listen for voice commands
# def listen_for_command():
#     with sr.Microphone() as source:
#         print("Listening for command...")
#         audio = recognizer.listen(source)

#     try:
#         command = recognizer.recognize_google(audio).lower()
#         print("Command:", command)
#         return command
#     except sr.UnknownValueError:
#         print("Sorry, I didn't catch that.")
#         speak("Sorry, I didn't catch that.")
#         return None
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))
#         speak("Could not request results.")
#         return None

# if __name__ == "__main__":
#   wishme()
#   while True:
#     command = listen_for_command()

#     if command:
#         if "white light on" in command:
#             toggle_led(red_led_pin, 1)
#             speak("Red LED turned on.")
#         elif "white light off" in command:
#             toggle_led(red_led_pin, 0)
#             speak("Red LED turned off.")
#         elif "green light on" in command:
#             toggle_led(green_led_pin, 1)
#             speak("Green LED turned on.")
#         elif "green light off" in command:
#             toggle_led(green_led_pin, 0)
#             speak("Green LED turned off.")
#         elif "blue light on" in command:
#             toggle_led(blue_led_pin, 1)
#             speak("Blue LED turned on.")
#         elif "blue light off" in command:
#             toggle_led(blue_led_pin, 0)
#             speak("Blue LED turned off.")
#         elif "exit" in command:
#             speak("Exiting program, have a good day sir")
#             break
#         else:
#             speak("Command not recognized.")




# import speech_recognition as sr
# from pyfirmata import Arduino, util
# import pyttsx3
# import time

# # Set up Arduino board
# board = Arduino('COM4')  # Replace with your actual port (e.g., COM4, COM5, etc.)
# it = util.Iterator(board)
# it.start()

# # Define LED pins
# red_led = board.digital[3]
# green_led = board.digital[6]
# blue_led = board.digital[9]

# # Set LED pins as OUTPUT
# red_led.mode = 1
# green_led.mode = 1
# blue_led.mode = 1

# # Voice recognition & text-to-speech setup
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# # Speak function
# def speak(message):
#     print("Assistant:", message)
#     engine.say(message)
#     engine.runAndWait()

# # Welcome function
# def wishme():
#     speak("Hello, Mr Stark. All systems are operational. How can I assist you?")

# # Listen function
# def listen_for_command():
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)  # Helps with noisy environment
#         audio = recognizer.listen(source)

#     try:
#         command = recognizer.recognize_google(audio).lower()
#         print("You said:", command)
#         return command
#     except sr.UnknownValueError:
#         speak("Sorry, I didn't catch that.")
#         return None
#     except sr.RequestError:
#         speak("Speech service is unavailable.")
#         return None

# # LED Control
# def toggle_led(led, state, color):
#     led.write(state)
#     if state == 1:
#         speak(f"{color} LED turned on.")
#     else:
#         speak(f"{color} LED turned off.")

# # Main function
# if __name__ == "__main__":
#     wishme()
#     while True:
#         try:
#             command = listen_for_command()
#             if command:

#                 if "red light on" in command:
#                     toggle_led(red_led, 1, "Red")
#                 elif "red light off" in command:
#                     toggle_led(red_led, 0, "Red")

#                 elif "green light on" in command:
#                     toggle_led(green_led, 1, "Green")
#                 elif "green light off" in command:
#                     toggle_led(green_led, 0, "Green")

#                 elif "blue light on" in command:
#                     toggle_led(blue_led, 1, "Blue")
#                 elif "blue light off" in command:
#                     toggle_led(blue_led, 0, "Blue")

#                 elif "all lights on" in command:
#                     toggle_led(red_led, 1, "Red")
#                     toggle_led(green_led, 1, "Green")
#                     toggle_led(blue_led, 1, "Blue")

#                 elif "all lights off" in command:
#                     toggle_led(red_led, 0, "Red")
#                     toggle_led(green_led, 0, "Green")
#                     toggle_led(blue_led, 0, "Blue")

#                 elif "exit" in command or "stop" in command:
#                     speak("Shutting down. Goodbye, Mr Stark.")
#                     break

#                 else:
#                     speak("Command not recognized. Please try again.")
#         except Exception as e:
#             print("Error:", e)
#             speak("Something went wrong.")






import speech_recognition as sr
from pyfirmata import Arduino, util
import pyttsx3
import time

# Set up Arduino board
board = Arduino('COM5')  # Replace with your port
it = util.Iterator(board)
it.start()

# Define LED pins
led_pins = {
    "red": board.digital4[3],
    "green": board.digital[5],
    "blue": board.digital[8],
    "yellow": board.digital[10],
    "white": board.digital[13]
}

# Set LED pins as OUTPUT
for pin in led_pins.values():
    pin.mode = 1

# Voice recognition & text-to-speech setup
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak(message):
    print("Assistant:", message)
    engine.say(message)
    engine.runAndWait()

# Welcome function
def wishme():
    speak("Hello, Mr Ram. All systems are operational. How can I assist you?")

# Listen for voice commands
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return None
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return None

# Toggle a single LED
def toggle_led(color, state):
    led = led_pins[color]
    led.write(state)
    if state == 1:
        speak(f"{color.capitalize()} LED turned on.")
    else:
        speak(f"{color.capitalize()} LED turned off.")

# LED Chassior/Chaser effect
def led_chassior():
    speak("Starting LED chassior effect.")
    for _ in range(5):  # Run the sequence 3 times
        for color, pin in led_pins.items():
            pin.write(1)
            print(f"{color} ON")
            time.sleep(0.2)
            pin.write(0)
            print(f"{color} OFF")
    speak("LED chassior effect completed.")

# Main function
if __name__ == "__main__":
    wishme()
    while True:
        try:
            command = listen_for_command()
            if command:
                if "red light on" in command:
                    toggle_led("red", 1)
                elif "red light off" in command:
                    toggle_led("red", 0)

                elif "green light on" in command:
                    toggle_led("green", 1)
                elif "green light off" in command:
                    toggle_led("green", 0)

                elif "blue light on" in command:
                    toggle_led("blue", 1)
                elif "blue light off" in command:
                    toggle_led("blue", 0)

                elif "yellow light on" in command:
                    toggle_led("yellow", 1)
                elif "yellow light off" in command:
                    toggle_led("yellow", 0)

                elif "white light on" in command:
                    toggle_led("white", 1)
                elif "white light off" in command:
                    toggle_led("white", 0)

                elif "all lights on" in command:
                    for color in led_pins:
                        toggle_led(color, 1)

                elif "all lights off" in command:
                    for color in led_pins:
                        toggle_led(color, 0)

                elif "chassior" in command or "chaser" in command:
                    led_chassior()

                elif "exit" in command or "stop" in command:
                    speak("Shutting down. Goodbye, Mr Stark.")
                    break

                else:
                    speak("Command not recognized. Please try again.")

        except Exception as e:
            print("Error:", e)
            speak("Something went wrong.")
