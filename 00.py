    import threading


try:
    def Alarm():
        while True:
           print("Alarm is done!")
           time.sleep(300)
    t1 = threading.Thread(target=hello_world)
    t1.start()
    while True:
       print('in loop')
       time.sleep(1)
     