import PIL
import torchvision.transforms as transforms
import os
from tqdm import tqdm
from multiprocessing import Pool

def __transform_image(image_path: str):
    image = PIL.Image.open(image_path)
    if not all(image.size):
        crop_size = min(image.size)
        image_transformations = transforms.Compose([transforms.CenterCrop(crop_size), 
                                                    transforms.Resize(1024)])
        image = image_transformations(image)
        image.save(image_path)
    pbar.update(1)
    
    
if __name__ == '__main__':
    
    IMAGE_DIR = '../../unsplash/'
    
    all_images = os.listdir(IMAGE_DIR)
    all_images = os.path.join(IMAGE_DIR, all_images)
    
    pbar = tqdm(total=len(all_images))
    
    with Pool(processes=N_PROCESSES) as pool:
        pool.map(__transform_images, all_images)
            
    
    
    
    