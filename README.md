# Matter IoT Emulator 

    - This repo is created to implement Matter IoT Emulator to simulation matter device (https://github.com/project-chip/connectedhomeip/tree/v1.2.0.1), written on Python3 
    - Virtual matter devices build on linux platform
    - Matter IoT Emulator run on Raspberry-Pi 4

## Advantages
    - Supports for running multiple virtual matter devices (max: 15 devices) concurrently
    - Tab for monitor running devices
    - Can recover devices operation which were commissioned
    - Only support wifi and ethernet interface

## Installation Guide
### 1. Setup Raspberry-Pi 4
    - PI 4 Model B microSD card 32/64GB
    - OS version (64bit): https://downloads.raspberrypi.org/raspios_arm64/images/raspios_arm64-2022-09-26/2022-09-22-raspios-bullseye-arm64.img.xz
    - Raspberry PI Imager Tool for Window: https://downloads.raspberrypi.org/imager/imager_1.8.5.exe, Ubuntu: $ sudo apt install rpi-imager,
      You can refer to https://www.raspberrypi.com/news/raspberry-pi-imager-imaging-utility/ to flash image for Pi
### 2. Download source code
    $ cd ~
    $ git clone <URL_TO_REPO>
### 3. Setup environment
    $ cd matter-emulator/MatterIoTEmulator/scripts/
    $ ./install.sh

## Usage
### 1. Run Matter IoT Emulator
    After installing environment successfully without errors. You can enjoy with Matter IoT Emulator.
    (Pre-condition: Need to connect wifi or ethernet to Raspberry-Pi)
    $ cd matter-emulator/MatterIoTEmulator/scripts/
    $ ./run-matter-emulator-app

    After Matter IoT Emulator launched success:
    - On the left side "Device Type" label:
        * Select the device type which you need to use
        * Fill device information as Serial Number, Vendor ID, Product ID, Discriminator and Pin code (For each device Serial Number or Vendor ID or Product ID should be unique)
    - On the right side "Device Control" label:
        * After select device and fill device information, Click Start device button to power on this device
        * Then, wait to QR code generated and you can use some commissioners to connect device such as LG TV, SmartThings Station,... 
        (You can refer to https://www.lg.com/us/support/help-library/lg-thinq-how-to-connect-matter-devices--20153454569708 to know how LG TV, ThinQ App connect to matter device)
        * Device is connected to commissioner successfully when statusbar displays "Device is connected successfully..." and device was saved to Emulator, so you do not need to connect to device again when power off -> power on (Start device -> Stop device) 
        * Now, You can control device from Matter IoT Emulator and Commissioner(LG TV, SmartThings Station...) 
        * You can click Stop device to power off device
        * When you start a device with the same information Serial Number, Vendor ID, Product ID of a connected device was power off -> this device will be re-connect to commissioner (LG TV, SmartThings Station...)
    - Tab "INFO":
        * You can see connected device are running at tab "INFO"
    - When you need to use more devices, click "+" button on the top-left to open new tab
    - When click "X" button on the right of device tab name, this device will be deleted and can not be recovered

### 2. Remove un-use commissioned devices
    $ cd matter-emulator/MatterIoTEmulator/temp/
    $ rm -r <folder_name> (folder_name is a combination of VID, PID and SerialNumber in hexa, EX: VID: 0xffff, PID: 0x8001, SerialNumber: 0x1111 -> folder_name: ffff8001-1111)