#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def install():
    shelltools.system("./install.sh")
    pisitools.remove("/usr/share/cows/mech-and-cow")
    pisitools.dodoc("LICENSE", "README*")