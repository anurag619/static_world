Testing production apps on mobile
----------------------------------
:date: 2014-05-22 12:01
:category: programming
:tags: phonegap, Fedora
:author: Anurag
:excerpt: 


Assuming you have ADB and Eclipse IDE installed.

I am using Samsung Galaxy Pro to connect to fedora 19 but it shouldn't really matter if you have a different device.

In the eclipse toolkit, you have the option to run it directly on a device. It's rather quick to do so but the experience is same as that of emulator.  On your phone:

1. Enable USB debugging (modern android versions this is present as Developers Option ) as well as installation of apk from sources other than the market (in the settings > security option).

2. In the AndroidManifest.xml file , add::


		android: debuggable="True" 

to the <application> element.

3. Connect your device with your system via USB cable, then Open terminal::


		$ adb devices


you will get a unique id for the device attached. Keep a note of this id, we will be using this below.

4. You need to add a udev rules file that contains a USB configuration for each type of device you want to use for development. In the rules file, each device manufacturer is identified by a unique vendor ID, as specified by the *ATTR{idVendor}* property. For a list of vendor IDs, see `vendor ids <http://developer.android.com/tools/device.html#VendorIds>`_ .

Log in as root and create this file: /etc/udev/rules.d/51-android.rules.

And Use this format to add each vendor to the file::


		SUBSYSTEM=="usb", ATTR{idVendor}=="0bb4", MODE="0666", GROUP="plugdev"

In this example, the vendor ID is for HTC, change it according to your device.

Now execute::


		chmod a+r /etc/udev/rules.d/51-android.rules

5. Your device is now configured, when testing apps from Eclipse IDE select this device when prompted.


**Other ADB uses**

After step 4 above, type::


		$ adb shell

this will list the root contents of your phone. Next if you do::


		$ ls

All the files will be visible to you. Other operations such as: *cd, mkdir* etc are also applicable.

If you wish to know more about ADB operations type $ adb in your terminal, you will get all available commands to play with.



`reference <http://developer.android.com/tools/device.html>`_