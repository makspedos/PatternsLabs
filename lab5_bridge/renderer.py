from abc import ABC, abstractmethod
class Renderer:
    @abstractmethod
    def render(self, data:dict):
        pass

class HtmlRenderer(Renderer):
    def render(self, data:dict) ->str:
        html = f"<html><head><title>{data['title']}</title></head><body>"
        if 'content' in data:
            html += f"<h1>{data['title']}</h1><p>{data['content']}</p>"
        if 'product_name' in data:
            html += f"<h2>Product Information:</h2>"
            html += f"<p><strong>Name:</strong> {data['product_name']}</p>"
            html += f"<p><strong>Description:</strong> {data['description']}</p>"
            html += f"<p><img src='{data['image']}' alt='Product image'/></p>"
        html += "</body></html>"
        return html

class XMLRenderer(Renderer):
    def render(self, data:dict) ->str:
        xml = f"XML RENDER: <page><title>{data['title']}</title>"
        if 'content' in data:
            xml += f"<content>{data['content']}</content>"
        if 'product_name' in data:
            xml += "<product>"
            xml += f"<name>{data['product_name']}</name>"
            xml += f"<description>{data['description']}</description>"
            xml += f"<image>{data['image']}</image>"
            xml += "</product>"
        xml += "</page>"
        return xml


class JSONRenderer(Renderer):
    def render(self, data:dict)->dict:
        return data

