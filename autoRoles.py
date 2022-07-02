from pynput.keyboard import Key, Controller
import time

# Data is set according to the May '21 CWL week.

inputClan = input("Enter the Clan Name: ")

parallaxListMembers = [
    "Raanjal",
    "Tempest",
    "Unicorn✨",
    "Supachris210",
    "Kryptokipps13",
    "Zemut",
    "Batman",
    "tomとうふ",
    "Hyper ghost",
    "aloha/hassan",
    "Moishe",
    "Hulk",
    "Pascal",
    "AC",
    "Zen",
    "Waleed",
    "King Castle",
    "Pahk&nicholes",
    "Tempest",
    "Crossbones",
    "Triece",
    "ART3MIS",
    "Fardin",
    "2PiAreSquared",
    "Ericsharp",
    "Ace",
    "Brokenwind",
    "Xejo",
    "DeviousQB",
    "Peter",
    "Minibombers",
]


piratesListMembers = [
    "Hussein dia",
    "Apoptosis",
    "CLAN KING",
    "OMNI KING",
    "Peter",
    "Draken",
    "Dabombers",
    "kn0b",
    "Hulk",
    "Proto",
    "Dembones",
    "hjmmmmmmmmm",
    "wlupike",
    "STREET KING",
    "AC",
    "Dead Pixels",
    "Ace",
]

royalsListMembers = [
    "Steve-0",
    "Moishe",
    "Ali5",
    "Vampire13b",
    "Lord ArcanE™",
    "Dembones",
    "StarThief",
    "Grim",
    "Chaotyk Blood",
    "Tempest",
    "EliteBanter",
    "Crispee Chicken",
    "Naval Minister",
    "Atharva.26",
    "Shalaby",
    "Ubdynoz",
    "Kippster",
    "King Jeffery",
    "Park Music",
    "Tempest",
    "Agelastic",
    "Unicorn✨",
    "Chalkless",
    "b0nk",
    "Supa",
    "Vedant#1",
    "Lars",
    "Shot1923",
    "Vampire 13b",
    "Mini Clay.FBoom",
    "Emma",
    "Mike",
]

if inputClan == "parallax":
    print("Auto-type starts in 7 seconds...")
    time.sleep(7)
    for member in parallaxListMembers:
        text = "?role custom {} +Parallax CWL".format(member)

        keyboard = Controller()

        keyboard.type(text)

        keyboard.press(Key.enter)

        keyboard.release(Key.enter)

        time.sleep(10)
if inputClan == "pirates":
    print("Auto-type starts in 7 seconds...")
    time.sleep(7)
    for member in piratesListMembers:
        text = "?role custom {} +Pirates CWL".format(member)

        keyboard = Controller()

        keyboard.type(text)

        keyboard.press(Key.enter)

        keyboard.release(Key.enter)

        time.sleep(10)
if inputClan == "royals":
    print("Auto-type starts in 7 seconds...")
    time.sleep(7)
    for member in royalsListMembers:
        text = "?role custom {} +Royal Pirates CWL".format(member)

        keyboard = Controller()

        keyboard.type(text)

        keyboard.press(Key.enter)

        keyboard.release(Key.enter)

        time.sleep(10)
exit(0)
