# coding=utf8
import json
import requests


class JsonHtml:
    def __init__(self, url):
        data = self.read_json(url)
        # print(data)
        # print(self.__render_header(data[0]))
        header = self.__render_header(data[0])

        # print(self.__render_body(data))
        body = self.__render_body(data)

        self.read_template("template.html", header, body)

    def read_template(self, template, header, body):

        # Read in the file
        with open(template, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(' <!--tableheader-->', header)
        filedata = filedata.replace(' <!--tablebody-->', body)

        # Write the file out again
        with open('tabelle.html', 'w') as file:
            file.write(filedata)

    def read_json(self, url):
        response = requests.get(url)
        return json.loads(response.text)

    def __render_header(self, head: list):

        header = "<tr>\n"
        for h in head.keys():
            header += "<th>" + h + "</th>\n"
        header += "</tr>\n"
        return header

    def __render_body(self, data):
        body = "<tr>\n"
        for d in data:
            for field in d.values():
                body += "<td>" + field + "</td>\n"
            body += "</tr>\n"
        return body


json_html = JsonHtml(
    "https://raw.githubusercontent.com/walter-rothlin/Source-Code/master/DatenFiles/CSV/Adressliste.json")
