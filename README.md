![HBNB](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210701%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210701T033134Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=29e66d3505c8f710752f6f0014c56ecfe94687295085ecc70c6b8b0deb8e4092 "HBNB")
<h1 align="center">0x00. AirBnB clone - The console</h1>
<p align="center"></p>
------------
## Description
The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on the server a simple copy of the AirBnB website, only some of them to cover all fundamental concepts of the higher level programming track.

#### We will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging) which is capable of:
-> Create a new object
-> Retrieve an object
-> Update attributes of an object
-> Destroy an object

- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)- 
------------
## How to install it:
```
git clone https://github.com/Orcha02/AirBnB_clone.git
cd AirBnB_clone
```
## Usage
#### Interactive Mode
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
```
#### Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
#### Commands Sintax with Respective Usage
Command | Syntax | Output
------- | ------ | ------
help | `help [option]` | Displays all available commands
quit | `quit` | Exit command interpreter
EOF | `EOF` | Exit command interpreter
create | `create [class_name]` or `[class_name].create()`| Creates an instance of class_name
update | `update [class_name] [object_id] [update_key] [update_value]` or  `[class].update([object_id] [update_key] [update_value]()`| Updates the key:value of class_name.object_id instance
show | `show [class_name] [object_id]` or `[class_name].show([object_id])()` | Displays all attributes of class_name.object_id
all | `all [class_name]`, `[class_name].all()` | Displays every instance of class_name, if used without option displays every instance saved to the file
destroy | `destroy [class_name] [object_id]` or `[class_name].destroy([object_id])()` | Deletes all attributes of class_name.object_id
count | `count [class_name]` or `[class_name].count()`| Counts all the instances with class name specified)
[Authors]
# Authors

 👤 **Daniel Ortega**

- Twitter: [@OrtegaChaux](https://twitter.com/OrtegaChaux)
- Github: [@Orcha02](https://github.com/Orcha02)

👤 **Frank J. Grijalba H.**

- Twitter: [@FrankGrijalba](https://twitter.com/FrankGrijalba)
- Github: [@FRANK-GRIJALBA](https://github.com/FRANK-GRIJALBA)

jun-24-2021