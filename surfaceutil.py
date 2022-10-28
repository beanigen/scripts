#! /usr/bin/python3
import os
import sys
import subprocess
from trapdoor import Trapdoor 

config = Trapdoor('surfaceutil')

#fix this shit
resHasBeenSet = config.get('config.resHasBeenSet')
    


session = subprocess.Popen(['echo', '$XDG_SESSION_TYPE'], stdout=subprocess.PIPE)
sessionType = session.stdout.read()
if sessionType == "x11":
    command = 'xrandr'
    modeSet = '--mode'
    rateSet = '--rate'
    rate = '60'
else:
    command = 'wlr-randr'
    modeSet = '--custom-mode'
    rateSet = '@'
    rate = '60'



if resHasBeenSet == '0':
    #nativeResWidth = input("Please enter your native resolution width: ")
    nativeRes = input("Please enter your native resolution: ")
    #nativeResHeight = input("Please enter your native resolution height: ")
    #print(str(nativeResWidth) + 'x' + str(nativeResHeight))
    print(nativeRes)
    config.set('config.resHasBeenSet', '1')
    #config.set('config.nativeResWidth', int(nativeResWidth))
    config.set('config.nativeRes', nativeRes)
    #config.set('config.nativeResHeight', int(nativeResHeight))
    #print(f"Your native resolution has been set to {nativeResWidth}x{nativeResHeight}")
    print(f"Your native resolution has been set to {nativeRes}")
    sys.exit()


try:
    arg1 = str(sys.argv[1])

except IndexError:
    print("You need to specify an argument!")
    sys.exit()


if arg1 == "profilecheck":
    cmd = subprocess.Popen(['surface', 'profile', 'get'], stdout=subprocess.PIPE)
    cmdOut = str(cmd.stdout.read())
    print(f"Your profile is {cmdOut}")
elif arg1 == "setres":
    subprocess.Popen([f'{command}', '--output', 'eDP-1', f'{modeSet}', f'{sys.argv[2]}', f'{rateSet}', f'{rate}'])
    print("Resolution set to 1080p, run surfaceutil restoreres to restore resolution to native")
elif arg1 == "restoreres":
    subprocess.Popen([f'{command}', '--output', 'eDP-1', f'{modeSet}', config.get('config.nativeRes'), f'{rateSet}', f'{rate}'])
    print("Resolution restored")
elif arg1 == "-h" or "--help":
    print("list of commands \nprofilecheck - checks performance profile, requires surface-control\nsetres [resolution] - uses xrandr or wlr-randr to change resolution\nrestoreres - sets your resolution back to the one specified during first run")
