# -*- coding: utf-8 -*-
#
# This file is part of the WeatherUnderground project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" WeatherUnderground class access weather data

WeatherUnderground is a Python class to read the weather information from 
the Weather Underground site - https://www.wunderground.com/
"""

# PyTango imports
import PyTango
from PyTango import DebugIt
from PyTango.server import run
from PyTango.server import Device, DeviceMeta
from PyTango.server import attribute, command
from PyTango.server import device_property
from PyTango import AttrQuality, DispLevel, DevState
from PyTango import AttrWriteType, PipeWriteType
# Additional import
# PROTECTED REGION ID(WeatherUnderground.additionnal_import) ENABLED START #
import six
import time
import urllib3
import json
# PROTECTED REGION END #    //  WeatherUnderground.additionnal_import

__all__ = ["WeatherUnderground", "main"]


class WeatherUnderground(Device, metaclass=DeviceMeta):
    """
    WeatherUnderground is a Python class to read the weather information from 
    the Weather Underground site - https://www.wunderground.com/
    """
    __metaclass__ = DeviceMeta
    # PROTECTED REGION ID(WeatherUnderground.class_variable) ENABLED START #
    def read_temperature(self,_town):
        """read and return the temperature as float of the supplied town key,
         use the wunderground api key provided by init_device() """
        wu_url = 'http://api.wunderground.com/api/%s/geolookup/conditions/q/%s.json' % (self.wu_api_key,_town)
        self.debug_stream(wu_url)
        f = self.http.request('POST', wu_url)
        parsed_json = json.loads(f.data.decode('utf-8'))
        _t_read = float(parsed_json['current_observation']['temp_c'])
        return _t_read
    # PROTECTED REGION END #    //  WeatherUnderground.class_variable

    # -----------------
    # Device Properties
    # -----------------

    api_key_file = device_property(
        dtype='str', default_value=".wu_api_key"
    )

    # ----------
    # Attributes
    # ----------

    Grenoble_t = attribute(
        dtype='double',
        doc="Test attribute \n\nThis attribute test the generation of docstrings using the description in Pogo.\nThe output should be a multi-line docstring for the attribute method.",
    )

    Paris_t = attribute(
        dtype='double',
    )

    Trieste_t = attribute(
        dtype='double',
    )

    Barcelona_t = attribute(
        dtype='double',
    )

    Hamburg_t = attribute(
        dtype='double',
    )

    Lund_t = attribute(
        dtype='double',
    )

    Cape_Town_t = attribute(
        dtype='double',
    )

    Munich_t = attribute(
        dtype='double',
    )

    All_t = attribute(
        dtype=(('str',),),
        max_dim_x=1024, max_dim_y=1024,
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        Device.init_device(self)
        # PROTECTED REGION ID(WeatherUnderground.init_device) ENABLED START #
        self.
        self.debug_stream("api_key_file: %s" % self.api_key_file)
        key_file = open(self.api_key_file)
        _wu_api_key = key_file.readline()
        self.wu_api_key = _wu_api_key.strip()
        self.debug_stream("api_key: %s" % self.wu_api_key)
        self._Grenoble_t = 0.0
        self._Grenoble_t_last_read = 0
        self._Paris_t = 0.0
        self._Paris_t_last_read = 0
        self._Trieste_t = 0.0
        self._Trieste_t_last_read = 0
        self._Barcelona_t = 0.0
        self._Barcelona_t_last_read = 0
        self._Hamburg_t = 0.0
        self._Hamburg_t_last_read = 0
        self._Lund_t = 0.0
        self._Lund_t_last_read = 0
        self._Cape_Town_t = 0.0
        self._Cape_Town_t_last_read = 0
        self._Munich_t = 0.0
        self._Munich_t_last_read = 0
        self._all_towns_attr = {'Grenoble':self.read_Grenoble_t, 'Paris':self.read_Paris_t, 'Trieste':self.read_Trieste_t, 'Barcelona':self.read_Barcelona_t,
                           'Hamburg': self.read_Hamburg_t, 'Lund':self.read_Lund_t, 'Cape Town':self.read_Cape_Town_t, 'Munich':self.read_Munich_t}
        self.http = urllib3.PoolManager()
        # PROTECTED REGION END #    //  WeatherUnderground.init_device

    def always_executed_hook(self):
        # PROTECTED REGION ID(WeatherUnderground.always_executed_hook) ENABLED START #
        pass
        # PROTECTED REGION END #    //  WeatherUnderground.always_executed_hook

    def delete_device(self):
        # PROTECTED REGION ID(WeatherUnderground.delete_device) ENABLED START #
        pass
        # PROTECTED REGION END #    //  WeatherUnderground.delete_device

    # ------------------
    # Attributes methods
    # ------------------

    def read_Grenoble_t(self):
        # PROTECTED REGION ID(WeatherUnderground.Grenoble_t_read) ENABLED START #
        self.debug_stream("delta time %d" % (time.time() - self._Grenoble_t_last_read))
        if (time.time() - self._Grenoble_t_last_read) > 3600:
            self._Grenoble_t = self.read_temperature('France/Grenoble')
            self._Grenoble_t_last_read = time.time()
        self.debug_stream("Grenoble temperature %.2f" % (self._Grenoble_t))
        return self._Grenoble_t
        # PROTECTED REGION END #    //  WeatherUnderground.Grenoble_t_read

    def read_Paris_t(self):
        # PROTECTED REGION ID(WeatherUnderground.Paris_t_read) ENABLED START #
        if (time.time() - self._Paris_t_last_read) > 3600:
            self._Paris_t = self.read_temperature('France/Paris')
            self._Paris_t_last_read = time.time()
        self.debug_stream("Paris temperature %.2f" % (self._Paris_t))
        return self._Paris_t
        # PROTECTED REGION END #    //  WeatherUnderground.Paris_t_read

    def read_Trieste_t(self):
        # PROTECTED REGION ID(WeatherUnderground.Trieste_t_read) ENABLED START #
        if (time.time() - self._Trieste_t_last_read) > 3600:
            self._Trieste_t = self.read_temperature('Italy/Trieste')
            self._Trieste_t_last_read = time.time()
        self.debug_stream("Trieste temperature %.2f" % (self._Trieste_t))
        return self._Trieste_t
        # PROTECTED REGION END #    //  WeatherUnderground.Trieste_t_read

    def read_Barcelona_t(self):
        # PROTECTED REGION ID(WeatherUnderground.Barcelona_t_read) ENABLED START #
        if (time.time() - self._Barcelona_t_last_read) > 3600:
            self._Barcelona_t = self.read_temperature('Spain/Barcelona')
            self._Barcelona_t_last_read = time.time()
        self.debug_stream("Barcelona temperature %.2f" % (self._Barcelona_t))
        return self._Barcelona_t
        # PROTECTED REGION END #    //  WeatherUnderground.Barcelona_t_read

    def read_Hamburg_t(self):
        # PROTECTED REGION ID(WeatherUnderground.Hamburg_t_read) ENABLED START #
        if (time.time() - self._Hamburg_t_last_read) > 3600:
            self._Hamburg_t = self.read_temperature('Germany/Hamburg')
            self._Hamburg_t_last_read = time.time()
        self.debug_stream("Hamburg temperature %.2f" % (self._Hamburg_t))
        return self._Hamburg_t
        # PROTECTED REGION END #    //  WeatherUnderground.Hamburg_t_read

    def read_Lund_t(self):
        # PROTECTED REGION ID(WeatherUnderground.Lund_t_read) ENABLED START #
        if (time.time() - self._Lund_t_last_read) > 3600:
            self._Lund_t = self.read_temperature('Sweden/Lund')
            self._Lund_t_last_read = time.time()
        self.debug_stream("Lund temperature %.2f" % (self._Lund_t))
        return self._Lund_t
        # PROTECTED REGION END #    //  WeatherUnderground.Lund_t_read

    def read_Cape_Town_t(self):
        # PROTECTED REGION ID(WeatherUnderground.Cape_Town_t_read) ENABLED START #
        if (time.time() - self._Cape_Town_t_last_read) > 3600:
            self._Cape_Town_t = self.read_temperature('ZA/Cape_Town')
            self._Cape_Town_t_last_read = time.time()
        self.debug_stream("Cape_Town temperature %.2f" % (self._Cape_Town_t))
        return self._Cape_Town_t
        # PROTECTED REGION END #    //  WeatherUnderground.Cape_Town_t_read

    def read_Munich_t(self):
        # PROTECTED REGION ID(WeatherUnderground.Munich_t_read) ENABLED START #
        if (time.time() - self._Munich_t_last_read) > 3600:
            self._Munich_t = self.read_temperature('Germany/Munich')
            self._Munich_t_last_read = time.time()
        self.debug_stream("Munich temperature %.2f" % (self._Munich_t))
        return self._Munich_t
        # PROTECTED REGION END #    //  WeatherUnderground.Munich_t_read

    def read_All_t(self):
        # PROTECTED REGION ID(WeatherUnderground.All_t_read) ENABLED START #
        _all_towns_temps = []
        for _town in self._all_towns_attr:
            _read_t = (self._all_towns_attr[_town])()
            _read_t_str = "%.2f" % _read_t
            _all_towns_temps.append([_town,_read_t_str])
        #_all_towns_temps = [_all_towns, _all_temps]
        return _all_towns_temps
        # PROTECTED REGION END #    //  WeatherUnderground.All_t_read


    # --------
    # Commands
    # --------

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    # PROTECTED REGION ID(WeatherUnderground.main) ENABLED START #
    return run((WeatherUnderground,), args=args, **kwargs)
    # PROTECTED REGION END #    //  WeatherUnderground.main

if __name__ == '__main__':
    main()
