#!/usr/bin/python3
from PIL import Image
import os
from datetime import datetime
from uuid import uuid4
from werkzeug.utils import secure_filename
from flask import current_app as app


class CompressImage:
    time_format = '%Y%m%d_%H%M%S%f'
    SUPPORTED_EXTENSIONS = {
        'jpg', 'jpeg', 'png', 'gif', 'webp'
    }
    IMAGE_EXTENSIONS = {'jpg', 'jpeg', 'webp'}
    PNG_EXTENSIONS = {'png'}
    GIF_EXTENSIONS = {'gif'}

    def __init__(self, file=None, quality=70, compression_level=9, optimization_level=0, duration=0.1, user_id=uuid4()):
        file_extension = file.filename.split(".")[-1]
        self.user_id = user_id

        if file is None or not hasattr(file, 'filename'):
            raise ValueError("Invalid file provided.")
        self.file_extension = file.filename.split(".")[-1].lower()
        if self.file_extension not in self.__class__.SUPPORTED_EXTENSIONS:
            raise ValueError(f"Unsupported file extension: {self.file_extension}")
        self.original_file_name = file.filename
        self.upload_path = os.path.join(app.root_path, "uploads")
        self.compressed_path = os.path.join(app.root_path, "static/compressed")
        self.compressed_file_name = None
        self.compressed_at = None
        self.upload_at = None
        self.compression_status = "pending"
        self.image_file = file
        self.original_size = None
        self.compressed_size = None
        self.image_id = None
        self.compression_start_time = None
        self.compression_end_time = None
        self.duration = None
        self.file_extension = file_extension
        self.quality = quality if file_extension in self.__class__.IMAGE_EXTENSIONS else None
        self.compression_level = compression_level if file_extension in self.__class__.PNG_EXTENSIONS else None
        self.optimization_level = optimization_level if file_extension in self.__class__.GIF_EXTENSIONS else None
        self.duration = duration if file_extension in self.__class__.GIF_EXTENSIONS else None

    def set_compressed_name(self):
        """
        Generates a unique file name for an uploaded file.

        If the file already exists, it appends a numeric suffix to the file name.

        Returns:
            str: The generated file path.
        """
        if not isinstance(self.user_id, str):
            user_id = self.user_id.hex
        else:
            user_id = self.user_id
            try:
                split_userid = user_id.split("-")
                user_id = "".join(split_userid)
            except:
                pass

        full_path = os.path.join(self.compressed_path, self.original_file_name)
        file_name, file_extension = os.path.splitext(os.path.basename(full_path))
        dir_path = os.path.dirname(full_path)
        generated_path = os.path.join(dir_path, f"compressed_{user_id}_{file_name}{file_extension}")

        if not os.path.exists(generated_path):
            self.compressed_path = generated_path
        else:
            num = 1
            while os.path.exists(generated_path):
                if num > 9:
                    num_string = str(num)
                else:
                    num_string = f"0{num}"

                new_name = f"compressed_{user_id}_{file_name}_{num_string}{file_extension}"
                generated_path = os.path.join(dir_path, new_name)
                num += 1
            self.compressed_path = generated_path

        return self.compressed_path
    
    def set_upload_name(self):
        """
        Generates a unique file name for an uploaded file.
        
        If the file already exists, it appends a numeric suffix to the file name.
        
        Returns:
            str: The generated file path.
        """
        if not isinstance(self.user_id, str):
            user_id = self.user_id.hex
        else:
            user_id = self.user_id
            try: 
                split_userid = user_id.split("-")
                user_id = "".join(split_userid)
            except:
                pass
        
        full_path = os.path.join(self.upload_path, self.original_file_name)
        file_name, file_extension = os.path.splitext(os.path.basename(full_path))
        dir_path = os.path.dirname(full_path)
        
        generated_path = os.path.join(dir_path, f"upload_{user_id}_{file_name}{file_extension}")
        num = 1
        while os.path.exists(generated_path):
            if num > 9:
                num_string = str(num)
            else:
                num_string = f"0{num}"
            
            new_name = f"upload_{user_id}_{file_name}_{num_string}{file_extension}"
            generated_path = os.path.join(dir_path, new_name)
            num += 1
        
        self.upload_path = generated_path
        return self.upload_path

    def compress_jpeg(self):
        """
        Compress an image in JPEG/JPG format.

        :param upload_path: The path to the input image.
        :param compressed_path: The path to the output image.
        :param quality: The quality of the compressed image (0-100).
        """
        try:
            image = Image.open(self.upload_path)
            self.compression_start_time = datetime.utcnow()
            image.save(self.compressed_path, format='JPEG', quality=self.quality)
            self.compressed_at = datetime.utcnow()
            self.compression_end_time = self.compressed_at
            self.duration = (self.compression_end_time - self.compression_start_time).total_seconds()
            self.compression_start_time = self.compression_start_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            self.compressed_at = self.compressed_at.strftime('%Y-%m-%d %H:%M:%S.%f')
            self.compression_end_time = self.compression_end_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            self.compression_status = "success"
            app.logger.info("JPEG image compression successful")
        except Exception as e:
            self.compression_status = "failed"
            app.logger.error(f"Error compressing JPEG image: {e}")           

    def compress_png(self):
        """
        Compress an image in PNG format.

        :param upload_path: The path to the input image.
        :param compressed_path: The path to the output image.
        :param compression_level: The compression level of the compressed image (1-9).
        """
        try:
            image = Image.open(self.upload_path)
            self.compression_start_time = datetime.utcnow()
            image.save(self.compressed_path, format='PNG', compress_level=self.compression_level, optimize=True)
            self.compressed_at = datetime.utcnow()
            self.compression_end_time = self.compressed_at
            self.duration = (self.compression_end_time - self.compression_start_time).total_seconds()
            self.compression_start_time = self.compression_start_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            self.compressed_at = self.compressed_at.strftime('%Y-%m-%d %H:%M:%S.%f')
            self.compression_end_time = self.compression_end_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            self.compression_status = "success"
            app.logger.info("PNG image compression successful")
        except Exception as e:
            self.compression_status = "failed"
            app.logger.error(f"Error compressing PNG image: {e}")

    def compress_gif(self):
        """
        Compress an image in GIF format.

        :param upload_path: The path to the input image.
        :param compressed_path: The path to the output image.
        :param optimization_level: The optimization level of the compressed image (0-4).
        :param duration: The duration of each frame in seconds.
        """
        try:
            image = Image.open(self.upload_path)
            self.compression_start_time = datetime.utcnow()
            image.save(self.compressed_path, format='GIF', optimize=self.optimization_level, duration=self.duration)
            self.compressed_at = datetime.utcnow()
            self.compression_end_time = self.compressed_at
            self.duration = (self.compression_end_time - self.compression_start_time).total_seconds()
            self.compression_start_time = self.compression_start_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            self.compressed_at = self.compressed_at.strftime('%Y-%m-%d %H:%M:%S.%f')
            self.compression_end_time = self.compression_end_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            self.compression_status = "success"
            app.logger.info("GIF image compression successful")
        except Exception as e:
            self.compression_status = "failed"
            app.logger.error(f"Error compressing GIF image: {e}")

    def compress_webp(self):
        """
        Compress an image in WebP format.

        :param upload_path: The path to the input image.
        :param compressed_path: The path to the output image.
        :param quality: The quality of the compressed image (0-100).
        """
        try:
            image = Image.open(self.upload_path)
            self.compression_start_time = datetime.utcnow()
            image.save(self.compressed_path, format='WEBP', quality=self.quality, lossless=True)
            self.compressed_at = datetime.utcnow()
            self.compression_end_time = self.compressed_at
            self.duration = (self.compression_end_time - self.compression_start_time).total_seconds()
            self.compression_start_time = self.compression_start_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            self.compressed_at = self.compressed_at.strftime('%Y-%m-%d %H:%M:%S.%f')
            self.compression_end_time = self.compression_end_time.strftime('%Y-%m-%d %H:%M:%S.%f')
            self.compression_status = "success"
            app.logger.info("WebP image compression successful")
        except Exception as e:
            self.compression_status = "failed"
            app.logger.error(f"Error compressing WebP image: {e}")

    def compress(self):
        extracted_file_ext = self.original_file_name.split(".")[-1]
        if extracted_file_ext in self.__class__.SUPPORTED_EXTENSIONS:
            self.set_upload_name()
            self.set_compressed_name()
            self.save_file()

            if extracted_file_ext in {"jpeg", "jpg"}:
                try:
                    self.compress_jpeg()
                    self.compressed_size = os.path.getsize(self.compressed_path)
                    self.compression_status = "success"
                    return self.compression_status
                except:
                    self.compression_status = "failed"
                    return self.compression_status
            elif extracted_file_ext in {"png"}:
                try:
                    self.compress_png()
                    self.compression_status = "success"
                    self.compressed_size = os.path.getsize(self.compressed_path)
                    return self.compression_status    
                except:
                    self.compression_status = "failed"
                    return self.compression_status
            elif extracted_file_ext in {"gif"}:
                try:
                    self.compress_gif()
                    self.compression_status = "success"
                    self.compressed_size = os.path.getsize(self.compressed_path)
                    return self.compression_status
                except:
                    self.compression_status = "failed"
                    return self.compression_status
            elif extracted_file_ext in {"webp"}:
                try:
                    self.compress_webp()
                    self.compression_status = "success"
                    self.compressed_size = os.path.getsize(self.compressed_path)
                    return self.compression_status
                except:
                    self.compression_status = "failed"
                    return self.compression_status

    def save_file(self):
        filename = secure_filename(self.image_file.filename)
        if filename:
            self.image_file.save(self.upload_path)
            self.upload_at = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
            self.original_size = os.path.getsize(self.upload_path)
        return filename
    
    def to_dict(self):
        """
        Create a dictionary from the CompressImage class instance.
        """
        try:
            new_dict = self.__dict__
            instance_dict = {}
            for key, value in new_dict.items():
                if value is None:
                    continue
                instance_dict[key] = value
            app.logger.info(instance_dict)
            return instance_dict
        except Exception as e:
            app.logger.error(e)

    def __repr__(self):
        return f"CompressImage(file={self.original_file_name}, quality={self.quality}, compression_level={self.compression_level}, optimization_level={self.optimization_level}, duration={self.duration}, user_id={self.user_id})"
      