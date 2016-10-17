#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
QT front end to 'dd' and 'pv' for writing an image file to a USB
mass storage device.

:author: Martin Grønholdt (deadbok)
'''

from PyQt5 import QtCore, uic
import os
import sys

from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog


_version_ = '0.0.4'
_root = os.path.abspath(os.path.dirname(__file__))


class MainDialog(QDialog):
    '''
    Main window created from a QT designer .ui file.
    '''
    def __init__(self):
        super(MainDialog, self).__init__()

        # Set up the user interface from Designer.
        uic.loadUi(os.path.join(_root, 'ui/qtdd.ui'), self)

        self.isoBrowseButton.clicked.connect(self.browseIso)

        for devs in os.listdir('/dev/disk/by-path/'):
            # Only show usb disks and not partitions
            if 'usb' in devs and 'part' not in devs:
                path = os.path.join('/dev/disk/by-path/', devs)
                link = os.readlink(path)
                # Get the label of the first partition to help the user id the
                # device
                for label in os.listdir('/dev/disk/by-label'):
                    label_path = os.path.join('/dev/disk/by-label', label)
                    label_link = os.readlink(label_path)
                    if label_link.startswith(link):
                        link += ' (' + label.replace('\\x20', ' ') + ')'
                print('USB device: ' + '/dev/' + os.path.basename(link))
                self.usbDeviceSelect.addItem('/dev/' + os.path.basename(link))

    def browseIso(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,
                                                  "QFileDialog.getOpenFileName()",
                                                  "",
                                                  "ISO Files (*.iso);;All Files (*)",
                                                  options=options)
        if fileName:
            print('Image file: ' + fileName)
            self.isoPath.setText(fileName)
