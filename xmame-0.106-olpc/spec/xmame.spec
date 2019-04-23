###############################################################################
# Spec file for xmame for OLPC 1.75 
################################################################################
#
Summary: Multi-Arcade Machine Emulator for the OLPC 1.75 platform
Name: xmame
Version: 0.106
Release: 1
License: GPL
URL: http://www.mamedev.org
Group: Games
Packager: Fernando Sanchez
Requires: alsa-oss
BuildRoot: ~/rpmbuild/

%description
Multi-Arcade Machine Emulator for the OLPC 1.75 platform

%prep
################################################################################
# Create the build tree and copy the files from the development directories    #
# into the build tree.                                                         #
################################################################################
echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
mkdir -p $RPM_BUILD_ROOT/usr/local/share/utils

cp ../../xmame-0.106-olpc/xmame.x11 $RPM_BUILD_ROOT/usr/local/bin
cp ../../xmame-0.106-olpc/xmame $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/home/olpc/.xmame
mkdir -p $RPM_BUILD_ROOT/home/olpc/Desktop
cp -R ../../xmame-0.106-olpc/roms $RPM_BUILD_ROOT/home/olpc/.xmame
cp -R ../../xmame-0.106-olpc/cfg $RPM_BUILD_ROOT/home/olpc/.xmame
cp ../../xmame-0.106-olpc/mame-icon.png $RPM_BUILD_ROOT/home/olpc/.xmame/mame-icon.png
cp ../../xmame-0.106-olpc/xmame.desktop $RPM_BUILD_ROOT/home/olpc/Desktop/xmame.desktop
cp ../../xmame-0.106-olpc/license/* $RPM_BUILD_ROOT/usr/local/share/utils
cp ../../xmame-0.106-olpc/spec/* $RPM_BUILD_ROOT/usr/local/share/utils

exit

%files
%attr(0755, root, root) /usr/local/bin/*
%attr(0755, olpc, olpc) /home/olpc/.xmame/*
%attr(0655, root, root) /usr/local/share/utils/*
%attr(0755, olpc, olpc) /home/olpc/Desktop/xmame.desktop

%pre

%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT/usr/local/bin
rm -rf $RPM_BUILD_ROOT/usr/local/share/utils
rm -rf $RPM_BUILD_ROOT/home/olpc/

%changelog
* Mon Apr 22 2019 Fernando Sanchez <fernandosanchezmunoz@gmail.com>
  - Initial release with precompiled binary 
