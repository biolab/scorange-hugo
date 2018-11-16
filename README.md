# scorange-hugo

Files for scOrange web page in hugo.

### Installation

If you are on macOS and using Homebrew, you can install Hugo with the following one-liner:

	brew install hugo

If you are on a Windows machine and use Chocolatey for package management, you can install Hugo with the following one-liner:
```sh
choco install hugo -confirm
```

If you are on Debian or Ubuntu, you can install Hugo with the following one-liner:

    sudo apt-get install hugo
    
To prepare the files for the widget documentation, do (clones Orange add-ons with documentation, copies markdown files to content/widget-catalog):

    git init submodule
    git submodule update
    python copy.pu
    
### Run

    hugo server
