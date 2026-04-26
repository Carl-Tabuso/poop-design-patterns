from HTMLRenderer import HTMLRenderer
from JSONRenderer import JSONRenderer
from SimplePage import SimplePage
from Product import Product
from ProductPage import ProductPage

if __name__ == "__main__":
    html_renderer = HTMLRenderer()
    json_renderer = JSONRenderer()

    page = SimplePage(html_renderer, "Home", "Welcome to our website!")
    print("HTML view of a simple content page:\n")
    print(page.view())
    print("\n")

    page.change_renderer(json_renderer)
    print("JSON view of a simple content page, rendered with the same client code:")
    print(page.view())
    print("\n")

    product = Product(
        id="123", 
        title="Star Wars, episode1", 
        description="A long time ago in a galaxy far, far away...",
        image="/images/star-wars.jpeg",
        price=39.95,
    )

    page = ProductPage(html_renderer, product)
    print("HTML view of a product page, same client code:")
    print(page.view())
    print("\n")

    page.change_renderer(json_renderer)
    print("JSON view of a simple content page, with the same client code:\n")
    print(page.view())