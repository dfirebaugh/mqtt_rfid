# MQTT-RFID
A simple access control system using the Raspberry Pi Pico W and the RFID-RC522 module.

## Overview
This project allows you to control access using RFID fobs and MQTT. You can add fobs using MQTT or manually write them to the Raspberry Pi Pico. The device is designed to remain operational even without network access or when unable to connect to the MQTT broker. It will continuously attempt to reconnect without interrupting its main functionality (controlling access to the door).

The device keeps an ACL in internal memory.  It receives updates from the MQTT broker. It can publish a hash of the current ACL so that the server can verify that the ACL matches what the server expects it to have.

## Wiring
The Raspberry Pi Pico connects to the RC522 module via the SPI interface. The default pinouts are provided below:

| RFID Signal | Pico Pin |
|-------------|:--------:|
| SCK         |   GP2    |
| MOSI        |   GP3    |
| MISO        |   GP4    |
| RST         |   GP0    |
| SDA         |   GP1    |

## Dependencies
- MicroPython
- umqtt.simple (version: 1.3.4; installed to /lib/umqtt on the Raspberry Pi Pico)

> note: [Thonny](https://thonny.org/) can be a useful IDE for working with the Raspberry Pi Pico.

## MQTT Events
The device uses MQTT for communication. Here are the supported MQTT events:

### Subscriptions

| Topic | Payload | Notes |
|-------|---------|-------|
| `<topic_prefix>/acl` | n/a | The device will publish a `<topic_prefix>/acl_response` message. |
| `<topic_prefix>/adduser` | `uid of the RFID fob to add` | Adds the specified fob to the device's Access Control List (ACL). |
| `<topic_prefix>/removeuser` | `uid of the RFID fob to remove` | Removes the specified fob from the device's ACL. |
| `<topic_prefix>/open` | n/a | Opens the door. |

### Publish

| Topic | Payload | Notes |
|-------|---------|-------|
| `<topic_prefix>/acl_response` | `{'acl': '<SHA256 hash of the current ACL stored>'}` | Allows the server to verify if the device has the correct ACL. |
| `<topic_prefix>/heartbeat` | `OK` | Allows the server to verify the device's network connection. |
| `<topic_prefix>/access_granted` | `uid of the fob that is granted access` | Used for logging purposes. |
| `<topic_prefix>/access_denied` | `uid of the fob that is denied access` | Used for logging purposes. |
