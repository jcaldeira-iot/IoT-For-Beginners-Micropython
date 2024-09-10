# Virtual single-board computer

Instead of purchasing an IoT device, along with sensors and actuators, you can use your computer to simulate IoT hardware. The [CounterFit project](https://github.com/CounterFit-IoT/CounterFit) allows you to run an app locally that simulates IoT hardware such as sensors and actuators, and access the sensors and actuators from local Python code that is written in the same way as the code you would write on a Raspberry Pi using physical hardware.

## Setup

The instructions to install and configure the CounterFit app will be given at the relevant time in the assignment instructions as it is installed on a per-project basis.

## Hello world

It is traditional when starting out with a new programming language or technology to create a 'Hello World' application - a small application that outputs something like the text `"Hello World"` to show that all the tools are correctly configured.

The Hello World app for the virtual IoT hardware will ensure that you have Python and Visual Studio code installed correctly. It will also connect to CounterFit for the virtual IoT sensors and actuators. It won't use any hardware, it will just connect to prove everything is working.

This app will be in a folder called `nightlight`, and it will be re-used with different code in later parts of this assignment to build the nightlight application.

### Create a Python ´Hello world´ example and connect it to CounterFit

One of the powerful features of Python is the ability to install [Pip packages](https://pypi.org) - these are packages of code written by other people and published to the Internet. You can install a Pip package onto your computer with one command, then use that package in your code. You'll be using Pip to install a package to talk to CounterFit.

#### Task - install CounterFit

Install the Pip packages for CounterFit.

1. From your terminal or command line, run the following commands to install the Pip packages for CounterFit. These packages include the main CounterFit app as well as shims for Grove hardware. These shims allow you to write code as if you were programming using physical sensors and actuators from the Grove ecosystem but connected to virtual IoT devices.

    ```sh
    pip3 install CounterFit
    pip3 install counterfit-connection
    pip3 install counterfit-shims-grove
    ```

1. From your terminal or command line, run the following at a location of your choice to create and navigate to a new directory:

    ```sh
    mkdir nightlight
    cd nightlight
    ```

### Write the code

#### Task - write the code

Create a Python application to print `"Hello World"` to the console.

1. From your terminal or command line, run the following to create a Python file called `app.py`:

    * From Windows run:

        ```cmd
        type nul > app.py
        ```

    * On macOS or Linux, run:

        ```cmd
        touch app.py
        ```

1. Open the current folder in VS Code:

    ```sh
    code .
    ```

    > 💁 If your terminal returns `command not found` on macOS it means VS Code has not been added to your PATH. You can add VS Code to your PATH by following the instructions in the [Launching from the command line section of the VS Code documentation](https://code.visualstudio.com/docs/setup/mac?WT.mc_id=academic-17441-jabenn#_launching-from-the-command-line) and run the command afterwards. VS Code is installed to your PATH by default on Windows and Linux.

1. Launch a new VS Code Terminal by selecting *Terminal -> New Terminal, or pressing `` CTRL+` ``:

    ![VS Code Kill the active terminal instance button](../../../images/vscode-kill-terminal.png)
    ```output
    ...nightlight$
    ```

1. Open the `app.py` file from the VS Code explorer and add the following code:

    ```python
    print('Hello World!')
    ```

    The `print` function prints whatever is passed to it to the console.

1. From the VS Code terminal, run the following to run your Python app:

    ```sh
    python3 app.py
    ```

    The following will be in the output:

    ```output
    ...nightlight$ python3 app.py 
    Hello World!
    ```

😀 Your 'Hello World' program was a success!

### Connect the 'hardware'

As a second 'Hello World' step, you will run the CounterFit app and connect your code to it. This is the virtual equivalent of plugging in some IoT hardware to a dev kit.

#### Task - connect the 'hardware'

1. From the VS Code terminal, launch the CounterFit app with the following command:

    ```sh
    counterfit
    ```

    The app will start running and open in your web browser:

    ![The Counter Fit app running in a browser](../../../images/counterfit-first-run.png)

    It will be marked as *Disconnected*, with the LED in the top-right corner turned off.

1. Add the following code to the top of `app.py`:

    ```python
    from counterfit_connection import CounterFitConnection
    CounterFitConnection.init('127.0.0.1', 5000)
    ```

    This code imports the `CounterFitConnection` class from the `counterfit_connection` module, which comes from the `counterfit-connection` pip package you installed earlier. It then initializes a connection to the CounterFit app running on `127.0.0.1`, which is an IP address you can always use to access your local computer (often referred to as *localhost*), on port 5000.

    > 💁 If you have other apps running on port 5000, you can change this by updating the port in the code, and running CounterFit using `CounterFit --port <port_number>`, replacing `<port_number>` with the port you want to use.

1. You will need to launch a new VS Code terminal by selecting the **Create a new integrated terminal** button. This is because the CounterFit app is running in the current terminal.

    ![VS Code Create a new integrated terminal button](../../../images/vscode-new-terminal.png)

1. In this new terminal, run the `app.py` file as before. The status of CounterFit will change to **Connected** and the LED will light up.

    ![Counter Fit showing as connected](../../../images/counterfit-connected.png)

> 💁 You can find this code in the [code/virtual-device](code/virtual-device) folder.

😀 Your connection to the hardware was a success!
