from flask import jsonify, request


class BaseService:
    @staticmethod
    def create(controller):
        data, error = controller.create(request.json)
        response = data if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    @staticmethod
    def update(controller):
        data, error = controller.update(request.json)
        response = data if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    @staticmethod
    def get_by_id(controller, _id):
        data, error = controller.get_by_id(_id)
        response = data if not error else {'error': error}
        status_code = 200 if data else 404 if not error else 400
        return jsonify(response), status_code

    @staticmethod
    def get_all(controller):
        data, error = controller.get_all()
        response = data if not error else {'error': error}
        status_code = 200 if data else 404 if not error else 400
        return jsonify(response), status_code

    @staticmethod
    def get_report(controller):
        data, error = controller.get_report()
        response = data if not error else {'error': error}
        status_code = 200 if data else 404 if not error else 400
        return jsonify(response), status_code
