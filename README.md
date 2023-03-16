<<<<<<< Updated upstream
# 2023sp-420-MediaTek
<h1 align="center"><img src="https://preview.redd.it/pwpks2a80bj31.gif?width=800&auto=webp&s=48bfc3ad55d7d05c07ff193152deac92c9bb090e" alt="minecraft bee" width="200" height="200 />
<h2 align="center">Welcome to MediaTek's Spelling Bee Game!</h2>
  <h4 align="right">An Application created by Austin An, Devon Fair, Gabe Zimmerman, Noah Barger, and Tessa Hughes</h4>
=======
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>



[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
![Repo Size][repo-size-shield]
![Last Commit][last-commit-shield]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />

  # <div align="center">MediaTek's Spelling Bee Game</div>

  <div align="center">
    Created by Austin An, Devon Fair, Gabriel Zimmermann, Noah Barger, and Tess Hughes</div>
    <br />
  

  

<!-- GETTING STARTED -->
## Getting Started

To run our game locally, you will need to follow these steps.

### Prerequisites


* Python version 3.11.2, which can be downloaded at https://www.python.org/downloads/

### Installation



1. Clone the repo  
  WINDOWS/MAC:
   ```sh
   git clone https://github.com/mucsci-students/2023sp-420-MediaTek
   ```
2. Navigate to the folder inside your terminal  
  WINDOWS/MAC:
   ```sh
   cd path\to\folder\2023sp-420-MediaTek
   ``` 
3. If on MAC make sure pip is installed with the command, if on Windows skip this step.
  MAC:
  ```sh
  python3 -m ensurepip
  ```
4. Install dependencies with the following command  
  WINDOWS/MAC:
   ```sh
   pip install -r requirements.txt 
   ```
5. To build the program, run the following command while still inside the directory  
  WINDOWS/MAC:
   ```sh
   pip install -e .
   ```
  
The game should now be properly installed and ready to play.
 
 ### Running  
 
 
1. To launch the game in GUI mode  
  WINDOWS:
   ```sh
   py SpellingBee.py
   ```
   MAC:
   ```sh
   python3 SpellingBee.py --mac
   ```
2. To launch the game in CLI mode    
  WINDOWS:
   ```sh
   py SpellingBee.py --cli
   ```
  MAC:
  ```sh
  python3 SpellingBee.py --cli
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Test File
  
To run the test file, navigate to the test folder with  
  WINDOWS/MAC:
   ```sh
   cd path\to\folder\2023sp-420-MediaTek\test
   ```
then run the command  
  WINDOWS:
   ```sh
   py unittest.py
   ```
  MAC:
    ```sh
    python3 unittest.py
    ```


<!-- COMMANDS EXAMPLES -->
## Commands

See below for a list of CLI-specific commands and their functionality!
  
* ```!newpuzzle```  
  Generates a new puzzle. You will be given the option to provide your own pangram for puzzle creation.
* ```!showpuzzle```  
  Displays the current puzzle, including all kinds of fun stats.
* ```!showfoundwords```  
  Lists all of the correctly guessed words.
* ```!shuffle```  
  Shuffles the given letters in a random arangement (except the required letter which stays in the center).
* ```!savepuzzle```  
  Saves your puzzle to the root directory.  **NOTE: The GUI version lets you save anywhere on your machine.
* ```!loadpuzzle```  
  Allows you to load a saved puzzle from the root directory.  **NOTE: The GUI version lets you load from anywhere on your machine.
* ```!showstatus```  
  Shows your current rank, points earned, and total points possible.
* ```!help```  
  Displays the list of commands currently accessible.
* ```!exit```  
  Exits the game. You will be asked if you want to save your puzzle to not lose progress.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Meet the Team
  
| [![Tessa Hughes](https://avatars.githubusercontent.com/u/122769747?v=4)](https://github.com/tmhughes1) | [![Austin An](https://avatars.githubusercontent.com/u/113960168?v=4)](https://github.com/auanmu) | [![Devon Fair](https://avatars.githubusercontent.com/u/20361090?v=4)](https://github.com/SteamsDev) | [![Noah Barger](https://avatars.githubusercontent.com/u/98166939?v=4)](https://github.com/noahbarger) | [![Gabe Zimmermann](https://avatars.githubusercontent.com/u/80365452?v=4)](https://github.com/gabe2762) | 
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [Tessa Hughes](https://github.com/tmhughes1)                                                          | [Austin An](https://https://github.com/auanmu)                                                  | [Devon Fair](https://github.com/SteamsDev)                                                          | [Noah Barger](https://github.com/noahbarger)                                                           | [Gabe Zimmermann](https://github.com/gabe2762)                                                          |
>>>>>>> Stashed changes
  
  
  <h3 align="left">Setup and Installation</h3><br />
  
  <p align="left">
  For our game to run on your computer, ensure you have the following installed:
  <ul>
    <li>Latest version of Python, found <a href="https://www.python.org/downloads/">here</a></li>
  </ul><br />
  To install and run the game on your computer, do the following:
  <ul><br />
    <li>Download the most recent version of the repository</li>
    <li>For Windows OS:</li>
        Open your Command Prompt and open the directory of the game folder using <code>cd C:\Users\name\2023sp-420-MediaTek</code>.
        Once inside the directory, type <code>py gameapplication.py</code> OR <code>python3 gameapplication.py</code> to run!</li>
    <li>For Mac OS:</li>
        Open your Terminal and type <code>cd 2023sp-420-MediaTek</code>, ensuring you are in the correct directory where the folder is located first.
        Once inside, type <code>python3 gameapplication.py</code> OR <code>py gameapplication.py</code> to run!</li>
  </ul><br />
  </p>
  <h3>Commands</h3>
  <p>For a list of commands and their functionality, see below!
  <ul>
  <li><code>!newpuzzle</code></li>  Generates a new puzzle. You will be given the option to provide your own pangram for puzzle creation.
  <li><code>!showpuzzle</code></li>  Displays the current puzzle.
  <li><code>!showfoundwords</code></li>  Lists all of the correctly guessed words.
  <li><code>!shuffle</code></li>  Shuffles the given letters in a random arangement (except the required letter which stays in the center).
  <li><code>!savepuzzle</code></li>  Saves your puzzle to your local machine.
  <li><code>!loadpuzzle</code></li>  Allows the you to load a saved puzzle from files, type the file name of the saved puzzle with this command.
  <li><code>!showstatus</code></li>  Shows your current status.
  <li><code>!help</code></li>  Displays the list of commands currently accessible.
  <li><code>!exit</code></li>  Exits the game. You will be asked if you want to save your puzzle to not lose progress.
  </ul>
  </p><br />
  <br />
  <img src="https://64.media.tumblr.com/81e4263afa274df7639a083407fc603a/c2009d127ae92e1d-1d/s640x960/d2fa5e871d801b7f33fe4aa5c111778a3b434d5b.gif" alt="bees in a forest" width="800" height="200" />
  <h3 align="right">Enjoy playing our spelling bee game!</h3>
  <p align="right">(bees not included)</p>
