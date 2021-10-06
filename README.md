# Browse File System Rest API

This application takes root as input from user
and lets user browse the filesystem. If the path is given to directory 
it lists contents of directory or if it is file, it dumps the data of text file along with permissions, owner id, size, updated date and time.


* This application uses *Flask* and *Flask-Restful* 
* *os* for accessing filesystem of the user

## Assumptions:
1. The file system is the filesystem of user's computer.
2. Root is assumed as the starting point and cannot be proceeded backwards. 
3. Only files details are given and rest of the directories are listed in a list.
4. in case of windows as owner does not support owner id is returned



The application server is in *application.py*

To run locally on machine:
```
python application.py
```

To run in docker 
```
 docker build -t docker_image_name -f Dockerfile.
 docker run -dp 5000:5000 --env ROOT=path docker_image_name
```
 


# Post the root

## Request

`POST/`

```
curl -X POST http://127.17.0.2:5000/ -H 'Content-Type: application/json' -d '{"root":"//root//path//"}'
```
## Response
```
{
    "message": "Root registered"
}
```



# Get the root file or Directory content
## Request

`GET/`
```
curl -X GET http://127.17.0.2:5000/
```
## Response
```
 {"dir": [
        ".anaconda",
        ".AndroidStudio3.5",
        ".bash_history",
        ".cache",
        ".cisco",
        ".conda",
        ".condarc",
        ".config",
        ".docker",
        ".ebookreader",
        ".eclipse",
        ".emulator_console_auth_token",
        ".git-credentials"]
  }
```

# Get directory or file content
## Request

`GET/<req_path>`

```
curl -X GET http://127.17.0.2:5000/?req_path=Weavegrid

```

## Response
```
{
    "application.py": {
        "permissions": "-rw-rw-rw-",
        "size": 3015,
        "uid": 0,
        "created At": "Tue Sep 21 21:27:35 2021"
    },
    "only.txt": {
        "permissions": "-rw-rw-rw-",
        "size": 2815,
        "uid": 0,
        "created At": "Tue Sep 21 19:18:18 2021"
    },
    "requirements.txt": {
        "permissions": "-rw-rw-rw-",
        "size": 211,
        "uid": 0,
        "created At": "Wed Sep 22 02:26:47 2021"
    },
    "test.py": {
        "permissions": "-rw-rw-rw-",
        "size": 123,
        "uid": 0,
        "created At": "Wed Sep 22 02:41:21 2021"
    },
    "Weave Grid Coding Exercise.pdf": {
        "permissions": "-rw-rw-rw-",
        "size": 65081,
        "uid": 0,
        "created At": "Tue Sep 21 11:51:59 2021"
    },
    "dir": [
        "venv"
    ]
}
```

## Response
```
{
"permissions": "-rw-rw-rw-",
        "size": 123,
        "uid": 0,
        "created At": "Wed Sep 22 02:41:21 2021",
        "data":"this is sample text file"
}
```


# Create Folder
## Request

`POST/create-folder/root`

```

curl -X POST http://127.17.0.2:5000/create-folder/root -H 'Content-Type: application/json' -d '{"folder-name":"testfolder"}'

```
`POST/create-folder/{optional: req_path}`

```
curl -X POST http://127.17.0.2:5000/create-folder/ -H 'Content-Type: application/json' -d '{"folder-name":"testfolder"}'
```

## Response
```
Folder created Successfully
```


# Create file 
## Request

`POST/create-file/root`

```
curl -X POST http://127.17.0.2:5000/create-file/root -H 'Content-Type: application/json' -d '{"file-name":"testfile", "content": "test data"}'

```

`POST/create-file/`

```
curl -X POST http://127.17.0.2:5000/create-file/ -H 'Content-Type: application/json' -d '{"file-name":"testfile", "content": "test data"}'
```

```
File created successfully.
```


# Delete a File or Folder
## Request

`DELETE/file or folder name`

```
curl -X DELETE http://127.17.0.2:5000/?req_path=testfile.txt

```
## Response
```
File deleted successfully.

```

