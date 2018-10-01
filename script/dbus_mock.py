#!/usr/bin/env python

import atexit
import os
import subprocess
import sys

from dbusmock import DBusTestCase

from lib.config import is_verbose_mode

def stop():
    print('In dbus_mock stop')
    DBusTestCase.stop_dbus(DBusTestCase.system_bus_pid)
    print('In dbus_mock stop, stopped system bus')
    DBusTestCase.stop_dbus(DBusTestCase.session_bus_pid)
    print('In dbus_mock stop, stopped session bus')

def start():
    log = sys.stdout

    DBusTestCase.start_system_bus()
    DBusTestCase.spawn_server_template('logind', None, log)

    DBusTestCase.start_session_bus()
    DBusTestCase.spawn_server_template('notification_daemon', None, log)

if __name__ == '__main__':
    start()
    try:
        print 'About to call '+ sys.argv
        subprocess.check_call(sys.argv[1:])
        print 'Done calling ' + sys.argv
    finally:
        stop()
