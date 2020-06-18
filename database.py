from app import app, db
from app.models import User
from dotenv import load_dotenv
load_dotenv()


with app.app_context():
    db.drop_all()
    db.create_all()

    # thing1 = Thing(
    #     title="Thing 1",
    #     description="Thing 1 description",
    #     category_id=1,
    #     user_id=1,
    #     created_at="SOME_Time"
    # )

    # db.session.add(thing1)
    db.session.commit()
