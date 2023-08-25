import shutil


class Zip:
    def __init__(self):
        self.output_zip_filename = None
        self.folder_to_zip = None

    def zip_file(self, folder_path, zipped_file_name):
        self.folder_to_zip = folder_path
        self.output_zip_filename = zipped_file_name
        destination = "../"

        # Create the zip archive using shutil.make_archive
        shutil.make_archive(destination+self.output_zip_filename, 'zip', self.folder_to_zip)

        print(f'Zip archive "{self.output_zip_filename}" created.')
