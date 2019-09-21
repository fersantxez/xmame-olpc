# xmame-olpc

### TL;DR
[DOWNLOAD THE RPM HERE](https://github.com/fernandosanchezmunoz/xmame-olpc/blob/master/rpmbuild/RPMS/armv7hl/xmame-0.106-1.armv7hl.rpm) (This is a direct link. You may want to right-click and "Save as" in your "Downloads" folder)

## Intro

This repository provides a pre-compiled version of xmame for the XO 1.75 laptop already prepared to be installed and run on the platform with minimal effort. This has been tested to run correctly on an XO 1.75 unit running OLPC Linux version [13.2.10-22](http://download.laptop.org/xo-1.75/os/official/13.2.10-22/). Other versions may run as well, but haven't been tested. Instructions on how to upgrade the OLPC version of Linux can be found [here](http://wiki.laptop.org/go/Release_notes/13.2.10#XO-1.75)

[**MAME**](www.mamedev.org) is a multi-purpose emulation framework that allows classic arcade machines to run in standard computers.

[**One Laptop Per Child**](www.laptop.org) is a non-profit initiative established with the goal of transforming education for children around the world; this goal was to be achieved by creating and distributing educational devices for the developing world, and by creating software and content for those devices.

The [**OLPC XO 1.75**](http://wiki.laptop.org/go/XO-1.75) is a laptop designed, manufactured and shipped by OLPC, using an ARM processor. XO-1.75 is designed around the Armada 610 system on a chip, which features an 800 Mhz Marvell Sheeva ARM processor (ARMv7 architecture compatible). 

MAME is portable, and it was ported to Unix/X11 under the name XMAME -- which makes it possible to run on the XO 1.75 laptop. The XO 1.75 provides a nice form factor for gaming given its size and the joystick controls included around the screen. 

## Installation

Switch into the GNOME "traditional linux desktop" mode. You can  do that by going into "My Settings" by hovering your cursor over the XO figure. Afterwards, find the option to "Switch Desktop" at the bottom.

Once in GNOME, launch the web browser ("Applications" menu on the top left, "Internet" and "Epiphany Web Browser"), and [DOWNLOAD THE RPM FROM THE "DOWNLOAD" LINK HERE](https://github.com/fernandosanchezmunoz/xmame-olpc/blob/master/rpmbuild/RPMS/armv7hl/xmame-0.106-1.armv7hl.rpm). OLPC may want to open it with "Archive Manager", just cancel that. Open up a Terminal ("Applications" menu, "System Tools", "Terminal"), and install with:

`
sudo yum install -y /home/olpc/Downloads/xmame-0.106-1.armv7hl.rpm
`

## Usage

After installation, there should be a new Desktop icon called `xmame`. Simply clicking on it will launch a terminal showing the games available in the system. Enter the name of a game to launch it.

*NOTE*: `/usr/bin/xmame` is simply a wrapper script calling `/usr/bin/xmame.x11` with a number of options that I've found convenient. Feel free to adapt it or just call `xmame.x11` directly if you feel like tickling with how this works by default.

If you haven't used MAME before, here are some of the basic keys:

- 6 -- "insert coin"
- 1 -- "1 player"
- 2 -- "2 players"
- TAB -- "Advanced Menu"

The XO 1.75's keypad and buttons can be used to control Player 1.

## Screenshots

![Galaga](/pics/galaga.jpg)
![Robocop](/pics/robocop.jpg)
![Tehkan World Cup](/pics/tehkanwc.jpg)
![Punisher](/pics/finalfight.jpg)

## Content

If you are looking for a way to add additional content to the emulator, [this comment](https://github.com/fernandosanchezmunoz/xmame-olpc/issues/1) suggests an additional package to install.

## Credits

Most of the guidance around compiling xmame for ARM has been found in [this blog post](https://www.anavi.org/article/177/) by Leon Anavi.


I got to know the OLPC project thanks to the generosity and contagious enthusiasm of Martin Langhoff and Robert H. Hacker. 

# ENJOY!

