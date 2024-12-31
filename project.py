from reportlab.lib.pagesizes import letter

from reportlab.pdfgen import canvas

def generate_custom_pdf(title, customer_data, items):
    pdf_file = f"{title}.pdf"

    c = canvas.Canvas(pdf_file, pagesize=letter)

    c.setFont("Helvetica", 12)

    c.drawString(50, 750, title)

    c.drawString(50, 700, "Customer Information: ")

    y_offset = 680

    for key, value in customer_data.items():
        c.drawString(50, y_offset, f"{key}: {value}")
        y_offset -= 20

    c.drawString(50, y_offset - 20, "Items")
    c.drawString(50, y_offset - 40, "Item Name")
    c.drawString(200, y_offset - 40, "Quantity")
    c.drawString(300, y_offset - 40, "Price")
    c.drawString(400, y_offset - 40, "Description")

    y_offset -= 60

    total_amount = 0

    for item in items:
        item_name, quantity, price, description = item

        c.drawString(50, y_offset, item_name)
        c.drawString(200, y_offset, str(quantity))
        c.drawString(300, y_offset, f"${price:.2f}")
        c.drawString(400, y_offset, description)

        total_amount += quantity * price
        y_offset -= 20

        c.drawString(200, y_offset - 20, "Total")

        c.drawString(300, y_offset - 20, f"${total_amount:.2f}")


        c.save()

if __name__ == "__main__":
    title = input("Enter the invoice title: ")

    customer_data = {}

    customer_data["Name"] = input("Enter Customer Name: ")

    customer_data["Address"] = input("Enter Customer Address: ")

    customer_data["Email"] = input("Enter Customer Email: ")

    items = []

    while True:
        item_name = input("Enter Item Name (or 'done' ) to finish: ")

        if item_name.lower() == "done":
            break

        quantity = int(input("Enter Quantity: "))

        price = float(input("Enter Price: "))

        description = input("Enter Product Description: ")

        items.append((item_name, quantity, price, description))

        generate_custom_pdf(title, customer_data, items)