How to configure PhoneGap in Fedora 19
---------------------------------------
:date: 2014-05-31 12:01
:category: programming
:tags: phonegap, Fedora
:author: Anurag
:excerpt: 



Building android apps in native Java is cool but the only problem with this methodology is that you cannot port the same into other platforms (like Facebook, Windows etc). This drawback can be effectively removed if you use HTML5, CSS3 and Javascript to build the mobile apps. This is where `PhoneGap <http://phonegap.com/>`_ comes in handy.

The installation page of Phonegap gives some instruction on how to install some dependencies.

**Npm and NodeJS**

1. To install Node you need to install some dependencies such as c++/gcc, which is used in compilation of the former::


		$ sudo yum install gcc-c++

 then install node. You can either do::


		$ yum install nodejs


2. or you can install it from the source files.

	a: Download the source code from the website.

	b::

			$ cd Downloads

	c::


			$ tarnode-v0.8.15.tar.gz (change the versions accordingly)

	d::


			$ cd node-v0.8.15

	e::


			$ ./configure && make && sudo make install


	f: Add the path in system, if its not present::


			$ cd

			$sudo vi .bash_profile

	add these lines in the file::

    		PATH = $PATH:/usr/local/bin

    		export PATH 


3. Now that you have node, installation of npm will be very easy.

       * get the source from Github 

       * untar it, move into that directory and then::

		$ ./configure && make && sudo make install

4::

		$ sudo npm install -g phonegap

5. Phonegap should be installed now. Move into a directory where you wish to create a app::


		$ phonegap create my-app

		$ cd myapp

		$ phonegap run android

At this moment if you have a mobile device connected to the system the app will be installed on the device itself.