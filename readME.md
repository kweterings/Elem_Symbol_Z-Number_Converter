# <u> Element Symbol To Atomic/Z Number Converter </u>
###### Made by Kai Weterings, 30/07/2023

<div style="text-align: justify">
I present to you a conversion that works both ways for Element Symbols (ex: H, He, Li, Be, etc... )
to Atomic/Z number (number of protons in nucleus).</div>
<div style="text-align: justify">
Whilst performing a data sweep for benchmarking a Monte Carlo code about reactions of radiation-matter, I was faced with having to turn worded information from that data files into numerical values used as input for the simulation code.
Specifying reaction channels led to needing to convert element symbols into their respective atomic numbers 
for use in the Monte Carlo code. This led to tediously having to spend time writing out all element symbols in order
to be able to convert element symbol into its respective atomic number.</div>
<div style="text-align: justify">
This monotonous task made me realise many more people probably have to deal with this, hence I thought to create a project
with various formats of an element symbol to atomic number converter, and vice versa.</div>

##### You will find 3 different types of converters;  
* Script to run in a terminal command line, where the arguments act as the input to be converted
  (best for quick usage, bash scripting, etc...).
* Python executable file to be imported and called upon in another file (best for python scripting).
* A regular program which relies on user input whilst running (best for ease of use and being more 
user-friendly).

Below is a short description of how each file is intended to be used in its current state.
### File 1: sym_to_Z_number_cmdline.py
<div style="text-align: justify">
This file is currently designed for the Linux terminal (Linux, WSL, etc...), where any amount of arguments will be
converted. To receive an output please do the following;</div>

```
$ ./sym_to_Z_number_cmdline.py 2 He Ge 76 14            #Leading to an output of 5 seperate answers (He 2 32 Os Si)
```
<div style="text-align: justify">
If any of the inputs/arguments aren't recognised (not an element symbol or atomic number), the code will return the 
unknown argument in this way;</div>

```
$ Can't convert argument(s): xxxxx xxxxx                #xxxx being the unconvertable inputs
```
### File 2: sym_to_Z_number_exec.py
<div style="text-align: justify">
Possibly the handiest of the 3, this file is meant to act as an importable file/script in your project folder
for another python script. This code, like the rest, accepts as many arguments as you'd like. To
call upon this script in your work, please do the following;</div>

```python
import sym_to_Z_number_exec
sym_to_Z_number_exec.convert(2, 'He', 'Ge', 76, 14)     #convert is the definition which performs the conversion
```
The argument can of course also be a variable previously defined in the code.   
I have made it so that if any arguments to not represent an element symbol or atomic number, the code will
return the troubling inputs and quit with error code 1 (to prevent your work from continuing to run with faulty inputs).

### File 3: sym_to_Z_number_run.py
The 3rd and final format of the converter is the generic program, which asks for user input upon being run. 
The program will take as many element symbols or atomic numbers to be converted at once, and will keep asking for 
more user input after each output. To terminate the program, the user simply has to type 'q' and enter to stop the code.  
Feel free to try out this program to see what im talking about :stuck_out_tongue_winking_eye:!
