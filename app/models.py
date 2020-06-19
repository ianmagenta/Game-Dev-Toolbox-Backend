from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    unique_id = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    picture = db.Column(db.String(255), nullable=False)

    project = db.relationship("Project", back_populates="user")
    favorite_project = db.relationship(
        "FavoriteProject", back_populates="user")
    tagged_tool = db.relationship('TaggedTool', back_populates='user')


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    public = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='project')
    favorite_project = db.relationship(
        "FavoriteProject", back_populates="project")
    project_tool = db.relationship('ProjectTool', back_populates='project')


class FavoriteProject(db.Model):
    __tablename__ = "favorite_projects"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'projects.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    project = db.relationship("Project", back_populates="favorite_project")
    user = db.relationship('User', back_populates='favorite_project')


class ToolType(db.Model):
    __tablename__ = "tool_types"

    id = db.Column(db.Integer, primary_key=True)
    tool_type = db.Column(db.String(50), nullable=False)

    tool = db.relationship('Tool', back_populates='tool_type')


class Tool(db.Model):
    __tablename__ = "tools"

    id = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(50), nullable=False)
    picture = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    description_link = db.Column(db.String(255), nullable=False)
    tool_type_id = db.Column(
        db.Integer, db.ForeignKey('tool_types.id'), nullable=False)

    tool_type = db.relationship('ToolType', back_populates='tool')
    tagged_tool = db.relationship('TaggedTool', back_populates='tool')
    project_tool = db.relationship('ProjectTool', back_populates='tool')


class TaggedTool(db.Model):
    __tablename__ = "tagged_tools"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tool_id = db.Column(
        db.Integer, db.ForeignKey('tools.id'), nullable=False)

    user = db.relationship('User', back_populates='tagged_tool')
    tool = db.relationship('Tool', back_populates='tagged_tool')


class ProjectTool(db.Model):
    __tablename__ = "project_tools"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(
        db.Integer, db.ForeignKey('projects.id'), nullable=False)
    tool_id = db.Column(db.Integer, db.ForeignKey('tools.id'), nullable=False)

    project = db.relationship('Project', back_populates='project_tool')
    tool = db.relationship('Tool', back_populates='project_tool')


class AssociatedTool(db.Model):
    __tablename__ = "associated_tools"

    id = db.Column(db.Integer, primary_key=True)
    primary_tool_id = db.Column(
        db.Integer, db.ForeignKey('tools.id'), nullable=False)
    associated_tool_id = db.Column(
        db.Integer, db.ForeignKey('tools.id'), nullable=False)

    ptool = db.relationship('Tool', foreign_keys=[
                            primary_tool_id])
    atool = db.relationship('Tool', foreign_keys=[
                            associated_tool_id])
