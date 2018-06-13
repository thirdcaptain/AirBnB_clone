# AirBnB_clone

![hbnb](https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)

## Table of Contents

* [Description](#description)
* [Usage](#usage)
* [Examples](#examples)
* [Commands](#commands)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)


## Description

**hbnb** - Holberton BnB is a clone AirBnB, a student project to introduce and develop familiarity with the components of a full web application. Currently, the scope of the application acts as a command interpreter that can create, retrieve, update and delete objects.

## Usage

To launch the console application in interactive mode simply run:

```
console.py
```

or to use the non-interactive mode run:

```
echo "your-command-here" | ./console.py
```

## Usage Examples

### Interactive Mode

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

### Non-Interactive Mode

```c
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

##Commands

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

Commands | Description | Usage
-------- | ----------- |-------- |
**help** | Displays the documented commands | **help**
**quit** | Exits the program | **quit**
**EOF**  | Ends the program  | N/A
**create** | Creates a new instance of a class | **create** \<classname\>
**show** | Prints a string representation based on class name and id | **show** \<classname\> \<id\>
**destroy** | Delete an instance based on class name and id | **destroy** \<classname\> \<id\>
**all** | Prints a string representation of all instances, or all instances based on class name | **all** or **all** \<classname\>
**update** | Update an instance based on the class name and id or updating the attribute | **update** \<classname\> \<id\> \<attribute\> \<attribute value\>


## Bugs
At this time, there are no known bugs.

## Authors

* Artur Adamian | [GitHub](https://github.com/arturadamian) | [Twitter](https://twitter.com/arturadamian)
* Isaac Wong | [GitHub](https://github.com/thirdcaptain) | [Twitter](https://twitter.com/KYIsaacWong)

## License

**hbnb** is open source and free to download and use