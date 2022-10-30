import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate
import docx
from controller.CurriculumController import CurriculumController
from definitions import DATA_DIR


cc = CurriculumController()
cc.create_curriculum(path_doc=f"{DATA_DIR}/template/curriculum-vitae.docx")
