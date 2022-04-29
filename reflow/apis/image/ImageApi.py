from .img_utils import scrape_images, image_classify


class ImageApi:
    def __init__(self, config):
        self.config = config


output_paths = image_classify(config)
print(output_paths)

if os.path.exists('filtered_images'):
    shutil.rmtree('filtered_images')

os.mkdir('filtered_images')

for path in output_paths:
    shutil.copy(path, 'filtered_images/')
