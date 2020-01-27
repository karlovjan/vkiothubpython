#!/usr/bin/env python3

import mqttsubscriber as subscriber

subscriber.subscribe_to_aqara_temp_sensor("zigbee2mqtt/aqara_temp_loznice")

subscriber.subscribe_to_aqara_temp_sensor("zigbee2mqtt/aqara_temp_chodba")

subscriber.subscribe_to_aqara_temp_sensor("zigbee2mqtt/aqara_temp_koupelna")
