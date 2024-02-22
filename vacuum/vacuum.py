import curses
import random
import threading
import time

class Vacuum:

    def __init__(self):
        self.position = 0
        self.world = {0: False, 1: False}
    
    def moveLeft(self,stdscr):
        if(self.position > 0):
            self.position -= 1
            stdscr.addstr(3, 0, "ASPIRADORA SE MOVIO A LA IZQUIERDA")
        else:
            stdscr.addstr(3, 0, "ASPIRADORA NO HACE NADA")
    
    def moveRight(self,stdscr):
        if(self.position < 1):
            self.position += 1
            stdscr.addstr(3, 0, "ASPIRADORA SE MOVIO A LA DERECHA")
        else:
            stdscr.addstr(3, 0, "ASPIRADORA NO HACE NADA")
    
    def dirtyARoom(self,room):
        self.world[room] = True        
    
    def cleanARoom(self,stdscr):
        self.world[self.position] = False
        stdscr.addstr(3, 0, "ASPIRADORA LIMPIO EL CUARTO")        
    
    def doNothing(self,stdscr):
        stdscr.addstr(3, 0, "ASPIRADORA NO HACE NADA")        

    def dumbMode(self,stdscr):
        #Set a random action
        actions = ["left","right","clean","nothing"]
        action = random.choice(actions)
        if action == "left":
            self.moveLeft(stdscr)
        elif action == "right":
            self.moveRight(stdscr)
        elif action == "clean":
            self.cleanARoom(stdscr)
        else:
            self.doNothing(stdscr)

    def smartMode(self,stdscr):
        #Find the trash and try to clean
        #Prioritize cleaning the room
        #Only for 2 rooms
        if self.world[0] or self.world[1]:
            if self.world[self.position]:
                self.cleanARoom(stdscr)
            elif self.position == 0:
                self.moveRight(stdscr)
            else:
                self.moveLeft(stdscr)
        else:
            self.doNothing(stdscr)
    
    def printVacuum(self):
        roomsToPrint = ""
        roomPosition = 0
        vacuumToPrint = ""
        for room,value in self.world.items():
            roomValue = "0"
            if value:
                roomValue = "1"

            roomsToPrint = roomsToPrint + "|" + roomValue
            if self.position == roomPosition:
                vacuumToPrint += "|" + "*"
            else:
                vacuumToPrint += "|" + " "
            roomPosition +=1

        vacuumToPrint += "|"
        roomsToPrint += "|"
            
        return (vacuumToPrint + "\n" + roomsToPrint)
        


exit_event = threading.Event()

def setVacuum(stdscr, vacuum):
    while not exit_event.is_set():
        stdscr.clear()
        vacuum.dumbMode(stdscr)
        #vacuum.smartMode(stdscr)
        stdscr.addstr(0, 0, vacuum.printVacuum())
        stdscr.refresh()
        time.sleep(1)

def setToDirty(stdscr, vacuum):
    while not exit_event.is_set():
        stdscr.addstr(4, 0, "Ingrese el numero de cuarto a ensuciar (1 o 2): ")
        stdscr.refresh()
        roomToDirty = stdscr.getch()  # GET ENTRY 1 OR 2
        roomToDirty = chr(roomToDirty)
        if roomToDirty.isdigit() and int(roomToDirty) in [1, 2]:
            vacuum.dirtyARoom(int(roomToDirty) - 1)
        time.sleep(1)

def main(stdscr):
    curses.curs_set(0)  # HIDE CURSOR

    vacuum = Vacuum()

    #CREATE THREADS
    vacuum_thread = threading.Thread(target=setVacuum, args=(stdscr, vacuum))
    dirty_thread = threading.Thread(target=setToDirty, args=(stdscr, vacuum))

    #INIT THREADS
    vacuum_thread.start()
    dirty_thread.start()

    try:
        # WAIT TIL q TO EXIT
        while True:
            char = stdscr.getch()
            if char == ord('q'):
                exit_event.set()  # EXIT
                break
    except KeyboardInterrupt:
        pass

    vacuum_thread.join()
    dirty_thread.join()

curses.wrapper(main)
    
