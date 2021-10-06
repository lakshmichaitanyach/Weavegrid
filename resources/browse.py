from flask import Response, request,jsonify, request, make_response, abort, render_template
from flask_restful import Resource, reqparse
from flask_cors import CORS

import sys 
import time
import json
import os
from os import environ
from pathlib import Path

import stat
from stat import S_ISREG, ST_CTIME, ST_MODE, ST_SIZE, ST_UID, ST_GID
from dotenv import load_dotenv
from resources.errors import RootDoesNotExistError, InvalidPathError, FolderAlreadyExistsError, FileDoesNotExistError, FileAlreadyExistsError, FolderNotEmptyError



load_dotenv()
#check whether there is body
path_args = reqparse.RequestParser()
path_args.add_argument("root", type=str, help="path to the root directory is required", required= True)


def get_file_contents(path):
    """
    helper function to dump text file data 

    path: path of the file
    """
    result = {}
    data = []
    result.update(get_meta_data(path))
    ext = os.path.splitext(path)[-1].lower()
    if ext == ".txt":
        with open(path) as f:
            data = f.readlines()
    result["data"] = data
    response = json.dumps(result)
    return response

def get_meta_data(path):
    """
    helper function to return meta data of file

    path : path of the file
    """
    stats = os.stat(path)
    result = {}
        
    result["permissions"] = stat.filemode(stats[ST_MODE])
    result["size"] = stats[ST_SIZE]
    result["uid"] = stats[ST_UID]
    date_created = stats[ST_CTIME]
    result["created_at"] = time.ctime(date_created)
        
    return result

def get_directory_contents(path):
    """
    helper function to get contents of directory

    param path: path to the directory
    """

    result = {}
    files = {}
    directories = []
    directory_contents = os.listdir(path)
    for content in directory_contents:
        if os.path.isfile(content):
            files[content] = get_meta_data(content)
        else:
            directories.append(content)
    result.update(files)
    result["dir"] = directories
    return result

def createFile(input, path):
    """
    function to create file

    input: input body from user
    path: path of file
    """
    try:
        filename = input['filename']
        if not os.path.exists(filename):
            if not input['file-content']:
                with open(os.path.join(path, filename), 'w') as fp:
                    pass
            else:
                content = input['file-content']
                with open(os.path.join(path, filename), 'w') as fp:
                    fp.write(content)
            return "File created successfully", 200
    except FileExistsError:
        raise FileAlreadyExistsError
    except Exception:
        raise InvalidPathError




def createFolder(input, path):
    """
    function to create folder
    input: input from user, folder-name
    path: path to create folder
    """
    try:
        folder_name = input['foldername']
        if not os.path.exists(folder_name):
            folder_path = os.path.join(path, folder_name)
            os.mkdir(folder_path)
        return "Folder created successfully", 200
    except FileExistsError:
        raise FolderAlreadyExistsError


class RootAPI(Resource):
    """
    The api endpoint called when the application 
    started.
    """
    def get(self):
        """
        get root content
        """
        try:
            path = environ.get('ROOT')
            if not path:
                abort("Please enter the root")
            if os.path.isfile(path):
                response = get_file_contents(path)
                return response, 200
            else:
                response = get_directory_contents(path)
                return response, 200
        except Exception:
            raise RootDoesNotExistError

    def post(self):
        """
        post root to the system from user
        """
        try:
            user_input = request.get_json()
            path = user_input['root']
            environ['ROOT'] = path
            return {"message":"Root registered"}, 200
        except Exception:
            raise InvalidPathError



class BrowseAPI(Resource):
    """
    Api to Browse through the files and directories once
    the root is given
    """
    def get(self, req_path):
        """
        Function takes the path from user and appends to root, from there displays content of the folder or the file
        req_path: it is the requested path to the file or folder that the user want to look
        """
        try:
            path = os.path.join(environ['ROOT'], req_path)
            if os.path.isfile(path):
                response = get_file_contents(path)
                return response, 200
            else:
                response = get_directory_contents(path)
                return response, 200
        except Exception:
            raise InvalidPathError

    

    def delete(self, req_path):
        try:
            path = os.path.join(environ['ROOT'], req_path)
            if os.path.exists(path):
                if os.path.isfile(path):
                    os.remove(path)
                    return "File deleted successfully", 200
                else:
                    if len(os.listdir(path)) == 0:
                        os.rmdir(path)
                    return "Folder deleted successfully", 200
        except FileNotFoundError:
            raise FileDoesNotExistError
        except Exception:
            raise FolderNotEmptyError
        

class CreateFolder(Resource):
    """
    endpoint to create folder
    """
    def post(self, req_path=None):
        try:
            path = environ['ROOT']
            if req_path:
                path = os.path.join(environ['ROOT'], req_path)
            user_input = request.get_json()
            createFolder(user_input, path)
        except Exception:
            raise InvalidPathError

class CreateFile(Resource):
    """
    endpoint to create file
    """
    def post(self, req_path=None):
        try:
            path = environ['ROOT']
            if req_path:
                path = os.path.join(environ['ROOT'], req_path)
            user_input = request.get_json()
            createFile(user_input, path)
        except Exception:
            raise InvalidPathError
                

