import os, json
from client import Client

if __name__ == "__main__" :
    # Get json file name and generate the path
    json_file_name =  input("Enter your json file name: ")
    current_path = os.path.dirname(__file__)
    json_file_path = os.path.join(current_path, json_file_name)

    with open(json_file_path) as file:
        command = json.loads(
            file.read()
        )

    cl = Client(command)
    cl2 = Client(command)
    cl3 = Client(command)
    for i in range(0, 1000) :
        resp = cl.run_command()
        print(resp)
        resp2 = cl2.run_command()
        print(resp2)
        resp3 = cl3.run_command()
        print(resp3)

    cl.close()
    cl2.close()
    cl3.close()