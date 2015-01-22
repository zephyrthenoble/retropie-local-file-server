This is a simple Python server that uses the Bottle framework.

Simple instructions:

run `sudo python server.py` to have the server run on port 80, looking in the /home/pi/RetroPie/roms directory.  Any changes to this will require changing the code

Purpose:

It's purpose is to allow one to run this server on a RetroPie, and upload ROMs to it.  This is because EmulationStation makes the Raspberry Pi into a simple to use arcade box, and I didn't want to screw that up by requiring my roommates, people not well versed in Linux, to go though the whole process of starting Xorg, opening a browser, downloading a rom, moving it to the right directory, exiting Xorg, and running EmulationStation.  Instead, they can do it on their own computer, and upload it over the network.
