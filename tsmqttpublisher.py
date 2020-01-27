import paho.mqtt.publish as publisher

# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
# channelID = "971761"

# The write API key for the channel.
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
# writeAPIKey = "5JFQA9XQPXCSQK7G"

# The hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"

# You can use any username.
mqttUsername = "BarosVK"

# Your MQTT API key from Account > My Profile.
mqttAPIKey = "A10S9VPOS7BM1CD4"

tTransport = "websockets"
tPort = 80


def publishAqaraTempToThingSpeak(channelID, writeAPIKey, temp, humidity, pressure):
    # Create the topic string.
    topic = "channels/" + channelID + "/publish/" + writeAPIKey

    # build the payload string.
    payload = "field1=" + str(temp) + "&field2=" + str(humidity) + "&field3=" + str(pressure)

    # attempt to publish this data to the topic.
    try:
        publisher.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort,
                         auth={'username': mqttUsername, 'password': mqttAPIKey})
        print(" Published Temperature = ", temp, " Humidity = ", humidity, " Pressure = ", pressure, " to host: ",
              mqttHost)

    # except (KeyboardInterrupt):
    #  break

    except Exception as ex:
        print("There was an error while publishing the data.", ex)

    return


def publishDHT11ToThingSpeak(channelID, writeAPIKey, temp, humidity):
    # Create the topic string.
    topic = "channels/" + channelID + "/publish/" + writeAPIKey

    # build the payload string.
    payload = "field1=" + str(temp) + "&field2=" + str(humidity)

    # attempt to publish this data to the topic.
    try:
        publisher.single(topic, payload, hostname=mqttHost, transport=tTransport, port=tPort,
                         auth={'username': mqttUsername, 'password': mqttAPIKey})
        print(" Published Temperature = ", temp, " Humidity = ", humidity, " to host: ", mqttHost)

    # except (KeyboardInterrupt):
    #  break

    except Exception as ex:
        print("There was an error while publishing the data.", ex)

    return
