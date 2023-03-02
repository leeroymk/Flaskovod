@app.route("/", methods=["GET", "POST"])
def index():
    form = ProfileForm()
    if form.validate_on_submit():
        username = form.username.data
        about_me = form.about_me.data
        password = form.password.data
        submit = form.submit.data
        return render_template('index.html',
                           form=form,
                           username=username,
                           about_me=about_me,
                           password=password)
    else:
        return render_template('index.html', form=form)