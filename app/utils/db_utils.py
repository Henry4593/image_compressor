import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import mysql.connector
from app.models.base_model import Base
from app.models.compression_histories import CompressionHistory
from app.models.users import Users
from app.models.images import Images
import re
import bcrypt
from sqlalchemy.exc import IntegrityError
from flask import current_app as app


class DatabaseUtil:
    """
    This class encapsulates database interaction logic.
    """

    def __init__(self):
        self.engine = None
        self.session = None
    
    def create_database(self):
        try:
            load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))
        except:
            pass
        db = mysql.connector.connect(
        host=os.getenv('COMPRESSIO_HOST'),
        user=os.getenv('COMPRESSIO_USER'),
        passwd=os.getenv('COMPRESSIO_PASSWORD')
        )
        with db.cursor() as cursor:
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {os.getenv("COMPRESSIO_DB")}')
        return db

    def connect(self):
        """
        Connects to the database using environment variables.
        """
        load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))
        self.engine = create_engine(os.getenv("DATABASE_URL"))
        Base.metadata.create_all(bind=self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def close(self):
        """
        Closes the database connection.
        """
        if self.session:
            self.session.close()

    def create_user(self, user_data):
        """
        Creates a new user in the database.
        """
        try:
            user = Users(
                first_name=user_data.get("firstName"),
                last_name=user_data.get("lastName"),
                username=user_data.get("username"),
                email=user_data.get("email"),
                password_hash=self.generate_hashpasswd(user_data.get("password"))
            )
            self.session.add(user)
            self.session.commit()
            return user
        except IntegrityError as e:
            self.session.rollback()
            app.logger.error(f"Failed to create user: {e}")
            return None
        finally:
            self.close()

    def generate_hashpasswd(self, password):
        """
        Generates a hashed password using bcrypt.
        """
        password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password, salt)
        return hashed_password

    def check_hashpasswd(self, user_id, password):
        """
        Checks if a provided password matches the hashed password for a user.
        """
        try:
            user = self.session.query(Users).filter_by(user_id=user_id).first()
            stored_password = user.password_hash.encode('utf-8')
            user_password = password.encode('utf-8')
            return bcrypt.checkpw(user_password, stored_password)
        except Exception as e:
            app.logger.error(f"Failed to check password for user {user_id}: {e}")
            return False
        finally:
            self.close()

    def get_user(self, user_id=None, email=None, username=None):
        """
        Retrieves a user by their ID.
        """
        try:
            user = self.session.query(Users).filter_by(user_id=user_id).first()
            email = self.session.query(Users).filter_by(email=email).first()
            username = self.session.query(Users).filter_by(username=username).first()
            if user:
                user_dict = user.__dict__
                return {k: v for k, v in user_dict.items() if k != '_sa_instance_state'}
            elif email:
                user_dict = email.__dict__
                return {k: v for k, v in user_dict.items() if k != '_sa_instance_state'}
            elif username:
                user_dict = username.__dict__
                return {k: v for k, v in user_dict.items() if k != '_sa_instance_state'} 
            else: 
                return None
        except Exception as e:
            app.logger.error(f"Failed to get user {user_id}: {e}")
            return None
        finally:
            self.close()

    def get_users(self):
        """
        Retrieves all users as a dictionary.
        """
        try:
            users = self.session.query(Users).all()
            user_list = [user.__dict__ for user in users]
            # Clean user dictionaries (similar to get_user)
            cleaned_users = {user["user_id"]: {k: v for k, v in user.items() if k != '_sa_instance_state'} for user in user_list}
            return cleaned_users
        except Exception as e:
            app.logger.error(f"Failed to get all users: {e}")
            return None
        finally:
            self.close()

    def create_compression_history(self, compression_history_data):
        """
        Creates a new compression history record in the database.
        """
        compression_history = CompressionHistory(
            image_id=compression_history_data.get("image_id"),
            compression_start_time=compression_history_data.get("compression_start_time"),
            compression_end_time=compression_history_data.get("compression_end_time"),
            duration=compression_history_data.get("duration"),
            result=compression_history_data.get("compression_status"),
            user_id=compression_history_data.get("user_id")
        )
        try:
            self.session.add(compression_history)
            self.session.commit()
        except:
            self.session.rollback()

    def get_compression_histories(self, user_id=None):
        """
        Retrieves compression history records for a specific user.
        """
        try:
            compression_history = self.session.query(CompressionHistory).filter_by(user_id=user_id)
            compression_history_dict = compression_history.__dict__
            new_dict = {}
            for key, value in compression_history_dict.items():
                if key != '_sa_instance_state':
                    new_dict[key] = value
            return new_dict
        except:
            app.logger.error("failed to retrieve compression history for the user")
            return None


    def create_image(self, image_data):
        """
        Creates a new image record in the database.
        """
        image = Images(
                user_id=image_data.get("user_id"),
                filename=image_data.get("original_file_name"),
                original_path=image_data.get("upload_path"),
                compressed_path=image_data.get("compressed_path"),
                upload_date=image_data.get("upload_at"),
                compression_date=image_data.get("compressed_at"),
                original_size=image_data.get("original_size"),
                compressed_size=image_data.get("compressed_size"),
                compression_status=image_data.get("compression_status"),
                image_format=image_data.get("file_extension")
            )
        try:
            self.session.add(image)
            self.session.commit()
            return image.image_id  # Return the ID of the newly created image
        except Exception as e:
            self.session.rollback()  # Rollback in case of error
            app.logger.error(f"Failed to create image record: {e}")
            return None  # Or raise an exception based on your error handling strategy
        

    def get_images(self, user_id=None):
        """
        Retrieves image records for a specific user.
        """
        try:
            images = self.session.query(Images).filter_by(user_id=user_id).all()
            images_list = []

            for image in images:
                image_dict = {}
                for key, value in image.__dict__.items():
                    if key != '_sa_instance_state':
                        image_dict[key] = value
                images_list.append(image_dict)
            
            return images_list
        except Exception as e:  # Catch specific exceptions
            app.logger.error(f"Error retrieving user images: {e}")
            return None
        finally:
            self.close()

    def get_image(self, image_id):
        try:
            if image_id:
                image = self.session.query(Images).filter_by(image_id=image_id).first()

                compressed_image_path = image.compressed_path
                return compressed_image_path
        except Exception as e:
            app.logger.error("Error: cant fetch image")
            return None
        finally:
            self.close()