#!/usr/bin/env python
# encoding: utf-8
"""
device.py

Created by Jarrod Hermer on 2010-07-16.
Copyright (c) 2010 off-the.net. All rights reserved.
"""

from google.appengine.ext import db

class Device(db.Model):
    """Describes a mobile devices capabilities"""
    name = db.StringProperty()
    user_agent = db.StringProperty()

class ProductInfo(db.Model):
    """docstring for ProductInfo"""
    device = db.ReferenceProperty(Device)
    mobile_browser
    nokia_feature_pack
    device_os
    nokia_series
    has_qwerty_keyboard
    pointing_method
    mobile_browser_version
    nokia_edition
    uaprof
    can_skip_aligned_link_row
    device_claims_web_support
    ununiqueness_handler
    model_name
    device_os_version
    uaprof2
    is_wireless_device
    uaprof3
    brand_name
    model_extra_info
    marketing_name
    can_assign_phone_number
    release_date
    unique
    
