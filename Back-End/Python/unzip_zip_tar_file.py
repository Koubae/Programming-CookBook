# ==================== < UnZip > ==================== #
import tarfile

def open_tarfile_function(tarfile_file_name):
    open_tarfile=tarfile.open("file_name.tar.gz")
    open_tarfile.extractall(path='tarfile_file_name')
    open_tarfile.close()

open_tarfile_function('data.tgz')


# ==================== < Zip Odoo > ==================== #

import tarfile
import os.path

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.sep)

output_filename = "file_name.tar.gz"
source_dir = "source_dir"

make_tarfile(output_filename, source_dir)



# ==================== < UnZip Odoo > ==================== #
import tarfile

def open_tarfile_function(tarfile_file_name):
    open_tarfile=tarfile.open("python-stdnum-1.8.tar_.gz")
    open_tarfile.extractall(path='stdnum')
    open_tarfile.close()

open_tarfile_function('data.tgz')


# ==================== < Zip > ==================== #

import tarfile
import os.path

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.sep)

output_filename = "python-stdnum-1.8.tar.gz"
source_dir = "stdnum\python-stdnum-1.8"

make_tarfile(output_filename, source_dir)

