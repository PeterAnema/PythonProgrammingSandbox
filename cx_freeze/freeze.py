from cx_Freeze import setup, Executable

# files = {"include_files": ["<Path to Files>/somefile.py",
#                            "<Path to file>/someotherfile.py"],
#          "packages": []}
#
# setup(
#     name = "Name of app",
#     version = "0.1",
#     author = "The author",
#     options = {'build_exe': files},
#     description = "Enter A Description Here",
#     executables = [Executable("main.py", base=None)])

files = {"include_files": ["somefile.py"],
         "packages": []}

setup(name="Hello",
      version="0.1",
      author="Peter Anema",
      options={'build_exe': files},
      description="An exe built with Python",
      executables=[Executable("main.py", base=None)])
