from flask import Flask, jsonify, abort, request
import json
from os import path

class myflask:

    app = Flask(__name__)

    def __init__(self):
        myflask.filename = "data.csv"
        try:
            if str(path.isfile(myflask.filename)):
                with open(myflask.filename) as fh:
                    myflask.inventory = json.load(fh)

        except FileNotFoundError:
            print("Creating invertory for the first time")
            myflask.inventory = [{
                'title': 'sample',
                'dued': 'nothing',
                'done': "False"
            }]
            with open(myflask.filename, "w") as fh:
                json.dump(myflask.inventory, fh)

    @app.route('/app/v1/todo', methods=['POST'])
    def addTask():
        title = request.json['title']
        dued = request.json['dued']

        task = {
            'title': title,
            'dued': dued,
            'done': "False"
        }
        myflask.inventory.append(task)
        with open(myflask.filename, "w+") as fh:
            json.dump(myflask.inventory, fh)
        return jsonify({'task': task}), 201

    def get_tasks_using_title(title):
        for task in myflask.inventory:
            if task['title'] == title:
                return task

    def get_status_using_title(title):
        for task in myflask.inventory:
            if task['title'] == title:
                return task

    @staticmethod
    @app.route('/app/v1/todo/<string:title>', methods=['GET'])
    def getTask(title):
        task_found = myflask.get_tasks_using_title(title)
        if not task_found:
            abort(404)
        else:
            return jsonify({'task': task_found})

    @app.route('/app/v1/todo', methods=['GET'])
    def getAllTask():
        return jsonify({'AllTasks': myflask.inventory}), 200

    @app.route('/app/v1/todo', methods=['PUT'])
    def updateTask():
        req_data = request.get_json()
        title = req_data['title']
        done = req_data['done']

        # Update item in the list
        for d in myflask.inventory:
            if d["title"] == title:
                d["done"] = done
                return jsonify({'updated': d}), 201
        abort (404)

    @app.route('/app/v1/todo', methods=['DELETE'])
    def delTask():
        req_data = request.get_json()
        title = req_data['title']

        for i in range(len(myflask.inventory)):
            if myflask.inventory[i]['title'] == title:
                deletedTask = myflask.inventory[i]
                del myflask.inventory[i]
                with open(myflask.filename, "w+") as fh:
                    json.dump(myflask.inventory, fh)
                return jsonify({'deletedTask': deletedTask}), 200
            # Return response
        abort(404)


myapp = myflask()
myapp.app.run(debug=True)