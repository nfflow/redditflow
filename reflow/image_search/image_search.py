from sentence_transformers import SentenceTransformer, util
import pickle
from PIL import Image
import os


class ImageSearch:
    def __init__(self, model_name='clip-ViT-B-32', img_dir="images"):
        self.model = SentenceTransformer(model_name)
        self.img_dir = img_dir

    def convert_images(self):
        for filename in os.listdir(self.img_dir):
            if filename.endswith((".png")):
                im1 = Image.open(os.path.join(self.img_dir, filename))
                im1 = im1.convert('RGB')
                im1.save(os.path.join(self.img_dir,
                         filename.replace(".png", ".jpg")))
                os.remove(os.path.join(self.img_dir, filename))

    def load_image_paths(self, folder):
        paths = []
        for filename in os.listdir(folder):
            if filename.endswith((".jpg", "png", "jpeg")):
                paths.append(os.path.join(folder, filename))
        return paths

    def encode_images(self, dirname):
        self.convert_images()
        img_names = self.load_image_paths(dirname)
        img_emb = self.model.encode([Image.open(filepath)
                                     for filepath in img_names],
                                    batch_size=128,
                                    convert_to_tensor=True,
                                    show_progress_bar=True)
        return img_emb, img_names

    def search(self, query, k=3, use_precomputed_embeddings=False,
               threshold_score=0.2):
        if use_precomputed_embeddings:
            emb_filename = 'unsplash-25k-photos-embeddings.pkl'
            # Download dataset if does not exist
            if not os.path.exists(emb_filename):
                util.http_get('http://sbert.net/datasets/' +
                              emb_filename, emb_filename)

            with open(emb_filename, 'rb') as fIn:
                img_names, img_emb = pickle.load(fIn)
            print("Images:", len(img_names))
        else:
            img_emb, img_names = self.encode_images(self.img_dir)
        query_emb = self.model.encode(
            [query], convert_to_tensor=True, show_progress_bar=False)
        hits = util.semantic_search(query_emb, img_emb, top_k=k)[0]
        matched_images = []
        for hit in hits:
            if hit["score"] > threshold_score:
                matched_images.append(img_names[hit['corpus_id']])
        return matched_images
