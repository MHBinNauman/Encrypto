from flask import Flask, render_template, request
import Encryption_Decryption_Modules

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/RSA", methods=['GET', 'POST'])
def RSA():
    if request.method == "POST":
        action = request.form.get("action")

        if action == "encrypt":
            public_key, private_key = Encryption_Decryption_Modules.generate_keys()
            plaintext = request.form.get("encrypt_text")

            if not plaintext:  # Check if plaintext is empty or None
                return render_template("apology.html", error="Please enter text to encrypt.", status_code=400)
            encrypted_message = Encryption_Decryption_Modules.rsa_encrypt(plaintext, public_key)
            Encryption_Decryption_Modules.save_to_file("static\\encrypted_rsa.txt", ','.join(map(str, encrypted_message)))
            encrypted_message = ''.join(chr(num) for num in encrypted_message)
            return render_template("RSA.html", public_key=public_key, private_key=private_key, encrypted_message=encrypted_message)
        
        elif action == "decrypt":   
            ciphertext = Encryption_Decryption_Modules.read_from_file("static\\encrypted_rsa.txt")
            ciphertext = [int(num) for num in ciphertext.split(',')]
            private_key = tuple(map(int, request.form["private_key"].split(',')))
            decrypted_message = Encryption_Decryption_Modules.rsa_decrypt(ciphertext, private_key)
            return render_template("RSA.html", decrypted_message=decrypted_message)
    else:
        return render_template("RSA.html")

@app.route("/CeasarCipher", methods=['GET', 'POST'])
def CeasarCipher():
    if request.method == "POST":
        action = request.form.get("action")
        plaintext = request.form.get("plaintext_ceasar")
        multiplier = request.form.get("multiplier")
        shift = request.form.get("shift")

        if action == "encrypt":
            if not plaintext:
                return render_template("apology.html", error="Please enter text to encrypt.", status_code=400)
            if Encryption_Decryption_Modules.gcd(int(multiplier), 95) != 1:
                return render_template("apology.html", error="Multiplier must be coprime with 95.", status_code=400)
            else:
                encrypted_message = Encryption_Decryption_Modules.generalized_caesar_encrypt(plaintext, int(multiplier), int(shift))
                Encryption_Decryption_Modules.save_to_file("static\\encrypted_ceasar.txt", encrypted_message)
                return render_template("CeasarCipher.html", encrypted_message=encrypted_message)

        elif action == "decrypt":
            ciphertext = Encryption_Decryption_Modules.read_from_file("static\\encrypted_ceasar.txt")
            decrypted_message = Encryption_Decryption_Modules.generalized_caesar_decrypt(ciphertext, int(multiplier), int(shift))
            return render_template("CeasarCipher.html", decrypted_message=decrypted_message)

    else:
        return render_template("CeasarCipher.html")

@app.route("/FrequencyAnalysis", methods=['GET', 'POST'])
def FrequencyAnalysis():
    action = request.form.get("action")
    if request.method == "POST":
        if action == "FA":
            results = Encryption_Decryption_Modules.frequency_analysis_break(request.form.get("ciphertext_analyze"))
            # Only pass the top 5 results to the template
            top_results = results[:5]
            return render_template("frequency_analysis.html", results=top_results)
    else:
        return render_template("frequency_analysis.html")

if __name__ == "__main__":
    app.run(debug=True)