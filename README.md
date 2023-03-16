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
  WINDOWS:
   ```sh
   git clone https://github.com/mucsci-students/2023sp-420-MediaTek
   ```
2. Navigate to the folder inside your terminal  
  WINDOWS:
   ```sh
   cd path\to\folder\2023sp-420-MediaTek
   ``` 
3. To build the program, run the following command while still inside the directory  
  WINDOWS:
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
2. To launch the game in CLI mode    
  WINDOWS:
   ```sh
   py SpellingBee.py --cli
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Test File
  
To run the test file, navigate to the test folder with  
  WINDOWS:
   ```sh
   cd path\to\folder\2023sp-420-MediaTek\test
   ```
then run the command  
  WINDOWS:
   ```sh
   py unittest.py
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
  
  
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/mucsci-students/2023sp-420-MediaTek.svg?style=for-the-badge&color=red
[contributors-url]: https://github.com/mucsci-students/2023sp-420-MediaTek/graphs/contributors
[repo-size-shield]: https://img.shields.io/github/repo-size/mucsci-students/2023sp-420-MediaTek.svg?style=for-the-badge&color=success
[last-commit-shield]: https://img.shields.io/github/last-commit/mucsci-students/2023sp-420-MediaTek.svg?style=for-the-badge&color=9cf
[issues-shield]: https://img.shields.io/github/issues/mucsci-students/2023sp-420-MediaTek.svg?style=for-the-badge&color=yellow
[issues-url]: https://github.com/mucsci-students/2023sp-420-MediaTek/issues
[license-shield]: https://img.shields.io/github/license/mucsci-students/2023sp-420-MediaTek.svg?style=for-the-badge&color=blueviolet
[license-url]: https://github.com/mucsci-students/2023sp-420-MediaTek/blob/master/LICENSE.txt
