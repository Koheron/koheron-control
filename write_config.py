from koheron_control import Controller

port="/dev/ttyUSB0"
ctl = Controller(port=port)

config = {
    "ldelay": 3000.0,
    "lason": 0,
    "ilaser": 200.0,
    "rtset": 11000.0
}

for param in config:
    ctl.set(param, config[param])

for param in config:
    print(f"{param.upper()} : {ctl.get(param)}")

user_input = input("Save configuration? (yes/no): ")
if user_input.lower() == "yes":
    print(ctl.set("save"))

