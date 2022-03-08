
<h1 align="center">
  <br>
  AntiLogOut
  <br>
</h1>

<h4 align="center">Raspberry Pi Pico (RP2040) HID input to simulate sporadic mouse clicks using <a href="https://circuitpython.org/" target="_blank">CircuitPython</a>.</h4>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#ideas">Ideas</a> •
  <a href="#license">License</a>
</p>

## Overview

Code to load onto a Raspberry Pi Pico which will produce mouse clicks and move the mouse.

## How To Use

* Download <a href="https://circuitpython.org/" target="_blank">CircuitPython</a>
* Plug your Raspberry Pi Pico into your PC <b> while holding the BOOTSEL button </b> (once the Raspberry Pi Pico appears in Explorer you can let go of the button)
* Drag the CircuitPython .UF2 file to your Raspberry Pi Pico in Explorer
* Download and install <a href="https://thonny.org/" target="_blank">Thonny</a>
* Open Thonny
* Select CircuitPython in the bottom right of your Thonny window
* Install the adafruit_hid library via Tools>Manage Packages
* Copy the contents of code.py from this repository to code.py on your Pi Pico and hit save
* You can now run the code with F5 and stop it with Ctrl+F2 (it can be hard to click the buttons while it is running because the code takes control of the mouse pointer!)

## Credits

This project relies on the following:

- [CircuitPython](https://circuitpython.org/)
- [adafruit_hid](https://docs.circuitpython.org/projects/hid/en/latest/)
- [Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

## Ideas

Now you have downloaded this code and tried it, what will you use it for? Here are some ideas:
* use it to stop yourself being logged out of your favourite game when you go for dinner
* secretly attach it to the computer of a friend or coworker so they think their computer is haunted(!)
* make some art in Paint
* modify it to perform key presses instead of or as well as mouse clicks
* change the time delay to be longer or shorter

## License

MIT

---
