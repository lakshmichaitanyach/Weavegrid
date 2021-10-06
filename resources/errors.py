from flask_restful import HTTPException

class InvalidPathError(HTTPException):
    pass
class RootDoesNotExistError(HTTPException):
    pass

class FolderAlreadyExistsError(HTTPException):
    pass

class FileDoesNotExistError(HTTPException):
    pass

class FileAlreadyExistsError(HTTPException):
    pass

class FolderNotEmptyError(HTTPException):
    pass


custom_errors = {
    'InavalidPathError': {
        'message': "Invalid Path",
        'status': 401,
    },
    'RootDoesNotExistError':{
        'message': 'Root is Not Defined',
        'status': 404 
    },
     'FileDoesNotExistError':{
         'message':'File does not exist',
        'status': 404

     },
     'FolderAlreadyExistsError':{
         'message': 'Folder already exists',
        'status': 404

     },
     'FileAlreadyExistsError':{
         'message': 'File already exists',
        'status': 404

     },
     'FolderNotEmptyError':{
         'message': 'Folder not empty',
         'status':404
     }
}