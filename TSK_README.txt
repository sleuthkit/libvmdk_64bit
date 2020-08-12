Last Updated 1.28.2016

This file describes how to build 32-bit and 64-bit Visual Studio 2010 libvmdk library for use with TSK. This process should be followed when new release of libvmdk comes out.
----------------------------------------------------------------

Download source code tag.gz file from https://github.com/libyal/libvmdk/releases, make sure it has all libraries like libcstring etc. Do not download just git repository or "sorce code" link, they don't include all libraries and require executing multiple scripts, some of which don't run on Windows.

If you are upgrading from a previous version of libvmdk, delete all contents of libvmdk_64bit git folder (i.e. the previous version of libvmdk) on local drive except .git subfolder, .gitignore, and.gitattributes (if using git).

libvmdk Visual Studio project requires zlib source code in order to build. More so, zlib source code must be located in a very specific location in relation to libvmdk source code. Specifically, zlib source package must be located in the directory containing the libvmdk directory. 

For example, if this repository is checked out into C:\cygwin64\home\user_name\libvmdk_64bit then the libvmdk_64bit folder must contain 2 sub-folders: libvmdk (containing livmdk source code) and zlib (containing zlib source code).

Extract contents of the archive containg source code into top level git libvmdk_64bit/libvmdk folder

Open project in VS2010 and let it convert the solution

Remove dokan, pyvmdk, and vmdkmount projects from the solution

At this point you should be able to build the 32-bit libvmdk solution

Run both 64-bit conversion scripts as described in 
https://github.com/libyal/libvmdk/wiki/Building

At this point you should be able to build the 64-bit libvmdk solution

Now need to modify where libraries are being stored after build. By default all output is stored in /Release folder so when you build a 32-bit library and then build a 64-bit library, the 32-bit binaries get overwritten. We need to modify where the 64-bit binaries get stored.

Select the "x64" configuration in VS. Then for each project in libvmdk solution:
- right click on the project, select properties
- in "configuration:" pull-down menu select "All configurations"
- Select "Configuration Properties" -> "General"
- Change "Output directory" from "$(SolutionDir)$(Configuration)\" to "$(SolutionDir)$(Platform)\$(Configuration)"
Repeat these steps for all VS projects in the libvmdk solution

In order to be used with TSK the user needs to define an environment variable LIBVMDK_HOME pointed at C:\cygwin64\home\user_name\libvmdk_64bit\libvmdk

--------
8.11.2020 notes:
- The dokan project was gone.
- The script didn't work, but everything seemed to be set up correctly.
- The output dir change only seemed to be needed on one project.