from flask import redirect, render_template, request, session, url_for, jsonify
from flask_login import logout_user
from models import User, NFT, photo_processing
from App import app, db, login_manager
from random import randint

@app.route("/")
def home():
    return render_template('index.html')


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route("/auth", methods = ['POST'])
def json_login():
    request_data = request.get_json()
    user = User.query.filter_by(username = request_data['login']).first()
    if(user is None):
        return jsonify({"answer" : "loginError"})
    if(user.check_password(request_data['password']) is not True):
        return jsonify({"answer" : "passwordError"})
    return jsonify({"answer" : user.id})


def default_image():
    index = randint(1,10)
    image =  url_for('static', filename = 'default/' + index + ".jpg")
    return image



@app.route("/registration", methods = ['POST'])
def json_register():
    request_data = request.get_json()
    new_user = User(email = request_data['email'], username = request_data['login'])
    new_user.set_password(request_data['password'])
    new_user.check_password(request_data['repeatPassword'])
    if(User.query.filter_by(username = request_data['login']).first() is not None):
        return jsonify({"answer" : "loginError"})
    if(User.query.filter_by(email = request_data['email']).first() is not None):
        return jsonify({"answer" : "emailError"})
    # new_user.verefication_email_token(request_data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"answer" : "done"})


# @app.route('/verification/<token>')
# def confirm_email(token):
#     user = User.query.filter_by(token = token).first()
#     try:
#         user.email = serializer.loads(token, salt = 'email-confirm', max_age = 120)
#     except SignatureExpired:
#         return jsonify({"answer" : "verificationError"})
#     user.verification = True
#     db.session.flush()
#     db.session.commit()
#     return jsonify({"answer" : "done"})


@app.route("/store/id=<int:id>")
def shop(id):
    nft = NFT.query.filter_by(id = id).first()
    product = {
        "id" : nft.id,
        "name" : nft.productName,
        "image" : nft.productImage,
        "price" : nft.price,
        "authorName" : nft.authorName.username,
        "authorImage" : nft.authorName.img_name, 
        "description" : nft.description,
        "authorId" : nft.authorName_id
    }
    return jsonify(product)

    
@app.route("/store/count")
def shop_count():
    nfts = NFT.query.count()
    return jsonify({"count" : nfts})


# @app.route("/logout")
# def logout():
#     logout_user()
#     return redirect(url_for('home'))


@app.route("/buy", methods = ['POST'])
def buy():
    request_data = request.get_json()
    nft = NFT.query.get(request_data["id"])
    nft.authorName_id = request_data["profile"]
    db.session.flush()
    db.session.commit()
    return jsonify({"answer" : "done"})


@app.route("/settings", methods = ['POST','GET'])
def account_settings():

    form = request.form
    form_image = request.files["image"]
    author = User.query.filter_by(username = form["authorName"]).first()
    if request.method == 'POST':
        image = url_for('static', filename = 'img/' + photo_processing(form_image))
        author.general_information = form["generalInformation"]
        author.img_name = image
        db.session.flush()
        db.session.commit()
        return jsonify({"answer" : "done"})
    elif request.method == 'GET':
        return jsonify(author[form["id"]])


@app.route("/upload", methods = ['POST'])
def new_nft():

    if(len(list(request.files.lists())) == 0):
        return jsonify({"answer" : "imageError"})

    form = request.form
    form_image = request.files["image"]

    if(len(form["name"]) < 5):
        return jsonify({"answer" : "nameError"})

    if(float(form["price"]) < 0):
        return jsonify({"answer" : "priceError"})

    image =  url_for('static', filename = 'img/' + photo_processing(form_image))
    author = User.query.filter_by(id = form["author"]).first()
    new_nft = NFT(productImage = image, productName = form["name"], description = form['description'],
    price = form['price'], authorName = author, ownerName = author)

    db.session.add(new_nft)
    db.session.commit()
    return jsonify({"answer":"done"})


@app.route("/profile/id=<int:id>")
def account(id):
    user = User.query.filter_by(id = id).first()
    nfts = NFT.query.filter_by(authorName_id = id).all()
    id = []
    for nft in nfts:
        id.append(nft.id)
    return jsonify({
        "name" : user.username,
        "email" : user.email,
        "image" : user.img_name,
        "nfts" : id
    })



@app.route("/store/<int:nft_id>", methods = ['GET'])
def nft(nft_id):
    nft = NFT.query.get_or_404(nft_id)
    return jsonify({
        "imagePath" : nft.productImage,
        "name" : nft.productName,
        "description" : nft.description,
        "price" : nft.price,
        "authorName" : nft.authorName.username,
        "authorImagePath" : nft.authorName.img_name
    })


# def send_reset_email(user):
#     token = user.get_reset_token()
#     message = Message('Password Reset Request', sender='ngorbunova41654@gmail.com', recipients=[user.email])
#     message.body = f'''To reset your password,visin the followink link:
# {url_for('reset_token', token = token, _external = True)}

# If you did not make this request then simply ignore this email and no changes will be made.
# '''
#     mail.send(message)


# @app.route("/reset_password", methods = ['POST', 'GET'])
# def reset_request():
#     if current_user.is_authenticated:
#         return redirect(url_for('shop'))
#     form = RequestResetForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email = form.email.data).first()
#         send_reset_email(user)
#         flash('An email ha been sent with instructions to reset you password', 'info')
#         return redirect(url_for('login'))
#     return render_template('reset_request.html', title = 'Reset Password', form_reset_request = form)


# @app.route("/reset_password/<token>", methods = ['POST', 'GET'])
# def reset_token(token):
#     if current_user.is_authenticated:
#         return redirect(url_for('shop'))
#     user = User.verify_reset_token(token)
#     if user is None:
#         flash('That is an invalid or expired token')
#         return redirect(url_for('reset_request'))
#     form = ResetPasswordForm()
#     if form.validate_on_submit():
#         user.set_password(form.password.data)
#         user.past_passwrod_check(form.password.data)
#         db.session.commit()
#         return redirect(url_for('login'))
#     return render_template('reset_token.html', title = 'Reset Password', form_reset_token = form)


if __name__ == '__main__':
    app.run(debug=True)