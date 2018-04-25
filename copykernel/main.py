#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# === This file is part of Calamares - <https://github.com/calamares> ===
#
#   Copyright 2014-2015, Philip Müller <philm@manjaro.org>
#   Copyright 2015-2017, Teo Mrnjavac <teo@kde.org>
#   Copyright 2017, Alf Gaida <agaida@siduction.org>
#   Copyright 2017, Adriaan de Groot <groot@kde.org>
#   Copyright 2017, Gabriel Craciunescu <crazy@frugalware.org>
#
#   Calamares is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Calamares is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Calamares. If not, see <http://www.gnu.org/licenses/>.

import libcalamares
import os
import glob
import shutil

def copykernel(root_mount_point):
    kernels = glob.glob('/cdrom/casper/*vmlinuz*')
    boot_path = os.path.join(root_mount_point,'boot')
    if os.path.exists(boot_path):
        for x in kernels:
            shutil.copy(x,boot_path)
    return None

def run():
    """
    Calls routine with given parameters to modify '/etc/default/grub'.

    :return:
    """
    root_mount_point = libcalamares.globalstorage.value("rootMountPoint")
    return copykernel(root_mount_point)
