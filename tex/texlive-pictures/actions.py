#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os
from distutils.dir_util import copy_tree

WorkDir = "."

def setup():
    # Unpack and prepare files
    for tar_file in shelltools.ls('.'):
        if tar_file.endswith("xz"):
            shelltools.system("tar Jxfv %s" % tar_file)

def build():
    for folder in ["tlpkg"]:
        shelltools.unlinkDir(folder)

def install():
    pisitools.dodir("/usr/share")

    wanteddirs = []
    for file_ in shelltools.ls('.'):
        if shelltools.isDirectory(file_) and not "texmf" in file_:
            wanteddirs.append(file_)

    for folder in wanteddirs:
        pisitools.insinto("/usr/share/texmf-dist", folder)

    if shelltools.can_access_directory("texmf-dist"):
        # Recursively copy on directory on top of another, overwrite duplicate files too
        copy_tree("texmf-dist", "%s/usr/share/texmf-dist" % get.installDIR())

    ## chmod of script files
    script_dir = get.installDIR() + "/usr/share/texmf-dist/scripts"
    if shelltools.can_access_directory(script_dir):
        for root, dirs, files in os.walk(script_dir):
            for name in files:
                shelltools.chmod(os.path.join(root, name), 0755)

    i = "/usr/share/texmf-dist/scripts"

    pisitools.dosym("%s/cachepic/cachepic.tlu" % i, "/usr/bin/cachepic")
    pisitools.dosym("%s/epspdf/epspdftk.tcl" % i, "/usr/bin/epspdftk")
    pisitools.dosym("%s/epspdf/epspdf.tlu" % i, "/usr/bin/epspdf")
    pisitools.dosym("%s/fig4latex/fig4latex" % i, "/usr/bin/fig4latex")
    pisitools.dosym("%s/getmap/getmapdl.lua" % i, "/usr/bin/getmapdl")
    pisitools.dosym("%s/mathspic/mathspic.pl" % i, "/usr/bin/mathspic")
    pisitools.dosym("%s/mkpic/mkpic" % i, "/usr/bin/mkpic")
    pisitools.dosym("%s/petri-nets/pn2pdf" % i, "/usr/bin/pn2pdf")

