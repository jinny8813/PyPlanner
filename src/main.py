import os
from pptx import Presentation

os.chdir(r'src')
prs = Presentation('assets/layout-2425-light-chinese.pptx')
prs.save(f'prep.pptx')
