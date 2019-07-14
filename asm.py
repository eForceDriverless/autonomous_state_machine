import time

class State:
    def __init__(self):
        self.state = "as_off"
        self.ts = "on"
        self.r2d = "on"
        self.sa = "unavailable"
        self.sb = "unavailable"
        self.ebs = "dont_care"
        self.assi = "off"

    def change_state(self,next_state):
        self.state = next_state
        if next_state == "manual_driving":
            self.ts = "on"
            self.r2d = "on"
            self.sa = "unavailable"
            self.sb = "unavailable"
            self.ebs = "unavailable"
            self.assi = "off"
        elif next_state == "as_off":
            self.ts = "off"
            self.r2d = "off"
            self.sa = "unavailable"
            self.sb = "unavailable"
            self.ebs = "dont_care"
            self.assi = "off"
        elif next_state == "as_ready":
            self.ts = "on"
            self.r2d = "off"
            self.sa = "available"
            self.sb = "engaged"
            self.ebs = "armed"
            self.assi = "yellow_cont"
        elif next_state == "as_driving":
            self.ts = "on"
            self.r2d = "on"
            self.sa = "available"
            self.sb = "available"
            self.ebs = "armed"
            self.assi = "yellow_flash"
        elif next_state == "as_emergency":
            self.ts = "off"
            self.r2d = "off"
            self.sa = "dont_care"
            self.sb = "dont_care"
            self.ebs = "activated"
            self.assi = "blue_flash"
        elif next_state == "as_finished":
            self.ts = "off"
            self.r2d = "off"
            self.sa = "dont_care"
            self.sb = "dont_care"
            self.ebs = "activated"
            self.assi = "blue_cont"

def main():
    formula_state = State()
    print "Program se vypina stiskem 'x', zacinas v AS off"
    while True:
        print " "
        print "Formule je ve stavu: "+formula_state.state
        if formula_state.state == "manual_driving":
            choice = raw_input("Pro AS off 'o'")
            if choice == "o":
                formula_state.change_state("as_off")
            elif choice == "x":
                return 0

        elif formula_state.state == "as_off":
            choice = raw_input("Pro Manual driving stiskni 'm', pro AS ready stiskni 'r'")
            if choice == "m":
                formula_state.change_state("manual_driving")
            elif choice == "r":
                formula_state.change_state("as_ready")
            elif choice == "x":
                return 0

        elif formula_state.state == "as_ready":
            choice = raw_input("Pro AS off stiskni 'o', pro AS Driving 'd', pro AS emergency 'e'")
            if choice == "o":
                formula_state.change_state("as_off")
            elif choice == "d":
                formula_state.change_state("as_driving")
            elif choice == "e":
                formula_state.change_state("as_emergency")
                time.sleep(5)
            elif choice == "x":
                return 0

        elif formula_state.state == "as_driving":
            choice = raw_input("Pro AS emergency stiskni 'e', pro AS finished 'f'")
            if choice == "m":
                formula_state.change_state("as_emergency")
            elif choice == "f":
                formula_state.change_state("as_finished")
            elif choice == "x":
                return 0

        elif formula_state.state == "as_emergency":
            choice = raw_input("Pro AS off stiskni 'o'")
            if choice == "o":
                formula_state.change_state("as_off")
            elif choice == "x":
                return 0

        elif formula_state.state == "as_finished":
            choice = raw_input("Pro AS off stiskni 'o', pro AS emergency 'e'")
            if choice == "o":
                formula_state.change_state("as_off")
            elif choice == "e":
                formula_state.change_state("as_emergency")
            elif choice == "x":
                return 0

if __name__ == '__main__':
    main()
