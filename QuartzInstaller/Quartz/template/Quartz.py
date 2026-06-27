import os
import time
import random

BASE = os.path.dirname(os.path.abspath(__file__))
PROGRAM = os.path.join(BASE, "TheThing.qrtz")

slots = [0, 0, 0, 0, 0]

slot = 0

functions = {}

RED = "\033[31m"
END = "\033[0m"

class QuartzError(Exception):
    pass

def forward():
    global slot
    if slot == 4:
        slot = 0
    else:
        slot = slot + 1

def backward():
    global slot
    if slot == 0:
        slot = 4
    else:
        slot = slot - 1

def reduce():
    global slot, slots
    slots[slot] = slots[slot] - 1

def increase():
    global slot, slots
    slots[slot] = slots[slot] + 1

def takeInput(way):
    global slot, slots
    a = input("> ")
    try:
        a = int(a)
        if way == "sub":
            slots[slot] = slots[slot] - a
        elif way == "add":
            slots[slot] = slots[slot] + a
        elif way == "ovv":
            slots[slot] = a
    except ValueError:
        raise QuartzError("Failed to convert input to integer")
    
def add(arg):
    global slots
    try:
        a, b = arg.split(":")
        a = int(a)
        b  = int(b)
        a = slots[a]
        b = slots[b]
        return a + b
    except ValueError:
        raise QuartzError("Failed to convert input to integer")
    except IndexError:
        raise QuartzError("Referenced slot does not exist")
    
def sub(arg):
    global slots
    try:
        a, b = arg.split(":")
        a = int(a)
        b  = int(b)
        a = slots[a]
        b = slots[b]
        return a - b
    except ValueError:
        raise QuartzError("Failed to convert input to integer")
    except IndexError:
        raise QuartzError("Referenced slot does not exist")
    
def parse(token):
    global slots, slot, functions
    if token == "~+":
        forward()
    elif token == ",,,":
        print(slots[slot])
    elif token == "~-":
        backward()
    elif token == "&*":
        takeInput("ovv")
    elif token == "+":
        increase()
    elif token == "-":
        reduce()
    elif token.startswith("%"):
        token = token.removeprefix("%")
        for c in token:
            if c == "+":
                increase()
            elif c == "-":
                reduce()
            else:
                raise QuartzError("Unsupported operator")
    elif token == "&*+":
        takeInput("add")
    elif token == "&*-":
        takeInput("sub")
    elif token.startswith("...") and token.endswith("..."):
        try:
            token = token.removesuffix("...")
            token = token.removeprefix("...")
            seconds = int(token)
            time.sleep(seconds)
        except ValueError:
            raise QuartzError("Failed to convert input to integer")
    elif token.startswith(",,,") and token.endswith(",,,"):
        token = token.removesuffix(",,,")
        token = token.removeprefix(",,,")
        argument = token
        if ":" in argument:
            print(add(argument))
        else:
            try:
                argument = int(argument)
                print(slots[argument])
            except ValueError:
                raise QuartzError("Failed to convert input to integer")
            except IndexError:
                raise QuartzError("Referenced slot does not exist")
    elif token.startswith("~>"):
        try:
            token = token.removeprefix("~>")
            a, b = token.split(":", 1)
            b = b.strip()
            a = int(a)
            while slots[slot] != a:
                parse(b)
                forward()
        except ValueError:
            raise QuartzError("Failed to convert input to integer")
        except IndexError:
            raise QuartzError("Expected colon")
    elif token.startswith("@"):
        try:
            token = token.removeprefix("@")
            name, func = token.split(":", 1)
            instructions = func.split("/")
            functions[name] = instructions
        except ValueError:
            raise QuartzError("Expected colon")
    elif token.startswith("$"):
        func = token.removeprefix("$")
        if func in functions:
            instructions = functions[func]
            for instr in instructions:
                instr = instr.strip()
                parse(instr)
        else:
            raise QuartzError(f"{func} is undefined")
    elif token.startswith("#"):
        token = token.removeprefix("#")
        try:
            token = int(token)
            slots[slot] = token
        except ValueError:
            raise QuartzError("Failed to convert input to integer")
    elif token.startswith("^"):
        token = token.removeprefix("^")
        try:
            b = int(token)
            rng = random.randint(1, b)
            slots[slot] = rng
        except ValueError:
            raise QuartzError("Failed to convert input to integer")
    elif token.startswith("?"):
        token = token.removeprefix("?")
        if not ":" in token:
            raise QuartzError("Expected colon")
        try:
            a, b = token.split(":", 1)
            a = int(a)
            if slots[slot] == a:
                parse(b)
        except ValueError:
            raise QuartzError("Failed to convert input to integer")
    elif token.startswith("!"):
        pass
    else:
        raise QuartzError(f"Unkown instruction: {token}")


with open(PROGRAM, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if "|" in line:
            tokens = line.split("|")
            for token in tokens:
                token = token.strip()
                if not token:
                    continue
                try:
                    parse(token)
                except QuartzError as e:
                    print(f"{RED}{e}{END}")
        else:
            if not line:
                continue
            try:
                parse(line)
            except QuartzError as e:
                print(f"{RED}{e}{END}")