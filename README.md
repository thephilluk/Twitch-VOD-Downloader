
<!-- PROJECT LOGO -->
<br />
<div align="center">

<h3 align="center">Twitch VOD Downloader</h3>

  <p align="center">
    A simple Twitch VOD Downloading script built upon <a href="https://github.com/lay295/TwitchDownloader">TwitchDownload made by lay295</a>
    <br />
    <a href="https://github.com/thephilluk/Twitch-VOD-Downloader/blob/main/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/thephilluk/Twitch-VOD-Downloader/issues">Report Bug</a>
    ·
    <a href="https://github.com/thephilluk/Twitch-VOD-Downloader/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

So I needed a way to download all VODs by a certain Twitch streamer and not just once but periodically. 
So in typical Developer fashion I decided to spend multiple hours automating this process rather than getting started doing it manually. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python 3
* Python requests module
  ```sh
  pip install requests
  ```

### Installation

1. Clone the repo
2. Download the latest TwitchDownloader from <a href="https://github.com/lay295/TwitchDownloader">here</a>
3. Place the .exe file into the same folder as the python script
4. Create a Twitch Application <a href="https://dev.twitch.tv/console">here</a>
5. Copy the Client ID and the Client Secret into the Python file

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

* Open the File in any Text Editor
* Add the Channel Name from which you want to Download the VODs at the Top
* (optional) create a `last.txt` file with a Date (format: dd.mm.yyyy) to only download VODs AFTER this date
* Open CMD or any other type of Terminal and run the file
* If you followed all of the steps it should start downloading the VODs one after another and place them in seperate subfolders for each day. It will include full Chat logs by default

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Check the current directory for already downloaded VODs

See the [open issues](https://github.com/thephilluk/Twitch-VOD-Downloader/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Philip - Currently not available via E-Mail

Project Link: [https://github.com/thephilluk/Twitch-VOD-Downloader](https://github.com/thephilluk/Twitch-VOD-Downloader)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
