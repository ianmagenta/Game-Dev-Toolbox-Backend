from app import create_app
from app.models import db, ToolType, Tool, AssociatedTool
from dotenv import load_dotenv
load_dotenv()

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    type1 = ToolType(tool_type="Programming Language")
    type2 = ToolType(tool_type="Game Engine")
    type3 = ToolType(tool_type="Level Editor")
    type4 = ToolType(tool_type="2D Art Tool")
    type5 = ToolType(tool_type="3D Art Tool")
    type6 = ToolType(tool_type="Shader Tool")
    type7 = ToolType(tool_type="Sound Effects Tool")
    type8 = ToolType(tool_type="Music Tool")
    type9 = ToolType(tool_type="Framework")
    type10 = ToolType(tool_type="Library")
    type11 = ToolType(tool_type="Fantasy Console")

    tool1 = Tool(
        tool_name="C#",
        picture="https://upload.wikimedia.org/wikipedia/commons/7/7a/C_Sharp_logo.svg",
        website="https://docs.microsoft.com/en-us/dotnet/csharp/",
        description="""C# is a general-purpose, multi-paradigm programming language encompassing strong typing, lexically scoped, imperative, declarative, functional,
        generic, object-oriented (class-based), and component-oriented programming disciplines. It was developed around 2000 by
        Microsoft as part of its .NET initiative and later approved as an international standard by Ecma (ECMA-334) in 2002 and ISO
        (ISO/IEC 23270) in 2003. Mono is the name of the free and open-source project to develop a compiler and runtime for the language.
        C# is one of the programming languages designed for the Common Language Infrastructure (CLI).""",
        description_link="https://en.wikipedia.org/wiki/C_Sharp_(programming_language)",
        tool_type_id=1,
    )

    tool2 = Tool(
        tool_name="C++",
        picture="https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg",
        website="https://www.cplusplus.com/",
        description="""C++ is a general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language,
        or "C with Classes". The language has expanded significantly over time, and modern C++ now has object-oriented, generic, and functional features
        in addition to facilities for low-level memory manipulation. It is almost always implemented as a compiled language, and many vendors provide C++
        compilers, including the Free Software Foundation, LLVM, Microsoft, Intel, Oracle, and IBM, so it is available on many platforms.""",
        description_link="https://en.wikipedia.org/wiki/C%2B%2B",
        tool_type_id=1,
    )

    tool3 = Tool(
        tool_name="C",
        picture="https://upload.wikimedia.org/wikipedia/commons/3/35/The_C_Programming_Language_logo.svg",
        website="https://www.learn-c.org/",
        description="""C is a general-purpose, procedural computer programming language supporting structured programming, lexical variable scope,
        and recursion, with a static type system. By design, C provides constructs that map efficiently to typical machine instructions. It has
        found lasting use in applications previously coded in assembly language. Such applications include operating systems and various application
        software for computers architectures that range from supercomputers to PLCs and embedded systems.""",
        description_link="https://en.wikipedia.org/wiki/C_(programming_language)",
        tool_type_id=1,
    )

    tool4 = Tool(
        tool_name="Python",
        picture="https://www.python.org/static/community_logos/python-logo-generic.svg",
        website="https://www.python.org/",
        description="""Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in
        1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and
        object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.""",
        description_link="https://en.wikipedia.org/wiki/Python_(programming_language)",
        tool_type_id=1,
    )

    tool5 = Tool(
        tool_name="JavaScript",
        picture="https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png",
        website="https://www.javascript.com/",
        description="""JavaScript often abbreviated as JS, is a programming language that conforms to the ECMAScript specification. JavaScript is
        high-level, often just-in-time compiled, and multi-paradigm. It has curly-bracket syntax, dynamic typing, prototype-based object-orientation,
        and first-class functions. Alongside HTML and CSS, JavaScript is one of the core technologies of the World Wide Web. JavaScript enables interactive
        web pages and is an essential part of web applications. The vast majority of websites use it for client-side page behavior, and all major web browsers
        have a dedicated JavaScript engine to execute it.""",
        description_link="https://en.wikipedia.org/wiki/JavaScript",
        tool_type_id=1,
    )

    tool6 = Tool(
        tool_name="Lua",
        picture="https://upload.wikimedia.org/wikipedia/commons/c/cf/Lua-Logo.svg",
        website="http://www.lua.org/",
        description="""Lua is a lightweight, high-level, multi-paradigm programming language designed primarily for embedded use in applications. Lua is cross-platform,
        since the interpreter of compiled bytecode is written in ANSI C, and Lua has a relatively simple C API to embed it into applications.""",
        description_link="https://en.wikipedia.org/wiki/Lua_(programming_language)",
        tool_type_id=1,
    )

    tool7 = Tool(
        tool_name="Haxe",
        picture="https://haxe.org/img/branding/haxe-logo-glyph.svg",
        website="https://haxe.org/",
        description="""Haxe is an open source high-level cross-platform multi-paradigm programming language and compiler that can produce applications and source code,
        for many different computing platforms, from one code-base. It is free and open-source software, distributed under the GNU General Public License (GPL) version 2,
        and the standard library under the MIT License.""",
        description_link="https://en.wikipedia.org/wiki/Haxe",
        tool_type_id=1,
    )

    tool8 = Tool(
        tool_name="Godot",
        picture="https://godotengine.org/themes/godotengine/assets/download/godot_logo.svg",
        website="https://godotengine.org/",
        description="""Godot Engine is a feature-packed, cross-platform game engine to create 2D and 3D games from a unified interface. It provides a comprehensive set of
        common tools, so that users can focus on making games without having to reinvent the wheel. Games can be exported in one click to a number of platforms, including the
        major desktop platforms (Linux, Mac OSX, Windows) as well as mobile (Android, iOS) and web-based (HTML5) platforms. Godot is completely free and open source under the
        very permissive MIT license. No strings attached, no royalties, nothing. The users' games are theirs, down to the last line of engine code. Godot's development is fully
        independent and community-driven, empowering users to help shape their engine to match their expectations. It is supported by the
        Software Freedom Conservancy not-for-profit.""",
        description_link="https://github.com/godotengine/godot",
        tool_type_id=2,
    )

    tool9 = Tool(
        tool_name="GDScript",
        picture="https://godotengine.org/themes/godotengine/assets/download/godot_logo.svg",
        website="https://docs.godotengine.org/en/stable/getting_started/scripting/gdscript/gdscript_basics.html",
        description="""GDScript is a high-level, dynamically typed programming language used to create content. It uses a syntax similar to Python (blocks are indent-based and many
        keywords are similar). Its goal is to be optimized for and tightly integrated with Godot Engine, allowing great flexibility for content creation and integration.""",
        description_link="https://docs.godotengine.org/en/stable/getting_started/scripting/gdscript/gdscript_basics.html",
        tool_type_id=1,
    )

    tool10 = Tool(
        tool_name="GDScript",
        picture="https://godotengine.org/themes/godotengine/assets/download/godot_logo.svg",
        website="https://docs.godotengine.org/en/stable/getting_started/scripting/gdscript/gdscript_basics.html",
        description="""GDScript is a high-level, dynamically typed programming language used to create content. It uses a syntax similar to Python (blocks are indent-based and many
        keywords are similar). Its goal is to be optimized for and tightly integrated with Godot Engine, allowing great flexibility for content creation and integration.""",
        description_link="https://docs.godotengine.org/en/stable/getting_started/scripting/gdscript/gdscript_basics.html",
        tool_type_id=1,
    )

    association1 = AssociatedTool(primary_tool_id=8, associated_tool_id=2)
    association2 = AssociatedTool(primary_tool_id=8, associated_tool_id=3)
    association3 = AssociatedTool(primary_tool_id=8, associated_tool_id=9)

    db.session.add(type1)
    db.session.add(type2)
    db.session.add(type3)
    db.session.add(type4)
    db.session.add(type5)
    db.session.add(type6)
    db.session.add(type7)
    db.session.add(type8)
    db.session.add(type9)
    db.session.add(type10)
    db.session.add(type11)

    db.session.add(tool1)
    db.session.add(tool2)
    db.session.add(tool3)
    db.session.add(tool4)
    db.session.add(tool5)
    db.session.add(tool6)
    db.session.add(tool7)
    db.session.add(tool8)
    db.session.add(tool9)
    db.session.add(tool10)

    db.session.add(association1)
    db.session.add(association2)
    db.session.add(association3)

    db.session.commit()
    print("Seeding Finished!")
