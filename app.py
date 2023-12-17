from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

class MyForm:
    def __init__(self):
        self.link = ""
        self.qr_generated = False

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    my_form = MyForm()

    if request.method == 'POST':
        my_form.link = request.form.get('link')
        if my_form.link:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(my_form.link)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            # Save the generated QR code image in the static directory
            img.save('static/qrcode.png')

            my_form.qr_generated = True

    return render_template('index.html', form=my_form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
