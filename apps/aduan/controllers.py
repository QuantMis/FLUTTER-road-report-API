from flask import Blueprint, request, render_template, jsonify, flash, abort
from sqlalchemy import desc
import time
from apps.aduan.models import Aduan
from apps import db

aduan_bp = Blueprint('aduan', __name__, url_prefix='/aduan')


@aduan_bp.route('/', methods=['GET', 'POST'])
def senarai_aduan():
    if request.method == "POST":

        request_data = request.get_json()

        image_path = request_data['image_path']
        latitude = request_data['latitude']
        longitude = request_data['longitude']
        address = request_data['address']
        status = request_data['status']

        aduan_baru = Aduan(image_path, latitude, longitude, address, status)

        db.session.add(aduan_baru)
        db.session.commit()

    list_ = []
    senarai_aduan = Aduan.query.all()
    for i in senarai_aduan:
        aduan = {
            "image_path": i.image_path,
            "latitude": i.latitude,
            "longitude": i.longitude,
            "address": i.address,
            "status": i.status,
        }
        list_.append(aduan)

    return jsonify(list_)


@aduan_bp.route('/<int:id>', methods=['GET', 'PUT'])
def satu_aduan(id):
    aduan = Aduan.query.get(id)
    if request.method == "PUT":

        request_data = request.get_json()
        aduan.image_path = request_data['image_path']
        aduan.latitude = request_data['latitude']
        aduan.longitude = request_data['longitude']
        aduan.address = request_data['address']
        aduan.status = request_data['status']
        db.session.commit()

    aduan_serialized = {
        "image_path": aduan.image_path,
        "latitude": aduan.latitude,
        "longitude": aduan.longitude,
        "address": aduan.address,
        "status": aduan.status,
    }

    return jsonify(aduan_serialized)
