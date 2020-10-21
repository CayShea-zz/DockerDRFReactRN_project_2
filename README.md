# DockerDRFReactRN_project

## Prerequisites

Ensure you have Python installed.

[Homebrew for Mac](https://brew.sh/)
[Installing Python 3 on Mac OS X](https://docs.python-guide.org/starting/install3/osx/)

Set up your .bash_profile (go to bottom of this README file). If you're using ZSH, you will have to do
some different stuff, setting up .zshrc, compinit, etc. to get completion working nicely and what not.

You should also install virtualenv for Python development within an isolated environment.

[Virtualenv - Installation](https://virtualenv.pypa.io/en/latest/installation.html#)

Optionally virtualenvwrapper extensions may also be installed.

[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)

Ensure you have Docker installed which will also install docker-compose.

[Get Started with Docker](https://www.docker.com/get-started)

If you are working on the UI you will also need to install Yarn.

[Yarn Installation Mac](https://yarnpkg.com/lang/en/docs/install/#mac-stable)



## Set up your .bash_profile if needed.
```bash
vi ~/.bash_profile
# Paste in .bash_profile content below and save.
source ~/.bash_profile
```
### .bash_profile
```
# Setting PATH for Python 3.8
PATH="/Library/Frameworks/Python.framework/Versions/3.8/bin:${PATH}"
export PATH

# Only necessary if using VS Code...
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"

alias python='python3'
alias pip='pip3'
export VIRTUALENVWRAPPER_PYTHON=/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /Library/Frameworks/Python.framework/Versions/3.8/bin/virtualenvwrapper.sh
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
ssh-add
```

