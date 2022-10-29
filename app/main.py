import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate
import docx

from controller.CurriculumController import CurriculumController


cc = CurriculumController()
cc.create_curriculum(path_doc="data/template/curriculum-vitae.docx")
