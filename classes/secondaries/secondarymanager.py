from classes.secondaries.secondary import Secondary
import random

class SecondaryManager:
    def __init__(self, number_of_secondaries):
        self.discarded_secondaries = []
        self.available_secondaries = []

        self.current_seconaries = []
        self.number_of_secondaries = number_of_secondaries

        self.populate_secondaries()


    def populate_secondaries(self):
        self.available_secondaries.append(Secondary("AREA DENAIL", "some long text", True))
        self.available_secondaries.append(Secondary("ASSASSINATION", "some long text", True))
        self.available_secondaries.append(Secondary("A TEMPTING TARGET", "some long text", True))
        self.available_secondaries.append(Secondary("BEHIND ENEMY LINES", "some long text", True))
        self.available_secondaries.append(Secondary("BRING IT DOWN", "some long text", True))
        self.available_secondaries.append(Secondary("CAPTURE ENEMY OUTPUST", "some long text", True))
        self.available_secondaries.append(Secondary("CLEANSE", "some long text", True))
        self.available_secondaries.append(Secondary("DEFEND STRONGHOLD", "some long text", False))
        self.available_secondaries.append(Secondary("DEPLOY TELEPORT HOMER", "some long text", True))
        self.available_secondaries.append(Secondary("ENGAGE ON ALL FRONTS", "some long text", True))
        self.available_secondaries.append(Secondary("EXTEND BATTLE LINES", "some long text", True))
        self.available_secondaries.append(Secondary("INVESTIGATE SIGNALS", "some long text", True))
        self.available_secondaries.append(Secondary("NO PRISONERS", "some long text", True))
        self.available_secondaries.append(Secondary("OVERWHELMING FORCE", "some long text", True))
        self.available_secondaries.append(Secondary("SECURE NO MAN'S LAND", "some long text", True))
        self.available_secondaries.append(Secondary("STORM HOSTILE OBJECTIVE", "some long text", False))

    def drawSecondary(self):
        if len(self.current_seconaries) == self.number_of_secondaries:
            return

        while True:
            random_index = random.randint(0, len(self.available_secondaries) - 1)

            if self.available_secondaries[random_index].getIsAvailableTurnOne():
                self.current_seconaries.append(self.available_secondaries.pop(random_index))
                break

    def discardSecondary(self, discard_index):
        if discard_index > len(self.current_seconaries):
            return

        self.discarded_secondaries.append(self.current_seconaries.pop(discard_index))