from Form import Form
from Input import Input
from Fieldset import Fieldset
from Button import Button
    
if __name__ == "__main__":
    form = Form("product", "Add product", "/product/add")
    form.add(Input("name", "Name", "text"))
    form.add(Input("description", "Description", "text"))

    picture = Fieldset("photo", "Product Photo")
    picture.add(Input("caption", "Caption", "text"))
    picture.add(Input("image", "Image", "file"))
    form.add(picture)

    form.add(Button("savebtn", "Save", "submit"))

    data = {
        "name": "Apple MacBook",
        "description": "A decent laptop.",
        "photo": {
            "caption": "Front photo.",
            "image": "photo1.png",
        },
    }

    form.set_data(data)

    print(form.render())