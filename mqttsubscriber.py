import json

import paho.mqtt.subscribe as subscribe

import tsmqttpublisher as publisher


def subscribe_to_aqara_temp_sensor(topic):
    def get_channel_id():
        switcher = {
            "zigbee2mqtt/aqara_temp_loznice": "971761",
            "zigbee2mqtt/aqara_temp_chodba": "972228",
            "zigbee2mqtt/aqara_temp_koupelna": "972229",
        }
        return switcher.get(topic, "")

    def get_write_api_key():
        switcher = {
            "zigbee2mqtt/aqara_temp_loznice": "5JFQA9XQPXCSQK7G",
            "zigbee2mqtt/aqara_temp_chodba": "MVYOOW4L5TH1KTCO",
            "zigbee2mqtt/aqara_temp_koupelna": "O3HNGWT7088YI437",
        }
        return switcher.get(topic, "")

    def on_message_received(client, userdata, message):
        print("%s %s" % (message.topic, message.payload))

        payload = json.loads(message.payload)
        temperature = payload.temperature
        humidity = payload.humidity
        pressure = payload.pressure

        channel_id = get_channel_id()
        write_api_key = get_write_api_key()

        if channel_id and write_api_key:
            publisher.publishAqaraTempToThingSpeak(channel_id, write_api_key, temperature, humidity, pressure)
        else:
            print("channelID or writeAPIKey was not found")

    subscribe.callback(on_message_received, topic, hostname="localhost")

    return
