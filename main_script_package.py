"""This is the main program to demonstarte user defined packages in python
    Use __init__.py file inside every folder you want to create in order to
        understande it as a package


    This how scripts lie inside this example package

    --main_script_package.py
      main_package folder
            --__init.py
            --main_package.py
            --subpackage folder
                    --__init__.py
                    --supackage.py"""
from main_package.main_package import test_package
from main_package.sub_package.sub_package import test_sub_package
test_package()
test_sub_package()
