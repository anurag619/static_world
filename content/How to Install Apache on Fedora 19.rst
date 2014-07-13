How to Install and configure Apache on Fedora 19
##################################################

:date: 2014/07/13
:category: fedora
:tags: internet
:author: Anurag


Few days back I was juggling to install the `apache <http://en.wikipedia.org/wiki/Apache_HTTP_Server>`_ web server on my local machine which has fedora 19. Information on the internet is scattered around and there isn't one tutorial which can you through the entire process. It tooks me quite some time to figure out the exact procedure and the below mentioned steps are the result of that.

I assume you have a previous knowledge of vim and its subsequesnt commands, if not this `tutorial <http://www.engadget.com/2012/07/10/vim-how-to/>`_ might help you.

Installing Apache webserver
---------------------------

1::


		sudo yum install httpd


Configure Apache to run your local website
--------------------------------------------

2::


		vim /etc/httpd/conf/httpd.conf

Browse to the end of file (you do not need to change anything else) and append the following at bottom::


		<VirtualHost *:80>
		DocumentRoot /var/www/your-site-name
		ServerName local.your-mysite-name
		</VirtualHost>

Add your site (folder) name to DocumentRoot and ServerName. For example in my case it would be /var/www/site and local.site

Note: whatever site/folder-name you are adding above, must exists. If its not create such folder. After adding the above, you can save and close the file.

3::


		vim /etc/hosts

Append the following to the file::



		127.0.0.1    local.your-site-name

For example in my case it will be: local.mysite. Now, save and close the file.

4. Start Apache::


		sudo service httpd start

5. Check if apache is running or not::


		sudo service httpd status


6. Run::


		ps -eZ | grep httpd 


to view the httpd processes


You can now access your site at the address you specified above, e.g. local.your-site-name .

Note:  do not add www at the start.