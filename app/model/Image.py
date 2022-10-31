from PIL import Image as Img
from definitions import IMAGE_DIR

class Image:
    def image_resize(self, img_path_to_resize:str, name_of_new_image:str) -> str:
        img = Img.open(img_path_to_resize)
        newimg = img.resize((500, 1000))
        
        path_to_new_img = f"{IMAGE_DIR}/{name_of_new_image}.png"
        newimg.save(f"{path_to_new_img}")
        
        return path_to_new_img