# Few Requirements Inorder to run blink code:

## Hardware:

- 1 x Ardunio board
- 2 x Jumper wires
- 1 x LED
- 1 x USB A to USB B

## Pre-requisites:

Install:

1) Any code editor (Visual Code Studio Recommended)
2) Python3+
3) pip
4) Ardunio IDE

Libraries:

` pyfirmata `

## Step By Step Procedure:

1. Install using the command: 

   `pip install pyfirmata`


2. Connect your Ardunio Board and launch Ardunio:

   - In Ardunio check if you board is connected by going to Tools -> "Port"

   - You should see your port has connected to your pc.

   - Now go to 

     File -> Examples -> Firmata and click on **StandardFirmata** 

   - This will open the code in a new window. Now upload the standard firmata code to your Arduino using the upload button. 
     After successfully uploading the code you will see a message on the Ardunio IDE that the code has beeen uploaded sucessfully.

3. Finding put the Port Name/Number

  - For Windows

    - Device Manager -> Ports(COM and LPT) 

    - Over there you will see your Ardunio's Name with the port in brackets (Usually it is COM3)

    - It would loook something like this:

    - `Arduino Mega 2560(COM3)` and copy 'COM3'

  - For MacOS
  
    - In the Ardunio IDE go to Tools -> "Port"
    
    - Port will show somthing like this `/dev/cu.usbmodem*` (where * is my Port Number, Eg: 14410, it would look like "/dev/cu.usbmodem14410" )
 
    - Copy that and paste it somewhere temporarily.


4. Paste the port Name/Number into the quotes on line 5

  ` port = 'Add your Port Name here'`

5. Now execute the code


That should do it, you can further add a external LED to the board to see it blink 

## For Ultrasonic Python code:

### Diagram:

![alt text](https://toptechboy.com/wp-content/uploads/2014/07/ultrasonic_bb.jpg) 



















