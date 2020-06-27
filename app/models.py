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
    tagged_tool = db.relationship(
        'TaggedTool', back_populates='user', uselist=False)


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    public = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    user = db.relationship('User', back_populates='project')
    favorite_project = db.relationship(
        "FavoriteProject", back_populates="project")
    project_tool = db.relationship('ProjectTool', back_populates='project')
    project_screenshot = db.relationship(
        "ProjectScreenshot", back_populates="project")


class ProjectScreenshot(db.Model):
    __tablename__ = "project_screenshots"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'projects.id'), nullable=False)
    screenshot = db.Column(db.String(255), nullable=False)

    project = db.relationship("Project", back_populates="project_screenshot")


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

    def to_dict(self):
        return dict(id=self.id, tool_type=self.tool_type)


class Tool(db.Model):
    __tablename__ = "tools"

    id = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(50), nullable=False)
    picture = db.Column(db.String(255))
    website = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    description_link = db.Column(db.String(255), nullable=False)
    tool_type_id = db.Column(
        db.Integer, db.ForeignKey('tool_types.id'), nullable=False)

    tool_type = db.relationship('ToolType', back_populates='tool')
    tagged_tool = db.relationship('TaggedTool', back_populates='tool')
    project_tool = db.relationship('ProjectTool', back_populates='tool')

    def to_dict(self):
        return dict(id=self.id, tool_name=self.tool_name, picture=self.picture,
                    website=self.website, description=self.description,
                    description_link=self.description_link, tool_type=self.tool_type.to_dict())


class TaggedTool(db.Model):
    __tablename__ = "tagged_tools"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    tool_id = db.Column(
        db.Integer, db.ForeignKey('tools.id'), nullable=False)

    user = db.relationship('User', back_populates='tagged_tool')
    tool = db.relationship('Tool', back_populates='tagged_tool')

    def to_dict(self):
        return dict(id=self.id, user_id=self.user_id, tool_id=self.tool_id, tool=self.tool.to_dict())


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

    def primary_to_dict(self):
        return dict(id=self.id, associated_tool_id=self.atool.to_dict())

    def associated_to_dict(self):
        return dict(id=self.id, primary_tool_id=self.ptool.to_dict())
