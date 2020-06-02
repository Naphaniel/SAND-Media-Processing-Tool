import subprocess


class VideoProcessing:
    def __init__(self, video_name, unprocessed_path, processed_path):
        self.video_name = video_name
        self.unprocessed_path = unprocessed_path
        self.processed_path = processed_path

    def split_video(self) -> None:
        video_no_type = self.video_name.split('.')[0]
        unprocessed_video_path = self.unprocessed_path + '/' + video_no_type
        print(self.unprocessed_path)
        subprocess.run(['mkdir', video_no_type], cwd=self.unprocessed_path, shell=True)
        subprocess.run(['move', self.video_name, video_no_type],
                       cwd=self.unprocessed_path,shell=True)
        subprocess.run(['mkdir', video_no_type], cwd=self.processed_path, shell=True)
        subprocess.run(['ffmpeg', '-i', self.video_name, 'frame%04d.jpg',
                        '-hide_banner'], cwd=unprocessed_video_path, shell=True)

    def combine_images(self):
        pass
