# facial recognition

facial recognition is a really simple project to add an additional layer of security to linux machines

facial recognition is made using the facial_recognition library https://github.com/ageitgey/face_recognition 


# How to use it #

you can just run the script as a normal python script (thats what you should do before applying it to your system)

to use as normal script :

- take a photo of yourself and name it me.jpg and put it in the same directory (you can use take_photo.py to do that)

- change the hardcoded location in the script from (/usr/share/.secrets/me.jpg) to me.jpg

- install the required libraries <it will take long time> (if you're not gonna use the setup.py be sure to install cmake first) ```apt install cmake``` 

```python3 facial_recognition.py```

after that if you wanna apply it to the system that's how:

- first run the take_photo.py script (python3 take_photo.py) and be sure to be infront of your webcam 

- if you changed the hardcoded location in the script change it back to (/usr/share/.secrets/me.jpg)
  
- then run the setup.py (python3 setup.py) and if you have a missing libraries or packages this will install it
and then it will configure the files for you


- after that open your (session and startup) software from your application menu denpending on your linux distro then click on (Application autostart)
then click on add or the plus (+) button give it a name of your choice and on the command section type (/usr/bin/python3 /location/to/facial_recognition.py)


- now everytime you open your machine after login it will run the facial_recognition in the background and if you're not there it will shutdown the system
