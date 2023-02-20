<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<div align="center">
  
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Twitter][twitter-shield]][twitter-url] 

</div>

<h3 align="center">FIVB Beach Player Data Exploration</h3>

  <p align="center">
    Quickly store player details and all tournament info for a list of players from the FIVB Beach Volleyball website.
    <br />
    <br />
    <a href="https://github.com/keatonrproud/FIVB_beach_exploration/issues">Report Bug</a>
    ·
    <a href="https://github.com/keatonrproud/FIVB_beach_exploration/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a small tool I built to store and analyse beach volleyball player data over time and their tournament history for future player development. It has helped with funding presentations and planning for future volleyball player development.


### Built With

[![Python][python-shield]][python-url]
[![Selenium][selenium-shield]][selenium-url]
[![PyCharm][pycharm-shield]][pycharm-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Clone the repo, install the required scripts, and get to exploring:

1) View the sample_output file in outputs to see what your end data will look like.
2) Replace the player names in player_list.csv with the players you want to search for. Some player names can be tricky due to nicknames, which are common in the database.
3) Run the script and view your data!
3b) If players you inputted return a missing player row in the output, you may need to check for their official name as stored in the database.

### Prerequisites

You'll need to install [selenium][selenium-url], [chromedriver-autoinstaller](https://github.com/yeongbin-jo/python-chromedriver-autoinstaller), and [Google Chrome](https://www.google.com/chrome/) to get going with the script.

The chromedriver version should automatically update based on your version of Chrome. If you have issues with the script, it would be worth ensuring your version of Chrome matches the chromedriver installed locally.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/keatonrproud/FIVB_beach_exploration.git
   ```
2. Install any missing packages
   ```sh
   pip install missing_package
   ```
3. Ensure you have Google Chrome installed

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". All feedback is appreciated!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Selenium Docs](https://www.selenium.dev/documentation/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Keaton Proud - [Twitter](https://twitter.com/keatonrproud) - [LinkedIn](https://linkedin.com/in/keatonrproud)- keatonrproud@gmail.com

Project Link: [https://github.com/keatonrproud/FIVB_beach_exploration](https://github.com/keatonrproud/FIVB_beach_exploration)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/keatonrproud/FIVB_beach_exploration.svg?style=for-the-badge
[contributors-url]: https://github.com/keatonrproud/FIVB_beach_exploration/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/keatonrproud/FIVB_beach_exploration.svg?style=for-the-badge
[forks-url]: https://github.com/keatonrproud/FIVB_beach_exploration/network/members
[stars-shield]: https://img.shields.io/github/stars/keatonrproud/FIVB_beach_exploration.svg?style=for-the-badge
[stars-url]: https://github.com/keatonrproud/FIVB_beach_exploration/stargazers
[issues-shield]: https://img.shields.io/github/issues/keatonrproud/FIVB_beach_exploration.svg?style=for-the-badge
[issues-url]: https://github.com/keatonrproud/FIVB_beach_exploration/issues
[license-shield]: https://img.shields.io/github/license/keatonrproud/FIVB_beach_exploration.svg?style=for-the-badge
[license-url]: https://github.com/keatonrproud/FIVB_beach_exploration/blob/main/license
[linkedin-shield]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/keatonrproud
[twitter-shield]: https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white
[twitter-url]: https://twitter.com/keatonrproud
[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://python.org/
[selenium-shield]: https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white
[selenium-url]: https://www.selenium.dev/
[pycharm-shield]: https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green
[pycharm-url]: [https://jupyter.org/](https://www.jetbrains.com/pycharm/)
