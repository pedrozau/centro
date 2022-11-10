from src.extension.database import db 


def create_db():
    """
    create all table 
    """
    db.create_all() 

def drop_db():
    """
    drop all table 
    """
    db.drop_all()


def init_app(app):
    for command in [create_db,drop_db]:
        app.cli.add_command(app.cli.command()(command))