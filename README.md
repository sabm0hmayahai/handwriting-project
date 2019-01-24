# Handwriting-project
An uber unique idea to digitalise handwriting on a chalkboard or whiteboard fitted with our sensors using Arduino UNO and ultrasonic sensors. 

# Technology and hardware stack : 
Arduino UNO, Ultrasonic sensors (HC-SR04), Coolterm software, Python, Shell script, Google cloud service.

# Brief description of idea : 
Basically the idea is to digitalise the written things. We are using Arduino microcontroller with two Ultrasonic sensors to analyze the movement on the board (2D). The ultrasonic sensors are placed at two corners of the blackboard/whiteboard and can track the precise coordinates of the chalk/marker on the board. Using these coordinates, we plot a digit copy of the writing on the board. We use python to process these and extract out the letters and symbols to convert it into a typed out PDF. Later by running a shell script this file will be uploaded to google cloud and it can be securily shared with people who want have a access to that perticular file.

# Instructions
1) Setup all hardware connections.

Arduino Uno is a microcontroller board based on the ATmega328P (datasheet). It has 14 digital input/output pins (of which 6 can be used as PWM outputs), 6 analog inputs, a 16 MHz quartz crystal, a USB connection, a power jack, an ICSP header and a reset button. It contains everything needed to support the microcontroller; simply connect it to a computer with a USB cable or power it with a AC-to-DC adapter or battery to get started.


Setup:

![Setup](https://github.com/BinaryNMIT/handwriting-project/blob/master/images/setup.jpg)


![uno](https://github.com/BinaryNMIT/handwriting-project/blob/master/images/uno.png)

2) Install and run Coolterm 
   CTRL+R (Record values) 
   CTRL+SHIFT+R (Stop recording)
   This will basically read the data values from the sensor and stores it in text file.
   
 Coolterm values:

![Coolterm values](https://github.com/BinaryNMIT/handwriting-project/blob/master/images/coolterm.jpg)


3) Now using this (x,y) values a graph is plotted using python program (using mathplotlib) the following visual graph is obtained and saved as pdf (or any kind)

Graphical images:
Letter R is unsmoothened

![R](https://github.com/BinaryNMIT/handwriting-project/blob/master/images/R_unsmooth.png)

Letter R is smoothened 

![R](https://github.com/BinaryNMIT/handwriting-project/blob/master/images/R_smooth.png)


4) Google cloud platform must be setup on your machine, also a bucket should be created in your project on the cloud.

Run the process.command script with proper "source" and "destination" file location.
This script contains python smoothening/processing code for all the read values and also uploads PDF result to the cloud and end users can access if they have proper permissions. (access to file)


Script output:

![Terminal](https://github.com/BinaryNMIT/handwriting-project/blob/master/images/terminal.jpg)

Google cloud:

![Cloud](https://github.com/BinaryNMIT/handwriting-project/blob/master/images/googlecloud.jpg)

Processed Alphabet:

![Data](https://github.com/BinaryNMIT/handwriting-project/blob/master/images/data-001.jpg)


Useful links: 

https://www.arduino.cc (Arduino official website)

http://freeware.the-meiers.org (Coolterm serial port value reader)

https://cloud.google.com
(Google cloud setup and official documentation)

https://matplotlib.org
(Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms)

