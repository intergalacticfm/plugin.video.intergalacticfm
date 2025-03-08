# Intergalactic FM TV video plugin for Kodi

![Intergalactic FM TV icon](resources/icon.png?raw=true)

## Installation

This add-on can be installed directly from Kodi's main repository and it will
update itself. For more information, see
http://kodi.wiki/view/Add-on:Intergalactic_FM_TV

Stepts to take to install from the Kodi main repository are:
1. Go to **Add-ons** in the main menu
2. Go to the **Add-on browser** (the box icon at the top left of the screen)
3. Choose **Install from repository**
4. Choose **Video add-ons**
5. Navigate to **Intergalactic FM TV** and select it
6. Choose **Install**

### Installing Kodi

Instructions for installing Kodi can be found here: https://kodi.tv/download

## Screenshots

![Screenshot 1](screenshots/s1.png?raw=true)

![Screenshot 2](screenshots/s2.png?raw=true)

![Screenshot 3](screenshots/s3.png?raw=true)

## Development

If you are a developer and you know what you are doing, the developement
version of this add-on can be installed by the following steps:
1. Go to **Add-ons** in the main menu
2. Navigate to previously installed add-on **Intergalactic FM TV**
3. Long-press the add-on and choose **Information**
4. Choose **Uninstall**
5. Download in a web browser
https://github.com/intergalacticfm/plugin.video.intergalacticfm/archive/refs/heads/develop.zip
6. Navigate up and go to the **Add-on browser**
7. Choose **Install from zip file**
8. Navigate to the directory where the zip file has been downloaded
9. Install the file **master.zip**

See https://www.intergalactic.fm/js/playing-now_415.js for stream details.

Install

    pip install kodi-addon-checker

and run

    kodi-addon-checker --branch matrix ../plugin.video.intergalacticfm

## Testing

The latest version of this plugin at the time of testing has been tested on the
following configurations for Kodi.

|            | Ubuntu       | Debian / Raspberry Pi OS | Android | LibreELEC |
|------------|--------------|--------------------------|---------|-----------|
| 21 Omega   | 22.04 Jammy  | 12 Bookworm              | 11      | no test   |
| 19 Matrix  | 21.10 Impish | 11 Bullseye              | no test | no test   |
| 18 Leia    | 19.04 Disco  | 10 Buster                | 09 Pie  | 09        |
| 17 Krypton | 19.04 Disco  | 09 Stretch               | 09 Pie  | 08        |

In general, the combination of latest stable version are supported. Most likely
also all combinations with the one-but-latest versions of Kodi and an operating
system are supported.

## See also

See also the audio plugin called Intergalactic FM at
http://kodi.wiki/view/Add-on:Intergalactic_FM and
https://github.com/intergalacticfm/plugin.audio.intergalacticfm

## Thanks

For version 2, thanks go to [Dreamer](https://github.com/dromer) and
[Pander](https://github.com/PanderMusubi) for developing and maintining it. For
version 1, thanks go to the authors of the original add-on that was developed
for Channel 31 and forked from
https://github.com/DamonToumbourou/plugin.video.c31

Credits go to [Yulia Vilenksy](http://yuliavilensky.com) for persmission to use
her photograph used as fanart.

Last but not least, thank you (I-f)[https://en.wikipedia.org/wiki/I-F] and
others for creating [Intergalactic FM](https://intergalacticfm.com) and
embracing new initiatives and technologies to keep us all in musical orbit.

*NO STATION SUCH DEDICATION*
