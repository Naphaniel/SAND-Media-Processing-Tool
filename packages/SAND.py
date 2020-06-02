from packages.SAND_features.sand_function import sand_function


class SAND:
    def __init__(self, unprocessed_image_path, processed_output_path, model_name, img_index_range):
        self.unprocessed_image_path = unprocessed_image_path
        self.processed_output_path = processed_output_path
        self.model_name = model_name
        self.img_index_range = img_index_range

    def process_image(self) -> None:
        sand_function(
            self.model_name,
            self.unprocessed_image_path,
            self.processed_output_path,
            self.img_index_range)
