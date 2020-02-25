from flask import Blueprint, flash, render_template, request, redirect, url_for

from app import images, db
from app.main.forms import ProfileForm
from app.models import Profile

main_bp = Blueprint('main', __name__)


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'info')


@main_bp.route('/', methods=['POST', 'GET'])
def index():
    form = ProfileForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            filename = images.save(request.files['img'])
            url = images.url(filename)
            from app.models import Profile
            new_profile = Profile(name=form.name.data, image_filename=filename, image_url=url)
            db.session.add(new_profile)
            db.session.commit()
            flash('New profile, {}, added!'.format(new_profile.name), 'success')
            return redirect(url_for('main.display_profile'))
        else:
            flash_errors(form)
            flash('ERROR! Profile was not added.', 'error')
    return render_template('add_profile.html', form=form)


@main_bp.route('/display_profile', methods=['GET', 'POST'])
def display_profile():
    profile = db.session.query(Profile).first()
    if profile is not None:
        return render_template('display_profile.html', profile=profile)
    else:
        return 'No profile found'
