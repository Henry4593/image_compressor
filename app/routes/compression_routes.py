from flask import Blueprint, redirect, url_for, request, jsonify, send_file, flash
from app.models.users import Users
from app.models.images import Images
from app.models.compression_histories import CompressionHistory
from app.utils.db_utils import DatabaseUtil
from app.utils.image_utils import CompressImage
from flask import current_app as app

compress = Blueprint("compress", __name__)

@compress.route('/api/compress', methods=["POST"])
def compress_not_auth():
    if request.method == "POST":
        database = DatabaseUtil()
        database.connect()
        try:
            files = request.files.getlist('image')
            if not files:
                files = request.files.getlist('files')
            if app.config["CURRENT_USER"]:
                for file in files: 
                    image = CompressImage(file=file, user_id=app.config["CURRENT_USER"])
                    image.compress()
                    user_dict = image.to_dict()
                    database.create_image(user_dict)
                    app.logger.info(f"Compressed image data:{image.to_dict()}")
                    app.logger.info(f'CURRENT USER: {app.config["CURRENT_USER"]}')
                return jsonify({"message": "images compressed successfully"}), 200
            database.close()
            # return redirect(url_for('main.upload_page'))
            return jsonify({"message": "failed to compress the file(s)!"}), 200
        except Exception as e:
            app.logger.error("Error processing file: {}".format(e))
            return jsonify({"message": "failed to compress the file(s)!"}), 400
    if request.method == "GET":
        return jsonify({"message": "Bad request!"}), 400    
    
