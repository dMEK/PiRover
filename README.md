# PiRover
Code for a Raspberry Pi driven Rover


This project is built off the Make magazine
RaspPi controlled Robot book by Wolfram Donat
And is to familiarise myself woth using both
The Pi and Python for robotic control

It covers DC and Servo Motor control, GPS and navigation
it uses Raspian libraries GPIO and gpsd, which are in the standard repository for Raspian
and servoBlaster by Richard Hirst

A lot of the original code was very ugly with redundancies
The code has been cleaned up somewhat, but is still untested as of 26/3/2017


EDIT: having now worked through Wolfram Donat's book, it explains some of the basics fairly well, 
but the desctiption of interfacing and functioning of the hardware is packing and in some cases innaccurate
And the code is quite buggy, having found numerous errors in the code while working through it
It is also decidedly ugly, not setting constants for pins, and repeating the entire control code block 
In the final script - once with GPS and once without
More detailed explenation of the use of Python Modules would also have helped in the clarity of this book
