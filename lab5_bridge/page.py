from product import Product
from renderer import Renderer
class Page:
    def __init__(self, title:str, render:Renderer):
        self.title = title
        self._render = render

    @property
    def render(self):
        return self._render

    @render.setter
    def render(self, render:Renderer):
        if not isinstance(render,Renderer ):
            raise ValueError("Render must be an instance of Renderer")
        self._render = render

    def render_page(self):
        return self._render.render(self.get_data())

    def get_data(self)->dict:
        return {
            'title': self.title,
        }
class SimplePage(Page):
    def __init__(self, title: str,render:Renderer, content: str):
        super().__init__(title, render)
        self.content = content

    def get_data(self)->dict:
        data = super().get_data()
        data.update(
            {'content': self.content}
        )
        return data


class ProductPage(Page):
    def __init__(self, title: str, render:Renderer, product:Product):
        super().__init__(title, render)
        self.product = product

    def get_data(self)->dict:
        data = super().get_data()
        data.update(
            {
                'product_name': self.product.product_name,
                'id': self.product.id,
                'description': self.product.description,
                'image': self.product.image,
            }
        )
        return data
