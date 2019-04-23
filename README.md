# xmame-olpc

## TL;DR
[DOWNLOAD THE RPM HERE](https://github.com/fernandosanchezmunoz/xmame-olpc/blob/master/rpmbuild/RPMS/armv7hl/xmame-0.106-1.armv7hl.rpm) (This is a direct link. You may want to right-click and "Save as")

[**MAME**](www.mamedev.org) is a multi-purpose emulation framework that allows classic arcade machines to run in standard computers.

MAME’s purpose is to preserve decades of software history. As electronic technology continues to rush forward, MAME prevents this important "vintage" software from being lost and forgotten. This is achieved by documenting the hardware and how it functions. The source code to MAME serves as this documentation. The fact that the software is usable serves primarily to validate the accuracy of the documentation (how else can you prove that you have recreated the hardware faithfully?). Over time, MAME (originally stood for Multiple Arcade Machine Emulator) absorbed the sister-project MESS (Multi Emulator Super System), so MAME now documents a wide variety of (mostly vintage) computers, video game consoles and calculators, in addition to the arcade video games that were its initial focus.

[**XMAME**](http://freshmeat.sourceforge.net/projects/xmame) is the X11/Unix port of MAME.

[**One Laptop Per Child**](www.laptop.org) is a non-profit initiative established with the goal of transforming education for children around the world; this goal was to be achieved by creating and distributing educational devices for the developing world, and by creating software and content for those devices.

The [**OLPC 1.75**](http://wiki.laptop.org/go/XO-1.75) is a laptop designed, manufactured and shipped by OLPC, using an ARM processor. XO-1.75 is designed around the Armada 610 system on a chip, whichfeatures an 800 Mhz  Marvell Sheeva ARM (ARMv7 architecture compatible). 

MAME and XMAME are portable, and the OLPC laptop provides a nice form factor for gaming given its size and the joystick controls included around the screen. 

This repository provides a pre-compiled version of xmame for the OLPC laptop already prepared to be installed and run on the platform with minimal effort. This has been tested to run correctly on  an OLPC 1.75 unit running OLPC Linux version [13.2.10-22](http://download.laptop.org/xo-1.75/os/official/13.2.10-22/). Instructions on how to upgrade the OLPC version of Linux can be found [here](http://wiki.laptop.org/go/XO-1.75#Upgrading_Linux)

# Installation

Switch into the GNOME "traditional linux desktop" mode. You can  do that by going into "Settings" by hovering your cursor over the XO figure. Afterwards, find the option to "Switch Desktop".

Once in GNOME [DOWNLOAD THE RPM HERE](https://github.com/fernandosanchezmunoz/xmame-olpc/blob/master/rpmbuild/RPMS/armv7hl/xmame-0.106-1.armv7hl.rpm) and install either by clicking on it, or by executing `yum install ` from a terminal. For example, if the RPM file is in the `/home/olpc/Downloads` folder:

`
sudo yum install -y /home/olpc/Downloads/xmame-0.106-1.armv7hl.rpmrpm
`

# Usage

After installation, there should be a new Desktop icon called `xmame`. Simply clicking on it will launch a terminal showing the games available in the system. Enter the name of a game to launch it.

`/usr/bin/xmame` is simply a wrapper script calling `/usr/bin/xmame.x11` with a number of options that I've found convenient. Feel free to adapt it or just call `xmame.x11` directly.

# Credits

Most of the guidance around compiling xmame for ARM has been found in [this blog post](https://www.anavi.org/article/177/) by Leon Anavi. Thanks!
I got to know the OLPC project, got involved in it, and got inspiration from Martin Langhoff and Roberth H. Hacker. Thanks!

# ENJOY!

