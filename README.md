# DITA2Trisoft Fixer

SDL's DITA2Trisoft tool, used for importing DITA into SDL, sometimes fails
to generate the `filemap.xml` file properly. If you get an error saying that
the field FMASTERTYPE or FMODULETYPE does not have enough values, then 
an `ishfield` element is missing from one or more `ishfields` elements.

```<ishfield name="FMODULETYPE" level="logical">Task</ishfield>```

`fixfilemap.py` corrects for these error messages:

# ```The field "FMASTERTYPE" does not have enough values```
# ```The field "FMODULETYPE" does not have enough values```

### Installation

1. [Install Python 2.7](https://www.python.org/download/releases/2.7.8/)
2. [Install
BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup).
3. `git clone https://github.com/tintinno/fixfilemap`
4. `cd fixfilemap`

### Fixing `filemap.xml`

1. If necessary, create a ~/Desktop/import directory.
2. Open DITA2Trisoft.
3. Set the Conversion Output folder to ~/Desktop/import.
4. Click Next.
5. Open the command line.
6. Navigate to the directory where you downloaded the script.
7. Run `python fixfilemap.py`.
8. Click Next to upload your content to SDL.
