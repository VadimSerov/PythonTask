echo "# PythonTask" >> README.md
%CURRENTDRIVE%/STAR/Portable/GIT/bin/git init
%CURRENTDRIVE%/STAR/Portable/GIT/bin/git config --global --add safe.directory I:/STAR/Portable/PythonTask
%CURRENTDRIVE%/STAR/Portable/GIT/bin/git add *
%CURRENTDRIVE%/STAR/Portable/GIT/bin/git commit -m "PythonTask 16 07 2022 new0"
%CURRENTDRIVE%/STAR/Portable/GIT/bin/git branch -M main
%CURRENTDRIVE%/STAR/Portable/GIT/bin/git remote add origin https://github.com/VadimSerov/PythonTask.git
%CURRENTDRIVE%/STAR/Portable/GIT/bin/git push -u origin main

