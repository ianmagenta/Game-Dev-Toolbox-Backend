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
        description="""C# is a general-purpose, multi-paradigm programming language encompassing strong typing, lexically scoped, imperative, declarative, functional, generic, object-oriented (class-based), and component-oriented programming disciplines. It was developed around 2000 by Microsoft as part of its .NET initiative and later approved as an international standard by Ecma (ECMA-334) in 2002 and ISO (ISO/IEC 23270) in 2003. Mono is the name of the free and open-source project to develop a compiler and runtime for the language. C# is one of the programming languages designed for the Common Language Infrastructure (CLI).""",
        description_link="https://en.wikipedia.org/wiki/C_Sharp_(programming_language)",
        tool_type_id=1,
    )

    tool2 = Tool(
        tool_name="C++",
        picture="https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg",
        website="https://www.cplusplus.com/",
        description="""C++ is a general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language, or "C with Classes". The language has expanded significantly over time, and modern C++ now has object-oriented, generic, and functional features in addition to facilities for low-level memory manipulation. It is almost always implemented as a compiled language, and many vendors provide C++ compilers, including the Free Software Foundation, LLVM, Microsoft, Intel, Oracle, and IBM, so it is available on many platforms.""",
        description_link="https://en.wikipedia.org/wiki/C%2B%2B",
        tool_type_id=1,
    )

    tool3 = Tool(
        tool_name="C",
        picture="https://upload.wikimedia.org/wikipedia/commons/3/35/The_C_Programming_Language_logo.svg",
        website="https://www.learn-c.org/",
        description="""C is a general-purpose, procedural computer programming language supporting structured programming, lexical variable scope, and recursion, with a static type system. By design, C provides constructs that map efficiently to typical machine instructions. It has found lasting use in applications previously coded in assembly language. Such applications include operating systems and various application software for computers architectures that range from supercomputers to PLCs and embedded systems.""",
        description_link="https://en.wikipedia.org/wiki/C_(programming_language)",
        tool_type_id=1,
    )

    tool4 = Tool(
        tool_name="Python",
        picture="https://www.python.org/static/community_logos/python-logo-generic.svg",
        website="https://www.python.org/",
        description="""Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.""",
        description_link="https://en.wikipedia.org/wiki/Python_(programming_language)",
        tool_type_id=1,
    )

    tool5 = Tool(
        tool_name="JavaScript",
        picture="https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png",
        website="https://www.javascript.com/",
        description="""JavaScript often abbreviated as JS, is a programming language that conforms to the ECMAScript specification. JavaScript is high-level, often just-in-time compiled, and multi-paradigm. It has curly-bracket syntax, dynamic typing, prototype-based object-orientation, and first-class functions. Alongside HTML and CSS, JavaScript is one of the core technologies of the World Wide Web. JavaScript enables interactive web pages and is an essential part of web applications. The vast majority of websites use it for client-side page behavior, and all major web browsers have a dedicated JavaScript engine to execute it.""",
        description_link="https://en.wikipedia.org/wiki/JavaScript",
        tool_type_id=1,
    )

    tool6 = Tool(
        tool_name="Lua",
        picture="https://upload.wikimedia.org/wikipedia/commons/c/cf/Lua-Logo.svg",
        website="http://www.lua.org/",
        description="""Lua is a lightweight, high-level, multi-paradigm programming language designed primarily for embedded use in applications. Lua is cross-platform, since the interpreter of compiled bytecode is written in ANSI C, and Lua has a relatively simple C API to embed it into applications.""",
        description_link="https://en.wikipedia.org/wiki/Lua_(programming_language)",
        tool_type_id=1,
    )

    tool7 = Tool(
        tool_name="Haxe",
        picture="https://haxe.org/img/branding/haxe-logo-glyph.svg",
        website="https://haxe.org/",
        description="""Haxe is an open source high-level cross-platform multi-paradigm programming language and compiler that can produce applications and source code, for many different computing platforms, from one code-base. It is free and open-source software, distributed under the GNU General Public License (GPL) version 2, and the standard library under the MIT License.""",
        description_link="https://en.wikipedia.org/wiki/Haxe",
        tool_type_id=1,
    )

    tool8 = Tool(
        tool_name="Godot",
        picture="https://godotengine.org/themes/godotengine/assets/download/godot_logo.svg",
        website="https://godotengine.org/",
        description="""Godot Engine is a feature-packed, cross-platform game engine to create 2D and 3D games from a unified interface. It provides a comprehensive set of common tools, so that users can focus on making games without having to reinvent the wheel. Games can be exported in one click to a number of platforms, including the major desktop platforms (Linux, Mac OSX, Windows) as well as mobile (Android, iOS) and web-based (HTML5) platforms. Godot is completely free and open source under the very permissive MIT license. No strings attached, no royalties, nothing. The users' games are theirs, down to the last line of engine code. Godot's development is fully independent and community-driven, empowering users to help shape their engine to match their expectations. It is supported by the Software Freedom Conservancy not-for-profit.""",
        description_link="https://github.com/godotengine/godot",
        tool_type_id=2,
    )

    tool9 = Tool(
        tool_name="GDScript",
        picture="https://godotengine.org/themes/godotengine/assets/download/godot_logo.svg",
        website="https://docs.godotengine.org/en/stable/getting_started/scripting/gdscript/gdscript_basics.html",
        description="""GDScript is a high-level, dynamically typed programming language used to create content. It uses a syntax similar to Python (blocks are indent-based and many keywords are similar). Its goal is to be optimized for and tightly integrated with Godot Engine, allowing great flexibility for content creation and integration.""",
        description_link="https://docs.godotengine.org/en/stable/getting_started/scripting/gdscript/gdscript_basics.html",
        tool_type_id=1,
    )

    tool10 = Tool(
        tool_name="CryEngine",
        picture="https://www.cryengine.com/assets/brand-assets/cryengine-logo-vertical-white.svg",
        website="https://www.cryengine.com",
        description="""CryEngine (officially stylized as CRYENGINE) is a game engine designed by the German game developer Crytek. It has been used in all of their titles with the initial version being used in Far Cry, and continues to be updated to support new consoles and hardware for their games. It has also been used for many third-party games under Crytek's licensing scheme, including Sniper: Ghost Warrior 2 and SNOW. Warhorse Studios uses a modified version of the engine for their medieval RPG Kingdom Come: Deliverance. Ubisoft maintains an in-house, heavily modified version of CryEngine from the original Far Cry called the Dunia Engine, which is used in their later iterations of the Far Cry series. According to various anonymous reports in April 2015, CryEngine was licensed to Amazon for $50–70 million. Consequently, in February 2016, Amazon released its own reworked and extended version of CryEngine under the name of Amazon Lumberyard.""",
        description_link="https://en.wikipedia.org/wiki/CryEngine",
        tool_type_id=2,
    )

    tool11 = Tool(
        tool_name="Amazon Lumberyard",
        picture="https://upload.wikimedia.org/wikipedia/en/f/f2/Lumberyard_Logo.png",
        website="https://aws.amazon.com/lumberyard/",
        description="""Amazon Lumberyard is a free cross-platform game engine developed by Amazon and based on CryEngine (init. released 2002), which was licensed from Crytek in 2015. The engine features integration with Amazon Web Services to allow developers to build or host their games on Amazon's servers, as well as support for livestreaming via Twitch. Additionally, the engine includes Twitch ChatPlay, allowing viewers of the Twitch stream to influence the game through the associated chat, a method of play inspired by the Twitch Plays Pokémon phenomenon. The source code is available to end users with limitations: Users may not publicly release the Lumberyard engine source code or use it to release their own game engine. Lumberyard launched on February 9, 2016 alongside GameLift, a fee-based managed service for deploying and hosting multiplayer games, intended to allow developers the easy development of games that attract "large and vibrant communities of fans." As of March 2018, the software is currently in beta status and can be used to build games for Microsoft Windows, PlayStation 4, Xbox One, with limited support for iOS and Android and the support of Linux and Mac being planned for future releases. Virtual reality integration was added in Beta 1.3, allowing developers to build games supporting devices like Oculus Rift and HTC Vive.""",
        description_link="https://en.wikipedia.org/wiki/Amazon_Lumberyard",
        tool_type_id=2,
    )

    tool12 = Tool(
        tool_name="Unreal Engine",
        picture="https://upload.wikimedia.org/wikipedia/commons/2/20/UE_Logo_Black_Centered.svg",
        website="https://www.unrealengine.com/en-US/",
        description="""Unreal Engine is a game engine developed by Epic Games, first showcased in the 1998 first-person shooter game Unreal. Although initially developed for first-person shooters, it has been successfully used in a variety of other genres, including platformers, fighting games, MMORPGs, and other RPGs. Written in C++, the Unreal Engine features a high degree of portability, supporting a wide range of platforms. The latest release is Unreal Engine 4, which launched in 2014 under a subscription model. Since 2015, it can be downloaded for free, with its source code available on GitHub. Epic allows for its use in commercial products based on a royalty model, typically asking developers for 5% of revenues from sales, though with the success of Fortnite, which has become a testbed for Unreal Engine for Epic, Epic waives this fee for developers that publish their games through the Epic Games Store, and more recently for revenues up through the first US$1 million. Epic has announced Unreal Engine 5 to be released by late-2021.""",
        description_link="https://en.wikipedia.org/wiki/Unreal_Engine",
        tool_type_id=2,
    )

    tool13 = Tool(
        tool_name="Source Engine",
        picture="https://upload.wikimedia.org/wikipedia/commons/6/67/Source_engine_logo_and_wordmark.svg",
        website="https://developer.valvesoftware.com/wiki/SDK_Docs",
        description="""Source is a 3D game engine developed by Valve. It debuted as the successor to GoldSrc with Counter-Strike: Source in June 2004, followed shortly by Half-Life 2 in November, and has been in active development since. Source does not have a concise version numbering scheme; instead, it is designed in constant incremental updates. The successor, Source 2, was officially announced in March 2015, with the first game to use it being Dota 2, which was ported over from Source later that year.""",
        description_link="https://en.wikipedia.org/wiki/Source_(game_engine)",
        tool_type_id=2,
    )

    tool14 = Tool(
        tool_name="Tiled Map Editor",
        picture="https://www.mapeditor.org/img/tiled-logo-white.png",
        website="https://www.mapeditor.org/",
        description="""Tiled is a general purpose tile map editor for all tile-based games, such as RPGs, platformers or Breakout clones. Tiled is highly flexible. It can be used to create maps of any size, with no restrictions on tile size, or the number of layers or tiles that can be used. Maps, layers, tiles, and objects can all be assigned arbitrary properties. Tiled's map format (TMX) is easy to understand and allows multiple tilesets to be used in any map. Tilesets can be modified at any time.""",
        description_link="https://github.com/bjorn/tiled",
        tool_type_id=3,
    )

    tool15 = Tool(
        tool_name="Ogmo Editor",
        picture="https://img.itch.zone/aW1nLzI0NDE3MjgucG5n/original/6JTXjR.png",
        website="https://ogmo-editor-3.github.io/",
        description="""OGMO Editor is a free, open source 2D level editor built by indie game developers for indie game developers. OGMO Editor focuses on a fast, intuitive project-based workflow to make level design as efficient and as fun as possible. Build levels using tilesets, add functionality by placing entities, decorate the stage with decals, and leverage custom metadata to jumpstart content creation for your game! OGMO Editor strives to be platform and engine agnostic, so it saves project files and level files as human readable and easy to implement JSON files. This makes it easy for developers to add OGMO Editor into their workflow.""",
        description_link="https://ogmo-editor-3.github.io/docs/#/manual/introduction.md",
        tool_type_id=3,
    )

    tool16 = Tool(
        tool_name="Aseprite",
        picture="https://www.aseprite.org/assets/images/header-logo.png",
        website="https://www.aseprite.org/",
        description="""Aseprite is a sprite editor that lets you create 2D animations for videogames. It can be used to create pixel-art, retro style graphics, and whatever you like about the 8-bit (and 16-bit) era.""",
        description_link="https://dacap.itch.io/aseprite",
        tool_type_id=4,
    )

    tool17 = Tool(
        tool_name="Pyxel Edit",
        picture="https://pyxeledit.com/images/logo_heart.png",
        website="https://pyxeledit.com/index.php",
        description="""Pyxel Edit is a pixel art drawing application especially designed for working with tiles. Place tiles to form a level, edit them directly to see how they all work together, then export your tileset and the level data, and load it into your game. Tiles can even be flipped and rotated, still being editable and synced. This feature is inspired by the awesome Pixothello and Cosmigo Pro Motion, but taken one step further. It also supports making animations, and exporting them as sprite sheets or animated GIFs. Pyxel Edit is built in Adobe Air and runs on Mac and Windows. (It reportedly also runs well in Linux under Wine).""",
        description_link="https://pyxeledit.com/about.php",
        tool_type_id=4,
    )

    tool18 = Tool(
        tool_name="Blender",
        picture="https://download.blender.org/branding/blender_logo_socket.svg",
        website="https://www.blender.org/",
        description="""Blender is the free and open source 3D creation suite. It supports the entirety of the 3D pipeline—modeling, rigging, animation, simulation, rendering, compositing and motion tracking, even video editing and game creation. Advanced users employ Blender’s API for Python scripting to customize the application and write specialized tools; often these are included in Blender’s future releases. Blender is well suited to individuals and small studios who benefit from its unified pipeline and responsive development process.""",
        description_link="https://www.blender.org/about/",
        tool_type_id=5,
    )

    tool19 = Tool(
        tool_name="MagicaVoxel",
        picture="https://pbs.twimg.com/profile_images/1211832444539801600/yz0qPQoR_400x400.jpg",
        website="https://ephtracy.github.io/",
        description="""A free lightweight GPU-based voxel art editor and interactive path tracing renderer.""",
        description_link="https://ephtracy.github.io/",
        tool_type_id=5,
    )

    tool20 = Tool(
        tool_name="SHADERed",
        picture="https://shadered.org/img/icon.png",
        website="https://shadered.org/",
        description="""SHADERed is a lightweight tool for creating and testing HLSL and GLSL shaders. It is easy to use, open source, cross-platform (runs on Windows & Linux - HLSL shaders work on both OSes) and -frequently updated with new features.""",
        description_link="https://github.com/dfranx/SHADERed",
        tool_type_id=6,
    )

    tool21 = Tool(
        tool_name="ShaderFrog",
        picture="https://s3-us-west-1.amazonaws.com/shader-frog/shader-frog-logo-small.png",
        website="https://shaderfrog.com/",
        description="""Shader Frog is a WebGL shader editor that lets you design shaders without writing code. Shader Frog lets you create visual effects by composing two or more shaders together, and tweaking their parameters. You can build a complex effect out of simple components. You can then export your shader for use in your THREE.js game or application.""",
        description_link="https://shaderfrog.com/about",
        tool_type_id=6,
    )

    tool22 = Tool(
        tool_name="jfxr",
        website="https://jfxr.frozenfractal.com/",
        description="""Jfxr is a browser-based tool to generate sound effects, for example for use in games. It was inspired by bfxr, but aims to be more powerful and more intuitive to use.""",
        description_link="https://github.com/ttencate/jfxr",
        tool_type_id=7,
    )

    tool23 = Tool(
        tool_name="Blendwave",
        picture="https://beta.blendwave.net/img/bw_logo.svg",
        website="https://beta.blendwave.net/",
        description="""Blendwave is a sound design application inspired by the ease of use of samplers and the “sfxr family” of sound creation software. It uses the Web Audio API, mostly through the Pizzicato Library, to achieve most of the DSP functionalities.""",
        description_link="https://github.com/midipixel/blendwave",
        tool_type_id=7,
    )

    tool24 = Tool(
        tool_name="LMMS",
        picture="""https://raw.githubusercontent.com/LMMS/artwork/master/Icon%20%26%20Mimetypes/lmms-64x64.svg""",
        website="https://lmms.io/",
        description="""LMMS is a free cross-platform alternative to commercial programs like FL Studio®, which allow you to produce music with your computer. This includes the creation of melodies and beats, the synthesis and mixing of sounds, and arranging of samples. You can have fun with your MIDI-keyboard and much more; all in a user-friendly and modern interface.""",
        description_link="https://github.com/LMMS/lmms",
        tool_type_id=8,
    )

    tool25 = Tool(
        tool_name="FamiStudio",
        picture="""https://img.itch.zone/aW1nLzI1OTgxMTYucG5n/original/sAaQvD.png""",
        website="https://famistudio.org/",
        description="""FamiStudio is a very simple, DAW-style, music editor for the Nintendo Entertainment System. It is designed for both chiptune enthusiasts and the NES homebrew community.""",
        description_link="https://bleubleu.itch.io/famistudio",
        tool_type_id=8,
    )

    tool26 = Tool(
        tool_name="Bosca Ceoil",
        picture="""https://img.itch.zone/aW1hZ2UvMzE5MjYvMTM1NzcwLnBuZw==/original/32QXIc.png""",
        website="https://boscaceoil.net/",
        description="""Bosca Ceoil is a free, easy to use tool for creating music! Bosca is designed for beginners! It takes less than five minutes to learn, and comes with a quick built in tutorial to walk you through everything, step by step. Bosca supports lots of different scales and chords, so even if you've never composed music before, it's really easy to get something that sounds good straight away. No messing around getting instruments to work! Bosca comes with over a hundred presets, including MIDI and Chiptune instuments. Bosca Ceoil is completely free, and open source!""",
        description_link="https://terrycavanagh.itch.io/bosca-ceoil",
        tool_type_id=8,
    )
    tool27 = Tool(
        tool_name="LÖVE",
        picture="""https://raw.githubusercontent.com/love2d/love/60278b0532036d404c0b7b011c7b63ab58a5ddaf/platform/unix/love.svg""",
        website="https://love2d.org/",
        description="""LÖVE is an awesome framework you can use to make 2D games in Lua. It's free, open-source, and works on Windows, Mac OS X, Linux, Android, and iOS.""",
        description_link="https://github.com/love2d/love",
        tool_type_id=9,
    )

    tool28 = Tool(
        tool_name="raylib",
        picture="""https://www.raylib.com/common/img/raylib_logo.png""",
        website="https://www.raylib.com/",
        description="""raylib is a simple and easy-to-use library to enjoy videogames programming. raylib is highly inspired by Borland BGI graphics lib and by XNA framework and it's specially well suited for prototyping, tooling, graphical applications, embedded systems and education.""",
        description_link="https://github.com/raysan5/raylib",
        tool_type_id=9,
    )

    tool29 = Tool(
        tool_name="pygame",
        picture="""https://www.pygame.org/docs/pygame_logo.gif""",
        website="https://www.pygame.org/",
        description="""Pygame is a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language. Pygame is highly portable and runs on nearly every platform and operating system.""",
        description_link="https://www.pygame.org/wiki/about",
        tool_type_id=9,
    )

    tool30 = Tool(
        tool_name="Heaps",
        picture="""https://raw.githubusercontent.com/HeapsIO/heaps.io/master/assets/logo/logo-heaps-color.png""",
        website="https://heaps.io/",
        description="""Heaps.io is a mature cross platform graphics engine designed for high performance games.It is designed to leverage modern GPUs that are commonly available on both desktop and mobile devices.""",
        description_link="https://heaps.io/",
        tool_type_id=9,
    )

    tool31 = Tool(
        tool_name="SDL",
        picture="""https://www.libsdl.org/media/SDL_logo.png""",
        website="https://www.libsdl.org/download-2.0.php",
        description="""Simple DirectMedia Layer is a cross-platform development library designed to provide low level access to audio, keyboard, mouse, joystick, and graphics hardware via OpenGL and Direct3D. It is used by video playback software, emulators, and popular games including Valve's award winning catalog and many Humble Bundle games. SDL officially supports Windows, Mac OS X, Linux, iOS, and Android. Support for other platforms may be found in the source code. SDL is written in C, works natively with C++, and there are bindings available for several other languages, including C# and Python.""",
        description_link="https://www.libsdl.org/index.php",
        tool_type_id=10,
    )

    tool32 = Tool(
        tool_name="OpenGL",
        picture="""https://www.opengl.org/img/opengl_logo.jpg""",
        website="https://www.opengl.org/",
        description="""OpenGL is the premier environment for developing portable, interactive 2D and 3D graphics applications. Since its introduction in 1992, OpenGL has become the industry's most widely used and supported 2D and 3D graphics application programming interface (API), bringing thousands of applications to a wide variety of computer platforms. OpenGL fosters innovation and speeds application development by incorporating a broad set of rendering, texture mapping, special effects, and other powerful visualization functions. Developers can leverage the power of OpenGL across all popular desktop and workstation platforms, ensuring wide application deployment.""",
        description_link="https://www.opengl.org/about/",
        tool_type_id=10,
    )

    tool33 = Tool(
        tool_name="PICO-8",
        picture="""https://upload.wikimedia.org/wikipedia/commons/3/33/PICO-8_logo.png""",
        website="https://www.lexaloffle.com/pico-8.php",
        description="""PICO-8 is a fantasy console for making, sharing and playing tiny games and other computer programs. It feels like a regular console, but runs on Windows / Mac / Linux. When you turn it on, the machine greets you with a commandline, a suite of cartridge creation tools, and an online cartridge browser called SPLORE.""",
        description_link="https://www.lexaloffle.com/pico-8.php",
        tool_type_id=11,
    )

    tool34 = Tool(
        tool_name="TIC-80",
        picture="""https://tic.computer/img/logo64.png""",
        website="https://tic.computer/",
        description=""" TIC-80 is a fantasy computer for making, playing and sharing tiny games. There are built-in tools for development: code, sprites, maps, sound editors and the command line, which is enough to create a mini retro game. At the exit you will get a cartridge file, which can be stored and played on the website. Also, the game can be packed into a player that works on all popular platforms and distribute as you wish. To make a retro styled game the whole process of creation takes place under some technical limitations: 240x136 pixels display, 16 color palette, 256 8x8 color sprites, 4 channel sound and etc.""",
        description_link="https://tic.computer/",
        tool_type_id=11,
    )

    # Godot
    association1 = AssociatedTool(primary_tool_id=8, associated_tool_id=2)
    association2 = AssociatedTool(primary_tool_id=8, associated_tool_id=1)
    association3 = AssociatedTool(primary_tool_id=8, associated_tool_id=9)
    # Cryengine
    association4 = AssociatedTool(primary_tool_id=10, associated_tool_id=2)
    association5 = AssociatedTool(primary_tool_id=10, associated_tool_id=6)
    association6 = AssociatedTool(primary_tool_id=10, associated_tool_id=1)
    # Lumberyard
    association7 = AssociatedTool(primary_tool_id=11, associated_tool_id=2)
    association8 = AssociatedTool(primary_tool_id=11, associated_tool_id=6)
    # Unreal
    association9 = AssociatedTool(primary_tool_id=12, associated_tool_id=2)
    # Source
    association10 = AssociatedTool(primary_tool_id=13, associated_tool_id=2)
    # Tiled
    association11 = AssociatedTool(primary_tool_id=14, associated_tool_id=2)
    # Ogmo
    association12 = AssociatedTool(primary_tool_id=15, associated_tool_id=7)
    # Aseprite
    association13 = AssociatedTool(primary_tool_id=16, associated_tool_id=2)
    # Blender
    association14 = AssociatedTool(primary_tool_id=18, associated_tool_id=3)
    association15 = AssociatedTool(primary_tool_id=18, associated_tool_id=2)
    association16 = AssociatedTool(primary_tool_id=18, associated_tool_id=4)
    # Shadered
    association17 = AssociatedTool(primary_tool_id=20, associated_tool_id=2)
    association18 = AssociatedTool(primary_tool_id=20, associated_tool_id=3)
    # jfxr
    association19 = AssociatedTool(primary_tool_id=22, associated_tool_id=5)
    # Blendwave
    association20 = AssociatedTool(primary_tool_id=23, associated_tool_id=5)
    # LMMS
    association21 = AssociatedTool(primary_tool_id=24, associated_tool_id=2)
    # FamiStudio
    association22 = AssociatedTool(primary_tool_id=25, associated_tool_id=1)
    # Love
    association23 = AssociatedTool(primary_tool_id=27, associated_tool_id=6)
    association24 = AssociatedTool(primary_tool_id=27, associated_tool_id=2)
    # raylib
    association25 = AssociatedTool(primary_tool_id=28, associated_tool_id=3)
    # pygame
    association26 = AssociatedTool(primary_tool_id=29, associated_tool_id=4)
    # Heaps
    association27 = AssociatedTool(primary_tool_id=30, associated_tool_id=7)
    # SDL
    association28 = AssociatedTool(primary_tool_id=31, associated_tool_id=3)
    # OpenGL
    association29 = AssociatedTool(primary_tool_id=32, associated_tool_id=3)
    # Pico-8
    association30 = AssociatedTool(primary_tool_id=33, associated_tool_id=6)
    # TIC-80
    association31 = AssociatedTool(primary_tool_id=34, associated_tool_id=6)
    association32 = AssociatedTool(primary_tool_id=34, associated_tool_id=5)

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
    db.session.add(tool11)
    db.session.add(tool12)
    db.session.add(tool13)
    db.session.add(tool14)
    db.session.add(tool15)
    db.session.add(tool16)
    db.session.add(tool17)
    db.session.add(tool18)
    db.session.add(tool19)
    db.session.add(tool20)
    db.session.add(tool21)
    db.session.add(tool22)
    db.session.add(tool23)
    db.session.add(tool24)
    db.session.add(tool25)
    db.session.add(tool26)
    db.session.add(tool27)
    db.session.add(tool28)
    db.session.add(tool29)
    db.session.add(tool30)
    db.session.add(tool31)
    db.session.add(tool32)
    db.session.add(tool33)
    db.session.add(tool34)

    db.session.add(association1)
    db.session.add(association2)
    db.session.add(association3)
    db.session.add(association4)
    db.session.add(association5)
    db.session.add(association6)
    db.session.add(association7)
    db.session.add(association8)
    db.session.add(association9)
    db.session.add(association10)
    db.session.add(association11)
    db.session.add(association12)
    db.session.add(association13)
    db.session.add(association14)
    db.session.add(association15)
    db.session.add(association16)
    db.session.add(association17)
    db.session.add(association18)
    db.session.add(association19)
    db.session.add(association20)
    db.session.add(association21)
    db.session.add(association22)
    db.session.add(association23)
    db.session.add(association24)
    db.session.add(association25)
    db.session.add(association26)
    db.session.add(association27)
    db.session.add(association28)
    db.session.add(association29)
    db.session.add(association30)
    db.session.add(association31)
    db.session.add(association32)

    db.session.commit()
    print("Seeding Finished!")
