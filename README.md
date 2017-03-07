nova.instrumentation
====================

Supporting code for Digital Instrumentation class at Universidade Nova de Lisboa.


## **Installation**
>### **Manual**

### 1. Download and install the required applications:
* [Anaconda](http://continuum.io/downloads) (choose python 3);
* [Supporting code](https://github.com/hgamboa/novainstrumentation).

### 2. Complete the installation
Copy the support code to `C:\Users\[username]\Anaconda\Lib\` directory and rename to guarantee that the directory is called `novainstrumentation`.

In macOS: `\Users\[username]\Anaconda\Lib\`. 
  
<span style="color: gray; font-family: Babas; font-size: 12px;">
Note: users with spaces and special characters will not be able to install.
We suggest creating a new user in the system.</span>

### 3. Check if the module was successfully installed  
Make sure that the following code line works in `ipython`:

      import novainstrumentation

If no error appears you have successfully installed the needed tools for a scientific python environment.

### 4. Notes

If introlab.py raises `ImportError: No module named '_tkinter', please install the python3-tk package`
while on ubuntu, run the following code in terminal:
```
sudo apt-get install python3-tk
```