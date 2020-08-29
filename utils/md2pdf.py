import pypandoc

''' if running for first time, run this snippet

# expects an installed pypandoc: pip install pypandoc
from pypandoc.pandoc_download import download_pandoc
# see the documentation how to customize the installation path
# but be aware that you then need to include it in the `PATH`
download_pandoc()

#note for later: Put this in setup.py @Josh TODO://

'''

# This is all just making the file into one nice long string
f = open("../assignment_dates.md")
string = f.readlines()
string = "".join(string)

output = pypandoc.convert_text(string, 'pdf', outputfile="../output.pdf", format="md", extra_args=['-H','../static_files/options.sty'])
