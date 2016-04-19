import CodeGenV1
from sys import argv
import json

if __name__ == "__main__":
    test_application = {"apps": ["test_app"]}
    file_path = argv[0]
    parsed_route = json.loads(argv[1])

    vgen = CodeGenV1.VenomGen()
    vgen.start(file_path)
    vgen.write_header(test_application)
    vgen.write_route(parsed_route)

    vgen.generate(file_path)
