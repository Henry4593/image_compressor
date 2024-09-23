from flask import Blueprint, redirect, url_for, request, jsonify, send_file, send_from_directory
from app.models.users import Users
from app.models.images import Images
from app.models.compression_histories import CompressionHistory
from app.utils.db_utils import DatabaseUtil
from app.utils.image_utils import CompressImage
from flask import current_app as app

compress = Blueprint("compress", __name__)

@compress.route('/api/images', methods=["POST", "GET"])
def compress_auth():
    database = DatabaseUtil()
    database.connect()
    if request.method == "POST":
        try:
            files = request.files.getlist('image') or request.files.getlist('files')

            if not files:
                return jsonify({"message": "No files provided!"}), 400

            if app.config.get("CURRENT_USER"):
                for file in files:
                    image = CompressImage(file=file, user_id=app.config["CURRENT_USER"])
                    image.compress()
                    user_dict = image.to_dict()
                    image_id = database.create_image(user_dict)
                    user_dict["image_id"] = image_id
                    database.create_compression_history(user_dict)
                    app.logger.info(f"IMAGE ID: {image_id}")
                    app.logger.info(f"Compressed image data: {user_dict}")
                    app.logger.info(f'CURRENT USER: {app.config["CURRENT_USER"]}')

                return jsonify({"message": "Images uploaded and compressed successfully"}), 200

            return jsonify({"message": "User not authenticated!"}), 401

        except Exception as e:
            app.logger.error(f"Error processing file: {e}")
            return jsonify({"message": "Failed to compress the file(s)!"}), 500

        finally:
            database.close()
    if request.method == "GET":
        if app.config.get("CURRENT_USER"):
           images = database.get_images(user_id=app.config.get("CURRENT_USER"))
           return jsonify({"images": images})
        else:
            app.logger.error("Server failed to retrieve CURRENT_USER")
            return jsonify({"message": "failed to retrieve user compressed images"})

@compress.route("/api/images/<id>", methods=["GET", "DELETE"])
def get_image(id):
    database = DatabaseUtil()
    database.connect()
    compressed_path = database.get_image(id)
    if not compressed_path:
        return jsonify({"message": f"image with the {id} not found"})
    try:

        return send_file(compressed_path, as_attachment=True)
    except Exception as e:
        return jsonify({"message": "operation failed to download image"})
    finally:
        database.close()

