# scorange-hugo

Files for scOrange web page in hugo.

## Installation

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
    
## Run

    hugo server

## Guidelines

Following is a set of guidelines for authors of material on scOrange web page.

* Use spell checker (and Grammarly) before submission.

### Guidelines for Workflows

* Markdown file with a workflow description should have the same name as the title of the workflow, all lowercase, with dashes in place of spaces.
* Order workflows from simple to more complex ones.
* Ordering is set by the `weight` parameters. Workflows with higher weight appear first.
* Images on the cover page are listed in `images` parameter. The aspect ratio for these images should strictly be 460 : 280. Use low resolution. Reduce the number of colors in color palette (In Gimp, Image > Mode > Indexed).
