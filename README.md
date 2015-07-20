# Take Home Test in Python (3, of course)
## Set Up
1. Install python3, pip3, and libmagic for your OS.

  Yum, APT, and Homebrew all work well for this.
2. Set up your python dependencies.

        virtualenv -p python3 venv
        source venv/bin/activate
        pip3 install -r requirements.txt

3. ...
4. Profit (or, at least employment).

## Running It

    python3 crawler.py --help

## Current Limitations
1. Only uses file extensions (.txt, .zip)
2. Only goes into .zip and not .tgz/.tar.gz
3. No error handling... shame on me
