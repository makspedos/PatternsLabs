from renderer import XMLRenderer, JSONRenderer, HtmlRenderer
from page import *
from product import Product

if __name__ == '__main__':
    render_html = HtmlRenderer()
    render_xml = XMLRenderer()
    render_json = JSONRenderer()

    simple_page = SimplePage('Hello test', render_html, content="This is a simple page")
    print(simple_page.render_page())
    simple_page.render = render_xml
    print(simple_page.render_page())

    product = Product(id=1, product_name='product_name',description='product_description',image='product_image')
    product_page = ProductPage('Hello product', render_html, product=product)
    print(product_page.render_page())
    product_page.render = render_json
    print(product_page.render_page())





