import keyboard
import time

print('Author: Aden M\nLanguage: Python\n\nName: Send Custom Repeating Text\nImportant Information: Use F6 to pause the script\n')

paused = 0
pauseKey = 'F6'
yesorno = 'n'
predefinedVar = None

if yesorno == 'y':
    predefinedVar = input('\nplease specify the 1st Message Part: ')
elif yesorno == 'n':
    predefinedVar = None

if yesorno == 'y':
    input1 = input('\nplease specify the 2nd Message Part: ')
elif yesorno == 'n':
    input1 = input('Please type the message you would like to send: ')



yesorno3 = None

repeatVar = 9999999999*9999999999


yesorno3 = input('\nWould you like to set a custom repeat number? Default is infinity. (y/n): ')

if yesorno3 == 'y':
    repeatVar = input('\nPlease specify the custom repeat amount (Use a integer, example 2): ')
    converted1 = (int(repeatVar)+ 1)

if yesorno3 == 'n':
    converted1 = 9999999999*9999999999

settime = input('\nHow many seconds would you like in between each message? (Decimals Work): ')

if yesorno == 'y':
    if yesorno3 == 'n':
        print(f'\n1st Message is: {predefinedVar}\nMessage is set to: {input1}\nTime between is: {settime}\nAmount Repeating is: infinite')
    elif yesorno3 == 'y':
        print(f'\n1st Message is: {predefinedVar}\nMessage is set to: {input1}\nTime between is: {settime}\nAmount Repeating is: {repeatVar}')

elif yesorno == 'n':
    if yesorno3 == 'n':
        print(f'\n1st Message is off\nMessage is set to: {input1}\nTime between is: {settime}\nAmount Repeating is: infinite')
    elif yesorno3 == 'y':
        print(f'\n1st Message is off\nMessage is set to: {input1}\nTime between is: {settime}\nAmount Repeating is: {repeatVar}')


    print('\nStarting in:')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)

    def togglePaused():
        global paused
        if paused == 0:
            paused = 1
        else:
            paused = 0

    def typeMessage(message):
        keyboard.write(message)

    inte = 1
    settimec = (float(settime))

    def main():
        keyboard.add_hotkey(pauseKey,togglePaused)
        x = 1
        while True:  
            while x < converted1:   
                time.sleep(1)
                if paused == 0:
                    time.sleep (settimec)
                    if yesorno == 'y':
                        typeMessage(f"{predefinedVar} {input1}")
                    elif yesorno == 'n':
                        typeMessage(f'{input1}')
                    keyboard.send('enter')
                    print(f"Repeating: {x}")
                    x += 1

                else:
                    print("Paused, press "+pauseKey+" to continue.")
                    keyboard.wait(hotkey=pauseKey)

if __name__ == "__main__":
    main()
